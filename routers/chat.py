
from fastapi import APIRouter, HTTPException

from schemas.chat import ChatRequest, ChatResponse
from services.ai_service import AIService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

ai_service = AIService()


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        reply = ai_service.generate_response(
            request.message
        )

        return ChatResponse(reply=reply)

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="AI service is temporarily unavailable. Please try again later."
        )