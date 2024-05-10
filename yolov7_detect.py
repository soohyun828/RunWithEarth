import os
import cv2
from IPython.display import Image, clear_output
import shutil
import base64

def YoloV7(img_path):
    path = 'result/result'
    shutil.rmtree(path)
    os.system(f"python yolov7\detect.py --weights /content/yolov7/yolov7-e6e.pt --source {img_path} --project result --name result --save-txt")
    with open('result/result/'+str(img_path), 'rb') as f:
        image_bytes = f.read()
        encoded_image = base64.b64encode(image_bytes).decode('utf-8')
    return encoded_image 

def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
    return line_count

