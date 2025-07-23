import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO


def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))
peacock_url ="https://img.freepik.com/premium-photo/beautiful-peacock-bird-feather-vibrant-color_800563-4625.jpg"
peacock = load_image_from_url(peacock_url)
# display an original image
plt.figure(figsize=(6,4))
plt.imshow(peacock)
plt.title("Peacock")
plt.axis('off')
plt.show()
