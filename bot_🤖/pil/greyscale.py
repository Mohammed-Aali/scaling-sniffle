from PIL import Image, ImageOps

with Image.open("../images/image.jpg").convert('L') as img:
    img.save('../images/greyscale.jpg', 'JPEG')


