""" This app gets the most retweeted tweet of a twitter user """

from twitter import *

token = "226849265-P8X9zlTdx5WkzKsuCBiTWlOqibb0gLwiuDAkvgIK"          	#token key
token_key = "K7AClLUTVzTD44IMW8oW6s5YDUZs1QTlys6CeUnCfdYwO"				#token_secret
con_secret = "yYpenGW8K835LBzmv6yrwdZ2z"								#consumer_key
con_secret_key = "KduEOuMuKXkL8qgDR3d00xJKk7SJrziQias6pOi48joZTfJCbg"	#consumer_secret

twtr_handle = input("Enter the twitter handle: ")
total_tweets = []

""" Creating an instance of the class Twitter and connecting to Twitter API """

t = Twitter(auth = OAuth(token, token_key, con_secret, con_secret_key))

""" Getting status of the given user """

read_data = t.statuses.user_timeline(screen_name = twtr_handle, count = 200)

total_tweets.extend(read_data)

oldest_tweet_id = total_tweets[-1]["id"]

while len(read_data) != 0:

	read_data = t.statuses.user_timeline(screen_name = twtr_handle, count = 200, max_id = oldest_tweet_id-1)
	total_tweets.extend(read_data)
	oldest_tweet_id = total_tweets[-1]["id"]

""" Printing the details """

print("Total tweets: " + str(len(total_tweets)))
 
max_rt = 0

for tweet in total_tweets:
	if tweet["retweet_count"] > max_rt and tweet["text"][0:2] != "RT":
		max_rt = tweet["retweet_count"]
		tweet_text = tweet["text"]

print("The most RTed tweet is: {}".format(tweet_text))
print("No of RTs : {}".format(max_rt))

# """ To send a DM to a twitter user """
# t.direct_messages.new(
# user=twtr_handle,
# text="Hi dude!")

