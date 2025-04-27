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

# Create a layout for the calculator buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("1"):
        update_input(1)
    if st.button("4"):
        update_input(4)
    if st.button("7"):
        update_input(7)
    if st.button("0"):
        update_input(0)
    
with col2:
    if st.button("2"):
        update_input(2)
    if st.button("5"):
        update_input(5)
    if st.button("8"):
        update_input(8)
    if st.button("."):
        update_input(".")
    
with col3:
    if st.button("3"):
        update_input(3)
    if st.button("6"):
        update_input(6)
    if st.button("9"):
        update_input(9)
    if st.button("+"):
        update_input("+")
    
with col4:
    if st.button("-"):
        update_input("-")
    if st.button("*"):
        update_input("*")
    if st.button("/"):
        update_input("/")
    if st.button("="):
        result = calculate_result()
        st.write(f"Result: {result}")
    if st.button("C"):
        clear_input()

