from PIL import Image, ImageDraw, ImageFont, ImageColor
import random
import requests
import sys
import tweepy

import keys

def main():

    client = auth(keys.consumer_key, keys.consumer_secret, access_token=keys.access_token, access_token_secret=keys.access_secret)

    categories = ['age', 'alone', 'amazing', 'anger', 'architecture', 'art', 'attitude', 'beauty', 'best', 'birthday', 'business', 'car', 'change', 'communications', 'computers', 'cool', 'courage', 'dad', 'dating', 'death', 'design', 'dreams', 'education', 'environmental', 'equality', 'experience', 'failure', 'faith', 'family', 'famous', 'fear', 'fitness', 'food', 'forgiveness', 'freedom', 'friendship', 'funny', 'future', 'god', 'good', 'government', 'graduation', 'great', 'happiness', 'health', 'history', 'home', 'hope', 'humor', 'imagination', 'inspirational', 'intelligence', 'jealousy', 'knowledge', 'leadership', 'learning', 'legal', 'life', 'love', 'marriage', 'medical', 'men', 'mom', 'money', 'morning', 'movies', 'success']
    category = categories[random.randint(0, len(categories) - 1)]

    quote_data = get_quote(keys.ninja_api, category)
    author = quote_data[0]['author']
    quote = quote_data[0]['quote']
    print(quote)
    quote = add_new_lines(quote, 45)

    print(quote, author)
    image_date = get_image_data(keys.unsplash_api,f'{author},{category}')

    img = download_img(keys.unsplash_api, image_date)

    # grayscale(img, 'modified.jpeg')

    color = pick_font_color(img)
    print(color)

    modify_image(img, (1980, 1080), 'modified.jpeg', 'JPEG', 99)

    draw('modified.jpeg', 'bot.jpg', 'JPEG', quote, author, color)

    # client.create_tweet(text=f'{python_obj["quote"]}\n\n\"{python_obj["author"]}\"')

def auth(consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str) -> tweepy.Client:
    try:
        client = tweepy.Client(consumer_key=consumer_key,
                           consumer_secret=consumer_secret,
                           access_token=access_token,
                           access_token_secret=access_token_secret)
        return client
    except requests.exceptions.RequestException as e:
        sys.exit(f"Request Error: {str(e)}") 

    

def get_quote(api_key: str, category: str, limit: int=1) -> requests:
    try:
        response = requests.get(url='https://api.api-ninjas.com/v1/quotes', headers={'X-Api-Key': f'{api_key}'}, params={'limit': limit, 'category': category})
        print(response)
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
        return f.name

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
    s = []
    for char in string:
       s.append(char)
    for char in s[slashed:]:
        try:
            n = s[slashed:].index(' ')
        except Exception:
            continue
        s[n+slashed] = '\n'
        slashed+=45
        if slashed > len(s):
            return ''.join(s)

def pick_font_color(image_path: str) -> str:
    with Image.open(image_path) as img:
        colors = img.getcolors(1000000)
        try:
            luminances = [(0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]) / 255 for count, color in colors] 
        except TypeError:
            sys.exit('The number of color values in the picture exceeds limit. Try increasing the limit, or try another image.')
        average_luminance = sum(luminances) / len(luminances)
        
    if average_luminance > 0.5:
        return 'black'
    else:
        return 'white'
        
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