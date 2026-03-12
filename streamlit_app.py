import streamlit as st

# Create columns for menu and content
col1, col2 = st.columns([1, 5])

with col1:
    st.write("Menu")
    menu_option = st.radio("", ["ACADEMIC REGISTER", "ASSIGNMENTS REPORT", "EXAM-SCHEDULE"])

with col2:
    if menu_option == "ACADEMIC REGISTER":
        st.write("Academic Register content")
    elif menu_option == "ASSIGNMENTS REPORT":
        st.write("Assignments Report content")
    elif menu_option == "EXAM-SCHEDULE":
        st.write("Exam Schedule content")
