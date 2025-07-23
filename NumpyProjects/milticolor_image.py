from urllib import response
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO


# load image from url
def load_image(url):
     response = requests.get(url)
     return Image.open(BytesIO(response.content))
rama_image = "https://img.freepik.com/premium-photo/lord-rama-lord-ram-bhagwan-rama-indian-god-shri-ram-king-ayodhya-lord-shree-ram_789916-6432.jpg"
r_image = load_image(rama_image)
    
  # display image
plt.figure(figsize=(6,4))
plt.imshow(r_image)  
plt.title("Lord baala Rama")
plt.axis("off")
plt.show()

# convert Numpy array to shape
r_np = np.array(r_image)
print("rama image shae:",r_np.shape)
# convert to grayscale
r_gray = r_image.convert("L")
# Display Grayscale image
plt.figure(figsize=(6,4))
plt.imshow(r_gray,cmap="gray")
plt.title("Grascale Image")
plt.axis("off")
plt.show()       
     