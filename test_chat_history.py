from services.chat_history import ChatHistory


def test_add_and_get_history():
    history = ChatHistory()

    history.add_message(
        "conversation-1",
        "user",
        "Hello"
    )

    messages = history.get_history("conversation-1")

    assert messages == [
        {"role": "user", "content": "Hello"}
    ]


def test_conversations_are_separate():
    history = ChatHistory()

    history.add_message(
        "conversation-1",
        "user",
        "Hello"
    )

    history.add_message(
        "conversation-2",
        "user",
        "Good morning"
    )

    assert len(history.get_history("conversation-1")) == 1
    assert history.get_history("conversation-2") == [
        {"role": "user", "content": "Good morning"}
    ]


def test_unknown_conversation_is_empty():
    history = ChatHistory()

    assert history.get_history("unknown") == []