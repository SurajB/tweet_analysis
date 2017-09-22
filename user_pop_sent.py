import tweepy
from textblob import TextBlob
import csv
import matplotlib.pyplot as plt

twtr_handle = input("Enter the twitter handle to perform sentiment analysis: ")

tweets_collection = []
tweet_no = 0
tweets_lang = dict()
pos_tweet_cnt, neg_tweet_cnt, neu_tweet_cnt = 0, 0, 0

consumer_key = "yYpenGW8K835LBzmv6yrwdZ2z" 								#"thO5D3znaNrUvPNUzhQVnipPB"
consumer_secret = "KduEOuMuKXkL8qgDR3d00xJKk7SJrziQias6pOi48joZTfJCbg" 	#"0OEBfqgSVd6urMNkTH52fD92OUSzz2JASKQQOzbC3ZxQvNdnO6"

access_token = "226849265-P8X9zlTdx5WkzKsuCBiTWlOqibb0gLwiuDAkvgIK" 	#"226849265-PWLIIF7Ycnx1xIVQBjAKx7nElJmwRoYyAwhv6rl3"
access_token_secret = "K7AClLUTVzTD44IMW8oW6s5YDUZs1QTlys6CeUnCfdYwO" 	#"fs2rl2jxTUy9TtgzZk3VVhk9OhjKGBb91OdMMSYzQoU1V"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

read_tweets = api.user_timeline(screen_name = twtr_handle, count = 200)

tweets_collection.extend(read_tweets)

oldest_tweet_id = tweets_collection[-1].id

while len(read_tweets) != 0:

	read_tweets = api.user_timeline(screen_name = twtr_handle, count = 200, max_id = oldest_tweet_id-1)
	tweets_collection.extend(read_tweets)
	oldest_tweet_id = tweets_collection[-1].id

""" To anlayse the tweets in various languages and depicting the data in a pie chart """

# for tweet in tweets_collection:
# 	tweet_no += 1
# 	print("Tweet {}: {}".format(tweet_no, tweet.text))
# 	tweets_lang[tweet.lang] = tweets_lang.get(tweet.lang, 1) + 1

# en_tweets = tweets_lang["en"]
# ta_tweets = tweets_lang["ta"]

# print("Total tweets in Ta: {}".format(tweets_lang["ta"]))
# print("Total tweets in En: {}".format(tweets_lang["en"]))

# labels = "English", "Tamil"
# sizes = [en_tweets, ta_tweets]

# plt.pie(sizes, labels = labels, shadow = True, startangle = 90)
# plt.title("Language of tweets")
# plt.show()

""" To analyse the sentiment of the tweets and depict them in a pie chart """

for tweet in tweets_collection:
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
plt.title("Popular sentiments of {}'s latest tweets".format(twtr_handle))
plt.show()


