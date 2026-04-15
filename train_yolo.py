from ultralytics import YOLO

# load YOLOv8 nano model
model = YOLO("yolov8n.pt")

# train
model.train(
    data="data.yaml",
    epochs=20,
    imgsz=256,
    batch=8,
    name="sar_ship_detector"
)