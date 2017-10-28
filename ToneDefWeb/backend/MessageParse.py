__author__ = 'Andrew'

import random
import urllib
import json
import watson_developer_cloud
from watson_developer_cloud import ToneAnalyzerV3
from os.path import join, dirname

tonedef = watson_developer_cloud.ToneAnalyzerV3(
    '2017-10-27',
    username= "f0d16349-4f18-4669-9fff-a53ad63fa956",
    password='UvaNFrrMqnlH')

messages = open('Lucas', 'r+')
convo = ""

switch = 0;
for line in messages:
    if(switch == 0):
        switch = 1
        ind = line.index(':')
        person = line[:ind]
        mess = line[ind+2:]
        mess = mess[:-1]
        convo = convo + mess
        print(person)
        print(mess)
    else:
        switch = 0
        ind = line.index(':')
        hour = line[ind-1:ind]
        minute = line[ind+1:ind+3]
        print(hour + ':' + minute)
print convo

print("\ntone_chat() example 1:\n")
utterances = [{'text': 'I am very happy.', 'user': 'glenn'},
              {'text': 'It is a good day.', 'user': 'glenn'}]
print(json.dumps(tonedef.tone_chat(utterances), indent=2))


with open(join(dirname(__file__), 'tone.json')) as tone_json:
  tone = tonedef.tone(json.load(tone_json)[convo], tones='emotion',
    content_type='text/plain')

print(json.dumps(tone, indent=2))
