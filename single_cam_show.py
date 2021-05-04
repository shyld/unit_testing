import numpy as np
import cv2
import time
import datetime 
#import FaceDetection
#import torch
#import torchvision

width = 600#3280
height = 400#2464
rate = 5

def gstreamer_pipeline(
    sensor_id=0,
    #ensor_mode=3,
    capture_width=width,
    capture_height=height,
    display_width=width,
    display_height=height,
    framerate=rate,
    #flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d !" #sensor-mode=%d ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=vertical-flip ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            #sensor_mode,
            capture_width,
            capture_height,
            framerate,
            #flip_method,
            display_width,
            display_height,
        )
    )

cap = cv2.VideoCapture(gstreamer_pipeline(sensor_id=0), cv2.CAP_GSTREAMER)


fourcc = cv2.VideoWriter_fourcc(*"MP4V")

timestr = time.strftime("%m_%d_%Y_%H%M%S")
writer = cv2.VideoWriter(timestr+'.mp4', fourcc, rate, (width, height), True)

#model1 = torchvision.models.detection.keypointrcnn_resnet50_fpn(pretrained=True)
#model1 = model1.eval().cuda()
#torch.save(model1, 'model1.pth')

if cap.isOpened():
    print('cap open')

    for i in range(500):
        ret_val, img = cap.read()
        #img = np.array(img)
        #img = FaceDetection.detector(img, model1)

        cv2.imshow('Title',img)
        #writer.write(img)

        if cv2.waitKey(40) == 27:
            break

writer.release()
cap.release()
print('video saved')
