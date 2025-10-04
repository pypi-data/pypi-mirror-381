"""Base retriever interface for vector store implementations."""

from abc import ABC, abstractmethod

from langchain_core.retrievers import BaseRetriever as LangChainBaseRetriever


class BaseRetriever(ABC):
    """Abstract base class for vector store retrievers.

    Provides a minimal wrapper around LangChain retrievers to enable
    pluggable vector store implementations (Pinecone, Weaviate, Qdrant, etc.).
    """

    @abstractmethod
    def get_retriever(self) -> LangChainBaseRetriever:
        """Get the configured LangChain retriever.

        Returns:
            LangChainBaseRetriever: Configured retriever (e.g., SelfQueryRetriever)
                that can be used with LangChain chains.

        Example:
            retriever = pinecone_retriever.get_retriever()
            chain = create_retrieval_chain(retriever, combine_docs_chain)
        """
        pass
