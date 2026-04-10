import os
import rasterio
import matplotlib.pyplot as plt
import pandas as pd

import os
import rasterio
import matplotlib.pyplot as plt

tiny_path = "Dataset/xview3/tiny_scenes"

scene_folder = [f for f in os.listdir(tiny_path)
                if os.path.isdir(os.path.join(tiny_path, f))][0]

image_path = os.path.join(tiny_path, scene_folder, "VV_dB.tif")

with rasterio.open(image_path) as src:
    image = src.read(1)

print("Image shape:", image.shape)

# take small patch
patch = image[:1000, :1000]

plt.figure(figsize=(8, 8))
plt.imshow(patch, cmap="gray")
plt.title("Small SAR Patch")
plt.axis("off")
plt.show()