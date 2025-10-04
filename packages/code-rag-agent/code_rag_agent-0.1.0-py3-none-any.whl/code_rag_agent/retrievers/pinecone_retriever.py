"""Pinecone retriever implementation with Self-Query support."""

import warnings

# Suppress LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain_core.retrievers import BaseRetriever as LangChainBaseRetriever
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from code_rag_agent.config import AppSettings

from .base_retriever import BaseRetriever


class PineconeRetriever(BaseRetriever):
    """Pinecone retriever with Self-Query for automatic metadata filtering.

    Uses LangChain's SelfQueryRetriever to automatically convert natural language
    queries into metadata filters, enabling smart code search.

    Example queries:
        "Find GET endpoints in MusicController"
        "Show me REST controllers in the payment package"
        "What methods are in PaymentService?"
    """

    def __init__(self, settings: AppSettings):
        """Initialize Pinecone retriever with configuration.

        Args:
            settings: Application settings with Pinecone and embedding config
        """
        self.settings = settings
        self._retriever = None

        # Initialize Pinecone client
        pc = Pinecone(api_key=settings.pinecone_api_key)
        self.index = pc.Index(settings.pinecone_index_name)

        # Create embeddings (must match code-ingestion-service!)
        self.embeddings = self._create_embeddings()

        # Create vector store
        self.vectorstore = PineconeVectorStore(
            index=self.index,
            embedding=self.embeddings,
            namespace=settings.pinecone_namespace,
        )

    def _create_embeddings(self) -> HuggingFaceEmbeddings:
        """Create embedding function matching code-ingestion-service.

        Uses HuggingFaceEmbeddings with Nomic model and trust_remote_code=True
        to exactly match the ingestion process.

        Returns:
            HuggingFaceEmbeddings: Configured embeddings
        """
        return HuggingFaceEmbeddings(
            model_name=self.settings.embedding_model,
            model_kwargs={"trust_remote_code": True},
        )

    def _get_metadata_field_info(self) -> list[AttributeInfo]:
        """Define metadata schema for Self-Query filtering.

        These fields are extracted during code ingestion and can be used
        for automatic filtering based on natural language queries.

        Returns:
            List of AttributeInfo describing available metadata fields
        """
        return [
            # Core identifiers
            AttributeInfo(
                name="class_name",
                description="Java class name (e.g., MusicController, PaymentService)",
                type="string",
            ),
            AttributeInfo(
                name="file_path",
                description="Source file path relative to repository root",
                type="string",
            ),
            # Method information
            AttributeInfo(
                name="methods",
                description="List of method names in this code chunk",
                type="list[string]",
            ),
            # Code hierarchy
            AttributeInfo(
                name="parent_chunk_id",
                description="Parent chunk identifier for method-level chunks (e.g., 'class:MusicController')",
                type="string or null",
            ),
            AttributeInfo(
                name="chunk_type",
                description="Type of code chunk: 'class' or 'method'",
                type="string",
            ),
            # REST API metadata
            AttributeInfo(
                name="is_rest_controller",
                description="Whether this code is a REST API controller",
                type="boolean",
            ),
            AttributeInfo(
                name="http_methods",
                description="HTTP methods used in this code (e.g., ['GET', 'POST'])",
                type="list[string]",
            ),
            AttributeInfo(
                name="api_path",
                description="REST API endpoint path(s) defined in this code",
                type="string or null",
            ),
        ]

    def get_retriever(self) -> LangChainBaseRetriever:
        """Get configured LangChain SelfQueryRetriever.

        Creates a SelfQueryRetriever that automatically converts natural language
        queries into metadata filters using an LLM (GPT-4o-mini).

        Returns:
            SelfQueryRetriever: Configured retriever ready for use in chains

        Example:
            retriever = pinecone_retriever.get_retriever()
            chain = create_retrieval_chain(retriever, combine_docs_chain)
        """
        if self._retriever is None:
            # Create LLM for query translation (use cheaper model)
            llm = ChatOpenAI(
                model=self.settings.openai_query_model,
                temperature=0,  # Deterministic for query translation
                api_key=self.settings.openai_api_key,
            )

            # Document content description for Self-Query
            #TODO need to externalize this, so that consumers have control on their agent
            document_content_description = (
                "Java source code chunks from Spring Boot microservices. "
                "Includes REST API controllers with endpoint definitions, "
                "service layer business logic, and utility methods. "
                "Chunks may represent complete classes or grouped methods "
                "with annotations and dependencies."
            )

            # Create SelfQueryRetriever
            self._retriever = SelfQueryRetriever.from_llm(
                llm=llm,
                vectorstore=self.vectorstore,
                document_contents=document_content_description,
                metadata_field_info=self._get_metadata_field_info(),
                verbose=False,  # Set to True for debugging
                search_kwargs={"k": self.settings.retrieval_top_k},
            )

        return self._retriever
