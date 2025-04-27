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

# Function to handle the input
if "input_str" not in st.session_state:
    st.session_state.input_str = ""

def update_input(char):
    """Update input string with clicked button"""
    st.session_state.input_str += str(char)

def clear_input():
    """Clear the input string"""
    st.session_state.input_str = ""

def calculate_result():
    """Evaluate the input string"""
    try:
        result = eval(st.session_state.input_str)
        return result
    except:
        return "Error"

# Display the input area and the current input string
st.write(f"Input: {st.session_state.input_str}")

# Arrange the buttons in a 4x4 grid layout
button_layout = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create the grid of buttons
for row in button_layout:
    cols = st.columns(4)
    for i, button in enumerate(row):
        with cols[i]:
            if st.button(button):
                if button == "=":
                    result = calculate_result()
                    st.write(f"Result: {result}")
                elif button == "C":
                    clear_input()
                else:
                    update_input(button)
