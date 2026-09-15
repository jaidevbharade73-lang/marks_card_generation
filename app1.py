import streamlit as st
import pandas as pd
import random

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Student Marks Card Analysis",
    page_icon="🎓",
    layout="centered"
)

# ---------------------------------------------------------
# Generate Random Student Dataset
# ---------------------------------------------------------
random.seed(42)

student_names = [
    "Aarav", "Aditya", "Akash", "Amruth", "Ananya",
    "Bhavana", "Chetan", "Darshan", "Deepak", "Gowtham",
    "Harshith", "Kiran", "Manoj", "Nikhil", "Pavan",
    "Pranav", "Rahul", "Rohit", "Sanjay", "Vijay"
]

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
        return