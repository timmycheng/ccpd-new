import torch



# Load YOLO model with weights
model = torch.load('./weights/yolov5/best_yolov5s_final.pt',weights_only=False)
print(model.yaml)