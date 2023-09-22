import cv2
import os

# Path to the folder containing the images
images_folder = 'Images'

# Output folder to save the resized images
output_folder = 'ResizedImages'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through the images in the folder
for filename in os.listdir(images_folder):
    # Read the image
    img_path = os.path.join(images_folder, filename)
    img = cv2.imread(img_path)

    # Resize the image to 224x224 pixels
    resized_img = cv2.resize(img, (224, 224))

    # Save the resized image in the output folder
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, resized_img)

    print(f"Resized {filename} and saved as {output_path}")

print("Image resizing complete.")
