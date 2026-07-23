from src.services.conversation_memory import ConversationMemory


def test_memory_adds_messages():

    memory = ConversationMemory()

    memory.add_user_message("Hello")

    memory.add_assistant_message("Hi!")

    history = memory.get_history()

    assert len(history) == 2

    assert history[0].role == "user"

    assert history[1].role == "assistant"