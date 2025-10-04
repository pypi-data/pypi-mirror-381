"""Base LLM client interface for language model implementations."""

from abc import ABC, abstractmethod

from langchain_core.language_models import BaseChatModel


class BaseLLMClient(ABC):
    """Abstract base class for LLM providers.

    Provides a minimal wrapper around LangChain LLMs to enable
    pluggable LLM implementations (OpenAI, Anthropic, local models, etc.).
    """

    @abstractmethod
    def get_llm(self, model_override: str = None) -> BaseChatModel:
        """Get the configured LangChain LLM.

        Args:
            model_override: Optional model name to override default configuration.
                Useful for using different models for query translation vs answer generation.

        Returns:
            BaseChatModel: Configured LangChain LLM (e.g., ChatOpenAI, ChatAnthropic)
                that can be used with LangChain chains.

        Example:
            # Use default model (from config)
            llm = client.get_llm()

            # Use specific model
            query_llm = client.get_llm(model_override="gpt-4o-mini")
            answer_llm = client.get_llm(model_override="gpt-4o")
        """
        pass
