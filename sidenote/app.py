import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.summarizer import summarize_text


st.set_page_config(page_title="SideNote", layout="wide")

st.title("📖 SideNote – AI-Powered Paper Explainer")

uploaded_file = st.file_uploader("Upload a research paper (PDF)", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf(uploaded_file)
    
    st.subheader("📄 Full Extracted Text")
    st.markdown("Scroll through the raw text below.")
    st.text_area("PDF Content", text, height=400)

if st.button("🔍 Summarize This Paper"):
    with st.spinner("Summarizing..."):
        summary = summarize_text(text)
    st.subheader("📌 Summary")
    st.success(summary)

