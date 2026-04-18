from ultralytics import YOLO

# load trained model
model = YOLO("runs/detect/sar_ship_detector/weights/best.pt")

# run prediction on one SAR patch
results = model.predict(
    source="processed_ai_dataset/images/train/ship_181.png",
    conf=0.25,
    save=True
)

print("Prediction completed!")