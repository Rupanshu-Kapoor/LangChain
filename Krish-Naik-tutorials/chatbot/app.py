from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import LLMChain


import streamlit as st
import os

from dotenv import load_dotenv

load_dotenv()


os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# for langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

st.title("LangChain Demo with Open Source LLM")
input_text = st.text_input("Please provide your question:")

# defining HuggingFaceEndpoint
repo_id = repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")


hf_llm = HuggingFaceEndpoint(repo_id=repo_id, max_lenght=128, temperature=0.7, token=hf_token)
output_parser = StrOutputParser()
chain = prompt|hf_llm|output_parser


if input_text:
    st.write(chain.invoke({"question": input_text}))