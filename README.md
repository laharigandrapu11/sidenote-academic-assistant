# 🧾 BillSleuth – Understand Legal & Policy Docs with AI

> TL;DR for complex laws, policies, and bills — with summaries, highlights, and pro/con arguments.

## 🚀 Overview

**BillSleuth** is an LLM-powered app that helps users — citizens, students, journalists — make sense of dense legal or policy documents by:
- Summarizing complex language into simple bullet points
- Highlighting key clauses and potentially controversial parts
- Generating arguments **for** and **against** the document
- Allowing natural language Q&A (e.g., “How does this impact small businesses?”)

> 📌 Built using Hugging Face Transformers, Streamlit, and Python.

---

## 🧠 Features

| Feature                | Description |
|------------------------|-------------|
| 📄 Document Upload     | Upload or paste legal/policy text (PDF or plain text) |
| 📝 Summary Generator   | Bullet-point summary in layman’s terms |
| 🧩 Key Clause Extractor| Highlights important terms, obligations, or conditions |
| ⚖️ Pro/Con Generator   | AI-written arguments from both perspectives |
| ❓ Ask a Question       | Natural language Q&A about the document |

---

## 🔧 Tech Stack

- `Streamlit` – UI
- `FastAPI` (optional for backend separation)
- `PyMuPDF` or `pdfminer.six` – PDF parsing
- `transformers` – Hugging Face model integration
- `torch` – model support
- `sentence-transformers` – similarity-based clause highlighting

---

## 🤖 Models Used

| Task | Model |
|------|-------|
| Summarization | `facebook/bart-large-cnn`, `google/pegasus-xsum` |
| Text Generation (Pro/Con) | `tiiuae/falcon-7b-instruct`, `mistralai/Mistral-7B-Instruct-v0.1` |
| Question Answering | `deepset/roberta-base-squad2` |
| Clause Extraction | `bert-base-cased` for token classification |
| Bias Detection (optional) | `roberta-base-openai-detector` |

---

## 🔄 Example Input & Output

### Input:
> PDF: "Digital Privacy Bill – 2024" (10 pages)

### Output:
- **Summary**: 5 bullet points
- **Pro**: “Ensures stronger consumer control over data...”
- **Con**: “May increase compliance costs for startups...”
- **Highlight**: `"Companies must provide opt-out options..."`

---

## 🧪 Run Locally

```bash
git clone https://github.com/yourname/billsleuth.git
cd billsleuth

# Backend + Models
pip install -r requirements.txt

# Launch UI
streamlit run app.py
