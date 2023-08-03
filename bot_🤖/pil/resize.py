from PIL import Image, ImageColor
import sys
with Image.open('../images/nature.jpeg') as img:
    width, height = img.size
    colors = [img.getpixel((0, 0)), img.getpixel((width-1, 0)), img.getpixel((0, height-1)), img.getpixel((width-1, height-1))]
    luminances = [(0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]) / 255 for color in colors] 
    average_luminance = sum(luminances) / len(luminances)
    
    if average_luminance > 0.5:
        font = 'black'
    else:
        font = 'white'


