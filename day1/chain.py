import os
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt import prompt
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()

def create_chain():
    #gọi model model="gemini-pro"
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY"), temperature=0.7)
    
    #kết hợp llm với PromptTemplate thành 1 chain
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain