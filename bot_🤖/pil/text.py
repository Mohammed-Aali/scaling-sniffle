from PIL import Image, ImageDraw, ImageFont

def add_new_lines(string: str, slashed: int) -> str:
    if len(string) <= slashed:
        return string
    s = []
    for char in string:
       s.append(char)
    for char in s[slashed:]:
        try:
            n = s[slashed:].index(' ')
        except Exception:
            continue
        s[n+slashed] = '\n'
        slashed+=slashed
        if slashed > len(s):
            return ''.join(s)

def draw(image_path: str, saved_image: str, format: str, quote: str, auther: str, font_color: str='black') -> None:
    with Image.open(image_path) as img:
        draw = ImageDraw.Draw(img)

    fnt = ImageFont.truetype("../font/static/Raleway-Bold.ttf", 80)

    # get the middle dimensions for main
    left, top, right, bottom = draw.textbbox((0,0), text=quote, font=fnt)
    quote_width = right - left
    quote_height = bottom - top

    center_x_q = (img.size[0] - quote_width) / 2
    center_y_q = (img.size[1] - quote_height) / 2

    # drawing the text
    draw.multiline_text((center_x_q, center_y_q - 150), text=quote, fill=font_color, font=fnt, align='center')

    # get the middle dimension for auther
    left, top, right, bottom = draw.textbbox((0,0), auther, font=fnt)
    auther_width = right - left
    auther_height = bottom - top

    center_x_a = (img.size[0] - auther_width) / 2
    center_y_a = (img.size[1] - auther_height) / 2

    # drawing the text
    y = center_y_a - center_y_q
    draw.text((center_x_a, center_y_a + y), text=f'"{auther}"', fill=font_color, font=fnt, align='center')

    img.save(saved_image, format.upper())

quote = "Don't think of yourself as a woman in business, Think of yourself as man."
author = 'Hello ladies'
x = add_new_lines(quote, 40)
media_path_pre = '../images/premod.jpg'
media_path_post = 'postmod.webp'

draw(media_path_pre, media_path_post, 'WEBP', x, author)
print(len(quote))
print(x)