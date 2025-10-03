"""Text standard response wrappers for OpenAI."""

from openai.types.responses import (
    Response as OpenAIResponse,
    ResponseUsage as OpenAIResponseUsage,
)

from atta.ai.responses.common import (
    InputTokensDetails as AttaInputTokensDetails,
    OutputTokensDetails as AttaOutputTokensDetails,
    ResponseUsage as AttaResponseUsage,
)
from atta.ai.responses.standard.text import TextResponse as AttaTextResponse
from atta_openai._constants import PROVIDER_NAME
from atta_openai._exceptions import OpenAIWrapperError
from atta_openai._shared import wrap_output_item


def wrap_usage(usage: OpenAIResponseUsage) -> AttaResponseUsage:
    """Convert OpenAI usage data to unified format.

    Args:
        usage: OpenAI usage object.

    Returns:
        Unified usage object.

    Raises:
        OpenAIWrapperError: If usage conversion fails.
    """
    try:
        input_details = (
            AttaInputTokensDetails(
                cached_tokens=usage.input_tokens_details.cached_tokens
            )
            if usage.input_tokens_details
            else None
        )
        output_details = (
            AttaOutputTokensDetails(
                reasoning_tokens=usage.output_tokens_details.reasoning_tokens
            )
            if usage.output_tokens_details
            else None
        )
        return AttaResponseUsage(
            input_tokens=usage.input_tokens,
            input_tokens_details=input_details,
            output_tokens=usage.output_tokens,
            output_tokens_details=output_details,
            total_tokens=usage.total_tokens,
        )
    except Exception as e:
        raise OpenAIWrapperError(f"Failed to wrap usage: {e}") from e


def to_atta_response(response: OpenAIResponse) -> AttaTextResponse:
    """Convert OpenAI response to unified format.

    Args:
        response: OpenAI response object.

    Returns:
        Unified text response.

    Raises:
        OpenAIWrapperError: If response conversion fails.
    """
    try:
        output = [
            item
            for openai_item in (response.output or [])
            if (item := wrap_output_item(openai_item))  # type: ignore[arg-type]
            if openai_item is not None
        ]
        usage = wrap_usage(response.usage) if response.usage else None
        return AttaTextResponse(
            id=response.id,
            model=response.model,
            provider=PROVIDER_NAME,
            output=output,
            usage=usage,
            status="completed",
        )
    except Exception as e:
        raise OpenAIWrapperError(f"Failed to wrap text response: {e}") from e
