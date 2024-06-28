import streamlit as st
import os

def main():
    # Read the HTML content
    with open(os.path.join('app', 'index.html'), "r", encoding="utf-8") as f:
        html_content = f.read()

    # Display the HTML content using Streamlit's `st.components.v1.html` function
    st.components.v1.html(html_content)

if __name__ == "__main__":
    main()
