
import os
import streamlit as st
from dotenv import load_dotenv

from document_reader import extract_text_from_pdf
from comparison import compare_documents
from report_generator import create_report

load_dotenv()

st.set_page_config(
    page_title="AI Document Comparison Assistant",
    page_icon="📄",
    layout="wide"
)

# Initialize upload version for resetting file upload widgets
if "upload_version" not in st.session_state:
    st.session_state.upload_version = 0


# Reset callback
def reset_uploads():
    st.session_state.upload_version += 1


# Application heading
st.title("AI Document Comparison Assistant")

st.write(
    "Upload two text-based PDF documents to compare them "
    "using Generative AI."
)

# Reset button
st.button(
    "Reset / Compare Again",
    on_click=reset_uploads
)

# Dynamic keys create fresh upload fields after reset
upload_version = st.session_state.upload_version

file_a = st.file_uploader(
    "Document A",
    type=["pdf"],
    key=f"a_{upload_version}"
)

file_b = st.file_uploader(
    "Document B",
    type=["pdf"],
    key=f"b_{upload_version}"
)

# Compare documents
if st.button("Compare Documents", type="primary"):

    api_key = os.getenv("GEMINI_API_KEY")

    if file_a is None or file_b is None:
        st.error("Please upload both PDF documents.")

    elif not api_key:
        st.error(
            "Gemini API key is missing. "
            "Check your .env file or Streamlit Secrets."
        )

    elif file_a.size == 0 or file_b.size == 0:
        st.error(
            "One of the uploaded files is empty. "
            "Please upload valid PDF documents."
        )

    else:
        try:
            with st.spinner(
                "Reading and comparing documents..."
            ):
                # Extract text from both PDFs
                text_a = extract_text_from_pdf(file_a)
                text_b = extract_text_from_pdf(file_b)

                # Check for readable text
                if not text_a.strip() or not text_b.strip():
                    st.error(
                        "No readable text found in one or both PDFs. "
                        "Please upload text-based PDF documents."
                    )
                    st.stop()

                # Check combined text length
                if len(text_a) + len(text_b) > 50000:
                    st.error(
                        "Documents are too long. "
                        "Please upload shorter PDFs."
                    )
                    st.stop()

                # Display extracted document information
                st.subheader("Extracted Document Information")

                col1, col2 = st.columns(2)

                with col1:
                    st.write("**Document A**")
                    st.write(f"Characters: {len(text_a)}")
                    st.write(f"Words: {len(text_a.split())}")

                with col2:
                    st.write("**Document B**")
                    st.write(f"Characters: {len(text_b)}")
                    st.write(f"Words: {len(text_b.split())}")

                # Preview extracted text
                with st.expander("Preview Extracted Text"):
                    st.subheader("Document A Text")
                    st.text_area(
                        "Text from Document A",
                        text_a,
                        height=200,
                        disabled=True
                    )

                    st.subheader("Document B Text")
                    st.text_area(
                        "Text from Document B",
                        text_b,
                        height=200,
                        disabled=True
                    )

                # Compare documents with Gemini
                result = compare_documents(
                    text_a,
                    text_b,
                    api_key
                )

            # Show comparison results
            st.subheader("Comparison Results")
            st.markdown(result)

            # Generate DOCX report
            report = create_report(
                file_a.name,
                file_b.name,
                result
            )

            st.download_button(
                label="Download Comparison Report",
                data=report,
                file_name="comparison_report.docx",
                mime=(
                    "application/vnd.openxmlformats-officedocument."
                    "wordprocessingml.document"
                )
            )

        except Exception as e:
            error_message = str(e)
            error_lower = error_message.lower()

            if (
                "503" in error_message
                or "429" in error_message
                or "unavailable" in error_lower
                or "high demand" in error_lower
                or "resource_exhausted" in error_lower
            ):
                st.error(
                    "Gemini service is temporarily busy. "
                    "Please wait a minute and try again."
                )

            elif (
                "no readable text found" in error_lower
                or "empty" in error_lower
            ):
                st.error(
                    "No readable text found in one or both PDFs. "
                    "Please upload valid PDFs containing readable text."
                )

            else:
                st.error(
                    "Comparison failed. Please check your connection "
                    "and API configuration, then try again."
                )
                st.caption(
                    f"Technical details: {error_message}"
                )
