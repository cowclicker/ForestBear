import requests
import tweepy
import time

# use this for production; set vars in heroku dashboard
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


def get_forestBearPrice():
	r = requests.get('https://api.scryfall.com/cards/ptk/135');
	j = r.json();
	return (j["prices"]['usd']);

def get_api_access():
	"""
		Returns the authenticated API for tweepy.
		NOTE:
		The keys are not filled in because it is a private key.
		The consumer key and access token can be easily found for 
		your twitter handle by going to app.twitter.com
		
	"""
	consumer_key = CONSUMER_KEY
	consumer_secret = CONSUMER_SECRET

	access_token = ACCESS_KEY
	access_token_secret = ACCESS_SECRET

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	return tweepy.API(auth)


api = get_api_access()

counter = 0

while True:
	
	timing = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
	price = get_forestBearPrice()
	message = "The price of Forest Bear is $" + price +".  The time is " + timing

	api.update_status(status=message)

