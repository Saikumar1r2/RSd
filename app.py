import streamlit as st

# Title
st.title("Insert Boxes in Streamlit")

# Custom HTML and CSS for boxes
html_code = """
<style>
/* Styling the box container */
.box {
    width: 300px;
    height: 150px;
    margin: 20px auto;
    padding: 20px;
    background-color: #f2f2f2;
    border: 2px solid #ccc;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    font-family: Arial, sans-serif;
    font-size: 18px;
    color: #333;
}

/* Add hover effect */
.box:hover {
    background-color: #e0e0e0;
    transform: scale(1.05);
    cursor: pointer;
}
</style>

<!-- Creating the boxes -->
<div class="box">This is Box 1</div>
<div class="box">This is Box 2</div>
<div class="box">This is Box 3</div>
"""

# Render the boxes
st.markdown(html_code, unsafe_allow_html=True)
