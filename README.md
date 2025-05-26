# 📘 SideNote Claude – AI-Powered Research Paper Summarizer

**SideNote Claude** is a smart assistant that uses Anthropic's Claude LLM to help you quickly understand academic research papers. Upload a PDF, and the app will summarize it, extract a glossary, answer your questions, and even explain complex content in simple language — all via a clean Streamlit interface.

---

## 🚀 Features

✅ Upload any academic paper in PDF format  
✅ Get a clear, structured summary using Claude  
✅ Ask natural-language questions about the paper  
✅ Automatically extract a glossary of technical terms and their definitions  
✅ “Explain Like I’m 12” mode for non-technical summaries  
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

## ▶️ How to Run This App (in Google Colab)

You don’t need to deploy anything — just follow these steps to run the app directly from a notebook:

---

### ✅ Steps to Reproduce

1. 📥 **Download the notebook**  
   Go to this link and download the `.ipynb` file:  
   [sidenote-academic-assistant/sideNote.ipynb](https://github.com/laharigandrapu11/sidenote-academic-assistant/blob/main/sideNote.ipynb)

2. 🔑 **Get your Claude API key**  
   Sign up at [console.anthropic.com](https://console.anthropic.com)  
   Generate and copy your Claude API key.

3. 🌐 **Set up an ngrok account**  
   Visit [ngrok.com](https://ngrok.com), sign up, and copy your ngrok auth token.  
   (Used to create a public link to your Streamlit app.)

4. 🚀 **Open the notebook in Google Colab and run all cells**  
   - Paste your **Claude API key** and **ngrok auth token** into the appropriate cells in the notebook  
   - Run the notebook  
   - A public link will appear — click to launch your app!

---

## 💡 Notes

- This app runs inside Colab and uses `ngrok` to expose it publicly.
- Your Claude API key is required to interact with the language model.
- Be careful **not to share your API key** publicly.

---

## 🙌 Credits

- Built using [Anthropic Claude API](https://console.anthropic.com)
- UI powered by [Streamlit](https://streamlit.io)
