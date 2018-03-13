#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf8
import re
import json
import MeCab
import os
from collections import defaultdict
import csv


f_dir_name="home/billy"

fileList = os.listdir(f_dir_name)

title_num=len(fileList)

for g in range(42,43,1):
    
    all_D = defaultdict(dict)
    tagger = MeCab.Tagger ("mecabrc")
    count=0
    
    fileList = os.listdir(f_dir_name + "/source" + str(g))
    
    file_crash=0
    for k in range(0,len(fileList),1):
        
        print("source" + str(g) + " output " + str(k))
        f_name=f_dir_name + "/source" + str(g)  + "/output" + str(k) + ".json"
        with open(f_name, 'r') as F:
            try:
                data = json.load(F)
            except:
                print("file" + str(g) + "error")
                file_crash=1
                break
    
        for y in range(len(data['context_array'])):
            context= data['context_array'][y]['context'].encode('utf-8')
            context= re.sub("[A-Za-z0-9\.\/\:]", "",context)
  
            S=re.split(',|！|、|　| |？|。|：',context)
            for x in range(len(S)):
                temp=S[x]
                temp= re.sub("　", "",temp)
                temp= re.sub(" ", "",temp)
                if(all_D.has_key(temp)):
                    all_D[temp]+=1
                else:
                    all_D[temp]=1

    if(file_crash):
        print("file_crash")
        continue

    dir_name = "sta"
    if not os.path.exists(dir_name):    #先確認資料夾是否存在
        os.makedirs(dir_name)

    f = open(dir_name +"/Out" + str(g)  + ".csv","w")
    w = csv.writer(f)

    sentence=""
    abc=sorted(all_D.items(), key=lambda d:d[1],reverse=True)
    for y in range(len(abc)):
        
        sentence=abc[y][0]
        if(sentence==""):
            continue
        lst=[]
        lst.append(sentence)
        lst.append(abc[y][1])
        w.writerow(lst)
    f.close()

