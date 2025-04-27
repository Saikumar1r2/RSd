import streamlit as st

# Directly setting font size with CSS
st.markdown(
    "<p style='text-align: center; font-size: 24px; color: navy;'>Hello, World!</p>",
    unsafe_allow_html=True
)

st.write("Welcome to your first Streamlit app.")
