from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
from langchain_core.messages import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()

langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_api_key is None:
    raise ValueError("LANGCHAIN_API_KEY environment variable is not set.")

