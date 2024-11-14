from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")

# Train the model
if __name__ == '__main__':
    train_results = model.train(
        data="custom_dataset.yaml",  # path to dataset YAML
        epochs=16,  # number of training epochs
        imgsz=640,  # training image size
        device="0",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
    )

    # Evaluate model performance on the validation set
    # metrics = model.val()

    # # Perform object detection on an image
    # results = model("test.jpg")
    # results[0].show()

    # Export the model to ONNX format
    path = model.export(format="onnx")  # return path to exported model