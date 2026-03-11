import streamlit as st

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def show_home():
    st.title("Study Portal")
    st.write("Please enter your details:")
    name = st.text_input("Name")
    roll_number = st.text_input("Roll Number")
    if st.button("Submit"):
        if name and roll_number:
            st.session_state.name = name
            st.session_state.roll_number = roll_number
            st.session_state.page = 'options'
        else:
            st.error("Please fill in all fields")

def show_options():
    st.title(f"Welcome, {st.session_state.name}!")
    st.write(f"Roll Number: {st.session_state.roll_number}")
    st.write("Choose an option:")
    if st.button("Study Materials"):
        st.session_state.page = 'study_materials'
    if st.button("Video Lectures"):
        st.session_state.page = 'video_lectures'

def show_study_materials():
    st.title("Study Materials")
    st.write("This page is under construction.")

def show_video_lectures():
    st.title("Video Lectures")
    st.write("This page is under construction.")

if st.session_state.page == 'home':
    show_home()
elif st.session_state.page == 'options':
    show_options()
elif st.session_state.page == 'study_materials':
    show_study_materials()
elif st.session_state.page == 'video_lectures':
    show_video_lectures()
