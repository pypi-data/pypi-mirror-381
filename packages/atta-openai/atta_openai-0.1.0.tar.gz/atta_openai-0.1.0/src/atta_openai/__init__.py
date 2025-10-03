"""Atta OpenAI: OpenAI integration for Atta."""

from importlib.metadata import version as get_version

from atta_openai._constants import PROVIDER_NAME
from atta_openai._exceptions import OpenAIWrapperError
from atta_openai._shared import (
    wrap_logprobs,
    wrap_message_content,
    wrap_message_content_annotations,
    wrap_output_item,
)
from atta_openai.text_standard import to_atta_response
from atta_openai.text_streaming import to_atta_event

__version__ = get_version("atta-openai")


# Test function
def test() -> str:
    """Return a test message."""
    return "OpenAI integration ready!"


__all__ = [
    "PROVIDER_NAME",
    "OpenAIWrapperError",
    "__version__",
    "test",
    "to_atta_event",
    "to_atta_response",
    "wrap_logprobs",
    "wrap_message_content",
    "wrap_message_content_annotations",
    "wrap_output_item",
]
