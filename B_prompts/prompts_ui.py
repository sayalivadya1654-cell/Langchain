import streamlit as st
from langchain_ollama import ChatOllama

st.title("🤖 Ollama Chatbot")

llm = ChatOllama(model="llama3.2")

user_input = st.text_input("Enter your question:")

if st.button("Generate"):
    if user_input:
        response = llm.invoke(user_input)
        st.write("### Response:")
        st.write(response.content)