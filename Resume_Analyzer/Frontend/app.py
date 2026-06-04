import streamlit as st
import requests
import pypdf

st.title("Resume Analyzer")

# Restrict the file uploader to PDF files
resume = st.file_uploader("Upload your resume here", type=["pdf"])

if st.button("Analyze"):
    if resume is not None:
        try:
            # 1. Read and extract text from the PDF file
            pdf_reader = pypdf.PdfReader(resume)
            extracted_text = ""
            for page in pdf_reader.pages:
                extracted_text += page.extract_text() or ""

            # Double check if text extraction was successful
            if not extracted_text.strip():
                st.error("Could not extract text from the PDF. Is it an image/scanned PDF?")
            else:
                # 2. Send the clean extracted string text to your API
                response = requests.post(
                    "http://65.2.125.250:8000/analyze", 
                    json={"text": extracted_text}
                )
                
                # 3. Display results
                result = response.json()
                st.write(result)
                
        except Exception as e:
            st.error(f"An error occurred while processing the PDF: {e}")
    else:
        st.warning("Please upload a PDF file first before clicking Analyze.")