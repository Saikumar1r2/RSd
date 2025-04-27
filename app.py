import streamlit as st

# Title
st.title("Interactive Streamlit Example")

# Slider for user input
number = st.slider("Pick a number", 1, 100)

# Show the squared value
st.write(f"The square of {number} is {number ** 2}.")
