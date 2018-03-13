from __future__ import absolute_import, print_function
import tweepy
import json
import os
import time
import logging

from tweepy import OAuthHandler


def get_tweet(user_name,file_name,dir_name):
    
    c=0
    f=open(dir_name + "/" + file_name,'w')

    f.write("{\"tweet_array\":{")

    try:
        for tweet in tweepy.Cursor(api.user_timeline,id = user_name).items():
            
            json_s = json.dumps(tweet._json)
            if(c!=0):
                f.write(",")
            f.write("\"tweet" + str(c) + "\":" + json_s)
            c+=1
            print("tweet" + str(c))
    except tweepy.TweepError:
        print("No tweet")

    f.write("}}")
    
    f.close()

consumer_key="wBU0SNxW1FCNw91IXR4hH0pPV"
consumer_secret="TwDINvcvSrd5eGuDIVDpbg2N8HhFwftkZ9zQDeRyQqQRXPFuBu"
access_token="847012783816290304-SPzns2FILICjnGqOm2UG2E8UCoxXaZW"
access_secret="izd418m0ONf9Pw7mpJ1Wt4MuDD4PCNrcTaCcMlELTYgpv"

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)



dir_name = "User_information"

if not os.path.exists(dir_name):
    os.makedirs(dir_name)

logging.basicConfig()

X=0

f=open("id_list.txt",'r')

for line in f:

    try:
        person=api.get_user(line)
        print(person.name + " " + str(X))
        get_tweet(person.screen_name,"follower" + str(X) + ".json",dir_name)
        X+=1

 
    except tweepy.TweepError:
        print("wait")
        time.sleep(60*15)
        continue












