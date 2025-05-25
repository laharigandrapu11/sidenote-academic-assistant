from transformers import pipeline
import textwrap

# Load a stronger summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def chunk_text(text, max_chunk_tokens=800):
    paragraphs = text.split("\n\n")
    current_chunk = ""
    chunks = []

    for para in paragraphs:
        if len((current_chunk + para).split()) <= max_chunk_tokens:
            current_chunk += para + "\n\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def summarize_text(text):
    chunks = chunk_text(text)
    full_summary = []

    for chunk in chunks[:3]:  # Limit to 3 chunks for performance
        summary = summarizer(chunk, max_length=250, min_length=80, do_sample=False)[0]["summary_text"]
        full_summary.append(summary)

    return "\n\n".join(full_summary)
