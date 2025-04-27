import streamlit as st
import numpy as np

st.set_page_config(page_title="Calculator + Multi RSD", page_icon=":bar_chart:", layout="centered")

st.title("Calculator + Multi-Column RSD")

# Basic Calculator
st.header("Basic Calculator")

expression = st.text_input("Enter expression (e.g. 2+3*5):")

if st.button("Calculate"):
    try:
        result = eval(expression)
        st.success(f"Result: {result}")
    except:
        st.error("Invalid Expression")

# Divider
st.markdown("---")

# RSD Calculator
st.header("RSD Calculator")

# Number of rows and columns
cols1, cols2 = st.columns(2)

with cols1:
    num_rows = st.number_input("Number of Rows", min_value=1, value=3)
with cols2:
    num_cols = st.number_input("Number of Columns", min_value=1, value=2)

# Input grid
data = []
for row in range(num_rows):
    row_data = []
    st.subheader(f"Row {row + 1}")
    cols = st.columns(num_cols)  # Create columns based on num_cols
    for col in range(num_cols):
        value = cols[col].number_input(f"Value {col + 1}", key=f"{row}_{col}", format="%.5f")
        row_data.append(value)
    data.append(row_data)

data = np.array(data)

if st.button("Calculate RSDs"):
    st.subheader("Results")
    for i in range(data.shape[1]):
        column_data = data[:, i]
        column_data = column_data[column_data != 0]  # Ignore empty (zero) entries
        if len(column_data) < 2:
            st.warning(f"Column {i+1}: Not enough data")
            continue
        mean = np.mean(column_data)
        std_dev = np.std(column_data, ddof=1)
        rsd = (std_dev / mean) * 100
        st.success(f"Column {i+1}: RSD = {rsd:.2f}%")