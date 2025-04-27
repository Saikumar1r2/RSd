import streamlit as st

# Set page layout and configuration
st.set_page_config(page_title="4x6 Grid", page_icon=":bar_chart:", layout="centered")

# Hide Streamlit's default header and footer
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Create a 4x6 grid layout
grid_layout = []

# Create the grid with 4 rows and 6 columns
for i in range(4):  # 4 rows
    row = st.columns(6)  # 6 columns in each row
    for j in range(6):  # 6 columns in total
        with row[j]:
            # Display a button for each box in the grid
            if st.button(f"Box {i*6 + j + 1}"):
                st.write(f"Box {i*6 + j + 1} clicked")

