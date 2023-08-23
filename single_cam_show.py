import numpy as np
import cv2
import time
import datetime 
#import FaceDetection
#import torch
#import torchvision

width = 3280
height = 2464
rate = 5

def gstreamer_pipeline(
    sensor_id=1,
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
camera_id = 0 #IR
camera_id = 1 #RGB
cap = cv2.VideoCapture(gstreamer_pipeline(sensor_id=camera_id), cv2.CAP_GSTREAMER)


fourcc = cv2.VideoWriter_fourcc(*"mp4v")

timestr = time.strftime("%m_%d_%Y_%H%M%S")
#writer = cv2.VideoWriter(timestr+'.mp4', fourcc, rate, (width, height), True)

#model1 = torchvision.models.detection.keypointrcnn_resnet50_fpn(pretrained=True)
#model1 = model1.eval().cuda()
#torch.save(model1, 'model1.pth')

if cap.isOpened():
    print('cap open')

    for i in range(5000):
        ret_val, img = cap.read()
        
        scale_percent = 20 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        #img = np.array(img)
        #img = FaceDetection.detector(img, model1)

        cv2.imshow('Title',img)
        #writer.write(img)

        if cv2.waitKey(40) == 27:
            break

#writer.release()
cap.release()
print('video saved')