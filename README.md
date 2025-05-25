# 📖 SideNote – AI Explainer for Academic Papers

> Understand research papers with AI-powered summaries, glossaries, and inline explanations.

## 🚀 Overview

**SideNote** is a web app that simplifies academic PDFs and research papers using large language models (LLMs). It helps users:
- Read papers with **layman-friendly explanations**
- Get **inline tooltips** for technical terms and equations
- Generate **custom Q&A** from any section
- Auto-create a **glossary of terms** and summary per page

> 📌 Built using Hugging Face Transformers, Streamlit, and PyMuPDF.

---

## 🧠 Features

| Feature                 | Description |
|-------------------------|-------------|
| 📄 PDF Upload           | Upload any academic paper or textbook chapter |
| 📝 Simple Explanations  | Paragraph-wise simplification |
| 🔍 Glossary Generator   | Auto-detects technical terms and defines them |
| 💬 Ask the Paper        | Let users query any concept in natural language |
| 🧩 Equation Insight      | Explains key math expressions (if present) |

---

## 🔧 Tech Stack

- `Streamlit` – UI
- `PyMuPDF` – PDF parsing
- `transformers` – Hugging Face model interface
- `sentence-transformers` – for clause-level understanding
- `torch` – backend ML runtime

---

## 🤖 Models Used

| Task | Model |
|------|-------|
| Summarization | `facebook/bart-large-cnn`, `google/pegasus-xsum` |
| Text Simplification | `t5-small` (fine-tuned or with few-shot prompts) |
| Token/Term Highlighting | `bert-base-cased` + keyword extraction |
| Question Answering | `deepset/roberta-base-squad2` |
| (Optional) Math Parser | `sympy`, `regex`, or prompt-based LLM breakdowns |

---

## 🔄 Example Input/Output

**Input**: PDF upload of “Attention Is All You Need”  
**Output**:
- Summary: 4 main contributions in plain English
- Glossary:
  - “Multi-head attention” → “A mechanism that lets the model focus on different parts of a sentence at once.”
- Inline Q: “What is the point of positional encoding?”  
  A: “It helps the model know the order of words, since transformers don’t have sequence memory.”

---

## 🧪 Run Locally

```bash
git clone https://github.com/yourname/sidenote.git
cd sidenote
pip install -r requirements.txt
streamlit run app.py
