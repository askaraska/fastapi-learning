from pydantic import BaseModel, Field, field_validator


class ChatRequest(BaseModel):
    conversation_id: str = Field(
        min_length=1,
        max_length=100
    )
    message: str = Field(
        min_length=1,
        max_length=2000
    )

    @field_validator("conversation_id")
    @classmethod
    def validate_conversation_id(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Conversation ID cannot be blank.")

        return value


class ChatResponse(BaseModel):
    conversation_id: str
    reply: str
