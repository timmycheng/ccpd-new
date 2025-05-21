import torch
from ultralytics import YOLO, settings

settings.update({'datasets_dir': './datasets/'})
print(settings)
model = YOLO('yolov8s.pt') 
# model.info()  # print model information
model.val(data='./datasets/CCPD/splits_test.yaml')


# # Load YOLO model with weights
# model = torch.load('./weights/yolov5/best_yolov5s_final.pt',weights_only=False)
# print(model.yaml)
