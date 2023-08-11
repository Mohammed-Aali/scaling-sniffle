from colorthief import ColorThief
from PIL import Image, ImageDraw, ImageFont, ImageColor
import random
import requests
import sys
import tweepy

import keys

def main():

    api_v1 = auth(keys.consumer_key, keys.consumer_secret, access_token=keys.access_token, access_token_secret=keys.access_secret)
    api_v2 = auth_v2(keys.consumer_key, keys.consumer_secret, access_token=keys.access_token, access_token_secret=keys.access_secret)

    categories = ['age', 'alone', 'amazing', 'anger', 'architecture', 'art', 'attitude', 'beauty', 'best', 'birthday', 'business', 'car', 'change', 'communications', 'computers', 'cool', 'courage', 'dad', 'dating', 'death', 'design', 'dreams', 'education', 'environmental', 'equality', 'experience', 'failure', 'faith', 'family', 'famous', 'fear', 'fitness', 'food', 'forgiveness', 'freedom', 'friendship', 'funny', 'future', 'god', 'good', 'government', 'graduation', 'great', 'happiness', 'health', 'history', 'home', 'hope', 'humor', 'imagination', 'inspirational', 'intelligence', 'jealousy', 'knowledge', 'leadership', 'learning', 'legal', 'life', 'love', 'marriage', 'medical', 'men', 'mom', 'money', 'morning', 'movies', 'success']
    category = categories[random.randint(0, len(categories) - 1)]

    quote_data = get_quote(keys.ninja_api, category)
    try:
        author = quote_data[0]['author']
        quote = quote_data[0]['quote']
    except KeyError:
        sys.exit('Api response error')
    quote = add_new_lines(quote, 45)

    image_date = get_image_data(keys.unsplash_api,f'{author},{category}')

    download_img(keys.unsplash_api, image_date, 'image.jpg')

    color = pick_font_color('image.jpg')

    media_path_pre = 'images/premod.jpg'
    media_path_post = 'images/postmod.jpg'

    modify_image('image.jpg', (1980, 1080), media_path_pre, 'JPEG', 99)

    draw(media_path_pre, media_path_post, 'JPEG', quote, author, color)

    media = api_v1.media_upload(filename=media_path_post).media_id

    # creating the tweet
    api_v2.create_tweet(text=f'"{quote_data[0]["quote"]}"\n\n{author}', media_ids=[media])

def auth(consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str) -> tweepy.API:
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(
            access_token,
            access_token_secret
        )
        return tweepy.API(auth)
    except requests.exceptions.RequestException as e:
        sys.exit(f"Request Error: {str(e)}")

def auth_v2(api_key, api_secret, access_token, access_token_secret) -> tweepy.Client:
    try:
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
        )
        return client
    except requests.exceptions.RequestException as e:
        sys.exit(f"Request Error: {str(e)}") 

def get_quote(api_key: str, category: str, limit: int=1) -> requests:
    try:
        response = requests.get(url='https://api.api-ninjas.com/v1/quotes', headers={'X-Api-Key': f'{api_key}'}, params={'limit': limit, 'category': category})
        return response.json()
    except requests.exceptions.RequestException as e:
        sys.exit(f"Request Error: {str(e)}") 

def get_image_data(access_key: str, query: str, count: int=1) -> requests:
    params = {
    "query": query, 
    "orientation": "landscape", 
    "count": count, 
    "auto": "format",
    }
    try:
        response = requests.get(url='https://api.unsplash.com/photos/random?client_id={}'.format(access_key), params=params)
        return response.json()
    except requests.exceptions.RequestException as e:
        sys.exit(f'Request Error: {str(e)}')

def download_img(access_key: str, img_data, img_path: str='image.jpg') -> str:
    try:
        requests.get(img_data[0]['links']['download_location'], {'client_id': access_key})
    except requests.exceptions.RequestException as e:
        sys.exit(f'Request Error: {str(e)}')

    try:
        img_response = requests.get(img_data[0]["urls"]["raw"])
    except requests.exceptions.RequestException as e:
        sys.exit(f'Request Error: {str(e)}')

    with open(img_path, 'wb') as f:
        f.write(img_response.content)

def grayscale(image_path: str, saved_image: str, format: str='JPEG', quality: int=99,  Grayscale: bool=True):
    if Grayscale:
        with Image.open(image_path).convert('L') as im:   
            im.save(saved_image, format=format.upper(), quality=quality)
    else:
        with Image.open(image_path) as im:
            im.save(saved_image, format=format.upper(), quality=quality)

def modify_image(image_path: str ,size: tuple[int, int], modified_file: str, format: str , quality: int=99) -> None:
    with Image.open(image_path) as im:   
            im.resize(size).save(modified_file, format, quality=quality)

def add_new_lines(string: str, slashed: int) -> str:
    if len(string) <= slashed:
        return string
    s =[]
    for char in string:
        s.append(char)

    initial = slashed
    while True:
        n = string[:slashed].rindex(' ')
        s[n] = '\n'
        slashed += initial
        if len(string) <= slashed:
            return ''.join(s)

def pick_font_color(image_path: str) -> str:
    color_thief = ColorThief(image_path)
    dominant_color = color_thief.get_color(quality=10)

    red, green, blue = dominant_color
    red = red/255.0
    green = green/255.0
    blue = blue/255.0

    if red <= 0.03928:
        red = red / 12.92
    else:
        red = ((red + 0.055) / 1.055) ** 2.4

    if green <= 0.3928:
        green = green / 12.92
    else:
        green = ((green + 0.055) / 1.055) ** 2.4

    if blue <= 0.03928: 
        blue = blue / 12.92 
    else:
        blue = ((blue + 0.055) / 1.055) ** 2.4
    
    img_lum = (0.2126 * red + 0.7152 * green + 0.0722 * blue)
    
    red = ImageColor.getrgb('red')
    yellow = ImageColor.getrgb('yellow')
    green = ImageColor.getrgb('green')
    aqua = ImageColor.getrgb('aqua')
    blue = ImageColor.getrgb('blue')
    purple = ImageColor.getrgb('purple')
    silver = ImageColor.getrgb('silver')
    olive = ImageColor.getrgb('olive')
    font_colors = {'red': red, 'yellow': yellow, 'green': green, 'blue': blue, 'aqua': aqua, 'silver': silver, 'purple': purple, 'olive': olive}

    best_color = ''
    best_contrast = 0.0
    for font_color, font_rgb in font_colors.items():
        red, green, blue = font_rgb
        red = red/255.0
        green = green/255.0
        blue = blue/255.0

        if red <= 0.03928:
            red = red / 12.92
        else:
            red = ((red + 0.055) / 1.055) ** 2.4

        if green <= 0.3928:
            green = green / 12.92
        else:
            green = ((green + 0.055) / 1.055) ** 2.4

        if blue <= 0.03928: 
            blue = blue / 12.92 
        else:
            blue = ((blue + 0.055) / 1.055) ** 2.4
        
        font_lum = (0.2126 * red + 0.7152 * green + 0.0722 * blue)
        contrast = (max(font_lum, img_lum) + 0.05) / (min(font_lum, img_lum) + 0.05)
        if contrast > best_contrast:
            best_contrast = contrast
            best_color = font_color
    
    return best_color
  
def draw(image_path: str, saved_image: str, format: str, quote: str, auther: str, font_color: str='black') -> None:
    with Image.open(image_path) as img:
        draw = ImageDraw.Draw(img)

    fnt = ImageFont.truetype("font/static/Raleway-Bold.ttf", 80)

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

if __name__ == '__main__':
    main()