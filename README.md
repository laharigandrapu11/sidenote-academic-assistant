# 📘 SideNote Claude – AI-Powered Research Paper Summarizer

**SideNote Claude** is a smart assistant that uses Anthropic's Claude LLM to help you quickly understand academic research papers. Upload a PDF, and the app will summarize it, extract a glossary, answer your questions, and even explain complex content in simple language — all via a clean Streamlit interface.

---

## 🚀 Features

✅ Upload any academic paper in PDF format  
✅ Get a clear, structured summary using Claude  
✅ Ask natural-language questions about the paper  
✅ Automatically extract a glossary of technical terms and their definitions  
✅ “Explain Like I’m 12” mode for non-technical summaries  
✅ Downloadable output (optional)  
✅ Runs in Google Colab or locally via Streamlit and ngrok

---

## 🔧 Tech Stack

- **LLM**: [Claude 3.5 Sonnet](https://console.anthropic.com)
- **Frontend**: Streamlit
- **PDF Parsing**: PyMuPDF (`fitz`)
- **API Integration**: Anthropic Python SDK
- **Deployment**: Local / Google Colab (with `pyngrok` tunnel)

---

## 🧠 Core Capabilities

### 📝 Summarization
Generates a concise overview of the paper, covering:
- What it’s about  
- Key contributions  
- Methods used  
- Main findings

### ❓ Q&A Engine
Ask follow-up questions like:
> “What dataset was used?”  
> “How does this compare to previous work?”

Claude responds with grounded, document-aware answers.

### 📘 Glossary Generator
Extracts 5–10 key technical terms and explains them in simple language.

### 🧒 Explain Like I’m 12
Simplifies the paper for beginners:
> "Imagine you're explaining this to a 12-year-old."

Returns a kid-friendly summary with analogies or basic vocabulary.
