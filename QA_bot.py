from langchain.llms import OpenAI

from dotenv import load_dotenv

import streamlit as st

import os 
load_dotenv()

def get_response(question):
    llm = OpenAI(temperature = 0.8, openai_api_key = os.getenv("OPENAI_API_KEY"))
    response = llm.invoke(question)
    return response

st.set_page_config(page_title="Q&A Bot")

st.header("Q&A Model")


input = st.text_input("Input: ",key = "input")

response = get_response(input)

submit = st.button("Ask the Question")

if submit:
    st.subheader("Response is")
    st.write(response)

