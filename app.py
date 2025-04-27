import streamlit as st

# CSS to style the result box with sky blue background
st.markdown("""
    <style>
    .result-box {
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 20px;
        background-color: #87CEEB;  /* Sky Blue Color */
        width: 500px;
        margin: auto;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    .image-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Display the rectangular box with Sample Manager
st.markdown("""
    <div class="result-box">
        <h2>Sample Manager</h2>
    </div>
""", unsafe_allow_html=True)

# Display the human-like figure (You can replace this with your own generated image)
human_figure_url = "https://your-image-url.com/human-like-figure.png"  # Placeholder URL for human-like figure image

st.markdown(f"""
    <div class="image-container">
        <img src="{human_figure_url}" width="200" />
    </div>
""", unsafe_allow_html=True)
