from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["HUGGINFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")


# fastapi

app = FastAPI(
    title="Langchain server",
    version="1.0",
    description="A simple Langchain server"
)

mistral_repo = "mistralai/Mistral-7B-Instruct-v0.2"
llama3_repo = "meta-llama/Meta-Llama-3-8B-Instruct"

# add_routes(app, HuggingFaceEndpoint(), path="/huggingface")

# creating diffferent models for routing
mistral_model = HuggingFaceEndpoint(repo_id=mistral_repo, max_lenght=128, temperature=0.7)
llama3_model = HuggingFaceEndpoint(repo_id=llama3_repo, max_lenght=128, temperature=0.7)

# creatiing different prompts from each LLM
prompt_mistral = ChatPromptTemplate.from_template("Write me a essay on {topic} in about 100 words.")
prompt_llama3 = ChatPromptTemplate.from_template("Write me a poem on {topic} in about 100 words.")


# routing
add_routes(app, prompt_mistral|mistral_model, path="/essay")
add_routes(app, prompt_llama3|llama3_model, path="/poem")



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)