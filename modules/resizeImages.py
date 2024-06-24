from PIL import Image
import os

async def resizeImages(path, size):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".png"):
                im = Image.open(os.path.join(root, file))
                im = im.resize(size, Image.LANCZOS)
                im.save(os.path.join(root, file))
    print("Images resized successfully!")