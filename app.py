import streamlit as st
from utils import extract_text_from_pdf, calculate_similarity

st.title("🧠 Smart Resume Screener")
st.markdown("Match your resume with a job description using AI.")

resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
jd_text = st.text_area("Paste Job Description here")

if st.button("Analyze") and resume_file and jd_text:
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(resume_file.read())
    
    resume_text = extract_text_from_pdf("uploaded_resume.pdf")
    jd_clean = jd_text.lower()
    similarity = calculate_similarity(resume_text, jd_clean)

    st.success(f"🔍 Match Score: {similarity}%")
    if similarity > 70:
        st.balloons()
        st.info("Great! Your resume aligns well with this job.")
    else:
        st.warning("Consider revising your resume to better match the job.")
