import tweepy
import pandas as pd

api_key = ""
api_secret = ""
bearer_token = ""

client = tweepy.Client(bearer_token=bearer_token)

query = "Python programming is:retweet"
tweets = client.search_tweets(query=query, lang="en", max_results=100)
