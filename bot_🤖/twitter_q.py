import json
import keys
import requests
import sys
import tweepy

def main():

    client = auth(keys.consumer_key, keys.consumer_secret, access_token=keys.access_token, access_token_secret=keys.access_secret)

    api_url = 'https://api.api-ninjas.com/v1/quotes'
    response = requests.get(api_url, headers={'X-Api-Key': f'{keys.ninja_api}'})
    if response.status_code == requests.codes.ok:
        python_obj = json.loads(response.text)[0]
    else:
        print("Error:", response.status_code, response.text)

    print(python_obj)
    client.create_tweet(text=f'{python_obj["quote"]}\n\n\"{python_obj["author"]}\"')

def auth(consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
    try:
        client = tweepy.Client(consumer_key=consumer_key,
                           consumer_secret=consumer_secret,
                           access_token=access_token,
                           access_token_secret=access_token_secret)
    except:
        sys.exit("Wasn't able to establish a connection with API")
    return client

if __name__ == '__main__':
    main()