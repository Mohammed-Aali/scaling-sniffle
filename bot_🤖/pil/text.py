from PIL import Image, ImageDraw, ImageFont

quote = "Life is short, art long, opportunity fleeting, experience treacherous, judgment difficult.Life is short, art long, opportunity fleeting, experience treacherous, judgment difficult. Life is short, art long, opportunity fleeting, experience treacherous, judgment difficult."
auther = 'Hippocrates'
print(len(quote))
if 58 <= len(quote):
    slashed = 45
    s = []
    for char in quote:
       s.append(char)
    for char in s[slashed:]:
        try:
            n = s[slashed:].index(' ')
        except:
            continue
        s[n+slashed] = '\n'
        new_s = ''.join(s)
        slashed+=45
        if slashed > len(s):
            break
print(new_s)

with Image.open('../modified.jpeg') as img:
    draw = ImageDraw.Draw(img)

    text = new_s

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
    # draw.text((center_x_a, center_y_a), text=auther, fill='white', font=fnt, align='center')
    y = center_y_a - center_y_q
    draw.text((center_x_a, center_y_a + y), text=auther, fill='white', font=fnt, align='center')

    print(f'Coordinates for quote: x:{center_x_q}, y:{center_y_q}\nfor auther: x:{center_x_a} y:{center_y_a}\n the difference: y: {y}')

    

    img.save('text.webp', 'WEBP')