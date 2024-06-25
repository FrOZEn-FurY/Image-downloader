from PIL import Image
import os

async def resizeImages(path, size):
    for root, dirs, files in os.walk(path): # Walking in the content of the path
        for file in files:
            if file.endswith(".png"):
                im = Image.open(os.path.join(root, file)) # Opening the file using Pillow
                im = im.resize(size, Image.LANCZOS) # Resizing the file using LANCZOS filter for better quality
                im.save(os.path.join(root, file)) # Saving the file
    print("Images resized successfully!")