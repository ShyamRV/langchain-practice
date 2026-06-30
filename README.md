# LangChain Practice

Hands-on LangChain exercises covering LLM basics, chat models, and embeddings.

## Project Structure

```
langchain-practice/
├── 00-setup/
│   └── check_langchain_version.py   # Verify LangChain installation
├── 01-llm-basics/
│   └── anthropic_llm_invoke.py      # Basic LLM invoke with Anthropic
├── 02-chat-models/
│   └── anthropic_chat_invoke.py     # Chat model invoke with Anthropic
├── 03-embeddings/
│   ├── voyage_embedding_basics.py   # Single-text Voyage embedding
│   └── voyage_document_similarity.py # Document similarity search
├── requirements.txt
└── .env                             # API keys (not committed)
```

## Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/ShyamRV/langchain-practice.git
   cd langchain-practice
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   # source venv/bin/activate   # macOS / Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add API keys**

   Create a `.env` file in the project root:

   ```env
   ANTHROPIC_API_KEY=your_anthropic_key
   VOYAGE_API_KEY=your_voyage_key
   ```

## Running Scripts

```bash
python 00-setup/check_langchain_version.py
python 01-llm-basics/anthropic_llm_invoke.py
python 02-chat-models/anthropic_chat_invoke.py
python 03-embeddings/voyage_embedding_basics.py
python 03-embeddings/voyage_document_similarity.py
```

## Lessons

| Folder | Topic | Provider |
|--------|-------|----------|
| `01-llm-basics` | LLM invoke | Anthropic (Claude) |
| `02-chat-models` | Chat model invoke | Anthropic (Claude) |
| `03-embeddings` | Embeddings & similarity | Voyage AI |
