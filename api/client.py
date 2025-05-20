import requests
import streamlit as st

def get_deepseek_essay_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

def get_deepseek_poem_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}}) # 'topic' name corresponds to {topic} in prompt

    return response.json()['output']['content']
# def get_ollama_response(input_text):
#     response=requests.post(
#     "http://localhost:8000/poem/invoke",
#     json={'input':{'topic':input_text}})

#     return response.json()['output']

    ## streamlit framework

st.title('Langchain Demo With DeepSeek API')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

# we already created API in app.py, so now depending on input in streamlit
# we either post one API call or another (to the same provider)
if input_text:
    st.write(get_deepseek_essay_response(input_text))
if input_text1:
    st.write(get_deepseek_poem_response(input_text1))

# if input_text1:
#     st.write(get_ollama_response(input_text1))
