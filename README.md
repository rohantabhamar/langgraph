# 🤖 LangGraph Chatbot

A conversational AI chatbot built using **LangGraph**, **LangChain**, **Groq (LLaMA 3.1)**, and **Streamlit** — featuring multi-turn memory, streaming responses, and multi-conversation thread management.

This repo also contains step-by-step LangGraph practice notebooks covering core concepts from basic workflows to persistence and chatbots.

---

## 🗂️ Project Structure

```
langgarph/
│
├── 📓 LangGraph Tutorial Notebooks
│   ├── 1_bmi_workflow.ipynb                    # Simple node/edge workflow
│   ├── 2_simple_llm_workflow.ipynb             # LLM inside a graph node
│   ├── 3_prompt_chaining.ipynb                 # Sequential prompt chaining
│   ├── 4_parallel_work_flow.ipynb              # Parallel node execution
│   ├── 5_parallel_work_flow_with_LLM.ipynb     # Parallel LLM calls
│   ├── 6_conditional_workflow.ipynb            # Conditional edges
│   ├── 7_conditional_workflow_with_LLM.ipynb   # LLM-driven routing
│   ├── 8_xpost.ipynb                           # Real-world LLM workflow
│   ├── 9_chat_bot.ipynb                        # Chatbot prototype in notebook
│   └── 10_persistence.ipynb                    # MemorySaver & thread memory
│
├── 🤖 Chatbot App
│   ├── chatbot_langgraoh_backend.py            # LangGraph graph, state, LLM, memory
│   └── chatbot_streamlit_frontend.py           # Streamlit UI — streaming & multi-thread
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 Chatbot — How It Works

### Backend — `chatbot_langgraoh_backend.py`
- Defines a **LangGraph `StateGraph`** with a single `chat_node`
- Uses **`MemorySaver`** as a checkpointer for persistent conversation memory
- Connects to **Groq API** (`llama-3.1-8b-instant`) via LangChain's `ChatGroq`
- State typed using `TypedDict` with `add_messages` for automatic message accumulation

```
START → chat_node → END
```

### Frontend — `chatbot_streamlit_frontend.py`
- Multi-conversation sidebar with **New Chat** button
- Each conversation gets a unique **UUID thread ID** passed as `config` to LangGraph
- Responses stream token-by-token using `chatbot.stream()` + `st.write_stream()`
- Past conversations loadable via `chatbot.get_state()` from LangGraph memory

---

## 📓 LangGraph Notebooks — Learning Path

| Notebook | Concept |
|---|---|
| `1_bmi_workflow` | Basic StateGraph with nodes and edges |
| `2_simple_llm_workflow` | Integrating an LLM into a graph node |
| `3_prompt_chaining` | Sequential chained prompts |
| `4_parallel_work_flow` | Running nodes in parallel |
| `5_parallel_work_flow_with_LLM` | Parallel LLM calls |
| `6_conditional_workflow` | Conditional edges and routing |
| `7_conditional_workflow_with_LLM` | LLM-driven conditional routing |
| `8_xpost` | Real-world multi-step LLM workflow |
| `9_chat_bot` | Chatbot prototype in a notebook |
| `10_persistence` | MemorySaver, thread IDs, state persistence |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
https://github.com/rohantabhamar/langgraph.git
cd <langgraph>
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate       # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file
```
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the chatbot
```bash
streamlit run chatbot_streamlit_frontend.py
```

---

## ✨ Chatbot Features

| Feature | Detail |
|---|---|
| 🧠 Multi-turn memory | LangGraph `MemorySaver` persists conversation per thread |
| 🔀 Multiple conversations | Each chat gets a UUID thread ID; switch via sidebar |
| ⚡ Streaming responses | Token-by-token streaming with `st.write_stream` |
| 🦙 LLM | Groq `llama-3.1-8b-instant` — fast inference |
| 🎛️ New Chat | Resets history and creates a fresh thread |
| 📜 Load past chats | Reload any previous conversation from memory |

---

## 🛠️ Tech Stack

- [LangGraph](https://github.com/langchain-ai/langgraph) — stateful agent graph framework
- [LangChain](https://www.langchain.com/) — LLM tooling and message types
- [Groq](https://groq.com/) — ultra-fast LLM inference (LLaMA 3.1 8B)
- [Streamlit](https://streamlit.io/) — frontend UI
- [Python 3.11](https://www.python.org/)

---

## 👤 Author

**Rohanta Bhamare**  
AI/ML Engineer | MSc AI Candidate @ BSBI Berlin  
[GitHub](https://github.com/rohantabhamar) · [Email](mailto:rohantabhamare22@gmail.com)
