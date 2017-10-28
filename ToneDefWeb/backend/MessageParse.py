__author__ = 'Andrew'

import random
import urllib

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
        convo.append(mess)
        print(person)
        print(mess)
    else:
        switch = 0
        ind = line.index(':')
        hour = line[ind-1:ind]
        minute = line[ind+1:ind+3]
        print(hour + ':' + minute)
        print

print convo






