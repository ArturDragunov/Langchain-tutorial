from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser # default output parser for llm response

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["DEEPSEEK_API_KEY"]=os.getenv("DEEPSEEK_API_KEY") # we are setting env variables which are then looked by the lanchain library
## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With DEEPSEEK API')
input_text=st.text_input("Search the topic u want") # visible for user

# deepseek LLm 
llm=ChatDeepSeek(model="deepseek-chat")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser # it works like a pipeline. With the help of Langchain you create steps and then you put them in a chain. 

if input_text:
    st.write(chain.invoke({'question':input_text}))

# to run the application, write streamlit run .\chatbot\app.py in the console