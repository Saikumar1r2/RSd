import streamlit as st

# Set page title
st.set_page_config(page_title="Calibre LIMS Login")

# Create a blue rectangle box using markdown and custom CSS
st.markdown("""
    <style>
    .login-box {
        background-color: #1E90FF;
        padding: 40px;
        border-radius: 10px;
        text-align: center;
        color: white;
    }
    .login-box h1 {
        font-family: 'Calibri', sans-serif;
        font-size: 30px;
        margin-bottom: 20px;
    }
    .login-box input {
        width: 80%;
        padding: 12px;
        margin: 10px 0;
        border-radius: 5px;
        border: none;
        font-size: 14px;
    }
    .login-box button {
        background-color: #4682B4;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
    }
    </style>
    <div class="login-box">
        <h1>Calibre LIMS</h1>
        <form>
            <input type="text" placeholder="User ID" required><br>
            <input type="password" placeholder="Password" required><br>
            <button type="submit">Login</button>
        </form>
    </div>
""", unsafe_allow_html=True)

# Streamlit UI elements
user_id = st.text_input("User ID")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if user_id and password:
        st.success("Login successful!")
    else:
        st.error("Please enter both User ID and Password.")
