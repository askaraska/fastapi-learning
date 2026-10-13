from fastapi import APIRouter, HTTPException

from schemas.chat import ChatRequest, ChatResponse
from services.ai_service import AIService
from services.chat_history import ChatHistory


router = APIRouter(prefix="/chat", tags=["Chat"])

ai_service = AIService()
chat_history = ChatHistory()


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    conversation_id = request.conversation_id

    # Retrieve previous messages before adding the new message.
    previous_history = chat_history.get_history(conversation_id)

    # Store the current user message.
    chat_history.add_message(
        conversation_id,
        "user",
        request.message
    )

    try:
        # Build context from previous messages and the current message.
        context_messages = previous_history + [
            {
                "role": "user",
                "content": request.message
            }
        ]

        context_text = "\n".join(
            f"{message['role']}: {message['content']}"
            for message in context_messages
        )

        reply = ai_service.generate_response(context_text)

        # Save the AI reply only after successful generation.
        chat_history.add_message(
            conversation_id,
            "assistant",
            reply
        )

        return ChatResponse(
            conversation_id=conversation_id,
            reply=reply
        )

    except Exception:
        raise HTTPException(
            status_code=503,
            detail=(
                "AI service is temporarily unavailable. "
                "Please try again later."
            )
        )
