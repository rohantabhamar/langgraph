# LangGraph Chatbot Suite

Production-grade LangGraph implementation covering core concepts, 
advanced patterns, and a 7-variant chatbot application suite.

## Notebooks — learning path
| File | Concept |
|---|---|
| 1_bmi_workflow | Basic nodes and edges |
| 2_simple_llm_workflow | LLM inside a graph node |
| 3_prompt_chaining | Sequential chained prompts |
| 4_parallel_work_flow | Parallel node execution |
| 5_parallel_work_flow_with_LLM | Parallel LLM calls |
| 6_conditional_workflow | Conditional edges |
| 7_conditional_workflow_with_LLM | LLM-driven routing |
| 8_xpost | Real-world multi-step workflow |
| 9_chat_bot | Chatbot prototype |
| 10_persistence | MemorySaver + thread memory |
| 11_tools | Tool calling in LangGraph |
| 12_mcp.py | MultiServerMCPClient async integration |
| 13_rag | RAG inside a LangGraph graph |
| 14_HITL | Human-in-the-Loop with interrupt() + Command(resume=) |
| 15_subgraph | Subgraph composition patterns |

## Chatbot suite — 7 architectural variants
| Backend | Frontend | Key feature |
|---|---|---|
| chatbot_langgraoh_backend.py | chatbot_streamlit_frontend.py | Streaming + multi-thread memory |
| chatbot_with_logterm_memory_backend.py | chatbot_with_logterm_memory_frontend.py | SQLite long-term memory |
| langgraph_backend.py | streamlit_frontend_streaming.py | st.write_stream token streaming |
| langgraph_database_backend.py | streamlit_frontend_database.py | SQLite session persistence |
| langgraph_tool_backend.py | streamlit_frontend_tool.py | DuckDuckGo + stock price tools |
| langraph_rag_backend.py | streamlit_rag_frontend.py | Per-thread PDF upload + FAISS RAG |
| langgraph_mcp_backend.py | streamlit_frontend_mcp.py | MultiServerMCPClient async |

## Tech stack
LangGraph · LangChain · LangSmith · FastMCP · MultiServerMCPClient ·
SqliteSaver · AsyncSqliteSaver · DuckDuckGo · Streamlit · Groq Llama-3.1
