__author__ = 'Andrew'

import random
import urllib
import json
import watson_developer_cloud
from watson_developer_cloud import ToneAnalyzerV3
from os.path import join, dirname
from pprint import pprint

tonedef = watson_developer_cloud.ToneAnalyzerV3(
    '2017-10-27',
    username= "f0d16349-4f18-4669-9fff-a53ad63fa956",
    password='UvaNFrrMqnlH')

messages = open('Lucas', 'r+')
convo = []
data = []
switch = 0;
for line in messages:
    if line !=  "":
        if(switch == 0):
            switch = 1
            ind = line.index(':')
            person = line[:ind]
            mess = line[ind+2:]
            mess = mess[:-1]
            #convo.append({'text': mess, 'user':person})
            convo.append({'text': mess})
            convo2 = [{'text': mess}]
            print(person)
            print(mess)
        else:
            switch = 0
            a = line.index('/')
            line = line[a+1:]
            a = line.index('/')
            day = line[:a]
            ind = line.index(':')
            hour = line[ind-1:ind]
            minute = line[ind+1:ind+3]
            print(hour + ':' + minute)
            data2 = tonedef.tone_chat(convo2)
            toneName = ""
            score = 0
            print(data2)
            pprint(data2)
            for key in data2:
                output = data2.get(key)
                for dictionary in output:
                    for key2 in dictionary:
                        if key2 == "tones":
                            List = dictionary.get(key2)
                            if List:
                                dict5 = List[0]
                                for key5 in dict5:
                                    print("This is the key: " + key5)
                                toneName = (dict5.get("tone_name"))
                                score = (dict5.get("score"))
                                print("This is the score: ")
                                print score
            data.append([mess, hour,day, toneName, score])
print convo
print data
'''
print(json.dumps(tonedef.tone_chat(convo), indent=2))
i = 0
data2 = tonedef.tone_chat(convo)
for key in data2:
    output = data2.get(key)
    for dictionary in output:
        for key2 in dictionary:
            if key2 == "tones":
                print("This is the tones dict")
                List = dictionary.get(key2)
                if List:
                    dict5 = List[0]
                    for key5 in dict5:
                        print("This is the key: " + key5)
                    toneName = (dict5.get("tone_name"))
                    score = (dict5.get("score"))
                    print("This is the score: ")
                    print score
                    data[i].append(toneName)
                    data[i].append(score)
        i = i +1

pprint(data)


#pprint(output)
#print(tonedef.tone_chat(convo))
#data2 = json.load(tonedef.tone_chat(convo))
#pprint(data)
'''
