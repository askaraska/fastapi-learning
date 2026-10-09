import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = "-E5zpcW9nxkTyOmpOqQYu_k0xWy5ePhVRaHEYkmznZA"

AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")
AI_API_KEY = os.getenv("AI_API_KEY", "")