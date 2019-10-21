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


headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
'Referer':'https://trains.ctrip.com/TrainBooking/Search.aspx?from=beijing&to=nanjing&day=2019-09-25&number=&fromCn=%25E5%258C%2597%25E4%25BA%25AC&toCn=%25E5%258D%2597%25E4%25BA%25AC',
'Connection':'keep-alive'}

cookie={'cookie':'searchlist=searchlisttop=0; _abtest_userid=f5c43660-0115-402e-a723-67b6427aa11e; _RF1=60.191.34.166; _RSG=cVa1PnVuZd1gHJTiaYPNq8; _RDG=2876a35429adc32dc31d6b869e3592fa4d; _RGUID=19e3e1fc-5906-47e6-8d17-66292c75346a; _ga=GA1.2.643683381.1568272459; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _gid=GA1.2.2011220804.1569244069; ASP.NET_SessionSvc=MTAuMTUuMTI4LjIzfDkwOTB8b3V5YW5nfGRlZmF1bHR8MTU2Njg3MjAxNzI2Nw; gad_city=78a2062d1790b42fa1a75f591a7869b2; GUID=09031123111132037702; Union=OUID=index&AllianceID=4897&SID=155952&SourceID=&Expires=1569848917052; _jzqco=%7C%7C%7C%7C%7C1.2116179523.1568272693814.1569244069014.1569244117067.1569244069014.1569244117067.0.0.0.3.3; _gat=1; appFloatCnt=8; MKT_Pagesource=H5; _bfi=p1%3D108003%26p2%3D108002%26v1%3D157%26v2%3D154; __zpspc=9.4.1569244117.1569244154.5%232%7Csp0.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _bfa=1.1568272453274.3fkkr2.1.1568272453274.1569244148773.6.158.600003395; _bfs=1.10'}
url='https://webresource.ctrip.com/ResTrainOnline/R3/TrainBooking/JS/stationbus_gb2312.js?2019_9_23_17_16_35'

r=requests.get(url=url,headers=headers,cookies=cookie,timeout=10)

print(r.text)
#city_name=re.findall("贵(.*?)北",r.text)
#print(city_name)

a=r.text.split('|')

city_names=[]

for city_name in a:
    if '{' in city_name:
        pass
    else:
        city_names.append(city_name)


re=pd.DataFrame(city_names)
re.to_excel('name2.xlsx')
