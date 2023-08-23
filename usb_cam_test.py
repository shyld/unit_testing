import cv2

def main():
    # Initialize the camera
    capture = cv2.VideoCapture(2, cv2.CAP_GSTREAMER)

    if not capture.isOpened():
        print("Error: Could not open camera.")
        return

    # Set the desired width and calculate the corresponding height to maintain aspect ratio
    desired_width = 640
    ret, frame = capture.read()
    if not ret:
        print("Error: Could not read frame.")
        capture.release()
        return
    aspect_ratio = frame.shape[1] / frame.shape[0]
    desired_height = int(desired_width / aspect_ratio)

    while True:
        ret, frame = capture.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Resize the frame while maintaining aspect ratio
        resized_frame = cv2.resize(frame, (desired_width, desired_height))

        cv2.imshow("USB Camera Feed", resized_frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV window
    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
