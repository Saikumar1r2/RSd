import streamlit as st

# CSS to style the result boxes with sky blue background, centered layout for laptop
st.markdown("""
    <style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 100vh;
    }
    .result-box {
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 20px;
        background-color: #87CEEB;  /* Sky Blue Color */
        width: 300px;  /* Reduced size */
        margin: 10px;   /* Reduced space between boxes */
        text-align: center;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    .image-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Create a container for the layout
with st.container():
    # Display the rectangular box for Sample Manager
    st.markdown("""
        <div class="result-box">
            <h2>Sample Manager</h2>
        </div>
    """, unsafe_allow_html=True)

    # Display the rectangular box for Resource Manager
    st.markdown("""
        <div class="result-box">
            <h2>Resource Manager</h2>
        </div>
    """, unsafe_allow_html=True)

    # Display the rectangular box for System Manager
    st.markdown("""
        <div class="result-box">
            <h2>System Manager</h2>
        </div>
    """, unsafe_allow_html=True)

    # Display images for each manager (Replace with actual image URLs)
    # Placeholder for human-like figure image URL
    human_figure_url = "https://your-image-url.com/human-like-figure.png"  # Placeholder URL

    # Display the human-like figure below each manager box
    for _ in range(3):
        st.markdown(f"""
            <div class="image-container">
                <img src="{human_figure_url}" width="100" />
            </div>
        """, unsafe_allow_html=True)
