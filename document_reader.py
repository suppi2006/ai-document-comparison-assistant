
from pypdf import PdfReader


def extract_text_from_pdf(uploaded_file):
    """Extract readable text from an uploaded PDF file."""

    reader = PdfReader(uploaded_file)
    extracted_pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""

        if page_text.strip():
            extracted_pages.append(
                f"Page {page_number}:\n{page_text}"
            )

    full_text = "\n\n".join(extracted_pages)

    if not full_text.strip():
        raise ValueError(
            "No readable text found in this PDF. "
            "It may be empty or scanned."
        )

    return full_text
