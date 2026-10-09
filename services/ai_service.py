
from google import genai

from config import AI_API_KEY


class AIService:

    def generate_response(self, message: str) -> str:
        if (
            not AI_API_KEY
            or AI_API_KEY == "replace_with_your_real_key_later"
        ):
            raise RuntimeError(
                "Gemini API key is not configured."
            )

        client = genai.Client(
            api_key=AI_API_KEY
        )

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=message
        )

        if not response.text:
            raise RuntimeError(
                "Gemini returned an empty response."
            )

        return response.text