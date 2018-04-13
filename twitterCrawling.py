import tweepy
import csv

consumer_key = '<Consumer_Key>'
consumer_secret = '<Consumer_Secret>'
access_token = '<Access_Token>'
access_secret = '<Access_Secret>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

# Open/Create a file to append data
csvFile = open('crawling_data.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q="<Query>", since="2018-01-01", until="2018-03-15").items():
	try:
		print (tweet.created_at, tweet.text, tweet.user.location, tweet.coordinates, tweet.user.screen_name, tweet.user.followers_count)
		csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.location.encode('utf-8'), tweet.coordinates, tweet.user.screen_name, tweet.user.followers_count])
		filter(locations=[-6.109040, 106.686998, -6.370889, 106.940597])
	except:
		pass
