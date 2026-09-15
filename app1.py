import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="Student Marks Card",
    page_icon="🎓",
    layout="centered"
)

# -----------------------------
# Grade Function
# -----------------------------
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


# -----------------------------
# Student Dataset
# -----------------------------
random.seed(10)

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

students = []

for i in range(20):
    students.append({
        "Roll No": i + 1,
        "Name": names[i],
        "English": random.randint(35, 100),
        "Kannada": random.randint(35, 100),
        "Hindi": random.randint(35, 100),
        "Maths": random.randint(35, 100),
        "Science": random.randint(35, 100)
    })

df = pd.DataFrame(students)


# -----------------------------
# Welcome
# -----------------------------
st.title("🎓 Welcome to Shrikant and Pramod AIML Project")

st.markdown("---")

st.header("📚 Student Marks Card Analysis")

st.write(
    "Welcome to our Student Marks Card Analysis project."
)

st.write(
    "Enter a roll number between **1 and 20** to view the student's marks card."
)

st.info("👨‍💻 Project Developed by Shrikant and Pramod")

st.markdown("---")


# -----------------------------
# Roll Number
# -----------------------------
st.subheader("🔎 Search Student")

roll_no = st.number_input(
    "Enter Roll Number",
    min_value=1,
    max_value=20,
    value=1,
    step=1
)


# -----------------------------
# Show Marks Card
# -----------------------------
if st.button("📄 Show Marks Card"):

    student = df[df["Roll No"] == roll_no].iloc[0]

    st.markdown("---")

    st.header("📝 STUDENT MARKS CARD")

    # Student information
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Name:**")
        st.write(student["Name"])

    with col2:
        st.write("**Roll Number:**")
        st.write(student["Roll No"])

    st.markdown("---")

    # -----------------------------
    # Subject Marks
    # -----------------------------
    subjects = [
        "English",
        "Kannada",
        "Hindi",
        "Maths",
        "Science"
    ]

    marks_list = []

    for subject in subjects:

        mark = int(student[subject])

        marks_list.append({
            "Subject": subject,
            "Marks": mark,
            "Grade": get_grade(mark)
        })

    marks_table = pd.DataFrame(marks_list)

    st.subheader("📊 Subject-wise Marks")

    st.table(marks_table)


    # -----------------------------
    # Total
    # -----------------------------
    total = sum(int(student[subject]) for subject in subjects)

    percentage = total / 5

    # Result
    if any(int(student[subject]) < 35 for subject in subjects):
        result = "FAIL"
    else:
        result = "PASS"

    overall_grade = get_grade(percentage)

    st.markdown("---")

    st.subheader("📈 Result Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Marks",
            f"{total}/500"
        )

    with col2:
        st.metric(
            "Percentage",
            f"{percentage:.2f}%"
        )

    with col3:
        st.metric(
            "Result",
            result
