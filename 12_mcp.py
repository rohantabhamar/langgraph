from langgraph.graph import StateGraph,START
from dotenv import load_dotenv
from models import get_model
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage,BaseMessage
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode , tools_condition
from langchain_core.tools import tool
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
import os

load_dotenv()

os.environ["LANGCHAIN_PROJECT"] = 'MCP test'

llm = get_model()

# MCP client
client = MultiServerMCPClient(
        {"arith": {
            "transport": "stdio",
            "command": "python",          
            "args": ["E:/Rohanta_AI_workbook/MCP/local_server/expence_reacker_mcp_server/main.py"],
    }}
    )

class ChatSate(TypedDict):
    messages : Annotated[list[BaseMessage],add_messages]

async def build_graph():
    tools = await client.get_tools()

    llm_with_tools = llm.bind_tools(tools)

    async def chat_node(ChatSate):
        """
        LLM that gives ans or call tools as per requirments
        """
        message = ChatSate["messages"]
        response = llm_with_tools.invoke(message)
        return {"messages":[response]}
    
    tool_node = ToolNode(tools)

    graph = StateGraph(ChatSate)

    graph.add_node("chat_node",chat_node)
    graph.add_node("tools",tool_node)
    graph.add_edge(START,"chat_node")

    # If the LLM asked for a tool, go to ToolNode; else finish
    graph.add_conditional_edges("chat_node",tools_condition)
    graph.add_edge("tools","chat_node")

    chatbot = graph.compile()

    return chatbot


async def main():

    chatbot = await build_graph()

    # running the graph
    result = await chatbot.ainvoke({"messages": [HumanMessage(content="roll the dices and give me number")]})

    print(result['messages'][-1].content)

if __name__ == '__main__':
    asyncio.run(main())