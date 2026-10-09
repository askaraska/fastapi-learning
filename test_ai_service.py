import pytest

from services.ai_service import AIService


def test_ai_service_requires_api_key(monkeypatch):
    monkeypatch.setattr(
        "services.ai_service.AI_API_KEY",
        "replace_with_your_real_key_later"
    )

    service = AIService()

    with pytest.raises(
        RuntimeError,
        match="Gemini API key is not configured"
    ):
        service.generate_response("Hello")