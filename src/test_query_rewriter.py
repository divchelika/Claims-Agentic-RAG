from src.services.conversation_memory import ConversationMemory
from src.services.query_rewriter import QueryRewriter


memory = ConversationMemory()

memory.add_user_message(
    "Who is the claims adjuster?"
)

memory.add_assistant_message(
    "The claims adjuster is J. Whitfield."
)

rewriter = QueryRewriter()

question = "What is his email?"

new_question = rewriter.rewrite(
    question,
    memory,
)

print("\nOriginal:")
print(question)

print("\nRewritten:")
print(new_question)