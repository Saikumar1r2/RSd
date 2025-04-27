import streamlit as st

# Set the page layout
st.set_page_config(page_title="Calculator", layout="centered")

# Initialize session state for keeping track of input and operations
if 'input_value' not in st.session_state:
    st.session_state.input_value = ""

# Function to update the display based on button clicks
def update_input(button_text):
    st.session_state.input_value += button_text

# Function to clear the input display
def clear_input():
    st.session_state.input_value = ""

# Function to evaluate the input
def evaluate_input():
    try:
        result = eval(st.session_state.input_value)
        st.session_state.input_value = str(result)
    except Exception as e:
        st.session_state.input_value = "Error"

# Layout: Display the input field (calculation so far)
st.text_input("Display", value=st.session_state.input_value, disabled=True, key="display")

# Create the calculator buttons and arrange them in a grid layout
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7"): update_input("7")
    if st.button("4"): update_input("4")
    if st.button("1"): update_input("1")
    if st.button("C"): clear_input()

with col2:
    if st.button("8"): update_input("8")
    if st.button("5"): update_input("5")
    if st.button("2"): update_input("2")
    if st.button("0"): update_input("0")

with col3:
    if st.button("9"): update_input("9")
    if st.button("6"): update_input("6")
    if st.button("3"): update_input("3")
    if st.button("."): update_input(".")

with col4:
    if st.button("/"): update_input(" / ")
    if st.button("*"): update_input(" * ")
    if st.button("-"): update_input(" - ")
    if st.button("+"): update_input(" + ")
    if st.button("="): evaluate_input()

# Display the result or error
st.write("Result:", st.session_state.input_value)
