from __future__ import absolute_import, print_function
import tweepy
import json
import os
import time
import logging

from tweepy import OAuthHandler


consumer_key="wBU0SNxW1FCNw91IXR4hH0pPV"
consumer_secret="TwDINvcvSrd5eGuDIVDpbg2N8HhFwftkZ9zQDeRyQqQRXPFuBu"
access_token="847012783816290304-SPzns2FILICjnGqOm2UG2E8UCoxXaZW"
access_secret="izd418m0ONf9Pw7mpJ1Wt4MuDD4PCNrcTaCcMlELTYgpv"

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)




logging.basicConfig()

f=open("id_list.txt",'a')

f.write('ariyoshihiroiki' + '\n')


pages = tweepy.Cursor(api.followers_ids, id = 'ariyoshihiroiki').pages()


X=0


while True:
    try:
        page=next(pages)
    except tweepy.TweepError:
        print("page wait")
        time.sleep(60*15)
        continue
    except StopIteration:
        break
    for user in page:
        try:
            f.write(str(user) + "\n")
            print("follower" + str(X) )
            X+=1
        except tweepy.TweepError:
            print("person not find")
f.close()












