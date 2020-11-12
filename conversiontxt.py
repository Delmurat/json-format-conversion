#!/usr/bin/python3 
# -*- coding:utf-8 -*-
import os
import jsonlines
import pandas as pd

filename="chat.json"
with open(filename,'r',encoding='utf-8') as f:
	for item in jsonlines.Reader(f):
		
		if 'text' in item.keys():
			chat = open('chat.txt',mode = 'a',encoding='utf-8')
			print(item['text'],file=chat)
