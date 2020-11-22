from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

ACCESS_TOKEN = "1322898321070006275-RQbh90aPyTeCvUKegJwBqhHi5ZcOc7"
TOKEN_SECRET = "sBQEFlhQ85eabPYVrmmKbaAY2WL1h7Vfsl8rlEqrCw0q6"
CONSUMER_KEY = "jEOfQkyNXNSuQpsFU99O7lleM"
CONSUMER_SECRET = "IeLd9urPuIROUpnmKyUZwJPQflSwk8uz2T1ylOXmexYr46OI7h"
TOPIC = "colab_tweets"

class StdOutListener(StreamListener):
	def on_data(self, data):
		producer.send_messages(TOPIC, data.encode("UTF-8"))
		print ("Tweet Sent")
		return True
	def on_error(self, status):
		print (status)

kafka = KafkaClient("localhost:9099")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)
stream = Stream(auth, l)
stream.filter(track="whatever")

