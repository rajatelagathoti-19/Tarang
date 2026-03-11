import streamlit as st

st.title("My Project")

with st.expander("Home"):
    st.write("Welcome to my project!")

with st.expander("Study Materials"):
    st.write("Materials here...")

with st.expander("Video Lectures"):
    st.write("Lectures here...")
