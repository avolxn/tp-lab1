"""
Порождающие паттерны проектирования
Lab 3
"""

from .singleton import LLM
from .factory_method import (
    LLMService,
    OpenAIService,
    AnthropicService
)
from .abstract_factory import (
    LLMFactory,
    OpenAIFactory,
    AnthropicFactory
)
from .builder import LLMRequestBuilder, LLMRequest

__all__ = [
    "LLM",
    "LLMService",
    "OpenAIService",
    "AnthropicService",
    "LLMFactory",
    "OpenAIFactory",
    "AnthropicFactory",
    "LLMRequestBuilder",
    "LLMRequest",
]

