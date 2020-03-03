# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:10:25 2020

@author: 00124175
"""
import json

f = open('./data/train-v2.0.json','r') 
all_data = json.load(f)
data = all_data['data']
paragraph = data[1]
qas = paragraph['paragraphs']
qas2 = qas[0]
qas3 = qas2['qas']
qas4 = qas3[0]

f.close()

