import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="Agentic Insurance Claims Assistant",
    page_icon="🩺",
    layout="wide",
)

st.title("🩺 Agentic Insurance Claims Assistant")
st.caption("Powered by Azure AI Search + Azure OpenAI")

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.header("About")

    st.write(
        """
This application demonstrates an Agentic RAG architecture using:

- Azure AI Search
- Azure OpenAI
- Hybrid Search
- Query Rewriting
- Planner Agent
- Specialized Agents
- Answer Verification
"""
    )

    st.divider()

    if st.button("🗑 Clear Conversation"):

        st.session_state.messages = []

        st.rerun()

# -----------------------------
# Conversation Memory
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Planner",
                message["planner"],
            )

            col2.metric(
                "Verified",
                "✅" if message["verified"] else "❌",
            )

            col3.metric(
                "Confidence",
                message["confidence"],
            )

            with st.expander("Sources"):

                for source in message["sources"]:

                    st.write(
                        f"📄 {source['source']} | Chunk {source['chunk_id']}"
                    )

# -----------------------------
# User Input
# -----------------------------

question = st.chat_input(
    "Ask an insurance question..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = requests.post(
                API_URL,
                json={
                    "question": question
                },
            )

            result = response.json()

        st.markdown(result["answer"])

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Planner",
            result["planner"],
        )

        col2.metric(
            "Verified",
            "✅" if result["verified"] else "❌",
        )

        col3.metric(
            "Confidence",
            result["confidence"],
        )

        with st.expander("Sources"):

            for source in result["sources"]:

                st.write(
                    f"📄 {source['source']} | Chunk {source['chunk_id']}"
                )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"],
            "planner": result["planner"],
            "verified": result["verified"],
            "confidence": result["confidence"],
            "sources": result["sources"],
        }
    )