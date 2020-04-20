from dotenv import load_dotenv
import os
from ClassTwitter import Twitter

load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_key_secret = os.getenv('CONSUMER_KEY_SECRET')

access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

twitter = Twitter(consumer_key, consumer_key_secret, access_token, access_token_secret)

dialogue = input('What do you want to tweet? ')
twitter.tweet(dialogue)