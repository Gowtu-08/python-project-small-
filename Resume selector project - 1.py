import streamlit as st
import pdfplumber
import docx
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import io

# Function to extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + " "
    return text

# Function to extract text from DOCX
def extract_text_from_docx(file):
    doc = docx.Document(file)
    return " ".join([para.text for para in doc.paragraphs])

# App title
st.title("📄 Resume Selector Web App")
st.write("Upload a job description and multiple resumes to find the best matches.")

# Job Description Input
job_desc_input = st.text_area("Paste Job Description Here:")
job_desc_file = st.file_uploader("Or upload job description as .txt", type=["txt"])

if job_desc_file is not None:
    job_desc_input = job_desc_file.read().decode("utf-8")

# Resume Upload
uploaded_resumes = st.file_uploader("Upload Resumes (.pdf or .docx)", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("Process Resumes"):
    if not job_desc_input.strip():
        st.error("Please provide a job description.")
    elif not uploaded_resumes:
        st.error("Please upload at least one resume.")
    else:
        resume_texts = []
        resume_names = []

        for resume in uploaded_resumes:
            if resume.type == "application/pdf":
                text = extract_text_from_pdf(resume)
            elif resume.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                text = extract_text_from_docx(resume)
            else:
                text = ""
            resume_texts.append(text)
            resume_names.append(resume.name)

        # TF-IDF + Similarity
        vectorizer = TfidfVectorizer(stop_words='english')
        vectors = vectorizer.fit_transform([job_desc_input] + resume_texts)
        similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

        # Ranking
        df = pd.DataFrame({"Resume": resume_names, "Match Score": similarities})
        df = df.sort_values(by="Match Score", ascending=False)

        st.subheader("📊 Ranking Results")
        st.dataframe(df)

        # Download option
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        st.download_button(
            label="📥 Download Results as CSV",
            data=csv_buffer.getvalue(),
            file_name="resume_ranking.csv",
            mime="text/csv"
        )
