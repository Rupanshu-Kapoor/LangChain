import requests
import streamlit as st


def get_mistral_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={"input": {"topic": input_text}})
    
    return response.json()["output"]


def get_llama3_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={"input": {"topic": input_text}})
    
    return response.json()["output"]





# streamlit app
st.title("LLMs routing using LangServe")

essay_text = st.text_input("Write a essay on:")
if essay_text:
    st.write(get_mistral_response(essay_text))
poem_text = st.text_input("Write a poem on:")
if poem_text:
    st.write(get_llama3_response(poem_text))