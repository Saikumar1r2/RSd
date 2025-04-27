import streamlit as st
import pandas as pd

# Create a 5x7 DataFrame
data = {
    "Column 1": [1, 2, 3, 4, 5],
    "Column 2": [6, 7, 8, 9, 10],
    "Column 3": [11, 12, 13, 14, 15],
    "Column 4": [16, 17, 18, 19, 20],
    "Column 5": [21, 22, 23, 24, 25],
    "Column 6": [26, 27, 28, 29, 30],
    "Column 7": [31, 32, 33, 34, 35]
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Display the table
st.table(df)
