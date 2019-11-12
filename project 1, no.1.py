# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:52:19 2019

@author: asus
"""

# credentials from https://apps.twitter.com/
import pandas
import tweepy
from tweepy import OAuthHandler, Stream, StreamListener
import datetime

tgl=int(input("tanggal mulai = "))
tgl1=int(input("tanggal brakhir = "))
akun=str(input("nama akun = "))
startDate = datetime.datetime(2019, 10, tgl, 0, 0, 0)
endDate =   datetime.datetime(2019, 10, tgl1, 0, 0, 0)

consumer_key="X2VfS0ODunWQ5IdmwJcQvrxdS"
consumer_secret="XTI3GGAU4r7xr6gELJaUfSKVQLuwRwI0PLRefIFRdINlE6rRI9"
access_token="2297856090-IRjQiWflrYPxkfHaR7Js1m8SBQOdL5cNUaA2Twm"
access_token_secret="Y3KtjH5BEraAbOCeDh51Lh68NOESbGTDaa0qp3OU4vtfP"
auth=OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

user_tweets=api.user_timeline(screen_name=akun, count=200,tweet_mode='exntended')
for tweet in user_tweets:
    print(tweet._json)

the_list=[]
tweet_user=api.user_timeline(screen_name=akun, count=200,tweet_mode='exntended')
for tweet in user_tweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        the_list.append(tweet._json)

data=pandas.DataFrame(the_list)
data1=data[['text','created_at']].head()
export_csv = data1.to_csv (r'F:\dokumen\FGA BD\export_dataframe2.csv', header=True)
print("")
print("EXPORT TO CSV SUCCESS!!!")
print(data1)

