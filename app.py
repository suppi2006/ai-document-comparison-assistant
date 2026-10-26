
import streamlit as st
import os
from dotenv import load_dotenv

from document_reader import extract_text_from_pdf
from comparison import compare_documents
from report_generator import create_report

load_dotenv()

st.set_page_config(page_title="AI Document Comparison Assistant")
st.title("AI Document Comparison Assistant")
st.write("Upload two text-based PDF documents to compare them.")

file_a = st.file_uploader("Document A", type=["pdf"], key="a")
file_b = st.file_uploader("Document B", type=["pdf"], key="b")

    
if st.button("Compare Documents"):
    api_key = os.getenv("GEMINI_API_KEY")

    if not file_a or not file_b:
        st.error("Please upload both PDF documents.")
    elif not api_key:
        st.error("Gemini API key is missing. Check your .env file.")
    elif file_a.size == 0 or file_b.size == 0:
        st.error(
            "One of the uploaded files is empty. "
            "Please upload valid PDF documents."
        )
    else:
        try:
            with st.spinner("Reading and comparing documents..."):
                text_a = extract_text_from_pdf(file_a)
                text_b = extract_text_from_pdf(file_b)

                if not text_a.strip() or not text_b.strip():
                    st.error(
                        "No readable text found in one or both PDFs. "
                        "Please upload text-based PDF documents."
                    )
                    st.stop()

                if len(text_a) + len(text_b) > 50000:
                    st.error("Documents are too long. Try shorter PDFs.")
                    st.stop()

                result = compare_documents(text_a, text_b, api_key)

            st.subheader("Comparison Results")
            st.markdown(result)

            report = create_report(file_a.name, file_b.name, result)

            st.download_button(
                "Download Comparison Report",
                data=report,
                file_name="comparison_report.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        
       
        except Exception as e:
            error_message = str(e)

            if "No readable text found" in error_message:
                st.error(
                    "No readable text found in one or both PDFs. "
                    "Please upload PDFs containing readable text."
                )
            else:
                st.error(
                    f"Comparison failed: {error_message}"
                )


