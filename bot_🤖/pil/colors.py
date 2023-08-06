from colorthief import ColorThief
from PIL import ImageColor, Image

def pick_font_color(image_path: str) -> str:
    color_thief = ColorThief(image_path)
    dominant_color = color_thief.get_color(quality=1)

    if luminance(dominant_color) > 0.1:
        return 'black'
    else:
        return 'white'

    # Convert RGB values to relative luminance
def luminance(color: tuple[int, int, int]) -> float:
    red, green, blue = color
    red = red/255.0
    green = green/255.0
    blue = blue/255.0
    if red <= 0.03928
    red = red / 12.92 if red <= 0.03928 else ((red + 0.055) / 1.055) ** 2.4
    green = green / 12.92 if green <= 0.3928 else ((green + 0.055) / 1.055) ** 2.4
    blue = blue / 12.92 if blue <= 0.03928 else ((blue + 0.055) / 1.055) ** 2.4
    return (0.2126 * red + 0.7152 * green + 0.0722 * blue)

# Test the function with an image
print(pick_font_color('../images/image.jpg'))
