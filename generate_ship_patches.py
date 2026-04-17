import os
import pandas as pd
import rasterio
import matplotlib.pyplot as plt

# load ship labels
df = pd.read_csv("Dataset/xview3/train.csv")

tiny_path = "Dataset/xview3/tiny_scenes"

# output folder
save_dir = "processed ai dataset/ships"
os.makedirs(save_dir, exist_ok=True)                            

# find first VV image
image_path = None
for root, dirs, files in os.walk(tiny_path):
    if "VV_dB.tif" in files:                                                                                            
        image_path = os.path.join(root, "VV_dB.tif")
        break

print("Using image:", image_path)

with rasterio.open(image_path) as src:
    image = src.read(1)

size = 128

# create first 200 ship patches
for i in range(200):
    ship = df.iloc[i]
    row = int(ship["detect_scene_row"])
    col = int(ship["detect_scene_column"])

    patch = image[row-size:row+size, col-size:col+size]

    save_path = os.path.join(save_dir, f"ship_{i}.png")

    plt.imsave(save_path, patch, cmap="gray")

print("200 ship patches saved successfully!")