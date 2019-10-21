#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:15:22 2019

@author: yura
"""

import requests
import json
import re
import pandas as pd
import time
import random


data=pd.read_excel('城市信息.xlsx')
city_names=data['name']


dep_city_name = input("请输入出发地的拼音：");

#补充ua和cookie信息
headers = {
'User-Agent':'',
'Referer':'https://trains.ctrip.com/TrainBooking/HubSingleTrip.aspx?from=haerbin&to=fuzhou&day=1&number=&fromCn=%B9%FE%B6%FB%B1%F5&toCn=%B8%A3%D6%DD&jumpflag=1',
'Connection':'keep-alive'}
cookie={'cookie':''}


url='https://trains.ctrip.com/TrainBooking/Ajax/SearchListHandler.ashx?Action=getSearchList'

arrive_city=[]
take_time=[]
train_type=[]
price=[]
seat_type=[]
error_city=[]

def get_basic_info(train_route):
#        print(seats['SeatName'])
    arrive_city.append(train_route['EndStationName'])
    take_time.append(train_route['TakeTime'])
    train_type.append(train_route['TrainType'])
    

for arrive_city_name in city_names:
        
    #data={'value':'{"IsBus":false,"Filter":"0","Catalog":"","IsGaoTie":false,"IsDongChe":false,"CatalogName":"","DepartureCity":"fuzhou","ArrivalCity":"haerbin","HubCity":"", "DepartureDate":"2019-09-25","DepartureDateReturn":"2019-09-27","ArrivalDate":"","TrainNumber":""}'}
    data={'value': '{"DepartureCity":'+dep_city_name+',"ArrivalCity":'+arrive_city_name+',"HubCity":"","DepartureDate":"2019-11-11"}'}
  
    print('能到达{}吗？'.format(arrive_city_name))

    
    time.sleep(random.random()*3)
    r=requests.post(url,data,headers=headers,cookies=cookie,timeout=10)
    
    #print(r)
#    print(r.text)
    
    try:
        content=json.loads(r.text,encoding='gbk')   
    except:
        print('该城市出错！')
        error_city.append(arrive_city_name)
        continue
    
    if content['TrainItemsList']: #判断是否有直达信息        
        for train_route in content['TrainItemsList']:
        #    print(train_route['TrainType'])
            for seats in  train_route['SeatBookingItem']:
                
                #动车一等座
                if train_route['TrainType']=='D' and seats['SeatName']=='一等座':
                    get_basic_info(train_route)
                    seat_type.append('动车一等座')
                    price.append(seats['Price'])
        
                #动车二等座
                elif train_route['TrainType']=='D' and seats['SeatName']=='二等座':
                    get_basic_info(train_route)
                    seat_type.append('动车二等座')
                    price.append(seats['Price'])            
                #动车商务座
                elif train_route['TrainType']=='D' and seats['SeatName']=='商务座':
                    get_basic_info(train_route)
                    seat_type.append('动车商务座')
                    price.append(seats['Price']) 
                #动车动卧
                elif train_route['TrainType']=='D' and seats['SeatName']=='动　卧':
                    get_basic_info(train_route)
                    seat_type.append('动车动卧')
                    price.append(seats['Price']) 
                
                #动车高级动卧
                elif train_route['TrainType']=='D' and seats['SeatName']=='高级动卧':
                    get_basic_info(train_route)
                    seat_type.append('动车高级动卧')
                    price.append(seats['Price'])  
                
                elif train_route['TrainType']=='D' and seats['SeatName']=='二等卧':
                    get_basic_info(train_route)
                    seat_type.append('动车二等卧')
                    price.append(seats['Price'])  
                    
                elif train_route['TrainType']=='D' and seats['SeatName']=='一等卧':
                    get_basic_info(train_route)
                    seat_type.append('动车一等卧')
                    price.append(seats['Price'])  
                    
                    
                    
                #高铁一等座
                elif train_route['TrainType']=='G' and seats['SeatName']=='一等座':
                    get_basic_info(train_route)
                    seat_type.append('高铁一等座')
                    price.append(seats['Price'])             
                               
                #高铁二等座
                elif train_route['TrainType']=='G' and seats['SeatName']=='二等座':
                    get_basic_info(train_route)
                    seat_type.append('高铁二等座')
                    price.append(seats['Price'])             
                    
                #高铁商务座
                elif train_route['TrainType']=='G' and seats['SeatName']=='商务座':
                    get_basic_info(train_route)
                    seat_type.append('高铁商务座')
                    price.append(seats['Price'])             
                    
                #火车硬座
                elif train_route['TrainType']=='K' or train_route['TrainType']=='T' or train_route['TrainType']=='Z' and seats['SeatName']=='硬　座':
                    get_basic_info(train_route)
                    seat_type.append('火车硬座')
                    price.append(seats['Price'])             
                          
                #火车硬卧
                elif train_route['TrainType']=='K' or train_route['TrainType']=='T' or train_route['TrainType']=='Z' and seats['SeatName']=='硬　卧':
                    get_basic_info(train_route)
                    seat_type.append('火车硬卧')
                    price.append(seats['Price'])             
                            
                #火车软卧
                elif train_route['TrainType']=='K' or train_route['TrainType']=='T' or train_route['TrainType']=='Z' and seats['SeatName']=='软　卧':
                    get_basic_info(train_route)
                    seat_type.append('火车软卧')
                    price.append(seats['Price'])   
                
                elif train_route['TrainType']=='K' or train_route['TrainType']=='T' or train_route['TrainType']=='Z' and seats['SeatName']=='高级软卧':
                    get_basic_info(train_route)
                    seat_type.append('火车高级软卧')
                    price.append(seats['Price'])   
                   
    
    
info={'到达城市':arrive_city,
      '花费时间':take_time,
      '火车类型':train_type,
      '座位类型':seat_type,
      '票价':price    
      }

result=pd.DataFrame(info)
result_final= result.drop_duplicates(subset=['到达城市','火车类型','座位类型','票价'])
result_final=result
result_final.to_excel('携程票价({}出发).xlsx'.format(dep_city_name))
print('以下城市爬虫出现错误：\n')
print(error_city)
