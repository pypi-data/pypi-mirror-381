from typing import Any, Iterable

from forge_utils import logger

from .llm_exceptions import ConfigurationError
from .models import (
    InputItem,
    InputToolResult,
    ResponseRequest,
    TextFormat,
    TextOutputConfig,
    Tool,
)
from .response import OpenAIResponse


class LLMOpenAIClient:
    def __init__(
        self,
        api_key: str,
        model: str = "gpt-4o",
        max_tokens: int | None = None,
        temperature: float = 1.0,
        user: str | None = None,
        store_local: bool = False,
        response: Any | None = None,
    ) -> None:
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.user = user
        self.response = response or OpenAIResponse(api_key, store_local=store_local)
        self._tools: list[Tool] | None = None
        self._tool_choice: str | dict | None = None
        self.last_request: ResponseRequest | None = None

    def configure_tools(
        self,
        *,
        tools: list[Tool] | None = None,
        tool_choice: str | dict | None = None,
    ) -> None:
        self._tools = tools
        self._tool_choice = tool_choice

    def _normalize_tool_choice(self, tool_choice: str | dict | None) -> str | dict | None:
        """Normalize tool_choice for compatibility across API variants.

        Accepts legacy shapes like {"type":"tool","name":"X"} or
        {"type":"function","function":{"name":"X"}} and adapts them to the
        Responses API contract {"type": "function", "name": "X"}.
        """
        if isinstance(tool_choice, dict):
            normalized: dict[str, Any] = dict(tool_choice)
            tool_type = normalized.get("type")
            name = normalized.get("name")
            func = (
                normalized.get("function")
                if isinstance(normalized.get("function"), dict)
                else None
            )

            if tool_type == "tool" and name:
                return {"type": "function", "name": name}

            if tool_type == "function":
                if func and func.get("name") and not name:
                    name = func["name"]
                if name:
                    return {"type": "function", "name": name}

            if func and func.get("name") and tool_type == "function":
                normalized.setdefault("name", func["name"])
                normalized.pop("function", None)
                return normalized
        return tool_choice

    def stream_events(
        self,
        prompt: str,
        *,
        tools: list[Tool] | None = None,
        tool_choice: str | dict | None = None,
        previous_response_id: str | None = None,
        input_override: list[InputItem | InputToolResult | dict[str, Any]] | str | None = None,
    ) -> Iterable[dict[str, Any]]:
        if not prompt or not isinstance(prompt, str):
            logger.warning("Prompt inválido recebido em send_prompt.")
            raise ConfigurationError("O prompt precisa ser uma string não vazia.")
        tools = tools if tools is not None else self._tools
        tool_choice = tool_choice if tool_choice is not None else self._tool_choice
        tool_choice = self._normalize_tool_choice(tool_choice)
        request = ResponseRequest(
            model=self.model,
            input=(input_override if input_override is not None else prompt),
            max_output_tokens=self.max_tokens,
            temperature=self.temperature,
            user=self.user,
            stream=True,
            text=TextOutputConfig(format=TextFormat(type="text")),
            tools=tools,
            tool_choice=tool_choice,
            previous_response_id=previous_response_id,
        )
        self.last_request = request

        return self.response.send_streaming_response(request)

    def send_prompt(
        self,
        prompt: str,
        streamed: bool = False,
        *,
        tools: list[Tool] | None = None,
        tool_choice: str | dict | None = None,
        previous_response_id: str | None = None,
        input_override: list[InputItem | InputToolResult | dict[str, Any]] | str | None = None,
    ) -> Any:
        if not prompt or not isinstance(prompt, str):
            logger.warning("Prompt inválido recebido em send_prompt.")
            raise ConfigurationError("O prompt precisa ser uma string não vazia.")
        tools = tools if tools is not None else self._tools
        tool_choice = tool_choice if tool_choice is not None else self._tool_choice
        tool_choice = self._normalize_tool_choice(tool_choice)

        if streamed:
            events = self.stream_events(
                prompt,
                tools=tools,
                tool_choice=tool_choice,
                previous_response_id=previous_response_id,
                input_override=input_override,
            )

            def stream_gen() -> Iterable[str]:
                logger.debug("Iniciando geração de resposta em modo streaming.")
                for event in events:
                    if event.get("type") == "response.output_text.delta":
                        delta = extract_text_delta(event)
                        if delta:
                            yield delta

            return stream_gen()

        logger.debug("Iniciando geração de resposta em modo direto.")
        request = ResponseRequest(
            model=self.model,
            input=(input_override if input_override is not None else prompt),
            max_output_tokens=self.max_tokens,
            temperature=self.temperature,
            user=self.user,
            stream=False,
            text=TextOutputConfig(format=TextFormat(type="text")),
            tools=tools,
            tool_choice=tool_choice,
            previous_response_id=previous_response_id,
        )
        self.last_request = request
        return self.response.send_response(request)

def extract_text_delta(event: dict) -> str:
    return event.get("delta", "")
