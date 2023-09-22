import cv2
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import os

# Path to the folder containing the images
images_folder = 'Images'

# Load the images and resize them
image_data = []
for filename in os.listdir(images_folder):
    img_path = os.path.join(images_folder, filename)
    img = cv2.imread(img_path)
    resized_img = cv2.resize(img, (224, 224))
    image_data.append(resized_img)

# Convert the image data to a numpy array
X = np.array(image_data)

# Reshape the data to match the expected number of features
X = X.reshape(X.shape[0], -1)

# Create the scaler and scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the model
labels = [filename.split('.')[0] for filename in os.listdir(images_folder)]
model = SVC(gamma='auto')
model.fit(X_scaled, labels)

# Rest of the code for live video monitoring


# MONITORING THE LIVE VIDEO FOR MATCHES:

# Initialize the video capture
cap = cv2.VideoCapture(0)

while True:
    # Read the current frame from the video capture
    ret, frame = cap.read()

    # Convert the frame to grayscale for matching
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform the prediction on the frame
    pred_label = model.predict(gray.flatten().reshape(1, -1))

    # If the prediction matches any training label, draw a box around the object
    if pred_label in train_labels:
        cv2.putText(frame, pred_label[0], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 255, 0), 3)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the windows
cap.release()
cv2.destroyAllWindows()
