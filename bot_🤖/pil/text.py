from PIL import Image, ImageDraw, ImageFont

quote = "Life is short, art long, opportunity fleeting, experience treacherous, judgment difficult."
auther = 'Hippocrates'
if len(quote) >= 58:
    s = list(quote)
    n = s[45:].index(' ')
    s[n+45] = '\n'
    new_s = ''.join(s)
    quote = new_s
    print(new_s)

with Image.open('resized.webp') as img:
    draw = ImageDraw.Draw(img)

    text = quote

    fnt = ImageFont.truetype("../font/static/Raleway-Bold.ttf", 80)

    # get the middle dimensions for main
    left, top, right, bottom = draw.textbbox((0,0), text, font=fnt)
    quote_width = right - left
    quote_height = bottom - top
    
    
    center_x_q = (img.size[0] - quote_width) / 2
    center_y_q = (img.size[1] - quote_height) / 2

    # drawing the text
    draw.multiline_text((center_x_q, center_y_q - 100), text=text, fill='white', font=fnt, align='center')

    # get the middle dimension for auther
    left, top, right, bottom = draw.textbbox((0,0), auther, font=fnt)
    auther_width = right - left
    auther_height = bottom - top

    center_x_a = (img.size[0] - auther_width) / 2
    center_y_a = (img.size[1] - auther_height) / 2
    
    # drawing the text
    draw.text((center_x_a, center_y_a + 100), text=auther, fill='white', font=fnt, align='center')
    

    img.save('text.webp', 'WEBP')