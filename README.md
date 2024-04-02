[中文版](README.zh.md)
# Picture Denoising

## Overview
This Python script, "Picture Denoising.py," is designed to denoise images in the current directory. Utilizing the OpenCV library, it provides an efficient way to reduce noise in various image formats including PNG, JPG, JPEG, TIFF, BMP, and GIF.

## Features
- **Support Multiple Image Formats:** Works with PNG, JPG, JPEG, TIFF, BMP, and GIF images.
- **Batch Processing:** Automatically denoises all supported image formats in the current directory.
- **Image Denoising:** Uses OpenCV's fastNlMeansDenoisingColored function for effective noise reduction.

## Requirements
- Python 3
- OpenCV Python library (`cv2`)

## Installation
1. Ensure Python 3 is installed on your system.
2. Install the OpenCV library: `pip install opencv-python`.

## Usage
1. Place the script in the directory containing the images.
2. Run the script using Python: `python Picture Denoising.py`.
3. The script will process each image, denoise it, and save the denoised image with a `denoised_` prefix in the same directory.

```txt
# Selected Code Snippet from Script
import os
import cv2

# Get the current working directory
cwd = os.getcwd()

# Iterate through all files in the directory
for filename in os.listdir(cwd):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        # Read the image
        image = cv2.imread(filename)
        # Denoise the color image
        dst = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
        # Build the denoised image filename
        denoised_filename = f"denoised_{filename}"
        # Save the denoised image
        cv2.imwrite(denoised_filename, dst)
        print(f"Processed and saved: {denoised_filename}")
```
