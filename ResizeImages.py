# This script will resize image
# Default resize = 40% of original
# Default location of large files = "C:/Users/Admin/Desktop/BigImages"
# Resized files will replace original size files in same location


import os
from PIL import Image

def resize_images(directory):
    for filename in os.listdir(directory):
        with Image.open(os.path.join(directory, filename)) as img:
            new_width, new_height = int(img.width * 0.4), int(img.height * 0.4)
            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(os.path.join(directory, filename))

if __name__ == "__main__":
    resize_images("C:/Users/Admin/Desktop/BigImages")
