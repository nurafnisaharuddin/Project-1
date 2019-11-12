
import tweepy
from config import create_api 
import time 
import pandas 
from tweepy import OAuthHandler, Stream, StreamListener
import csv

hashtag=str(input("masukkan Hashtag(mis #cendol) = "))

consumer_key="X2VfS0ODunWQ5IdmwJcQvrxdS"
consumer_secret="XTI3GGAU4r7xr6gELJaUfSKVQLuwRwI0PLRefIFRdINlE6rRI9"
access_token="2297856090-IRjQiWflrYPxkfHaR7Js1m8SBQOdL5cNUaA2Twm"
access_token_secret="Y3KtjH5BEraAbOCeDh51Lh68NOESbGTDaa0qp3OU4vtfP"
auth=OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

#csvFile = open('nama.csv', 'a')
#csvWriter = csv.writer(csvFile)

list=[]
for tweet in tweepy.Cursor(api.search,q=hashtag,count=100,lang="id",tweet_mode='exntended').items():
    list.append(tweet._json)
    

data=pandas.DataFrame(list)
data1=data[['text','user','created_at']].head()
export_csv = data1.to_csv (r'F:\dokumen\FGA BD\export_dataframe4.csv', header=True)
print("")
print("EXPORT TO CSV SUCCESS!!!")
print(data1)