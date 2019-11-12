# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:48:40 2019

@author: asus
"""

from __future__ import absolute_import, print_function
import tweepy
from tweepy import OAuthHandler, Stream, StreamListener

n=int(input("masukkan jumlah topik = "))
topik=[]
for i in range (n):
    temp=str(input("masukkan topik ke-{} = ".format(i+1)))
    topik.append(temp)
consumer_key="X2VfS0ODunWQ5IdmwJcQvrxdS"
consumer_secret="XTI3GGAU4r7xr6gELJaUfSKVQLuwRwI0PLRefIFRdINlE6rRI9"
access_token="2297856090-IRjQiWflrYPxkfHaR7Js1m8SBQOdL5cNUaA2Twm"
access_token_secret="Y3KtjH5BEraAbOCeDh51Lh68NOESbGTDaa0qp3OU4vtfP"
auth=OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_status(self, status):
        print(status.text,'\n')
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)    
    stream.filter(track=topik)