from PIL import Image, ImageColor
import sys
def main():
    ...
    x = pick_font_color('../images/mattress.jpg')
    print(x)

def pick_font_color(image_path: str) -> str:
    with Image.open(image_path) as img:
        colors = img.getcolors(1000000)
        print(colors)

        color_info = {}

        for count, color in colors:
            luminance = color_to_luminance(color)
            color_info[color] = (count, luminance)
        
        avg_luminance = sum([count * luminance for count, luminance in color_info.values()]) / sum([count for count, luminance in color_info.values()])

        white = ImageColor.getrgb('white')
        black = ImageColor.getrgb('black')
        red = ImageColor.getrgb('red')
        yellow = ImageColor.getrgb('yellow')

        white_lum = color_to_luminance(white)
        black_lum = color_to_luminance(black)
        red_lum = color_to_luminance(red)
        yellow_lum = color_to_luminance(yellow)

        cont_white = (white_lum + 0.05) / (avg_luminance + 0.05)
        cont_black = (black_lum + 0.05) / (avg_luminance + 0.05)
        cont_red = (red_lum + 0.05) / (avg_luminance + 0.05)
        cont_yellow = (yellow_lum + 0.05) / (avg_luminance + 0.05)

        font_colors = {'white': cont_white, 'black': cont_black, 'red': cont_red, 'yellow': cont_yellow}
        best_color = ''
        best_contrast = 0.0
        for key, value in font_colors.items():
            if value > best_contrast:
                best_contrast = value
                best_color = key
        
        return best_color

        
def color_to_luminance(color: tuple[int, int, int]) -> float:
    red, green, blue = color

    red = red/255.0
    green = green/255.0
    blue = blue/255.0

    red = red / 12.92 if red <= 0.03928 else ((red + 0.055) / 1.055) ** 2.4
    green = green / 12.92 if green <= 0.3928 else ((green + 0.055) / 1.055) ** 2.4
    blue = blue / 12.92 if blue <= 0.03928 else ((blue + 0.055) / 1.055) ** 2.4

    return (0.2126 * red + 0.7152 * green + 0.0722 * blue) 
        
if __name__ == '__main__':
    main()
