import cv2

# Set up the video capture from the USB web camera
cap = cv2.VideoCapture(0)

# Check if the video capture was successfully opened
if not cap.isOpened():
    print("Failed to open the video capture.")
    exit(1)

while True:
    # Read the current frame from the video capture
    ret, frame = cap.read()

    # Check if the frame was successfully retrieved
    if not ret:
        print("Failed to retrieve a frame from the video capture.")
        break

    # Convert the frame to grayscale for matching
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform the rest of the processing on the grayscale frame

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the windows
cap.release()
cv2.destroyAllWindows()
