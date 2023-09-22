import cv2
import numpy as np
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
import os

# SET UP TRAINING DATA

train_data = []
train_labels = []

# Path to the folder containing training images
train_folder = 'Images'

# Loop through the images in the training folder
for filename in os.listdir(train_folder):
    img = cv2.imread(os.path.join(train_folder, filename), cv2.IMREAD_GRAYSCALE)
    if img is not None:
        train_data.append(img.flatten())
        train_labels.append(filename.split('.')[0])


# TRAIN THE MODEL:

# Create a pipeline with a scaler and SVM classifier
model = make_pipeline(StandardScaler(), SVC(gamma='auto'))

# Train the model on the training data
model.fit(train_data, train_labels)


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
