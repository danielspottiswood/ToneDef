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

switch = 0;
for line in messages:
    if(switch == 0):
        switch = 1
        ind = line.index(':')
        person = line[:ind]
        mess = line[ind+2:]
        mess = mess[:-1]
        #convo.append({'text': mess, 'user':person})
        convo.append({'text': mess})
        print(person)
        print(mess)
    else:
        switch = 0
        ind = line.index(':')
        hour = line[ind-1:ind]
        minute = line[ind+1:ind+3]
        print(hour + ':' + minute)
print convo

print(json.dumps(tonedef.tone_chat(convo), indent=2))

data = tonedef.tone_chat(convo)
pprint(data)
print(tonedef.tone_chat(convo))
data2 = json.load(tonedef.tone_chat(convo))
pprint(data)
