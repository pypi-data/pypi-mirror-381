"""OpenAI LLM client implementation."""

from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI

from code_rag_agent.config import AppSettings

from .base_client import BaseLLMClient


class OpenAIClient(BaseLLMClient):
    """OpenAI LLM client wrapper for LangChain.

    Provides access to OpenAI models (GPT-4o, GPT-4o-mini) with
    configuration from settings.
    """

    def __init__(self, settings: AppSettings):
        """Initialize OpenAI client with configuration.

        Args:
            settings: Application settings with OpenAI config
        """
        self.settings = settings

    def get_llm(self, model_override: str = None) -> BaseChatModel:
        """Get configured ChatOpenAI instance.

        Args:
            model_override: Optional model name to override default.
                Useful for using different models for different tasks
                (e.g., gpt-4o-mini for query translation, gpt-4o for answers).

        Returns:
            ChatOpenAI: Configured LangChain LLM

        Example:
            # Use default answer model (gpt-4o)
            llm = client.get_llm()

            # Use query model for cheaper operations
            query_llm = client.get_llm(model_override="gpt-4o-mini")
        """
        model = model_override or self.settings.openai_answer_model

        return ChatOpenAI(
            model=model,
            temperature=self.settings.openai_temperature,
            max_tokens=self.settings.openai_max_tokens,
            api_key=self.settings.openai_api_key,
        )
