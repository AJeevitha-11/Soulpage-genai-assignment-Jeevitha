import streamlit as st
import wikipedia

from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain.llms.fake import FakeListLLM

# Streamlit setup
st.set_page_config(page_title="Conversational Knowledge Bot")
st.title("🧠 Conversational Knowledge Bot (Local Stable Version)")

# Wikipedia tool
def wikipedia_search(query):
    try:
        return wikipedia.summary(query, sentences=3)
    except Exception:
        return "No information found."

wiki_tool = Tool(
    name="Wikipedia",
    func=wikipedia_search,
    description="Useful for answering factual questions."
)

# Simple fake LLM (local)
llm = FakeListLLM(
    responses=[
        "Use Wikipedia tool to answer this question."
    ]
)

# Memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Agent
agent = initialize_agent(
    tools=[wiki_tool],
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=False
)

# Chat storage
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Directly use Wikipedia tool for response
    response = wikipedia_search(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
