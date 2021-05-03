import numpy as np
import cv2
import time
import datetime 

width = 3280
height = 2464
rate = 3

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

cap0 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=0), cv2.CAP_GSTREAMER)
cap1 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=1), cv2.CAP_GSTREAMER)


fourcc = cv2.VideoWriter_fourcc(*"XVID")
timestr = time.strftime("%m_%d_%Y_%H%M%S")

DISPLAY_WIDTH=640
DISPLAY_HEIGHT=480


writer0 = cv2.VideoWriter('/home/shyldai/shyld/save_video/saved_videos/dual_'+timestr+'0.avi', fourcc, rate, (DISPLAY_WIDTH, DISPLAY_HEIGHT), True)
writer1 = cv2.VideoWriter('/home/shyldai/shyld/save_video/saved_videos/dual_'+timestr+'1.avi', fourcc, rate, (DISPLAY_WIDTH, DISPLAY_HEIGHT), True)
DISPLAY_WIDTH=640
DISPLAY_HEIGHT=480

if cap0.isOpened() and cap1.isOpened():
    print('caps open')

    for i in range(200):
        ret_val, img0 = cap0.read()
        ret_val, img1 = cap1.read()


        img0 = cv2.resize(img0, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
        img1 = cv2.resize(img1, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

        #img_comb= np.hstack((img0, img1))

        writer0.write(img0)
        writer1.write(img1)

writer0.release()
writer1.release()
cap0.release()
cap1.release()
print('video saved')