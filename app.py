import streamlit as st

# Title (optional)
st.title("")

# Input fields (no labels, just placeholders)
num1 = st.number_input("", value=0.0, format="%.2f", key="num1")
num2 = st.number_input("", value=0.0, format="%.2f", key="num2")

# Simple operation buttons (without labels)
operation = st.radio("Choose operation", ("+", "-", "×", "÷"), horizontal=True)

# Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "×":
    result = num1 * num2
elif operation == "÷":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error"

# Display the result
st.write(result)
