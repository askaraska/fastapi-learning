# FastAPI Learning Project

A hands-on Python backend project developed while learning FastAPI, REST APIs, database operations, authentication, automated testing, asynchronous programming, and Generative AI integration.

## Features

- REST API development using FastAPI
- Product CRUD operations using SQLite and SQLAlchemy
- User authentication with JWT
- Request validation and response schemas using Pydantic
- Modular API routing
- Automated testing with pytest and FastAPI TestClient
- Asynchronous endpoints and background tasks
- Custom middleware and application lifespan management
- Gemini AI integration using Google's GenAI Python SDK
- Chat endpoint with conversation IDs and in-memory conversation history
- Environment-based configuration for AI credentials

## Technology Stack

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- JWT
- pytest
- Google GenAI SDK
- Uvicorn

## Project Structure

```text
fastapi-learning/
├── main.py
├── config.py
├── database.py
├── models/
├── routers/
├── schemas/
├── services/
├── utils/
├── test_main.py
├── test_basic.py
├── test_ai_service.py
├── test_chat_schema.py
├── test_chat_history.py
├── test_database.py
├── requirements.txt
└── README.md
```

The structure above highlights the main project files. Additional files may exist in the repository.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/askaraska/fastapi-learning.git
cd fastapi-learning
```

### 2. Create a virtual environment

For Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file in the project root:

```dotenv
AI_PROVIDER=gemini
AI_API_KEY=your_gemini_api_key
```

Replace the example value with your own valid Gemini API key. Never publish your API key or commit `.env` to GitHub.

The project also uses a JWT secret in `config.py`. Preserve your existing configuration and keep production secrets out of source control.

### 5. Run the application

```powershell
uvicorn main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## Running Tests

Run the automated test suite:

```powershell
pytest
```

AI-related tests use mocked responses where appropriate, allowing the tests to run without making a live Gemini request for every test.

## Chat API Example

Send a POST request to `/chat` with this JSON body:

```json
{
  "conversation_id": "demo-session-001",
  "message": "Explain FastAPI"
}
```

The API returns a conversation ID and an AI-generated reply. Reusing a conversation ID allows previous messages to be included as context.

## Current Limitations

- Conversation history is stored in application memory and is lost when the application restarts.
- A valid Gemini API key is required for live AI responses.
- Persistent conversation storage and production-ready deployment configuration can be added in future improvements.

## Learning Progress

This repository demonstrates hands-on learning and implementation of:

- FastAPI fundamentals and request parameters
- Pydantic validation and response models
- Modular application architecture
- Database CRUD operations
- JWT authentication
- Automated testing and error handling
- Asynchronous programming and background tasks
- GenAI service integration and chat history

## Future Improvements

- Persistent conversation history
- More comprehensive integration tests
- Improved AI error handling and logging
- Production deployment
- Stronger production secret management