from langchain_ollama import ChatOllama
import streamlit as st

#your gemma:2b model should be up and running on Ollama before running this script

llm = ChatOllama(model="gemma:2b")


st.title("Gemma2b chat bot intro")

ip = st.text_input("what is your question?")


if ip:
    response = llm.invoke(ip)
    st.write(response.content)