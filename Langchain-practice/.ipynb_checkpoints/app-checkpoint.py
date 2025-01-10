from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
#from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

if load_dotenv() is False:
    print("Warning: .env file not found")
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


gemini_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=GOOGLE_API_KEY)
#gpt_llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)
#model = ChatOpenAI(model="gpt-4o-mini")


model = ChatOpenAI(model="gpt-3.5-turbo")
print(model.invoke("hey").content)