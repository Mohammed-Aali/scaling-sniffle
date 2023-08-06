from colorthief import ColorThief
from PIL import ImageColor

def pick_font_color(image_path: str) -> str:
    # Get the dominant color from the image
    color_thief = ColorThief(image_path)
    dominant_color = color_thief.get_color(quality=1)
    
    # Define some font colors to choose from
    white = ImageColor.getrgb('white')
    black = ImageColor.getrgb('black')
    red = ImageColor.getrgb('red')
    yellow = ImageColor.getrgb('yellow')
    font_colors = [white, black, red, yellow]

    # Calculate the contrast ratio between the background color and each font color
    # Based on https://www.w3.org/TR/WCAG20/#contrast-ratiodef
    def contrast_ratio(color1: tuple[int, int, int], color2: tuple[int, int, int]) -> float:
        # Convert RGB values to relative luminance
        def luminance(color: tuple[int, int, int]) -> float:
            red, green, blue = color
            red = red/255.0
            green = green/255.0
            blue = blue/255.0
            red = red / 12.92 if red <= 0.03928 else ((red + 0.055) / 1.055) ** 2.4
            green = green / 12.92 if green <= 0.3928 else ((green + 0.055) / 1.055) ** 2.4
            blue = blue / 12.92 if blue <= 0.03928 else ((blue + 0.055) / 1.055) ** 2.4
            return (0.2126 * red + 0.7152 * green + 0.0722 * blue)

        # Calculate the contrast ratio
        lum1 = luminance(color1)
        lum2 = luminance(color2)
        return (max(lum1, lum2) + 0.05) / (min(lum1, lum2) + 0.05)

    # Find the font color with the highest contrast ratio
    best_color = ''
    best_contrast = 0.0
    for font_color in font_colors:
        contrast = contrast_ratio(dominant_color, font_color)
        if contrast > best_contrast:
            best_contrast = contrast
            best_color = font_color
    
    # Return the font color as a hex string
    return '#%02x%02x%02x' % best_color

# Test the function with an image
print(pick_font_color('../images/mattress.jpg'))
