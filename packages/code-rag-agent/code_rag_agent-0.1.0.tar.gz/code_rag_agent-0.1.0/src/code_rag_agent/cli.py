"""CLI interface for code-rag-agent."""

import sys
import warnings

# Suppress warnings BEFORE any imports (especially LangChain)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", message=".*pydantic.*")

import click

from code_rag_agent.agent import RAGAgent
from code_rag_agent.config import load_settings


@click.group()
def cli():
    """Code RAG Agent - Intelligent code analysis and question answering."""
    pass


@cli.command()
@click.argument("query")
@click.option(
    "--pinecone-api-key",
    envvar="PINECONE_API_KEY",
    help="Pinecone API key (overrides env var)",
)
@click.option(
    "--openai-api-key", envvar="OPENAI_API_KEY", help="OpenAI API key (overrides env var)"
)
@click.option(
    "--openai-model", help="Override answer model (default: gpt-4o from config)"
)
@click.option(
    "--top-k", type=int, help="Number of code chunks to retrieve (default: 10)"
)
@click.option("--verbose", is_flag=True, help="Show detailed output including retrieved chunks")
def query(
    query: str,
    pinecone_api_key: str = None,
    openai_api_key: str = None,
    openai_model: str = None,
    top_k: int = None,
    verbose: bool = False,
):
    """Query the codebase and get an AI-powered answer.

    QUERY: Natural language question about your codebase

    Examples:
        code-rag-agent query "How does payment processing work?"
        code-rag-agent query "What GET endpoints exist in MusicController?"
        code-rag-agent query "Show me the song upload flow"
    """
    try:
        # Load settings
        settings = load_settings()

        # Apply CLI overrides
        if pinecone_api_key:
            settings.pinecone_api_key = pinecone_api_key
        if openai_api_key:
            settings.openai_api_key = openai_api_key
        if openai_model:
            settings.openai_answer_model = openai_model
        if top_k:
            settings.retrieval_top_k = top_k

        if verbose:
            click.echo(f"🔍 Query: {query}")
            click.echo(f"📊 Settings: top_k={settings.retrieval_top_k}, model={settings.openai_answer_model}")
            click.echo(f"🗄️  Vector Store: {settings.pinecone_index_name}")
            click.echo("")

        # Create agent and query
        agent = RAGAgent(settings)
        result = agent.query(query, verbose=verbose)

        # Display result
        if verbose:
            click.echo(agent.format_result(result))
        else:
            # Simple output - answer + response time
            click.echo(result["answer"])
            response_time_ms = result.get("response_time_ms", 0)
            click.echo(f"\n⏱️  Response time: {response_time_ms}ms ({response_time_ms/1000:.2f}s)")

    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)
        if verbose:
            import traceback

            traceback.print_exc()
        sys.exit(1)


@cli.command()
def info():
    """Show configuration and system information."""
    try:
        settings = load_settings()

        click.echo("=" * 60)
        click.echo("Code RAG Agent - Configuration")
        click.echo("=" * 60)
        click.echo(f"Vector Store: Pinecone")
        click.echo(f"  Index: {settings.pinecone_index_name}")
        click.echo(f"  Namespace: {settings.pinecone_namespace or '(default)'}")
        click.echo(f"\nLLM Provider: OpenAI")
        click.echo(f"  Query Model: {settings.openai_query_model}")
        click.echo(f"  Answer Model: {settings.openai_answer_model}")
        click.echo(f"  Temperature: {settings.openai_temperature}")
        click.echo(f"\nEmbedding Model: {settings.embedding_model}")
        click.echo(f"\nRetrieval Settings:")
        click.echo(f"  Top-K: {settings.retrieval_top_k}")
        click.echo(f"  Min Score: {settings.retrieval_min_score}")
        click.echo(f"  Max Context Tokens: {settings.retrieval_max_context_tokens}")
        click.echo("=" * 60)

    except Exception as e:
        click.echo(f"❌ Error loading configuration: {str(e)}", err=True)
        sys.exit(1)


def main():
    """Main entry point for CLI."""
    cli()


if __name__ == "__main__":
    main()
