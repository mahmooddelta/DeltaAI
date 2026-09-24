# 🤖 Delta AI

AI chatbot backend built with **Python, LangChain, LangGraph, FastAPI, and PostgreSQL**.

## ✨ Features

* AI Agent with LangGraph
* PostgreSQL conversation persistence
* FastAPI REST API
* Swagger API documentation
* Interactive terminal chat
* Tool calling

## 🛠️ Tech Stack

* Python
* FastAPI
* LangChain
* LangGraph
* PostgreSQL
* SQLAlchemy
* Psycopg
* Uvicorn

## 🚀 Run

Install dependencies:

```bash
uv sync
```

Configure `.env`:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@127.0.0.1:5432/chat_bot
LANGGRAPH_DATABASE_URL=postgresql://postgres:password@127.0.0.1:5432/chat_bot
OPENAI_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

Start the API:

```bash
uv run python main.py
```

API:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

Run the Agent from terminal:

```bash
uv run python cli.py
```

## 📁 Structure

```text
delta_chatbot/
├── main.py
├── console.py
├── pyproject.toml
└── src/
    ├── agent/
    └── domain/
```

## 👨‍💻 Author

**Mahmood Afzali**

Backend Developer & AI Engineer
