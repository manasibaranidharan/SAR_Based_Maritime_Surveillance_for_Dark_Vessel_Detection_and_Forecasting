import os
import shutil

source_dir = "processed ai dataset/ships"
image_dir = "processed ai dataset/images/train"
label_dir = "processed ai dataset/labels/train"

# create folders
os.makedirs(image_dir, exist_ok=True)
os.makedirs(label_dir, exist_ok=True)

# fixed YOLO label:
# class x_center y_center width height
label_text = "0 0.5 0.5 0.08 0.08"

for filename in os.listdir(source_dir):
    if filename.endswith(".png"):
        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(image_dir, filename)

        # copy image
        shutil.copy(src_path, dst_path)

        # create label file
        txt_name = filename.replace(".png", ".txt")
        txt_path = os.path.join(label_dir, txt_name)

        with open(txt_path, "w") as f:
            f.write(label_text)

print("YOLO dataset prepared successfully!")