import streamlit as st
import numpy as np

# Set up Streamlit page configuration
st.set_page_config(page_title="Calculator", page_icon=":bar_chart:", layout="centered")

# Title for the application
st.title("Calculator")

# State management to toggle between the basic calculator and RSD calculator
if "show_basic_calculator" not in st.session_state:
    st.session_state.show_basic_calculator = True

# Basic Calculator Section
if st.session_state.show_basic_calculator:
    st.header("Basic Calculator")
    expression = st.text_input("Enter expression (e.g., 2+3*5):")
    
    if st.button("Calculate"):
        try:
            result = eval(expression)
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Invalid Expression: {e}")
    
    # Button to switch to RSD Calculator
    if st.button("Go to RSD Calculator"):
        st.session_state.show_basic_calculator = False
        st.experimental_rerun()

# RSD Calculator Section
if not st.session_state.show_basic_calculator:
    st.header("RSD Calculator")
    
    # Initialize number of rows and columns
    if "num_rows" not in st.session_state:
        st.session_state.num_rows = 3
    if "num_cols" not in st.session_state:
        st.session_state.num_cols = 2

    # Inputs for rows and columns
    cols1, cols2 = st.columns(2)
    
    with cols1:
        st.session_state.num_rows = st.number_input("Rows", min_value=1, value=st.session_state.num_rows)
    
    with cols2:
        st.session_state.num_cols = st.number_input("Columns", min_value=1, value=st.session_state.num_cols)

    # Input fields for RSD calculator
    data = []
    for row in range(st.session_state.num_rows):
        row_data = []
        cols = st.columns(st.session_state.num_cols)  # Create columns based on num_cols
        for col in range(st.session_state.num_cols):
            value = cols[col].number_input(f"Row {row + 1}, Col {col + 1}", key=f"{row}_{col}", format="%.5f")
            row_data.append(value)
        data.append(row_data)

    data = np.array(data)

    # Calculate RSD button
    if st.button("Calculate RSDs"):
        st.subheader("RSD Results:")
        for i in range(data.shape[1]):
            column_data = data[:, i]
            column_data = column_data[column_data != 0]  # Ignore zero values
            if len(column_data) < 2:
                st.warning(f"Column {i + 1}: Not enough data")
                continue
            mean = np.mean(column_data)
            std_dev = np.std(column_data, ddof=1)
            rsd = (std_dev / mean) * 100
            st.success(f"Column {i + 1}: RSD = {rsd:.2f}%")

    # Buttons to modify rows and columns
    cols3, cols4 = st.columns(2)
    with cols3:
        if st.button("Add Row"):
            st.session_state.num_rows += 1
        if st.button("Remove Row") and st.session_state.num_rows > 1:
            st.session_state.num_rows -= 1
    
    with cols4:
        if st.button("Add Column"):
            st.session_state.num_cols += 1
        if st.button("Remove Column") and st.session_state.num_cols > 1:
            st.session_state.num_cols -= 1

    # Button to return to the basic calculator
    if st.button("Back to Basic Calculator"):
        st.session_state.show_basic_calculator = True
        st.experimental_rerun()
