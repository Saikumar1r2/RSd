import streamlit as st

# Set page layout and configuration
st.set_page_config(page_title="Basic Calculator", page_icon=":bar_chart:", layout="centered")

# Hide Streamlit's default header and footer
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Basic calculator input
expression = st.text_input("Enter expression (e.g., 2+3*5):", "")

# Calculate button
if st.button("Calculate"):
    try:
        result = eval(expression)
        st.write(f"Result: {result}")
    except Exception as e:
        st.error(f"Invalid Expression: {e}")
