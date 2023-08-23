import numpy as np
import cv2
from frame_publisher.utils import gstreamer_pipeline
from frame_publisher.config import frame_publisher_parameters
import os 
from flex_sanitize_led.device.gpio import UV_driver


class DetectGo():
    def __init__(self):
        sensor_id = 2
        self.cap = cv2.VideoCapture(sensor_id)

    def get_scene(self):
        
        try:
            # Allow time for auto-exposure
            for _ in range(10):
                self.cap.read()

            # Capture the image
            ret, frame = self.cap.read()
            scale_percent = 40 # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)

            # resize image
            frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    
            # Rotate image

            if not ret:
                raise Exception("Failed to capture image")

            if frame_publisher_parameters.isRotate:
                frame = cv2.rotate(frame, cv2.ROTATE_180)

            print("Image captured successfully!")

        except Exception as e:
            print("Error:", e)
            
        return frame

    def calculate_pose(self, matches, kp1, kp2, scene_center):
        src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

        # Find homography matrix
        M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        # Calculate the centroid of the object in the scene
        object_center = np.mean(dst_pts, axis=0)

        # Calculate the pose of the object with respect to the center of the image
        delta = tuple(object_center[0] - scene_center[0])

        return delta

    def match_color(self):
        # Load the image
        image = self.get_scene().copy()

        # Convert the image to the HSV color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds for yellow color in HSV
        lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
        upper_yellow = np.array([30, 255, 255], dtype=np.uint8)

        # Threshold the image to get a binary mask of yellow pixels
        yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

        # Find contours in the yellow mask
        contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find the contour with the largest area
        largest_contour = max(contours, key=cv2.contourArea)

        # Calculate the centroid of the largest contour
        M = cv2.moments(largest_contour)
        centroid_x = int(M["m10"] / M["m00"])
        centroid_y = int(M["m01"] / M["m00"])

        # Calculate the center of the image
        image_height, image_width, _ = image.shape
        image_center_x = image_width // 2
        image_center_y = image_height // 2

        # Calculate the position relative to the image center
        relative_position_x = centroid_x - image_center_x
        relative_position_y = centroid_y - image_center_y

        self.delta_list = [(relative_position_x, relative_position_y)]

    def match_images(self, images_folder):
        # Load the scene image
        scene_image = self.get_scene().copy()

        # Calculate the center of the scene image
        scene_center = np.array([[scene_image.shape[1] / 2, scene_image.shape[0] / 2]], dtype=np.float32)

        # Create a kaze object
        kaze = cv2.KAZE_create()

        # Create a FLANN matcher
        flann = cv2.FlannBasedMatcher(dict(algorithm=1, trees=5), dict(checks=50))

        # Read images from the folder
        images = []
        for filename in os.listdir(images_folder):
            image_path = os.path.join(images_folder, filename)
            image = cv2.imread(image_path, 0)
            images.append((filename, image))

        # Perform feature matching for each image
        delta_list = []
        delta = []
        for img_name, img in images:
            scene_image = self.get_scene().copy()
            self.visualize_input(scene_image)
            # Find keypoints and descriptors
            try:
                kp1, des1 = kaze.detectAndCompute(img, None)
                kp2, des2 = kaze.detectAndCompute(scene_image, None)

                # Match keypoints using FLANN
                matches = flann.knnMatch(des1, des2, k=2)


                # Apply ratio test to filter good matches
                good_matches = []
                for m, n in matches:
                    if m.distance < 0.05 * n.distance:
                        good_matches.append(m)

                # If enough good matches found, calculate pose and draw object on the scene image
                delta = self.calculate_pose(good_matches, kp1, kp2, scene_center)
                delta_list.append(delta)


            
            except Exception as e:
                print('Error: ', e)
                print('detection failed for given image')

            # Print pose information
            print(f"Pose of {img_name}:")
            print("Translation (delta):", delta)
            print("-----------------------------------")

        print('Delta list: ',delta_list)
        self.delta_list = delta_list
    
    def go_near_object(self):
        x = 0
        y = 0
        if len(self.delta_list) == 0:
            return True
        for delta in self.delta_list:
            x += delta[0]
            y += delta[1]
        x = int(x/len(self.delta_list))
        y = int(y/len(self.delta_list))
        print('========================')
        print('Diff on x:', x, 'diff on y: ', y)
        if abs(x) < 10 and abs(y) < 10:
            return True
        maks_x = 50 #
        maks_y = -30 # cmd required to move the object upwards

        cmd_x = int((y * maks_y)/154) #Vertical motion
        cmd_y = int((x * maks_x)/204) #Horizantal motion

        print('Horizantal', cmd_y, 'Vertical', cmd_x)
        UV_driver(int(cmd_y), int(cmd_x))
        scene_image = self.get_scene().copy()
        #self.visualize_input(scene_image)
        # Release the camera

        return False


    def visualize_input(self, img):
        cv2.namedWindow('Frame') 
        cv2.imshow('Frame', img)
        if cv2.waitKey(40) == 79: # Press Ctrl + shift + o (79 ASCI code) to exit the run
            rclpy.shutdown()

    def converge(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Example usage:
        scene_path = os.path.join(current_directory, "uv_card_samples")

        # detect_go = DetectGo()
        for i in range(10): # Timeout
            self.match_images(scene_path)
            #self.match_color()
            result = self.go_near_object()
            if result == True:
                # detect_go.cap.release()
                break

if __name__ == '__main__':
    detect_go = DetectGo()
    detect_go.converge()
