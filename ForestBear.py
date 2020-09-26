import requests
import tweepy
import time

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
	consumer_key = ""
	consumer_secret = ""

	access_token = ""
	access_token_secret = ""

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	return tweepy.API(auth)


api = get_api_access()

while True:

	price = get_forestBearPrice()
	message = "The price of Forest Bear is $" + price

	api.update_status(status=message)
	time.sleep(43200)