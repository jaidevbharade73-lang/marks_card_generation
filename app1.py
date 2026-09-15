import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="Student Marks Card",
    page_icon="🎓"
)


def grade(mark):
    if mark >= 90:
        return "A+"
    if mark >= 80:
        return "A"
    if mark >= 70:
        return "B+"
    if mark >= 60:
        return "B"
    if mark >= 50:
        return "C"
    if mark >= 35:
        return "D"
    return "F"


names = [
    "Rahul Sharma",
    "Sanjay Kumar",
    "Pramod Patil",
    "Shrikant Rao",
    "Akash Gowda",
    "Rohit Kumar",
    "Kiran Shetty",
    "Manoj Reddy",
    "Vijay Kumar",
    "Darshan Hegde",
    "Pavan Kumar",
    "Nikhil Raj",
    "Chetan Gowda",
    "Gowtham Kumar",
    "Harshith Rao",
    "Aditya Patil",
    "Anil Kumar",
    "Abhishek Shetty",
    "Suresh Gowda",
    "Ramesh Kumar"
]


random.seed(100)

rows = []

for roll in range(1, 21):
    rows.append({
        "Roll No": roll,
        "Name": names[roll - 1],
        "English": random.randint(35, 100),
        "Kannada": random.randint(35, 100),
        "Hindi": random.randint(35, 100),
        "Maths": random.randint(35, 100),
        "Science": random.randint(35, 100)
    })


df = pd.DataFrame(rows)


st.title("🎓 Welcome to Shrikant and Pramod AIML Project")

st.markdown("---")

st.header("📚 Student Marks Card Analysis")

st.write(
    "Enter a roll number from 1 to 20 to view the marks card."
)
