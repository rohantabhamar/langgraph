from langgraph.graph import StateGraph, END, START
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
import sqlite3
from models import get_embeddings,get_model
import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph,END,START
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode,tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool

import requests
import random

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    max_tokens=1024,
    temperature=0.1,
    api_key=os.getenv("GROQ_API_KEY")
)
# Tools

search_tool = DuckDuckGoSearchRun(region = "us-en")

@tool
def calculator(first_num:float,second_num:float,operation:str) -> dict:
    """
    Perfom a basic arithmatic operation on two numbers.
    Supports operations: add,sub,nul,div
    """
    try:
        if operation == "add":
            result = first_num + second_num
        elif operation == "sub":
            result = first_num - second_num
        elif operation == "mul":
            result = first_num * second_num
        elif operation == "div":
            if second_num == 0:
                return {"error":"Division by zero is nit possible"}
            result = first_num/second_num
        
        else:
            return {"error":f"Unsupported operation {operation}"}
        return {"first_num": first_num, "second_num": second_num, "operation": operation, "result": result}
    except Exception as e:
        return {"error":str(e)}

@tool
def get_stock_price(symbol:str) -> dict:
    """
    Fetch latest stock price for a given symbol (e.g. 'AAPL', 'TSLA') 
    using Alpha Vantage with API key in the URL.
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=A8PUQ61B5VJMD17O"
    r = requests.get(url)
    return r.json()


tools = [get_stock_price,search_tool,calculator]

llm_with_tools = llm.bind_tools(tools)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]

def chat_node(ChatSate):
    """
    LLM that gives ans or call tools as per requirments
    """
    message = ChatSate["messages"]
    response = llm_with_tools.invoke(message)
    return {"messages":[response]}
    
tool_node = ToolNode(tools)


conn = sqlite3.connect(database="chatbot.db",check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)

graph.add_node("chat_node",chat_node)
graph.add_node("tools",tool_node)



graph.add_edge(START,"chat_node")
# If the LLM asked for a tool, go to ToolNode; else finish
graph.add_conditional_edges("chat_node",tools_condition)
graph.add_edge("tools","chat_node")

chatbot = graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():
    all_threads=set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads)



# print(responce)