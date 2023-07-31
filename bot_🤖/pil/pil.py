from PIL import Image, ImageDraw, ImageFont
import sys

with Image.open('../images/image.jpg').convert('RGBA') as base:
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    # get a font
    fnt = ImageFont.truetype("../font/static/Raleway-Medium.ttf", 300)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # get image dimensions 
    width, height = base.size
    # get text dimensions
    text = """ I wanted to eat food but there was no one"""
    left, top, right, bottom = fnt.getbbox(text)
    text_width = right - left
    text_height = bottom - top
    
    # get the middle dimensions
    center_x = (width - text_width) / 2
    center_y = (height - text_height) / 2
    

    # draw text, half opacity
    d.multiline_text((center_x, center_y), text, font=fnt, fill=(255, 255, 255, 128))
    # draw text, full opacity
    d.text((10, 60), "World", font=fnt, fill=(255, 255, 255, 255))

    out = Image.alpha_composite(base, txt)

    out.save('sample_text.webp')
# # Open the image
# image = Image.open("images/image.jpg")
# # Get the image dimensions
# width, height = image.size
# # Create an ImageDraw object
# draw = ImageDraw.Draw(image)
# # Create an ImageFont object with a large font size and a black color
# font = ImageFont.truetype("font/static/Raleway-Medium.ttf", 500)
# font_color = (0, 0, 0)
# # Get the text dimensions
# text = "Hello World"
# text_width, text_height = draw.textsize(text, font=font)
# # Calculate the center coordinates of the text
# text_x = (width - text_width) / 2
# text_y = (height - text_height) / 2
# # Draw the text on the image
# draw.text((text_x, text_y), text, font=font, fill=font_color)
# # Show or save the image
# # image.show()
# image.save("sample_text.jpg")