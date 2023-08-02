from PIL import Image, ImageColor
import sys
with Image.open('../images/image.jpeg') as im:
    colors = im.getcolors(1000)
    # catches 👆
    try:
        colors.sort(key=lambda color: color[0], reverse=True)
    except AttributeError:
        sys.exit('The number of color values in the picture exceeds limit. Try increasing the limit, or another image.')
    
luminances = [(0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]) / 255 for count, color in colors] # a list of luminances
average_luminance = sum(luminances) / len(luminances) # calculate the average
    
    
        
        



print(average_luminance)