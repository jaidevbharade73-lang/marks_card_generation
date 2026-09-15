import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Student Marks Card", page_icon="🎓")

st.title("🎓 Welcome to Shrikant and Pramod AIML Project")

st.write("## 📚 Student Marks Card Analysis")

st.write("Select a roll number to view the student's marks card.")

st.markdown("---")

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

# Create student data
random.seed(50)

data = []

for i in range(20):
    data.append({
        "Roll No": i + 1,
        "Name": names[i],
        "English": random.randint(40, 100),
        "Kannada": random.randint(40, 100),
        "Hindi": random.randint(40, 100),
        "Maths": random.randint(40, 100),
        "Science": random.randint(40, 100)
    })

df = pd.DataFrame(data)

# Roll number selection
st.subheader("🔎 Enter Roll Number")

roll_number = st.selectbox(
    "Roll Number",
    list(range(1, 21))
)

# Button
show_button = st.button("📄 Generate Marks Card")

# Generate marks card
if show_button:

    student = df[df["Roll No"] == roll_number].iloc[0]

    st.markdown("---")

    st.header("📝 STUDENT MARKS CARD")

    st.write("**Student Name:** " + student["Name"])

    st.write("**Roll Number:** " + str(student["Roll No"]))

    st.markdown("---")

    # Subjects
    subjects = [
        "English",
        "Kannada",
        "Hindi",
        "Maths",
        "Science"
    ]

    marks = []
    
    for subject in subjects:

        mark = int(student[subject])

        if mark >= 90:
            grade = "A+"
        elif mark >= 80:
            grade = "A"
        elif mark >= 70:
            grade = "B+"
        elif mark >= 60:
            grade = "B"
        elif mark >= 50:
            grade = "C"
        else:
            grade = "D"

        marks.append({
            "Subject": subject,
            "Marks": mark,
            "Grade": grade
        })

    marks_table = pd.DataFrame(marks)

    st.subheader("📊 Subject Marks")

    st.table(marks_table)

    # Total
    total = 0

    for subject in subjects:
        total = total + int(student[subject])

    percentage = total / 5

    # Result
    if percentage >= 35:
        result = "PASS"
    else:
        result = "FAIL"

    st.markdown("---")

    st.subheader("📈 Result")

    st.write("**Total Marks:** " + str(total) + " / 500")

    st.write("**Percentage:** " + str(round(percentage, 2)) + "%")

    st.write("**Result:** " + result)

    if percentage >= 90:
        overall = "A+"
    elif percentage >= 80:
        overall = "A"
    elif percentage >= 70:
        overall = "B+"
    elif percentage >= 60:
        overall = "B"
    elif percentage >= 50:
        overall = "C"
    else:
        overall = "D"

    st.write("**Overall Grade:** " + overall)

    if result == "PASS":
        st.success("🎉 Student Passed Successfully!")
    else:
        st.error("❌ Student Failed")
