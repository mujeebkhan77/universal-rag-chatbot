from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import LLM_MODEL, TEMPERATURE
from dotenv import load_dotenv
import os


load_dotenv()


def get_llm():

    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=TEMPERATURE
    )

    return llm