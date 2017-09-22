import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

tweet_cnt = 0
pos_tweet_cnt, neg_tweet_cnt, neu_tweet_cnt = 0, 0, 0
search_item = input("Enter the search text: ")

consumer_key = "yYpenGW8K835LBzmv6yrwdZ2z" 								#"thO5D3znaNrUvPNUzhQVnipPB"
consumer_secret = "KduEOuMuKXkL8qgDR3d00xJKk7SJrziQias6pOi48joZTfJCbg" 	#"0OEBfqgSVd6urMNkTH52fD92OUSzz2JASKQQOzbC3ZxQvNdnO6"

access_token = "226849265-P8X9zlTdx5WkzKsuCBiTWlOqibb0gLwiuDAkvgIK" 	#"226849265-PWLIIF7Ycnx1xIVQBjAKx7nElJmwRoYyAwhv6rl3"
access_token_secret = "K7AClLUTVzTD44IMW8oW6s5YDUZs1QTlys6CeUnCfdYwO" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search_twts = api.search(q = search_item, lang = "en", count = 200)

#total_twts = len(search_twts)

for tweet in search_twts:
	tweet_cnt += 1
	analysis = TextBlob(tweet.text)
	tweet_polarity = analysis.sentiment.polarity
	if tweet_polarity > 0:
		pos_tweet_cnt += 1
	elif tweet_polarity < 0:
		neg_tweet_cnt += 1
	else:
		neu_tweet_cnt += 1

labels = ["positive", "negative", "neutral"]
sizes = [pos_tweet_cnt, neg_tweet_cnt, neu_tweet_cnt]
colors = ["green", "yellow", "blue"]

plt.pie(sizes, labels = labels, colors = colors, autopct='%2.0f%%', shadow = True, startangle = 90)
plt.title("Sentiment analysis of latest {} tweets mentioning {}".format(tweet_cnt, search_item))
plt.show()