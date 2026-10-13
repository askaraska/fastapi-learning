
import pytest
from pydantic import ValidationError

from schemas.chat import ChatRequest, ChatResponse


def test_valid_chat_request():
    request = ChatRequest(
        conversation_id="test-session-001",
        message="Explain FastAPI"
    )

    assert request.conversation_id == "test-session-001"
    assert request.message == "Explain FastAPI"


def test_empty_chat_message():
    with pytest.raises(ValidationError):
        ChatRequest(
            conversation_id="test-session-001",
            message=""
        )


def test_chat_message_too_long():
    with pytest.raises(ValidationError):
        ChatRequest(
            conversation_id="test-session-001",
            message="a" * 2001
        )


def test_chat_response():
    response = ChatResponse(
        conversation_id="test-session-001",
        reply="FastAPI is a Python framework."
    )

    assert response.conversation_id == "test-session-001"
    assert response.reply == "FastAPI is a Python framework."


def test_blank_conversation_id_is_rejected():
    with pytest.raises(ValidationError):
        ChatRequest(
            conversation_id="   ",
            message="Hello"
        )
