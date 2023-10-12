# Compare two similar images and circle differences

import cv2

# Load the images
image1 = cv2.imread('image11.jpg')
image2 = cv2.imread('image12.jpg')

# Find the difference between the images
difference = cv2.absdiff(image1, image2)

# Convert the difference image to grayscale
gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

# Set a threshold for the grayscale image
thresh = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)[1]

# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over the contours
for contour in contours:
    # Get the rectangle bounding the contour
    (x, y, w, h) = cv2.boundingRect(contour)
    
    # Draw a green rectangle around the difference
    cv2.rectangle(image1, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the images
cv2.imshow("Original", image1)
cv2.imshow("Modified", image2)
cv2.waitKey(0)
