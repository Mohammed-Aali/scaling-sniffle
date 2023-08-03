from PIL import Image, ImageColor
import sys
with Image.open('../images/nature.jpeg') as im:
    colors = im.getcolors(1000000)
    # catches 👆
    try:
        luminances = [(0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]) / 255 for count, color in colors] 
    except TypeError:
         sys.exit('The number of color values in the picture exceeds limit. Try increasing the limit, or try another image.')
    average_luminance = sum(luminances) / len(luminances)

