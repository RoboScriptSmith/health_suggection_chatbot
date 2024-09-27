# -*- coding: utf-8 -*-
"""chatbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wuzo5vzWBeiPbDeAM38kuyux7QZsOQmn
"""

import google.generativeai as genai
import streamlit as st
import os

gemini_api_key = "AIzaSyAo4RnXH1xfNXp5MIYvI95YJLZytWUo-Zw"  # upload the api key

genai.configure(api_key=gemini_api_key)

## function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


## initialize our streamlit app
st.set_page_config(page_title="medical chatbot")
st.header("medical LLM Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question related to the medical field")

if submit and input:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
         st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("The Chat History is")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")


