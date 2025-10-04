"""
Code RAG Agent Service

A production-ready Python service for intelligent code retrieval and question answering
using RAG (Retrieval-Augmented Generation) with LangChain and vector stores.
"""

from .agent import RAGAgent
from .config import load_settings

__version__ = "0.1.0"
__author__ = "Sandeep G"

__all__ = ["RAGAgent", "load_settings"]
