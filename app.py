import streamlit as st
from PIL import Image, ImageDraw

# Increase resolution for clarity (e.g., 600x600)
img = Image.new('RGB', (600, 600), color='white')

# Create a drawing context
draw = ImageDraw.Draw(img)

# Draw a blue rectangle (more accurate)
draw.rectangle([150, 150, 450, 450], outline="blue", width=10)

# Draw a red circle (anti-aliasing for smooth edges)
draw.ellipse([200, 200, 400, 400], outline="red", width=10)

# Show the high-quality image
st.image(img, caption="High Clarity Circle and Rectangle", use_column_width=True)
