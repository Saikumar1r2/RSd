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

# Create a box around the calculator
st.markdown("""
    <style>
    .calculator-container {
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 20px;
        background-color: #f9f9f9;
        width: 320px;
        margin: auto;
    }
    .calculator-container input {
        width: 100%;
        height: 50px;
        font-size: 24px;
        text-align: right;
        padding: 10px;
        margin-bottom: 20px;
        border: 2px solid #ccc;
        border-radius: 5px;
    }
    .calculator-container button {
        width: 60px;
        height: 60px;
        font-size: 22px;
        margin: 5px;
        border-radius: 5px;
        border: 1px solid #ccc;
        background-color: #f1f1f1;
        cursor: pointer;
    }
    .calculator-container button:hover {
        background-color: #d0ffd6;
    }
    </style>
    """, unsafe_allow_html=True)

# Create the calculator box
with st.container():
    st.markdown('<div class="calculator-container">', unsafe_allow_html=True)
    
    # Display the input field (calculation so far)
    st.text_input("Display", value=st.session_state.input_value, disabled=True, key="display", label_visibility="collapsed")
    
    # Create the buttons for the calculator
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
    
    st.markdown('</div>', unsafe_allow_html=True)

# Display the result or error message
st.write("Result:", st.session_state.input_value)
