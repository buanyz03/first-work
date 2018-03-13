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

for g in range(191,192,1):
    
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
            temp=data['context_array'][y]['context'].encode('utf-8')
            temp = re.sub("[A-Za-z0-9\.\/\:]", "",temp)

            mecab_result = tagger.parseToNode(temp)
            mecab_result=mecab_result.next

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


    if(file_crash):
        print("file_crash")
        continue

    dir_name = "word"
    if not os.path.exists(dir_name):    #先確認資料夾是否存在
        os.makedirs(dir_name)

    f = open(dir_name +"/Out" + str(g) + ".csv","w")
    w = csv.writer(f)

    for y in range(len(all_D)):
        
        Posid=all_D.keys()[y]
        print(type(Posid))
        sortde_value=sorted(all_D[Posid].items(), key=lambda d:d[1])
        for x in range(len(sortde_value)):
            Context=sortde_value[x][0]
            lst=[]
            lst.append(str(Posid))
            lst.append(Context)
            lst.append(str(sortde_value[x][1]))
            w.writerow(lst)
    f.close()

