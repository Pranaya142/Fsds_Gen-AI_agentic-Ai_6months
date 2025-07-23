import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO


# set streamlit config
st.set_page_config("Beautiful Peacock Feather Image Processor",layout="wide")
# title of the streamlit
st.title("Peaacock Feather Image Processor")
# Load Image
@st.cache_data
def load_image():
    url = "https://img.freepik.com/premium-photo/beautiful-peacock-bird-feather-vibrant-color_800563-4625.jpg"
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGB")
#load image & display
peacock_image = load_image()
st.image(peacock_image,caption ="Original Image",use_container_width=True)
#convert to numpy array
peacock_np = np.array(peacock_image)
R,G,B = peacock_np[:,:,0],peacock_np[:,:,1],peacock_np[:,:,2]
# create channel images
red_img = np.zeros_like(peacock_np)
green_img = np.zeros_like(peacock_np)
blue_img = np.zeros_like(peacock_np)
red_img[:,:,0] = R
green_img[:,:,1] = G
blue_img[:,:,2] = B
# display RGB channel
st.subheader("RGB Channel Visualization")
col1,col2,col3 = st.columns(3)
with col1:
    st.image(red_img,caption = "Red Channel",use_container_width=True)
with col2:
    st.image(green_img,caption = "Green Channel",use_container_width=True)
with col3:
    st.image(blue_img,caption = "Blue Channel",use_container_width=True)
# Gray Scale + color Map
st.subheader("Colormapped Grayscale Image")
colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)
peacock_image_gray = peacock_image.convert("L")
peacock_gray_np = np.array(peacock_image_gray)
# Plot using matplotlib with colormap
fig,ax = plt.subplots(figsize=(6, 4))
ax.imshow(peacock_gray_np, cmap=colormap)
ax.axis("off")
st.pyplot(fig)
