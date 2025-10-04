"""RAG Agent orchestrator for code analysis."""

import time
from typing import Dict, Any

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from code_rag_agent.config import AppSettings, load_settings
from code_rag_agent.llm_clients.openai_client import OpenAIClient
from code_rag_agent.prompts import get_code_analysis_prompt
from code_rag_agent.retrievers.pinecone_retriever import PineconeRetriever


class RAGAgent:
    """RAG Agent for intelligent code analysis and question answering.

    Orchestrates retrieval, prompt engineering, and LLM generation to answer
    questions about codebases using the modern LangChain retrieval chain pattern.

    Example:
        agent = RAGAgent()
        result = agent.query("How does payment processing work?")
        print(result["answer"])
        print(f"Sources: {len(result['context'])} code chunks")
    """

    def __init__(self, settings: AppSettings = None):
        """Initialize RAG Agent with configuration.

        Args:
            settings: Optional settings. If not provided, loads from environment.
        """
        self.settings = settings or load_settings()

        # Initialize components
        self.retriever_impl = PineconeRetriever(self.settings)
        self.llm_client = OpenAIClient(self.settings)

        # Build RAG chain
        self._chain = self._build_chain()

    def _build_chain(self):
        """Build the RAG chain using modern LangChain pattern.

        Returns:
            Runnable chain that takes {"input": query} and returns {"answer": ..., "context": [...]}
        """
        # Get retriever (SelfQueryRetriever)
        retriever = self.retriever_impl.get_retriever()

        # Get LLM (use answer model for quality)
        llm = self.llm_client.get_llm()

        # Get code analysis prompt
        prompt = get_code_analysis_prompt()

        # Create document combination chain
        combine_docs_chain = create_stuff_documents_chain(llm, prompt)

        # Create full retrieval chain
        rag_chain = create_retrieval_chain(retriever, combine_docs_chain)

        return rag_chain

    def query(self, user_query: str, verbose: bool = False) -> Dict[str, Any]:
        """Query the codebase and get an answer.

        Args:
            user_query: Natural language question about the codebase
            verbose: If True, print timing breakdown

        Returns:
            Dictionary with:
                - answer (str): Generated answer from LLM
                - context (List[Document]): Retrieved code chunks used for answer
                - input (str): Original query
                - response_time_ms (int): Time taken in milliseconds

        Example:
            result = agent.query("What GET endpoints exist in MusicController?")
            print(result["answer"])
            print(f"Response time: {result['response_time_ms']}ms")
            for doc in result["context"]:
                print(f"  - {doc.metadata['file_path']}")
        """
        start_time = time.time()

        if verbose:
            print("🔍 Starting query processing...")

        result = self._chain.invoke({"input": user_query})
        end_time = time.time()

        # Add response time to result
        total_time_ms = int((end_time - start_time) * 1000)
        result["response_time_ms"] = total_time_ms

        if verbose:
            print(f"✓ Total time: {total_time_ms}ms")
            print(f"  Retrieved {len(result.get('context', []))} chunks")

        return result

    def format_result(self, result: Dict[str, Any]) -> str:
        """Format query result for display.

        Args:
            result: Result from query() method

        Returns:
            Formatted string with answer and code references

        Example:
            result = agent.query("...")
            print(agent.format_result(result))
        """
        answer = result["answer"]
        context = result.get("context", [])
        response_time_ms = result.get("response_time_ms", 0)

        # Format answer
        output = [answer]

        # Add performance metrics
        output.append("\n\n" + "=" * 60)
        output.append(f"⏱️  Response time: {response_time_ms}ms ({response_time_ms/1000:.2f}s)")

        # Add code references if available
        if context:
            output.append(f"📚 Retrieved from {len(context)} code chunk(s):")
            output.append("=" * 60)

            for i, doc in enumerate(context, 1):
                metadata = doc.metadata
                file_path = metadata.get("file_path", "Unknown")
                class_name = metadata.get("class_name", "")
                chunk_type = metadata.get("chunk_type", "")
                start_line = metadata.get("start_line", "")

                # Format reference
                ref = f"{i}. {file_path}"
                if class_name:
                    ref += f" - {class_name}"
                if chunk_type:
                    ref += f" ({chunk_type})"
                if start_line:
                    ref += f" [line {start_line}]"

                output.append(ref)
        else:
            output.append("=" * 60)

        return "\n".join(output)
