import os
import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

st.title("LangChain Chatbot")

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

# Track whether the conversation has started, so the system message can only
# be set once, before the first user message.
if "chat_started" not in st.session_state:
    st.session_state.chat_started = False
    st.session_state.chat_history = []

# --- Step 1: collect the system message before the conversation begins ---
if not st.session_state.chat_started:
    system_message = st.text_area(
        "System message",
        value="You are a helpful assistant",
        help="This sets the assistant's behavior for the whole conversation.",
    )
    if st.button("Start conversation"):
        st.session_state.chat_history = [SystemMessage(content=system_message)]
        st.session_state.chat_started = True
        st.rerun()

# --- Step 2: run the chat once the system message is locked in ---
else:
    # Show the active system message for reference.
    st.caption(f"System message: {st.session_state.chat_history[0].content}")

    # Replay the conversation so far (skip the system message).
    for message in st.session_state.chat_history[1:]:
        role = "user" if isinstance(message, HumanMessage) else "assistant"
        with st.chat_message(role):
            st.markdown(message.content)

    user_input = st.chat_input("Type your message here...")
    if user_input:
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        with st.chat_message("user"):
            st.markdown(user_input)

        result = model.invoke(st.session_state.chat_history)
        st.session_state.chat_history.append(AIMessage(content=result.content))
        with st.chat_message("assistant"):
            st.markdown(result.content)
