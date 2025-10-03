"""Text streaming response wrappers for OpenAI."""

from functools import singledispatch

from openai.types.responses import (
    ResponseCompletedEvent as OpenAIResponseCompletedEvent,
    ResponseContentPartAddedEvent as OpenAIResponseContentPartAddedEvent,
    ResponseContentPartDoneEvent as OpenAIResponseContentPartDoneEvent,
    ResponseCreatedEvent as OpenAIResponseCreatedEvent,
    ResponseFunctionCallArgumentsDeltaEvent as OpenAIResponseFunctionCallArgumentsDeltaEvent,
    ResponseInProgressEvent as OpenAIResponseInProgressEvent,
    ResponseOutputItemAddedEvent as OpenAIResponseOutputItemAddedEvent,
    ResponseOutputItemDoneEvent as OpenAIResponseOutputItemDoneEvent,
    ResponseReasoningSummaryTextDeltaEvent as OpenAIResponseReasoningSummaryTextDeltaEvent,
    ResponseTextDeltaEvent as OpenAIResponseTextDeltaEvent,
    ResponseTextDoneEvent as OpenAIResponseTextDoneEvent,
)

from atta.ai.responses.streaming.text import (
    TextResponseCompletedEvent as AttaTextResponseCompletedEvent,
    TextResponseOutputItemDoneEvent as AttaTextResponseOutputItemDoneEvent,
    TextResponseStreamEvent as AttaTextResponseStreamEvent,
    TextResponseSummaryTextDeltaEvent as AttaTextResponseSummaryTextDeltaEvent,
    TextResponseTextDeltaEvent as AttaTextResponseTextDeltaEvent,
)
from atta.observability.logging import get_logger
from atta_openai._exceptions import OpenAIWrapperError
from atta_openai._shared import wrap_logprobs, wrap_output_item
from atta_openai.text_standard import to_atta_response

type OpenAIStreamEvent = (
    OpenAIResponseCreatedEvent
    | OpenAIResponseInProgressEvent
    | OpenAIResponseOutputItemAddedEvent
    | OpenAIResponseContentPartAddedEvent
    | OpenAIResponseTextDeltaEvent
    | OpenAIResponseFunctionCallArgumentsDeltaEvent
    | OpenAIResponseReasoningSummaryTextDeltaEvent
    | OpenAIResponseTextDoneEvent
    | OpenAIResponseContentPartDoneEvent
    | OpenAIResponseOutputItemDoneEvent
    | OpenAIResponseCompletedEvent
)

logger = get_logger("atta.openai.stream")


@singledispatch
def to_atta_event(event: OpenAIStreamEvent) -> AttaTextResponseStreamEvent | None:
    """Convert OpenAI stream event to unified format.

    Args:
        event: OpenAI stream event.

    Returns:
        Unified stream event or None if unsupported.
    """
    logger.warning(f"Unsupported event type: {type(event)}")
    return None


@to_atta_event.register
def _(
    event: OpenAIResponseTextDeltaEvent | OpenAIResponseFunctionCallArgumentsDeltaEvent,
) -> AttaTextResponseStreamEvent:
    """Convert text/function call delta events.

    Args:
        event: Text or function call delta event.

    Returns:
        Unified text delta event.

    Raises:
        OpenAIWrapperError: If delta conversion fails.
    """
    try:
        return AttaTextResponseTextDeltaEvent(
            delta=event.delta,
            logprobs=wrap_logprobs(getattr(event, "logprobs", None)),
        )
    except Exception as e:
        raise OpenAIWrapperError(f"Failed to wrap delta event: {e}") from e


@to_atta_event.register
def _(
    event: OpenAIResponseReasoningSummaryTextDeltaEvent,
) -> AttaTextResponseStreamEvent:
    """Convert reasoning summary delta event.

    Args:
        event: Reasoning summary delta event.

    Returns:
        Unified summary delta event.

    Raises:
        OpenAIWrapperError: If summary conversion fails.
    """
    try:
        return AttaTextResponseSummaryTextDeltaEvent(delta=event.delta)
    except Exception as e:
        raise OpenAIWrapperError(f"Failed to wrap summary delta: {e}") from e


@to_atta_event.register
def _(event: OpenAIResponseOutputItemDoneEvent) -> AttaTextResponseStreamEvent:
    """Convert output item done event.

    Args:
        event: Output item done event.

    Returns:
        Unified output item done event.

    Raises:
        OpenAIWrapperError: If item conversion fails.
    """
    try:
        return AttaTextResponseOutputItemDoneEvent(item=wrap_output_item(event.item))  # type: ignore[arg-type]
    except Exception as e:
        raise OpenAIWrapperError(f"Failed to wrap item done event: {e}") from e


# OpenAI sends granular state events that don't map to unified format.
# We log them since they provide debugging value but return None to keep
# the stream focused on actual content and completion events.


@to_atta_event.register
def _(event: OpenAIResponseCreatedEvent) -> None:
    """Response started - useful for stream start detection."""
    logger.debug(f"Stream started: {event.response.id}")
    return


@to_atta_event.register
def _(event: OpenAIResponseInProgressEvent) -> None:
    """Response processing - heartbeat event."""
    logger.debug(f"Processing: {event.response.id}")
    return


@to_atta_event.register
def _(event: OpenAIResponseOutputItemAddedEvent) -> None:
    """New reasoning/message block starting - structure info."""
    logger.debug(f"New item: {getattr(event.item, 'type', 'unknown')}")
    return


@to_atta_event.register
def _(event: OpenAIResponseContentPartAddedEvent) -> None:
    """Content part initialized - prep for streaming."""
    logger.debug(f"Content part: {getattr(event.part, 'type', 'unknown')}")
    return


@to_atta_event.register
def _(event: OpenAIResponseTextDoneEvent) -> None:  # noqa: ARG001
    """Text block finished - before item completion."""
    logger.debug("Text block complete")
    return


@to_atta_event.register
def _(event: OpenAIResponseContentPartDoneEvent) -> None:
    """Content part finished - structure completion."""
    logger.debug(f"Part complete: {getattr(event.part, 'type', 'unknown')}")
    return


@to_atta_event.register
def _(event: OpenAIResponseCompletedEvent) -> AttaTextResponseStreamEvent:
    """Convert response completed event.

    Args:
        event: Response completed event.

    Returns:
        Unified response completed event.

    Raises:
        OpenAIWrapperError: If response conversion fails.
    """
    try:
        return AttaTextResponseCompletedEvent(response=to_atta_response(event.response))
    except Exception as e:
        raise OpenAIWrapperError(f"Failed to wrap completed event: {e}") from e
