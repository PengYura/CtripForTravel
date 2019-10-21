#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:30:56 2019

@author: yura
"""

import requests
import json
import re
import pandas as pd
import time
import random
import sys

#筛选函数
def get_routes_info(budget,train_type,seat_type):  
#选出符合条件的车次
    select_data=data[(data.票价<=int(budget))&(data.座位类型==train_type+seat_type)]
    
    if len(select_data):
        #按票价从低到高排序
        select_data_sort=select_data.sort_values(by = '票价',ascending=True)
        #去重（同目的地、同火车类型、同位置类型，不同价格保留最低价）
        select_data_sort_dup=select_data_sort.drop_duplicates(subset=['到达城市','火车类型','座位类型'], keep='first')
        #删除索引
        select_data_sort_dup=select_data_sort_dup.reset_index(drop=True)
        print('\n\n*************************************')
        print('\n你可以到达的地方有{}个👇：\n'.format(len(select_data_sort_dup)))
        
        print(select_data_sort_dup)
        print('\n祝旅途愉快：）')
        
    else:
        print('没找到符合条件的车次，先好好赚钱去吧～')

 
    
    
data=pd.read_excel('携程（杭州出发）.xlsx')

budget = input("STEP 1 请输入你的预算（纯数字）：")

try:
    budget=int(budget)
except:
    print('\n❌审题不仔细，输入非数字！服务到此为止，拜拜～')  
    sys.exit(0)
    

train_type=input('STEP 2 请输入你想坐的火车类型（高铁/动车/火车）:')


select_seat_types=[]
#seat_type=''
if train_type=='高铁':
    select_seat_types=['一等座','二等座','商务座']
elif train_type=='动车':
    select_seat_types=['一等座','二等座','商务座','动卧','高级动卧','一等卧','二等卧']
elif train_type=='火车':
    select_seat_types=['硬座','硬卧','软卧','高级软卧']
else:
    print('\n❌审题不仔细，输入错误！服务到此为止，拜拜～')
#    exit()  
    sys.exit(0)
    

print('\nSTEP 3 {}有{}座位类型：'.format(train_type,len(select_seat_types)),end='')
for seat in select_seat_types:
    print(seat,end=" ")
#print(select_seat_types)
seat_type=input("       请输入你想坐的座位类型(单选):")



if seat_type not in select_seat_types:
    print("\n❌好好审题！你选择的火车没有这种位置。服务到此为止，拜拜～")
    sys.exit(0)
else:
    get_routes_info(budget,train_type,seat_type)







