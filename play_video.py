import cv2
video_path = "runs/detect/exp3/09-27-29.mp4"
cap = cv2.VideoCapture(video_path)

# Get the video frame rate
fps = int(cap.get(cv2.CAP_PROP_FPS))
# Calculate the duration each frame should be displayed to achieve half speed
delay = int(1000 / fps * 2)  # multiply by 2 for half speed

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Process frame here
    cv2.imshow('Video Playback', frame)

    # Exit the program if the 'q' key is pressed
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

# Release the video stream and close all windows
cap.release()
cv2.destroyAllWindows()
