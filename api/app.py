from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_deepseek import ChatDeepSeek
from langserve import add_routes # create different routes to diff llm models
import uvicorn
import os
from dotenv import load_dotenv
# from langchain_community.llms import Ollama

load_dotenv()

os.environ["DEEPSEEK_API_KEY"]=os.getenv("DEEPSEEK_API_KEY") # we are setting env variables which are then looked by the lanchain library

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

add_routes(
    app,
    ChatDeepSeek(model="deepseek-chat"),
    path="/deepseek" # specifying a route to your llm model
)
model=ChatDeepSeek(model="deepseek-chat")
##ollama llama2
# llm=Ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay" # API url ending


)
#this one is for ollama
# add_routes(
#     app,
#     prompt2|llm,
#     path="/poem"
# )
add_routes(
    app,
    prompt2|model,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
