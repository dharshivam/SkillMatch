import streamlit as st
from pdfextractor import text_extractor 
import google.generativeai as genai
import pandas as pd
import os

#configure the model
key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash-lite")

#upload resume

st.sidebar.title(":blue[UPLOAD YOUR RESUME (PDF Only)]")

#Lets read the PDF file
file = st.sidebar.file_uploader("Resume", type=["pdf"])
resume_text = job_desc = " "
if file :
    resume_text = text_extractor(file)
    #st.write(resume_text)

#Lets define the main page
st.title(":blue[SKILLMATCH] : :orange[AI POWERED RESUME SCREENER]")
st.markdown("#### This app uses Generative AI to screen resumes based on Job Description")
tips = '''
Follow the below steps to use the app:
1. Upload your resume in PDF format using the sidebar.
2. Copy and paste the job description below for which you are applying.
3. Click on the 'Get Match Score' button to see how well your resume matches the job description.
'''
st.write(tips)   

job_desc = st.text_area(" Copy and Paste the Job Description here(Ctrl+Enter to run)", max_chars=10000)

prompt = f''' Assume you are expert in skill matching and creating profiles
Match the following resume with the job description provided by the user
resume = {resume_text}
job description = {job_desc}

Your output should be in the following format
* Give a brief description of the applicant in 3 to 5 lines.
* Give a range  expected ATS score along with the matching skills and non matching skills in bullet points.
* Give the chances of getting shortlisted for this position in percentage.
* Perform swot analysis and discuss each and everything in bullet points.
* Suggest improvements to the resume to better match the job description in bullet points.
* Finally give an overall assessment of the applicant in 2 to 3 lines.
* Also create two customised resumes as per the job description provided by the user.
* Prepare a one page resume in such a format that can be copied and pasted in the word and 
can be converted to pdf.
* Use markdown formatting for better readability.
* Use headings and subheadings where necessary.
* Use bullet points where necessary.
* Use bold and italics where necessary.
'''


if job_desc:
    if resume_text and job_desc:
            response = model.generate_content(
                prompt
            )
            st.write(response.text)
    else:
            st.write("Please upload your resume and enter the job description to get the match score.")

