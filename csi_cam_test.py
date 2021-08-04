from csi_camera import CSI_Camera
import cv2
import numpy as np

left_camera = CSI_Camera()
left_camera.create_gstreamer_pipeline(
                        capture_width=640,
                        capture_height=480,
                        sensor_id=0,
                        #sensor_mode=SENSOR_MODE_1080,
                        framerate=5,
                        flip_method=0,
                        display_height=480,
                        display_width=640)
left_camera.open(left_camera.gstreamer_pipeline)
left_camera.start()
cv2.namedWindow('IR Image', cv2.WINDOW_AUTOSIZE)

for i in range(500):
    _ , camera_image=left_camera.read()
    camera_image = cv2.resize(camera_image, (640,360), interpolation=cv2.INTER_AREA)
    translation_matrix = np.float32([[1,0,-16], [0,1,0] ])
    camera_image = cv2.warpAffine(camera_image, translation_matrix, (640,360))

    cv2.imshow('Title',camera_image)
    
    if cv2.waitKey(40) == 27:
        break

#left_camera.stop()
#left_camera.release()
#cv2.destroyAllWindows()