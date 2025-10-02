from __future__ import annotations

import json
from typing import Any, Callable, Dict, Iterable, List, Optional

from .interfaces import ILLMClient
from .llm_exceptions import ConfigurationError
from .models import InputFile, InputImage, InputText, InputToolResult, ResponseResult, Tool
from .openai_client import LLMOpenAIClient
from .response import OpenAIResponse


def _extract_text(resp: Any) -> str:
    """Extrai texto de ResponseResult suportando itens de mensagem ou partes diretas."""
    try:
        items = getattr(resp, "output", None) or []
        for item in items:
            parts = getattr(item, "content", None)
            if parts is None:
                # item pode ser um ContentPart direto
                if (
                    getattr(item, "type", "") in ("output_text", "text")
                    and getattr(item, "text", None)
                ):
                    return item.text.strip()
                continue
            for p in parts:
                if (
                    getattr(p, "type", "") in ("output_text", "text")
                    and getattr(p, "text", None)
                ):
                    return p.text.strip()
        return ""
    except Exception:
        return ""


class OpenAIProvider(ILLMClient):
    """Provider OpenAI que implementa ILLMClient sobre LLMOpenAIClient."""

    def __init__(self, client: Optional[LLMOpenAIClient] = None) -> None:
        self._client = client
        self._model = "gpt-4o"
        self._tools_defs: List[Tool] = []
        self._tool_choice: str | dict | None = "auto"
        self._tool_fns: Dict[str, Callable[[Dict[str, Any]], Any]] = {}

    @property
    def name(self) -> str:
        return "openai"

    def set_api_key(self, key: str) -> bool:
        if self._client is None:
            self._client = LLMOpenAIClient(api_key=key, model=self._model, temperature=0.7)
            return True
        # atualiza a response interna
        self._client.response.api_key = key
        return True

    # Tools configuration / registry
    def configure_tools(self, tools: List[Tool], tool_choice: str | dict | None = "auto") -> None:
        self._tools_defs = tools
        self._tool_choice = tool_choice
        if self._client:
            self._client.configure_tools(tools=tools, tool_choice=tool_choice)

    def register_tool(self, name: str, func: Callable[[Dict[str, Any]], Any]) -> None:
        self._tool_fns[name] = func

    def send_message(self, prompt: str, context: Optional[List[dict]] = None) -> str:
        if not isinstance(prompt, str) or not prompt:
            raise ConfigurationError("prompt inválido")
        if self._client is None:
            raise ConfigurationError("cliente não configurado (chame set_api_key)")
        # If tools are configured or registry exists, try orchestration
        if self._tools_defs or self._tool_fns:
            return self._send_with_tools(prompt)
        resp = self._client.send_prompt(prompt, streamed=False)
        return _extract_text(resp) or ""

    def send_stream(self, prompt: str, context: Optional[List[dict]] = None) -> Iterable[str]:
        if not isinstance(prompt, str) or not prompt:
            raise ConfigurationError("prompt inválido")
        if self._client is None:
            raise ConfigurationError("cliente não configurado (chame set_api_key)")

        if self._tools_defs or self._tool_fns:
            return self._stream_with_tools(prompt)

        from typing import cast
        return cast(Iterable[str], self._client.send_prompt(prompt, streamed=True))

    # Internal: one-step tool orchestration (sync)
    def _collect_tool_uses(self, resp: ResponseResult) -> List[dict]:
        uses: List[dict] = []
        for item in getattr(resp, "output", []) or []:
            # 1) function_call item (top-level)
            if getattr(item, "type", "") == "function_call":
                name = getattr(item, "name", "")
                call_id = getattr(item, "call_id", None) or getattr(item, "id", "")
                raw_args = getattr(item, "arguments", {})
                if isinstance(raw_args, str):
                    try:
                        args = json.loads(raw_args)
                    except Exception:
                        args = {}
                else:
                    args = raw_args
                # raw item to include back into input on follow-up (as docs recommend)
                try:
                    raw_item = {
                        "type": "function_call",
                        "name": name,
                        "call_id": call_id,
                        "arguments": raw_args if isinstance(raw_args, str) else json.dumps(args),
                    }
                except Exception:
                    raw_item = {
                        "type": "function_call",
                        "name": name,
                        "call_id": call_id,
                        "arguments": "{}",
                    }
                if call_id:
                    uses.append(
                        {
                            "kind": "function",
                            "name": name,
                            "id": call_id,
                            "args": args,
                            "raw": raw_item,
                        }
                    )
                continue

            # 2) tool_use em mensagem ou top-level
            parts = getattr(item, "content", None)
            candidate_parts = parts if parts is not None else [item]
            for part in candidate_parts:
                if getattr(part, "type", "") != "tool_use":
                    continue
                name = (getattr(part, "name", None) or "")
                tool_id = (getattr(part, "id", None) or getattr(part, "tool_use_id", None) or "")
                raw_args = getattr(part, "input", None) or getattr(part, "arguments", None) or {}
                if isinstance(raw_args, str):
                    try:
                        args = json.loads(raw_args)
                    except Exception:  # pragma: no cover - malformed JSON
                        args = {}
                else:
                    args = raw_args
                if tool_id:
                    # raw tool_use item for follow-up context
                    raw_item = {
                        "type": "tool_use",
                        "id": tool_id,
                        "name": name,
                        "input": (
                            raw_args
                            if isinstance(raw_args, str)
                            else json.dumps(args)
                        ),
                    }
                    uses.append(
                        {
                            "kind": "tool",
                            "name": name,
                            "id": tool_id,
                            "args": args,
                            "raw": raw_item,
                        }
                    )
        return uses

    def _eval_tools(self, uses: List[dict]) -> List[dict]:
        results: List[dict] = []
        is_real = isinstance(getattr(self._client, "response", None), OpenAIResponse)
        for u in uses:
            fn = self._tool_fns.get(u["name"]) if u.get("name") else None
            try:
                result = fn(u["args"]) if fn else "(tool not registered)"
            except Exception as exc:  # pragma: no cover - tool error
                result = f"tool_error: {exc}"

            if u.get("kind") == "function":
                # Build output payload
                if isinstance(result, (dict, list)):
                    output = json.dumps(result)
                else:
                    output = json.dumps({"result": str(result)})
                call_identifier = u.get("id")
                if not call_identifier:
                    continue
                if is_real:
                    results.append(
                        {
                            "type": "function_call_output",
                            "call_id": str(call_identifier),
                            "output": output,
                        }
                    )
                else:
                    # For tests/local, keep function_call_output and include raw call
                    raw = u.get("raw")
                    if isinstance(raw, dict):
                        results.append(raw)
                    results.append(
                        {
                            "type": "function_call_output",
                            "call_id": call_identifier,
                            "output": output,
                        }
                    )
            else:
                call_identifier = u.get("id")
                if not call_identifier:
                    continue
                if isinstance(result, (dict, list)):
                    output = json.dumps(result)
                else:
                    output = str(result)
                if is_real:
                    results.append(
                        {
                            "type": "custom_tool_call_output",
                            "call_id": str(call_identifier),
                            "output": output,
                        }
                    )
                else:
                    results.append(
                        {
                            "type": "custom_tool_call_output",
                            "call_id": call_identifier,
                            "output": output,
                        }
                    )
        return results

    def _stream_with_tools(self, prompt: str) -> Iterable[str]:
        assert self._client is not None
        client = self._client
        previous_response_id: Optional[str] = None
        context_items: Optional[List[InputText | InputToolResult | dict[str, Any] | InputImage | InputFile]] = None
        current_tool_choice: str | dict | None = self._tool_choice

        def run_loop() -> Iterable[str]:
            nonlocal previous_response_id, context_items, current_tool_choice
            for _ in range(3):
                any_delta = False
                events = client.stream_events(
                    prompt,
                    tools=self._tools_defs or None,
                    tool_choice=current_tool_choice,
                    previous_response_id=previous_response_id,
                    input_override=context_items,
                )
                response_obj: Optional[ResponseResult] = None
                for event in events:
                    event_type = event.get("type")
                    if event_type == "response.output_text.delta":
                        delta = event.get("delta", "")
                        if delta:
                            any_delta = True
                            yield delta
                    elif event_type == "response.completed" and event.get("response"):
                        try:
                            response_obj = ResponseResult(**event["response"])
                        except Exception:  # pragma: no cover - defensive
                            response_obj = None
                    elif event_type == "response.failed":
                        message = event.get("error", {}).get("message") if isinstance(event.get("error"), dict) else None
                        raise ConfigurationError(message or "Falha no streaming da API.")

                if response_obj is None:
                    break

                previous_response_id = response_obj.id
                uses = self._collect_tool_uses(response_obj)
                if not uses:
                    if not any_delta:
                        fallback = _extract_text(response_obj)
                        if fallback:
                            yield fallback
                    break

                tool_results = self._eval_tools(uses)
                if not tool_results:
                    break

                next_context: List[InputText | InputToolResult | dict[str, Any] | InputImage | InputFile] = []
                is_real = isinstance(getattr(client, "response", None), OpenAIResponse)
                for u in uses:
                    raw = u.get("raw")
                    if isinstance(raw, dict):
                        if is_real and raw.get("type") == "function_call":
                            next_context.append(raw)
                        elif not is_real:
                            next_context.append(raw)
                next_context.extend(tool_results)
                context_items = next_context

                follow_tool_choice = None if self._tool_choice == "required" else self._tool_choice
                current_tool_choice = follow_tool_choice or "auto"

        return run_loop()

    def _send_with_tools(self, prompt: str) -> str:
        assert self._client is not None
        client = self._client
        # First turn
        from typing import cast
        resp: ResponseResult = cast(ResponseResult, self._client.send_prompt(
            prompt,
            streamed=False,
            tools=self._tools_defs or None,
            tool_choice=self._tool_choice,
        ))

        # Iterate tool resolution up to N rounds
        for _ in range(3):
            uses = self._collect_tool_uses(resp)
            if not uses:
                text = _extract_text(resp)
                if text:
                    return text
                break
            tool_results = self._eval_tools(uses)
            if not tool_results:
                break
            # Build context: original user message + raw function/tool calls + their outputs
            # Build follow-up context: only call descriptors and their outputs
            context_items: List[InputText | InputToolResult | dict[str, Any] | InputImage | InputFile] = []
            is_real = isinstance(getattr(self._client, "response", None), OpenAIResponse)
            for u in uses:
                raw = u.get("raw")
                if isinstance(raw, dict):
                    # For real API calls, include the original function_call descriptor too
                    # (as per some Responses API examples) before its corresponding output.
                    if is_real and raw.get("type") == "function_call":
                        context_items.append(raw)
                    elif not is_real:
                        context_items.append(raw)
            context_items.extend(tool_results)

            # Importante: após executar ferramentas, permita o modelo responder.
            # Evite manter 'required' no follow-up para não forçar novos tool calls.
            follow_tool_choice = None if self._tool_choice == "required" else self._tool_choice
        resp = cast(ResponseResult, client.send_prompt(
                prompt,
                streamed=False,
                tools=self._tools_defs or None,
                tool_choice=follow_tool_choice or "auto",
                previous_response_id=resp.id,
                input_override=context_items,
            ))

        return _extract_text(resp) or ""


__all__ = ["OpenAIProvider"]
