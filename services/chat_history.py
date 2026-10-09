class ChatHistory:

    def __init__(self):
        self.conversations: dict[str, list[dict[str, str]]] = {}

    def add_message(
        self,
        conversation_id: str,
        role: str,
        content: str
    ) -> None:
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = []

        self.conversations[conversation_id].append({
            "role": role,
            "content": content
        })

    def get_history(
        self,
        conversation_id: str
    ) -> list[dict[str, str]]:
        return self.conversations.get(conversation_id, [])