import streamlit as st

# Title
st.title("Beautiful Table in Streamlit")

# Custom HTML and CSS
html_code = """
<style>
table {
  border-collapse: collapse;
  width: 60%;
  margin: 20px auto;
  font-family: Arial, sans-serif;
  font-size: 18px;
  text-align: center;
  box-shadow: 0 0 10px rgba(0,0,0,0.2);
}
th, td {
  padding: 12px;
  border: 1px solid #ccc;
}
th {
  background-color: #4CAF50;
  color: white;
}
tr:nth-child(even) {
  background-color: #f2f2f2;
}
tr:hover {
  background-color: #ddd;
  cursor: pointer;
}
</style>

<table>
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>City</th>
  </tr>
  <tr>
    <td>Alice</td>
    <td>24</td>
    <td>New York</td>
  </tr>
  <tr>
    <td>Bob</td>
    <td>30</td>
    <td>Los Angeles</td>
  </tr>
  <tr>
    <td>Charlie</td>
    <td>22</td>
    <td>Chicago</td>
  </tr>
</table>
"""

# Render the table
st.markdown(html_code, unsafe_allow_html=True)
