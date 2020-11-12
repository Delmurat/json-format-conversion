#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import csv
import json
import pandas as pd

filename = "C:\Users\Mikko\Desktop\101.json"
with open(filename,'r') as f:
  trump_list=json.load(f)
frame=pd.DataFrame(trump_list)
print(frame)
frame.to_csv("C:\Users\Mikko\Desktop\meet.csv")

