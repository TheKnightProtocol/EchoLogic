# EchoLogic
# 🎯 ECHOLOGIC – Voice-to-Visual Reasoning Engine

> 🎙️💡 **EchoLogic** is an AI-powered tool that transforms **spoken meetings or recordings** into structured documents and **logic flow diagrams** — enabling teams to **understand, collaborate, and execute** faster than ever.

<h1 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=40&color=F71313&center=true&vCenter=true&width=900&height=80&lines=⚙️+EchoLogic+⚙️;🧠+By+Guardians+of+Code+🧠;💻+Automate+%7C+Build+%7C+Hack+%7C+Repeat+💻" />
</h1>

---

## ✨ Key Features

- 🎧 **Automatic Audio Transcription** using Faster-Whisper
- 🧠 **LLM-Based Semantic Understanding** of discussions
- 📄 **Professional DOCX Report Generation**
- 🔍 **RAG Pipeline** powered by ChromaDB + nomic-embed-text
- 📊 **Logic Flow Diagram Auto-Generation** (using Graphviz / Matplotlib)
- 🧩 **Modular Python Architecture** (easy to customize)
- ⚡ **Streamlit Frontend** for intuitive use

---

## 🛠 Tech Stack

| Layer              | Technology |
|--------------------|------------|
| Transcription      | [`faster-whisper`](https://github.com/guillaumekln/faster-whisper) |
| Semantic Analysis  | OpenAI GPT / LLMs |
| Embeddings         | [`nomic-embed-text`](https://github.com/nomic-ai/nomic) |
| Vector Storage     | [ChromaDB](https://www.trychroma.com/) |
| Visualization      | Graphviz / Matplotlib |
| Audio Processing   | Pydub + FFmpeg |
| Document Output    | python-docx |
| User Interface     | Streamlit |

---
| Language        | Code    |
| --------------- | ------- |
| English (India) | `en-IN` |
| English (US)    | `en-US` |
| Hindi           | `hi-IN` |
| Spanish         | `es-ES` |
| French          | `fr-FR` |
| German          | `de-DE` |
| Tamil           | `ta-IN` |
| Bengali         | `bn-IN` |

---
## 📁 Project Structure

echologic/
├── transcription/ # Whisper-based audio extraction
├── semantic_analysis/ # LLM parsing for summary and key actions
├── rag_engine/ # Embedding + retrieval system using ChromaDB
├── doc_generation/ # Generates DOCX documentation
├── visualizer/ # Creates logic diagrams
├── ui/ # Streamlit interface
├── utils/ # Helpers and error handling
├── main.py # Main CLI entrypoint
└── requirements.txt

