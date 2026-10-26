
# AI Document Comparison Assistant

## Project Overview
The AI Document Comparison Assistant is a web application that compares two text-based PDF documents using Generative AI. It identifies summaries, similarities, differences, and important details, and generates a downloadable comparison report.

## Features
- Upload two PDF documents.
- Extract readable text from PDFs.
- Generate AI-powered document comparisons.
- Display summaries, similarities, differences, and key details.
- Validate missing and empty files.
- Handle PDFs without readable text.
- Check document text length before comparison.
- Download the results as a DOCX report.
- Display error messages when comparison fails.

## Technologies Used
- Python
- Streamlit
- Google Gemini API
- pypdf
- python-dotenv
- python-docx

## Project Structure
- `app.py` — Streamlit user interface and application workflow.
- `document_reader.py` — Extracts text from PDF files.
- `comparison.py` — Compares documents using Gemini.
- `report_generator.py` — Generates the DOCX report.
- `requirements.txt` — Project dependencies.
- `PROMPTS.md` — AI prompts, tools used, and project notes.

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/suppi2006/ai-document-comparison-assistant.git
cd ai-document-comparison-assistant
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
```

Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key
Create a `.env` file in the project folder and add:
```text
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own API key. Never commit your real API key to GitHub.

### 5. Run the application
```bash
streamlit run app.py
```

## Limitations
- The application requires PDFs containing readable text.
- Scanned PDFs may not work because OCR is not implemented.
- Document length is limited by the application's configured text-length check.
- Comparison depends on Gemini API availability and response quality.

## Testing
Tested the main workflow with sample policy PDFs, including document comparison and DOCX report download. Missing-file, empty-file, and no-readable-text validation were also tested locally.

## Future Improvements
- Add OCR support for scanned PDFs.
- Add more automated tests.
- Improve API error handling and input validation.
