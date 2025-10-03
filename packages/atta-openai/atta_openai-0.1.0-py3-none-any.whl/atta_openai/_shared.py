"""Shared utilities for OpenAI response wrappers."""

from functools import singledispatch
from typing import Any, cast

from openai.types.responses import (
    ParsedResponseOutputMessage as OpenAIParsedResponseOutputMessage,
    ParsedResponseOutputText as OpenAIParsedResponseOutputText,
    ResponseFunctionToolCall as OpenAIResponseFunctionToolCall,
    ResponseOutputMessage as OpenAIResponseOutputMessage,
    ResponseOutputRefusal as OpenAIResponseOutputRefusal,
    ResponseOutputText as OpenAIResponseOutputText,
    ResponseReasoningItem as OpenAIResponseReasoningItem,
)
from openai.types.responses.response_output_text import Logprob as OpenAILogprob
from pydantic import BaseModel

from atta.ai.responses.common import (
    MessageContent as AttaMessageContent,
    ResponseFunctionToolCall as AttaResponseFunctionToolCall,
    ResponseMessage as AttaResponseMessage,
    ResponseReasoningItem as AttaResponseReasoningItem,
)
from atta.ai.responses.common.content import (
    Annotation as AttaAnnotation,
    ContentRefusal as AttaContentRefusal,
    ContentText as AttaContentText,
    ParsedContent as AttaParsedContent,
)
from atta.ai.responses.common.reasoning import ReasoningContent, ReasoningSummary
from atta.utils.json import parse_json
from atta_openai._exceptions import OpenAIWrapperError

# -------------------------------
# Types
# -------------------------------

type OpenAIOutputItem = (
    OpenAIResponseReasoningItem
    | OpenAIResponseOutputMessage
    | OpenAIParsedResponseOutputMessage  # type: ignore[type-arg]
    | OpenAIResponseFunctionToolCall
)
type AttaOutputItem = (
    AttaResponseMessage | AttaResponseFunctionToolCall | AttaResponseReasoningItem
)
type OpenAIMessageContent = (
    OpenAIResponseOutputText
    | OpenAIResponseOutputRefusal
    | OpenAIParsedResponseOutputText  # type: ignore[type-arg]
)


# -------------------------------
# Shared Wrappers
# -------------------------------


def wrap_message_content_annotations(annotations: list[Any]) -> list[AttaAnnotation]:
    """Wrap OpenAI annotations to unified format.

    Args:
        annotations: List of OpenAI annotation objects.

    Returns:
        List of unified annotation objects.

    Raises:
        NotImplementedError: If annotations are provided (not yet supported).
    """
    if annotations:
        raise NotImplementedError("Annotations are not yet supported")
    return []


def wrap_logprobs(
    logprobs: list[OpenAILogprob] | None = None,
) -> dict[str, float] | None:
    """Convert OpenAI logprobs to token-probability mapping.

    Args:
        logprobs: OpenAI logprob objects.

    Returns:
        Token to probability mapping or None.

    Raises:
        OpenAIWrapperError: If logprob conversion fails.
    """
    if not logprobs:
        return None

    try:
        return {lp.token: lp.logprob for lp in logprobs}
    except (AttributeError, TypeError) as e:
        raise OpenAIWrapperError(f"Failed to wrap logprobs: {e}") from e


@singledispatch
def wrap_message_content(content: OpenAIMessageContent) -> AttaMessageContent:
    """Convert OpenAI message content to unified format.

    Args:
        content: OpenAI message content.

    Returns:
        Unified message content.

    Raises:
        OpenAIWrapperError: If content type not supported.
    """
    raise OpenAIWrapperError(f"Unsupported content type: {type(content)}")


@wrap_message_content.register
def _(
    content: OpenAIParsedResponseOutputText,  # type: ignore[type-arg]
) -> AttaParsedContent:
    """Convert parsed text content."""
    try:
        return AttaParsedContent(
            text=content.text,
            annotations=wrap_message_content_annotations(
                getattr(content, "annotations", [])
            ),
            parsed=cast(BaseModel, content.parsed),
            logprobs=wrap_logprobs(getattr(content, "logprobs", None)),
        )
    except Exception as e:
        raise OpenAIWrapperError(f"Failed to wrap parsed content: {e}") from e


@wrap_message_content.register
def _(content: OpenAIResponseOutputText) -> AttaContentText:
    """Convert text content."""
    try:
        return AttaContentText(
            text=content.text,
            logprobs=wrap_logprobs(getattr(content, "logprobs", None)),
            type="text",
            annotations=wrap_message_content_annotations(
                getattr(content, "annotations", [])
            ),
        )
    except Exception as e:
        raise OpenAIWrapperError(f"Failed to wrap text content: {e}") from e


@wrap_message_content.register
def _(content: OpenAIResponseOutputRefusal) -> AttaContentRefusal:
    """Convert refusal content."""
    try:
        return AttaContentRefusal(refusal=content.refusal, type="refusal")
    except Exception as e:
        raise OpenAIWrapperError(f"Failed to wrap refusal: {e}") from e


@singledispatch
def wrap_output_item(item: OpenAIOutputItem) -> AttaOutputItem:
    """Convert OpenAI output item to unified format.

    Args:
        item: OpenAI output item.

    Returns:
        Unified output item.

    Raises:
        OpenAIWrapperError: If item type not supported.
    """
    raise OpenAIWrapperError(f"Unsupported output item type: {type(item)}")


@wrap_output_item.register
def _(item: OpenAIResponseReasoningItem) -> AttaResponseReasoningItem:
    """Convert reasoning item."""
    try:
        summary = [
            ReasoningSummary(text=summary.text) for summary in (item.summary or [])
        ]
        content = (
            [ReasoningContent(content=content.text) for content in item.content]
            if item.content
            else None
        )
        return AttaResponseReasoningItem(
            id=item.id,
            summary=summary,
            content=content,
            encrypted_content=item.encrypted_content,
            type=item.type,
        )
    except Exception as e:
        raise OpenAIWrapperError(f"Failed to wrap reasoning item: {e}") from e


@wrap_output_item.register
def _(item: OpenAIResponseOutputMessage) -> AttaResponseMessage:
    """Convert output message."""
    return _wrap_message(item)


@wrap_output_item.register
def _(
    item: OpenAIParsedResponseOutputMessage,  # type: ignore[type-arg]
) -> AttaResponseMessage:
    """Convert parsed output message."""
    return _wrap_message(item)


@wrap_output_item.register
def _(item: OpenAIResponseFunctionToolCall) -> AttaResponseFunctionToolCall:
    """Convert function tool call."""
    try:
        return AttaResponseFunctionToolCall(
            id=item.id,  # type: ignore[arg-type]
            call_id=item.call_id,
            name=item.name,
            arguments=parse_json(item.arguments),
            status=getattr(item, "status", None),
        )
    except Exception as e:
        raise OpenAIWrapperError(f"Failed to wrap function call: {e}") from e


def _wrap_message(
    item: (  # type: ignore[type-arg]
        OpenAIResponseOutputMessage | OpenAIParsedResponseOutputMessage
    ),
) -> AttaResponseMessage:
    """Convert message items to unified format.

    Args:
        item: OpenAI message item.

    Returns:
        Unified response message.

    Raises:
        OpenAIWrapperError: If message conversion fails.
    """
    try:
        content = (
            [wrap_message_content(c) for c in item.content] if item.content else None
        )
        return AttaResponseMessage(
            id=item.id,
            content=content,
            role=item.role,
            status=getattr(item, "status", None),
        )
    except Exception as e:
        raise OpenAIWrapperError(f"Failed to wrap message: {e}") from e
