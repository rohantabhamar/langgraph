# 🤖 LangGraph Chatbot

A conversational AI chatbot built step-by-step using **LangGraph**, **LangChain**, **Groq (LLaMA 3.1)**, and **Streamlit** — featuring multi-turn memory, streaming responses, and multi-conversation thread management.

---

## 🗂️ Project Structure

```
langgarph/
│
├── chatbot_langgraoh_backend.py    # LangGraph graph definition, state, LLM, memory
├── chatbot_streamlit_frontend.py   # Streamlit UI with sidebar, streaming, thread switching
├── .env                            # API keys (not tracked in git)
├── .gitignore
└── README.md
```

---

## 🧠 How It Works

### Backend — `chatbot_langgraoh_backend.py`
- Defines a **LangGraph `StateGraph`** with a single `chat_node`
- Uses **`MemorySaver`** as a checkpointer for persistent conversation memory
- Connects to **Groq API** (`llama-3.1-8b-instant`) via LangChain's `ChatGroq`
- State is typed using `TypedDict` with `add_messages` annotation for automatic message accumulation

```
START → chat_node → END
```

### Frontend — `chatbot_streamlit_frontend.py`
- Multi-conversation sidebar with **New Chat** button
- Each conversation gets a unique **UUID thread ID** passed as `config` to LangGraph
- Responses stream token-by-token using `chatbot.stream()` + `st.write_stream()`
- Past conversations loadable via `chatbot.get_state()` from LangGraph's memory

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/rohantabhamar/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install streamlit langgraph langchain langchain-groq langchain-core python-dotenv
```

### 4. Set up your `.env` file
```
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the app
```bash
streamlit run chatbot_streamlit_frontend.py
```

---

## ✨ Features

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

## 📌 Notes

- The `venv/` folder and `.env` file are excluded from git via `.gitignore`
- Streamlit may show `ModuleNotFoundError: torchvision` warnings in the terminal — these are harmless file-watcher warnings from the `transformers` package and do not affect functionality. To silence them, add this to `.streamlit/config.toml`:

```toml
[server]
fileWatcherType = "none"
```

---

## 👤 Author

**Rohanta Bhamare**  
AI/ML Engineer | MSc AI Candidate @ BSBI Berlin  
[GitHub](https://github.com/rohantabhamar) · [Email](mailto:rohantabhamare22@gmail.com)
