from PIL import Image

with Image.open('../images/image.jpg') as im:
    
    resized_im = im.resize((1980, 1080))
    
    resized_im.save('resized.webp', quality=90)