import streamlit as st
from PIL import Image, ImageDraw

# Create a blank white image
img = Image.new('RGB', (200, 200), color='white')

# Draw a red rectangle
draw = ImageDraw.Draw(img)
draw.rectangle([50, 50, 150, 150], fill='red')

# Show in Streamlit
st.image(img, caption="Red Square")
