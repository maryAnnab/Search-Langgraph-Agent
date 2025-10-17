# 🔍 Search LangGraph Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-🦜-green.svg)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-🕸️-orange.svg)](https://langchain-ai.github.io/langgraph/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> ⚠️ **Early Stage Project** - This project is in active early development. Features and APIs may change significantly.

An advanced web search agent built with LangGraph and LangChain, designed to perform intelligent web searches and process information using AI-powered agents. This project explores the capabilities of LangGraph for building stateful, multi-agent workflows with web search integration[web:22][web:26].

## ✨ Features

- 🔍 **Intelligent Web Search** - Multi-step web search with query refinement
- 🤖 **AI-Powered Processing** - Advanced information extraction and synthesis using LLMs
- 🔄 **Stateful Workflows** - Persistent conversation management with LangGraph
- ⚙️ **Configurable Strategies** - Customizable search behavior and agent logic
- 🌐 **Multiple Providers** - Support for various search and LLM providers
- 💾 **Result Caching** - Optimized performance with intelligent caching
- 🛡️ **Safety First** - Built-in guardrails and validation

## 🎯 Use Cases

- Research automation with source validation
- Competitive intelligence gathering
- Content aggregation and summarization
- Real-time information retrieval for applications
- Market research and trend analysis

## 🛠️ Tech Stack

- **Python 3.12+** - Modern Python features and type hints
- **LangChain** - Framework for building LLM applications
- **LangGraph** - Library for stateful, multi-agent applications
- **UV** - Fast Python package installer and resolver
- **Pydantic** - Data validation using Python type annotations
- **Bright Data** - Enterprise-grade web data collection

## 📋 Prerequisites

Before you begin, ensure you have the following installed[web:26]:

- Python 3.12 or higher
- UV package manager ([installation guide](https://github.com/astral-sh/uv))
- Git
- API keys for your chosen LLM provider (OpenAI, Anthropic, etc.)

## 🚀 Quick Start

### Installation

1. **Clone the repository**
git clone https://github.com/maryAnnab/Search-Langgraph-Agent.git
cd Search-Langgraph-Agent


2. **Install dependencies with UV**
Install UV if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

Create virtual environment and install dependencies
uv venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
uv pip install -e .


3. **Set up environment variables**
Copy the example environment file
cp .env.example .env

Edit .env and add your API keys
Required: ANTHROPIC_API_KEY or OPENAI_API_KEY
Optional: BRIGHT_DATA_API_KEY

### Basic Usage

from search_agent import SearchAgent

Initialize the agent
agent = SearchAgent(
model="claude-3-5-sonnet-20241022",
max_iterations=5
)

Perform a search
result = agent.search("Latest developments in LangGraph")

Access results
print(result.answer)
print(result.sources)


### Running Examples

Run the basic search example
python examples/basic_search.py

Run the multi-step research example
python examples/research_workflow.py

Run with custom configuration
python examples/custom_config.py


## 🔧 Configuration

Create a `config.yaml` file to customize agent behavior[web:24][web:32]:

agent:
max_iterations: 5
temperature: 0.7
model: "claude-3-5-sonnet-20241022"

search:
provider: "bright_data"
max_results: 10
cache_ttl: 3600

graph:
checkpointer: "sqlite"
interrupt_before: ["tools"]


## 🧪 Development

### Setting Up Development Environment

Install development dependencies
uv pip install -e ".[dev]"

Install pre-commit hooks
pre-commit install


### Code Quality

Format code with black
black src/

Type checking with mypy
mypy src/

Lint with ruff
ruff check src/


## 📚 Documentation

- [Architecture Overview](docs/architecture.md)
- [API Reference](docs/api.md)
- [Tool Development Guide](docs/tools.md)
- [Deployment Guide](docs/deployment.md)

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a PR[web:2][web:15].

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🗺️ Roadmap

- [ ] Add support for additional search providers (Perplexity, Tavily)
- [ ] Implement result caching with Redis
- [ ] Add streaming responses
- [ ] Create web UI with Gradio/Streamlit
- [ ] Add multi-language support
- [ ] Implement RAG capabilities
- [ ] Add evaluation framework
- [ ] Deploy to LangGraph Cloud

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details[attached_file:1].

## 🙏 Acknowledgments

- Built with [LangChain](https://www.langchain.com/) and [LangGraph](https://langchain-ai.github.io/langgraph/)[web:22][web:26]
- Search powered by [Bright Data](https://brightdata.com/)
- Inspired by the LangGraph agent patterns and examples[web:27][web:30]

## 📧 Contact

**Author:** maryAnnab  
**Repository:** [github.com/maryAnnab/Search-Langgraph-Agent](https://github.com/maryAnnab/Search-Langgraph-Agent)

---

⭐ If you find this project useful, please consider giving it a star!
