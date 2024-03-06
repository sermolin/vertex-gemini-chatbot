# Source and attribution: Heiko Hotz https://github.com/marshmellow77/vertex-gemini/blob/main/chatbot-gemini.py
# Source and attribution: https://sparkapps.net/building-a-gemini-pro-chatbot-with-googles-latest-model/

from dotenv import load_dotenv
import streamlit as st
import vertexai
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from typing import Any, List, Mapping, Optional
from langchain_google_vertexai import ChatVertexAI


# Initialize Vertex AI
load_dotenv()
project_name = os.getenv("VERTEXAI_PROJECT")
vertexai.init(project=project_name)

# Setting page title and header
st.set_page_config(page_title="Gemini Pro Chatbot", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>Gemini Pro Chatbot</h1>", unsafe_allow_html=True)

# Load chat model
@st.cache_resource
def load_chain():
    #llm = ChatVertexAI(model_name="chat-bison@002")
    llm = ChatVertexAI(model_name="gemini-pro")
    memory = ConversationBufferMemory()
    chain = ConversationChain(llm=llm, memory=memory)
    return chain

chatchain = load_chain()

# Initialise session state variables
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.sidebar.title("Sidebar")
clear_button = st.sidebar.button("Clear Conversation", key="clear")

# Reset conversation
if clear_button:
    st.session_state['messages'] = []

# Display previous messages
for message in st.session_state['messages']:
    role = message["role"]
    content = message["content"]
    with st.chat_message(role):
        st.markdown(content)

# Chat input
prompt = st.chat_input("You:")
if prompt:
    st.session_state['messages'].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = chatchain(prompt)["response"]
    st.session_state['messages'].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
