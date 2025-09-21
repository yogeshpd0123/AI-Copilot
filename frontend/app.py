import streamlit as st
import requests
from fpdf import FPDF

API_BASE = "http://127.0.0.1:8000"

st.title("📚 AI Copilot ")

topic = st.text_input("Enter a topic:")
level = st.selectbox("Select student level:", ["Beginner", "Intermediate", "Advanced"])
duration = st.number_input("Lesson duration (minutes):", 10, 120, 30)
interests = st.text_input("Enter student interests:")

if st.button("Generate Lesson Plan"):
    payload = {"topic": topic, "level": level, "duration": duration, "interests": interests}
    res = requests.post(f"{API_BASE}/generate_lesson", json=payload)
    lesson_plan = res.json()["lesson_plan"]
    st.subheader("Lesson Plan")
    st.text_area("Editable Lesson Plan:", lesson_plan, height=300)

    if st.button("Generate Quiz"):
        res_q = requests.post(f"{API_BASE}/generate_quiz", json=payload)
        quiz = res_q.json()["quiz"]
        st.subheader("Quiz")
        st.text_area("Generated Quiz:", quiz, height=200)

    if st.button("Download as PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(200, 10, lesson_plan)
        pdf.output("lesson_plan.pdf")
        st.success("PDF saved as lesson_plan.pdf")