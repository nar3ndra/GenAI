from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain.globals import set_debug



# Simple sequential chain
set_debug(True)

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", api_key=google_api_key)




text = "what Country have the currency {currency}? Just tell me the name of the Country, nothing else"

template = PromptTemplate(input_variables=["currency"],
                          template=text)


second_prompt = "what is the Capital city of the {country} ? answer exactly with on word."

template2 = PromptTemplate(input_variables=["country"],
                           template=second_prompt)

first_chain = template | llm | StrOutputParser()
second_chain = template2 | llm 
# response = first_chain.invoke({
#     "country":"India"
# })

final_response = first_chain | second_chain | StrOutputParser()

print(final_response.invoke({"currency":"INR"}).content)