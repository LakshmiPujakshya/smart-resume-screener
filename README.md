# 🧠 Smart Resume Screener

This is a simple AI-based Streamlit app that automatically screens resumes based on a given job description. It extracts text from resumes (PDF), preprocesses them, and then uses NLP and Machine Learning techniques to rank candidates by relevance.

---

## 🚀 Features

- 📄 Upload multiple resumes in PDF format
- 📋 Upload or paste a Job Description
- 🧠 Automatically ranks resumes based on relevance using ML
- 📊 Shows match percentage for each resume

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** - for web UI
- **Scikit-learn** - for ML vectorization and similarity
- **PyMuPDF (`fitz`)** - for PDF parsing
- **NumPy** - numerical operations

---

## 📁 Project Structure
smart-resume-screener/
│
├── app.py                 # Main Streamlit app to run the UI
├── preprocess.py          # Functions to clean and preprocess text
├── utils.py               # Helper functions (e.g., PDF reading, similarity)
├── requirements.txt       # Python dependencies
│
├── sample_resumes/        # Folder to store sample PDF resumes
├── job_descriptions/      # Folder to store job descriptions
└── __pycache__/           # Auto-generated Python cache files

