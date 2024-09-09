import streamlit as st

# Title of the app
st.title("My Streamlit App")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("Sidebar content goes here.")

# Main content
st.write("Hello, welcome to my app!")

# Adding a simple widget
name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")
