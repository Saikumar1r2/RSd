import streamlit as st

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #333;
            color: white;
            padding: 15px 0;
            text-align: center;
        }
        nav {
            background-color: #444;
            overflow: hidden;
        }
        nav a {
            float: left;
            display: block;
            color: white;
            padding: 14px 16px;
            text-align: center;
            text-decoration: none;
        }
        nav a:hover {
            background-color: #ddd;
            color: black;
        }
        section {
            padding: 20px;
            margin: 20px;
            background-color: white;
            border-radius: 8px;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px;
        }
    </style>
</head>
<body>

<header>
    <h1>Welcome to My Portfolio</h1>
    <p>Your one-stop destination for all my projects and experience!</p>
</header>

<nav>
    <a href="#about">About Me</a>
    <a href="#projects">Projects</a>
    <a href="#contact">Contact</a>
</nav>

<section id="about">
    <h2>About Me</h2>
    <p>Hello, I'm John Doe, a passionate web developer with a love for creating innovative solutions.</p>
</section>

<footer>
    <p>© 2025 John Doe. All rights reserved.</p>
</footer>

</body>
</html>
"""

# Use markdown to render the HTML
st.markdown(html_code, unsafe_allow_html=True)
