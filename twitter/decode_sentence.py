#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf8
import re
import json
import MeCab
import os
from collections import defaultdict
import csv


def is_Japan(uchar):
    number = ord(uchar)
    '''
    if ((number>=12352 and number<=12447 ) or (number>=12448 and number<=12543) or (number>=19968 and number<=40895)):
    '''
    if((number>=12352 and number<=12447 ) or (number>=12448 and number<=12543)):
        return True
    else:
        return False


def check_J(ustring):
    for uchar in ustring:
        if(is_Japan(uchar)):
            return True
    return False


def pure_sentence(Context):

    Context = re.sub(' ',"",Context)
    Context = re.sub('　',"",Context)

    check_type=["@[A-Za-z0-9_]+(.+)","(.+)http.+","(.+)@.+"]

    for str in check_type:

        M = re.match(str,Context)

        while M:
            Context=M.group(1)
            M = re.match(str,Context)

    return Context

f_dir_name="User_information"

fileList = os.listdir(f_dir_name)

follower_num=len(fileList)

gap=60000
for g in range(0,60000,gap):

    all_D = defaultdict(dict)

    for k in range(gap):
        
        f_name=f_dir_name + "/follower" + str(g+k)  + ".json"
        print("follower " + str(g+k))
        try:
            with open(f_name, 'r') as F:
                data = json.load(F)

            for y in range(len(data['tweet_array'])):
                
                text=data['tweet_array']['tweet' + str(y)]['text']
                sentence=re.split(',|！|、| |　|？|。|\n|;|!|#',text)
                
                for z in range(len(sentence)):
                    
                    Context=sentence[z]
                    if(not check_J(Context)):
                        continue
                    
                    M = re.match('.?RT(.+)', Context)
                    if M:
                        break

                    Context=pure_sentence(Context)
                    
                    if(not check_J(text)):
                        continue
                    if(len(Context)<6 or len(Context)>15):
                        continue

                    if(all_D.has_key(Context)):
                        all_D[Context]+=1
                    else:
                        all_D[Context]=1

        except:
            print("wrong json type")
            continue

    f = open("sentence.csv","w")
    w = csv.writer(f)

    sorted_value=sorted(all_D.items(), key=lambda d:d[1],reverse=True)
    for y in range(len(sorted_value)):
    
        sentence=sorted_value[y][0].encode('utf-8')
        if(sentence=="" or sorted_value[y][1]<15):
            continue

        lst=[]
        lst.append(sentence)
        lst.append(str(sorted_value[y][1]))
        w.writerow(lst)
            
    f.close()







