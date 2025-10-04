# Code RAG Agent

A production-ready Python service for intelligent code retrieval and question answering using RAG (Retrieval-Augmented Generation).

**Author:** Sandeep G
**Copyright:** © 2025 Sandeep G
**License:** Apache License 2.0

## Features

- 🔍 **Intelligent Code Search**: Self-query retrieval with automatic metadata filtering
- 🧠 **Smart Question Answering**: Answers complex questions about your codebase
- 🔌 **Pluggable Architecture**: Swap LLM providers (OpenAI, Claude) and vector stores (Pinecone, Weaviate)
- ⚡ **Production-Ready**: Cost-efficient, fast, and reliable

## Quick Start

### Installation

#### From PyPI (Recommended)

```bash
pip install code-rag-agent
```

#### From Source

```bash
# Clone repository
git clone https://github.com/sandeepgovi/code-rag-agent
cd code-rag-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode
pip install -e .
```

### Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API keys
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_INDEX_NAME=your-index-name
PINECONE_NAMESPACE=default
OPENAI_API_KEY=your-openai-api-key
```

### Usage

#### CLI

```bash
# Ask questions about your codebase
code-rag-agent query "What methods are in SongService?"

# Use verbose mode for detailed output
code-rag-agent query "How does payment processing work?" --verbose

# Show configuration
code-rag-agent info
```

#### Example Output

```bash
$ code-rag-agent query "What GET endpoints exist in MusicController?"

MusicController has 3 GET endpoints: getSongById (/{id}), getAllSongs (/all),
and searchSongs (/search).

⏱️  Response time: 4320ms (4.32s)
```

## Architecture

Built with:
- **LangChain**: Self-query retrieval and LLM orchestration
- **Pinecone**: Vector store (pluggable)
- **OpenAI**: LLM provider (pluggable)
- **Pydantic**: Configuration management

## Development

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/ tests/
```

## License

Apache License 2.0 - see LICENSE file for details.