import streamlit as st
import pandas as pd
import random

# Page setup
st.set_page_config(
    page_title="Student Marks Card",
    page_icon="🎓",
    layout="centered"
)

# Grade function
def get_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B+"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 35:
        return "D"
    else:
        return "F"


# Student names
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


# Create random dataset
random.seed(10)

data = []

for roll in range(1, 21):

    data.append({
        "Roll No": roll,
        "Name": names[roll - 1],
        "English": random.randint(35, 100),
        "Kannada": random.randint(35, 100),
        "Hindi": random.randint(35, 100),
        "Maths": random.randint(35, 100),
        "Science": random.randint(35, 100)
    })


df = pd.DataFrame(data)


# -----------------------------
# WELCOME PAGE
# -----------------------------

st.title("🎓 Welcome to Shrikant and Pramod AIML Project")

st.markdown("---")

st.header("📚 Student Marks Card Analysis")

st.write(
    "Welcome to our Student Marks Card Analysis project."
)

st.write(
    "Enter
