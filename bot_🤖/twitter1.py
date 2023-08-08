import tweepy
import keys

def get_twitter_conn_v1(api_key, api_secret, access_token, access_token_secret) -> tweepy.API:
    """Get twitter conn 1.1"""
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(
        access_token,
        access_token_secret,
    )
    return tweepy.API(auth)

def get_twitter_conn_v2(api_key, api_secret, access_token, access_token_secret) -> tweepy.Client:
    """Get twitter conn 2.0"""
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
    return client
print()
# get connections for both versions
client_v1 = get_twitter_conn_v1(keys.consumer_key, keys.consumer_secret, keys.access_token, keys.access_secret)
client_v2 = get_twitter_conn_v2(keys.consumer_key, keys.consumer_secret, keys.access_token, keys.access_secret)

# upload an image using v1.1 and get its media_id
media_path = "bot.jpg"
media = client_v1.media_upload(filename=media_path)
media_id = media.media_id

# create a tweet with the media_id using v2
client_v2.create_tweet(text="", media_ids=[media_id])