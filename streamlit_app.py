import streamlit as st
import qrcode
from PIL import Image
import io

def home():
    st.title("Study Portal")
    st.write("Please enter your details:")
    name = st.text_input("Name")
    roll_number = st.text_input("Roll Number")
    if st.button("Submit"):
        if name and roll_number:
            st.session_state.name = name
            st.session_state.roll_number = roll_number
            st.session_state.page = 'options'
            st.experimental_rerun()
        else:
            st.error("Please fill in all fields")

def options():
    st.title(f"Welcome, {st.session_state.name}!")
    st.write(f"Roll Number: {st.session_state.roll_number}")
    st.write("Choose an option:")
    if st.button("Study Materials"):
        st.session_state.page = 'study_materials'
        st.experimental_rerun()
    if st.button("Video Lectures"):
        st.session_state.page = 'video_lectures'
        st.experimental_rerun()

def study_materials():
    st.title("Study Materials")
    st.write("This page is under construction.")
    if st.button("Back"):
        st.session_state.page = 'options'
        st.experimental_rerun()

def video_lectures():
    st.title("Video Lectures")
    st.write("Scan the QR code to access video lectures:")
    if st.button("Back"):
        st.session_state.page = 'options'
        st.experimental_rerun()

if 'page' not in st.session_state:
    st.session_state.page = 'home'

if st.session_state.page == 'home':
    home()
elif st.session_state.page == 'options':
    options()
elif st.session_state.page == 'study_materials':
    study_materials()
elif st.session_state.page == 'video_lectures':
    video_lectures()
