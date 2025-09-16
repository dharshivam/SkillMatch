# 🚀 SkillMatch: AI-Powered Resume Screener

SkillMatch is a lightweight **Streamlit application** that uses **Google Gemini (Generative AI)** to analyze resumes against job descriptions.  
It provides ATS scores, matching vs. non-matching skills, SWOT analysis, improvement suggestions, and even generates tailored resumes.

🔗 **Live App**: [SkillMatch Streamlit App](https://skill-match.streamlit.app/)  

---

## 📌 Problem Statement

In today’s competitive job market:
- Job seekers often submit **generic resumes** that fail to align with specific job postings.  
- Recruiters are overwhelmed by **irrelevant applications**, making ATS filtering time-consuming.  

---

## 🎯 Business Objective

SkillMatch helps:
- **Job Seekers** → Tailor resumes for each job description and improve ATS compatibility.  
- **Recruiters/HR Teams** → Receive higher-quality, job-relevant resumes, improving shortlisting efficiency.  

---

## ✨ Features

- 📄 Upload resume (PDF only).  
- 📋 Paste job description.  
- 🤖 AI-powered analysis:  
  - Applicant overview  
  - ATS score range  
  - Matching vs. non-matching skills  
  - Shortlisting probability  
  - SWOT analysis  
  - Resume improvement suggestions  
- 📝 Generates:  
  - Two **customized resumes** based on the JD  
  - A **one-page resume** (ready for Word/PDF conversion)  

---

## 🛠 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **LLM**: Google Gemini (via `google-generativeai`)  
- **PDF Parsing**: pypdf  
- **Deployment**: Streamlit Cloud  
- **Version Control**: Git & GitHub  

---

## 📊 Architecture Flow

```mermaid
flowchart TD
    A[📄 Resume Upload (PDF)] --> B[🔍 PDF Text Extraction (pypdf)]
    C[📋 Job Description Input] --> D[⚡ Prompt Construction]
    B --> D
    D --> E[🤖 Google Gemini AI Analysis]
    E --> F[📊 ATS Score & Skills Match]
    E --> G[📝 SWOT Analysis & Suggestions]
    E --> H[📑 Customized Resume Generation]
    F --> I[📺 Streamlit UI Output]
    G --> I
    H --> I
