from ultralytics import YOLO

# Load a model
model = YOLO("/Users/zhukaihong/PycharmProjects/Personal_Project/runs/detect/train10/weights/last.pt")  # build a new model from scratch

# Use the model
model.train(data="data.yaml", epochs=50) # train the model$
