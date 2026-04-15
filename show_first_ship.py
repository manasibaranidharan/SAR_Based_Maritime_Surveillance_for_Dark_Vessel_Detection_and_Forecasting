import os
import pandas as pd
import rasterio
import matplotlib.pyplot as plt

# load labels
df = pd.read_csv("Dataset/xview3/train.csv")

# pick first ship
ship = df.iloc[5]

scene_id = ship["scene_id"]
row = int(ship["detect_scene_row"])
col = int(ship["detect_scene_column"])

print("Scene ID:", scene_id)
print("Ship pixel:", row, col)

tiny_path = "Dataset/xview3/tiny_scenes"

# automatically find first VV image
image_path = None
for root, dirs, files in os.walk(tiny_path):
    if "VV_dB.tif" in files:
        image_path = os.path.join(root, "VV_dB.tif")
        break

print("Using image:", image_path)

with rasterio.open(image_path) as src:
    image = src.read(1)

# crop around ship
size = 128
patch = image[row-size:row+size, col-size:col+size]

plt.figure(figsize=(6, 6))
plt.imshow(patch, cmap="gray")
plt.title("First Ship Patch")
plt.axis("off")
plt.show()