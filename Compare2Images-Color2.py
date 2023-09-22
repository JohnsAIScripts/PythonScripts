# Compare two similar images and circle differences
# Save image file names as: image1.jpg and image2.jpg

import cv2

# Load the images
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')


# Find the absolute difference between the images
difference = cv2.absdiff(image1, image2)

# Convert the difference image to grayscale
gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

# Set a threshold for the grayscale image
threshold = 200
_, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw a green circle around the differences
for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.circle(image1, (int(x + w/2), int(y + h/2)), int(w/2), (0, 255, 0), 2)

# Display the images
cv2.imshow("Original", image1)
cv2.imshow("Modified", image2)
cv2.waitKey(0)
