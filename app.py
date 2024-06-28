import streamlit as st

# Read the HTML content
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display the HTML content using Streamlit's `st.components.v1.html` function
st.components.v1.html(html_content)
