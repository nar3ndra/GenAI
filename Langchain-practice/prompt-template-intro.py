from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import streamlit as st


llm = ChatOllama(model="gemma:2b")

template = "what is the currency of {country} ? Answer in one short paragraph."
prompt = PromptTemplate(input_variables=["country"],
                          template=template)


country = st.text_input("which country")

if country:
    response = llm.invoke(prompt.format(country=country))   
    st.write(response.content)


