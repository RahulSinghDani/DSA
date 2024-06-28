import streamlit as st

try:
    # Read the HTML content
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    # Display the HTML content using Streamlit's `st.components.v1.html` function
    st.components.v1.html(html_content)

except FileNotFoundError:
    st.error("File 'index.html' not found. Make sure the file exists and is in the correct location.")

except Exception as e:
    st.error(f"An error occurred: {e}")
