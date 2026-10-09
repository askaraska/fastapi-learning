import pytest
from pydantic import ValidationError

from schemas.chat import ChatRequest, ChatResponse


def test_valid_chat_request():
    request = ChatRequest(
        message="Explain FastAPI"
    )

    assert request.message == "Explain FastAPI"


def test_empty_chat_message():
    with pytest.raises(ValidationError):
        ChatRequest(message="")


def test_chat_message_too_long():
    with pytest.raises(ValidationError):
        ChatRequest(message="a" * 2001)


def test_chat_response():
    response = ChatResponse(
        reply="FastAPI is a Python framework."
    )

    assert response.reply == "FastAPI is a Python framework."