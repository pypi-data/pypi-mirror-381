"""Configuration models for code-rag-agent using Pydantic."""

from typing import Optional

from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class VectorStoreConfig(BaseModel):
    """Vector store configuration."""

    provider: str = Field(default="pinecone", description="Vector store provider")
    index_name: str = Field(..., description="Vector store index name")
    api_key: str = Field(..., description="Vector store API key")
    namespace: Optional[str] = Field(default=None, description="Optional namespace for multi-tenancy")

    @field_validator("api_key")
    def validate_api_key(cls, v: str) -> str:
        """Validate API key is not empty."""
        if not v or v.strip() == "":
            raise ValueError("Vector store API key cannot be empty")
        return v


class LLMConfig(BaseModel):
    """LLM provider configuration."""

    provider: str = Field(default="openai", description="LLM provider")
    query_model: str = Field(
        default="gpt-4o-mini", description="Model for query translation (cheap, fast)"
    )
    answer_model: str = Field(default="gpt-4o", description="Model for answer generation (quality)")
    api_key: str = Field(..., description="LLM API key")
    temperature: float = Field(default=0.2, ge=0.0, le=2.0, description="LLM temperature")
    max_tokens: int = Field(default=4096, gt=0, description="Max tokens for LLM response")

    @field_validator("api_key")
    def validate_api_key(cls, v: str) -> str:
        """Validate API key is not empty."""
        if not v or v.strip() == "":
            raise ValueError("LLM API key cannot be empty")
        return v


class EmbeddingConfig(BaseModel):
    """Embedding model configuration - must match code-ingestion-service."""

    model: str = Field(
        default="nomic-ai/nomic-embed-text-v1.5",
        description="Embedding model (must match ingestion service)",
    )

    @field_validator("model")
    def validate_model(cls, v: str) -> str:
        """Validate embedding model is not empty."""
        if not v or v.strip() == "":
            raise ValueError("Embedding model cannot be empty")
        return v


class RetrievalConfig(BaseModel):
    """Retrieval configuration for vector search."""

    top_k: int = Field(default=10, gt=0, le=50, description="Number of chunks to retrieve")
    min_score: float = Field(
        default=0.7, ge=0.0, le=1.0, description="Minimum similarity score threshold"
    )
    enable_reranking: bool = Field(default=False, description="Enable reranking (future)")
    max_context_tokens: int = Field(
        default=8000, gt=0, description="Max tokens for context assembly"
    )


class AppSettings(BaseSettings):
    """Main application settings loaded from environment variables and .env file.

    Supports both environment variables and .env file configuration.
    Priority: CLI args > OS environment variables > .env file > defaults

    Example .env file:
        PINECONE_API_KEY=your_key
        PINECONE_INDEX_NAME=code-embeddings
        OPENAI_API_KEY=sk-...
        OPENAI_ANSWER_MODEL=gpt-4o
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="ignore",
    )

    # Vector Store Settings
    pinecone_api_key: str = Field(..., description="Pinecone API key")
    pinecone_index_name: str = Field(..., description="Pinecone index name")
    pinecone_namespace: Optional[str] = Field(default=None, description="Pinecone namespace")

    # LLM Settings
    openai_api_key: str = Field(..., description="OpenAI API key")
    openai_query_model: str = Field(
        default="gpt-4o-mini", description="OpenAI model for query translation"
    )
    openai_answer_model: str = Field(
        default="gpt-4o", description="OpenAI model for answer generation"
    )
    openai_temperature: float = Field(
        default=0.2, ge=0.0, le=2.0, description="LLM temperature"
    )
    openai_max_tokens: int = Field(default=4096, gt=0, description="Max tokens for response")

    # Embedding Settings
    embedding_model: str = Field(
        default="nomic-ai/nomic-embed-text-v1.5",
        description="Embedding model (must match code-ingestion-service)",
    )

    # Retrieval Settings
    retrieval_top_k: int = Field(
        default=10, gt=0, le=50, description="Number of chunks to retrieve"
    )
    retrieval_min_score: float = Field(
        default=0.7, ge=0.0, le=1.0, description="Minimum similarity score"
    )
    retrieval_max_context_tokens: int = Field(
        default=8000, gt=0, description="Max tokens for context assembly"
    )

    @property
    def vector_store_config(self) -> VectorStoreConfig:
        """Build vector store config from settings."""
        return VectorStoreConfig(
            provider="pinecone",
            index_name=self.pinecone_index_name,
            api_key=self.pinecone_api_key,
            namespace=self.pinecone_namespace,
        )

    @property
    def llm_config(self) -> LLMConfig:
        """Build LLM config from settings."""
        return LLMConfig(
            provider="openai",
            query_model=self.openai_query_model,
            answer_model=self.openai_answer_model,
            api_key=self.openai_api_key,
            temperature=self.openai_temperature,
            max_tokens=self.openai_max_tokens,
        )

    @property
    def embedding_config(self) -> EmbeddingConfig:
        """Build embedding config from settings."""
        return EmbeddingConfig(model=self.embedding_model)

    @property
    def retrieval_config(self) -> RetrievalConfig:
        """Build retrieval config from settings."""
        return RetrievalConfig(
            top_k=self.retrieval_top_k,
            min_score=self.retrieval_min_score,
            max_context_tokens=self.retrieval_max_context_tokens,
        )


def load_settings() -> AppSettings:
    """Load application settings from environment variables and .env file.

    Reads from (in priority order):
    1. OS environment variables (highest priority)
    2. .env file in current directory
    3. Default values (lowest priority)

    Returns:
        AppSettings: Validated settings object

    Raises:
        ValidationError: If required fields are missing or invalid
    """
    return AppSettings()
