import streamlit as st

st.set_page_config(
    page_title="Student Marks Card",
    page_icon="🎓"
)

st.title("🎓 Welcome to Shrikant and Pramod AIML Project")

st.write("Student Marks Card Analysis")

st.success("✅ Website is working successfully!")

st.write("Enter Roll Number from 1 to 20")

roll_no = st.number_input(
    "Roll Number",
    min_value=1,
    max_value=20,
    value=1
)

if st.button("Show Marks Card"):
    st.header("📝 Student Marks Card")
    st.write("Roll Number:", roll_no)
    st.write("Name: Test Student")

    st.table({
        "Subject": ["English", "Kannada", "Hindi", "Maths", "Science"],
        "Marks": [85, 78, 91, 88, 82],
        "Grade": ["A", "B+", "A+", "A", "A"]
    })
