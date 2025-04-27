import streamlit as st
from PIL import Image, ImageDraw

# Create a blank white image
img = Image.new('RGB', (300, 300), color='white')

# Draw a rectangle (e.g., a blue square)
draw = ImageDraw.Draw(img)
draw.rectangle([50, 50, 250, 250], outline="blue", width=5)

# Draw a circle (e.g., a red circle inside the rectangle)
draw.ellipse([100, 100, 200, 200], outline="red", width=5)

# Show the image in Streamlit
st.image(img, caption="Circle and Rectangle", use_column_width=True)
