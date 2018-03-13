#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf8
import re
import json
import MeCab
import os
from collections import defaultdict
import csv


f_dir_name="User_information"

fileList = os.listdir(f_dir_name)

follower_num=len(fileList)

for g in range(0,follower_num-2,10000):
    
    all_D = defaultdict(dict)
    gap=10000
    for k in range(gap):

        f_name=f_dir_name + "/follower" + str(g+k)  + ".json"

        try:
            with open(f_name, 'r') as F:
                data = json.load(F)
        except:
            print("wrong json type")
            continue

        print("follower " + str(g+k))

        tagger = MeCab.Tagger ("mecabrc")

        for y in range(len(data['tweet_array'])):

            text=data['tweet_array']['tweet' + str(y)]['text'].encode('utf-8')
            m = re.search('(.*)http.*',text)

            if(m!=None):
                text=m.group(1)

            sentence=text.split('\n')
            for z in range(len(sentence)):

                mecab_result = tagger.parseToNode(sentence[z])
                mecab_result = mecab_result.next
                    
                while mecab_result.next:

                    Posid=mecab_result.posid
                    Context=mecab_result.surface + "," + mecab_result.feature
                    if(all_D.has_key(Posid)):
                        if(all_D[Posid].has_key(Context)):
                            all_D[Posid][Context]+=1
                        else:
                            all_D[Posid][Context]=1
                    else:
                        all_D[Posid][Context]=1
                        
                    mecab_result=mecab_result.next

    dir_name = "words"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    f = open(dir_name +"/part" + str(g/10000) + ".csv","w")
    w = csv.writer(f)
    
    for y in range(len(all_D)):
        
        Posid=all_D.keys()[y]
        
        sortde_value=sorted(all_D[Posid].items(), key=lambda d:d[1])
        for x in range(len(sortde_value)):
            Context=sortde_value[x][0]
            lst=[]
            lst.append(str(Posid))
            lst.append(Context)
            lst.append(str(sortde_value[x][1]))
            w.writerow(lst)
    f.close()


