import streamlit as st

st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select operation:",
    ["Add", "Subtract", "Multiply", "Divide"]
)

# Perform calculation based on selection
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 == 0:
        result = "Cannot divide by zero!"
    else:
        result = num1 / num2
else:
    result = 0

# Display the result
st.write(f"Result of {operation}: {result}")
