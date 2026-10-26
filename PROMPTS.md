# AI Document Comparison Assistant — Prompts Log

## 1. Project Goal

Build a web application that allows users to upload two PDF documents, compare their contents using AI, view a structured comparison, and download the results as a Word document.

## 2. AI Tools Used

- ChatGPT: Used for beginner-friendly guidance, debugging assistance, project structure, and understanding GitHub and deployment steps.
- Google Gemini API: Used by the application to generate summaries, identify similarities and differences, extract key details, and produce an overall conclusion.

## 3. Prompts Used During Development

### Prompt 1: Project Setup

"Help me build an AI Document Comparison Assistant using Python. Guide me step by step through the setup and explain each step in beginner-friendly language."

### Prompt 2: Document Comparison

"Compare two PDF documents using only their extracted text. Provide Summary A, Summary B, Similarities, Differences (added, removed, and changed information), Key Details, Overall Conclusion, and Limitations. Do not invent facts. If information is missing, state that it was not found in the provided text."

### Prompt 3: Error Handling

"Help me handle missing PDF uploads, missing API configuration, long documents, and API errors gracefully. Explain the changes so I can understand and maintain the code."

### Prompt 4: Report Generation

"Help me generate a downloadable Word report containing the names of the compared documents and the AI-generated comparison results."

### Prompt 5: Deployment

"Guide me through uploading the project to GitHub and deploying the Streamlit application. Keep API credentials private and use deployment secrets for the Gemini API key."

## 4. AI Limitations and Mistakes

- AI-generated comparisons may miss context or interpret ambiguous text incorrectly.
- Extracted PDF text may be incomplete, especially for scanned documents or complex layouts.
- The AI output must be checked against the original documents before relying on it.
- API model availability and temporary service errors can affect execution.

## 5. Validation Performed

- Tested the application with two sample company policy PDFs.
- Checked whether the comparison identified changes in annual leave, advance notice, working hours, and work-from-home allowance.
- Checked whether unchanged sick-leave approval information was identified as a similarity.
- Tested downloading the comparison report.
- Deployed the application and tested document comparison through the live application.

## 6. Developer Reflection

AI tools assisted with development and troubleshooting. I tested the application and reviewed its outputs. I will continue improving my understanding of the code and validating the results. Any additional testing or limitations should be documented accurately before submission.
