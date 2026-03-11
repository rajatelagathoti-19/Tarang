import streamlit as st

st.set_page_config(layout="wide")

# Sidebar
with st.sidebar:
    st.title("Menu")
    st.button("Home")
    st.button("About")
    st.button("Resources")

# Main content
st.title("Welcome to eCap")
st.write("Announcements and notices here...")
