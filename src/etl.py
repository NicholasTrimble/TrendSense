import tweepy
import pandas as pd

api_key = ""
api_secret = ""
bearer_token = ""

client = tweepy.Client(bearer_token=bearer_token)

query = "Python programming is:retweet"
tweets = client.search_tweets(query=query, lang="en", max_results=100)


data = []
for tweet in tweets.data:
    data.append({"text": tweet.text, "id": tweet.id})

df = pd.DataFrame(data)
df.to_csv("data/X_data.csv", index=False)
