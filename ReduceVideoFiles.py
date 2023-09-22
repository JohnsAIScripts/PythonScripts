# This script will resize your videos
# Default file type = mov
# Default size change = -50%
# Default file location = LargeFiles
# Default resized location = COMPRESSED
#-----------------------------------------
# DO THIS FIRST --> pip install moviepy
#-----------------------------------------

import os
from moviepy.editor import VideoFileClip

# Input folder containing the MOV videos
input_folder = "LargeFiles"

# Output folder where compressed videos will be saved
output_folder = "COMPRESSED"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Desired reduction percentage (e.g., 50%)
reduction_percentage = 50

# List all MOV files in the input folder
mov_files = [file for file in os.listdir(input_folder) if file.endswith(".mov")]

print("about to shrink")

# Loop through each MOV file and compress it
for mov_file in mov_files:
    input_path = os.path.join(input_folder, mov_file)
    output_path = os.path.join(output_folder, mov_file)
    
    # Load the video clip
    clip = VideoFileClip(input_path)
    
    # Calculate the new dimensions to reduce the file size
    new_width = int(clip.size[0] * (1 - reduction_percentage / 100))
    new_height = int(clip.size[1] * (1 - reduction_percentage / 100))
    
    # Resize the video clip
    resized_clip = clip.resize((new_width, new_height))
    
    # Write the resized clip to the output file
    resized_clip.write_videofile(output_path, codec='libx264')

print("Compression completed.")
