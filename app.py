import streamlit as st

# Title of the application
st.title("Streamlit Number Input Example")

# Number input for specifying the number of rows
num_rows = st.number_input("Number of rows", min_value=1, max_value=100, value=5)

# Display the number of rows selected
st.write(f"You selected {num_rows} rows.")

# Example use case: display a table based on the number of rows input
import pandas as pd

# Create a simple DataFrame based on the number of rows input
data = {'Column 1': [f'Row {i+1}' for i in range(num_rows)], 'Column 2': [i+1 for i in range(num_rows)]}
df = pd.DataFrame(data)

# Display the DataFrame
st.write(df)
