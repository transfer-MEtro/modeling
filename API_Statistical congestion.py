#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('python -m pip install requests')


# In[91]:


import requests
import pandas as pd
import json


# In[6]:


subway=[{"subwayLine":"1호선","stationName":"소요산역","stationCode":"100"},{"subwayLine":"1호선","stationName":"동두천역","stationCode":"101"},{"subwayLine":"1호선","stationName":"보산역","stationCode":"102"},{"subwayLine":"1호선","stationName":"동두천중앙역","stationCode":"103"},{"subwayLine":"1호선","stationName":"지행역","stationCode":"104"},{"subwayLine":"1호선","stationName":"덕정역","stationCode":"105"},{"subwayLine":"1호선","stationName":"덕계역","stationCode":"106"},{"subwayLine":"1호선","stationName":"양주역","stationCode":"107"},{"subwayLine":"1호선","stationName":"녹양역","stationCode":"108"},{"subwayLine":"1호선","stationName":"가능역","stationCode":"109"},{"subwayLine":"1호선","stationName":"의정부역","stationCode":"110"},{"subwayLine":"1호선","stationName":"회룡역","stationCode":"111"},{"subwayLine":"1호선","stationName":"망월사역","stationCode":"112"},{"subwayLine":"1호선","stationName":"도봉산역","stationCode":"113"},{"subwayLine":"1호선","stationName":"도봉역","stationCode":"114"},{"subwayLine":"1호선","stationName":"방학역","stationCode":"115"},{"subwayLine":"1호선","stationName":"창동역","stationCode":"116"},{"subwayLine":"1호선","stationName":"녹천역","stationCode":"117"},{"subwayLine":"1호선","stationName":"월계역","stationCode":"118"},{"subwayLine":"1호선","stationName":"광운대역","stationCode":"119"},{"subwayLine":"1호선","stationName":"석계역","stationCode":"120"},{"subwayLine":"1호선","stationName":"신이문역","stationCode":"121"},{"subwayLine":"1호선","stationName":"외대앞역","stationCode":"122"},{"subwayLine":"1호선","stationName":"회기역","stationCode":"123"},{"subwayLine":"1호선","stationName":"청량리역","stationCode":"124"},{"subwayLine":"1호선","stationName":"제기동역","stationCode":"125"},{"subwayLine":"1호선","stationName":"신설동역","stationCode":"126"},{"subwayLine":"1호선","stationName":"동묘앞역","stationCode":"127"},{"subwayLine":"1호선","stationName":"동대문역","stationCode":"128"},{"subwayLine":"1호선","stationName":"종로5가역","stationCode":"129"},{"subwayLine":"1호선","stationName":"종로3가역","stationCode":"130"},{"subwayLine":"1호선","stationName":"종각역","stationCode":"131"},{"subwayLine":"1호선","stationName":"시청역","stationCode":"132"},{"subwayLine":"1호선","stationName":"서울역","stationCode":"133"},{"subwayLine":"1호선","stationName":"남영역","stationCode":"134"},{"subwayLine":"1호선","stationName":"용산역","stationCode":"135"},{"subwayLine":"1호선","stationName":"노량진역","stationCode":"136"},{"subwayLine":"1호선","stationName":"대방역","stationCode":"137"},{"subwayLine":"1호선","stationName":"신길역","stationCode":"138"},{"subwayLine":"1호선","stationName":"영등포역","stationCode":"139"},{"subwayLine":"1호선","stationName":"신도림역","stationCode":"140"},{"subwayLine":"1호선","stationName":"구로역","stationCode":"141"},{"subwayLine":"1호선","stationName":"구일역","stationCode":"142"},{"subwayLine":"1호선","stationName":"개봉역","stationCode":"143"},{"subwayLine":"1호선","stationName":"오류동역","stationCode":"144"},{"subwayLine":"1호선","stationName":"온수역","stationCode":"145"},{"subwayLine":"1호선","stationName":"역곡역","stationCode":"146"},{"subwayLine":"1호선","stationName":"소사역","stationCode":"147"},{"subwayLine":"1호선","stationName":"부천역","stationCode":"148"},{"subwayLine":"1호선","stationName":"중동역","stationCode":"149"},{"subwayLine":"1호선","stationName":"송내역","stationCode":"150"},{"subwayLine":"1호선","stationName":"부개역","stationCode":"151"},{"subwayLine":"1호선","stationName":"부평역","stationCode":"152"},{"subwayLine":"1호선","stationName":"백운역","stationCode":"153"},{"subwayLine":"1호선","stationName":"동암역","stationCode":"154"},{"subwayLine":"1호선","stationName":"간석역","stationCode":"155"},{"subwayLine":"1호선","stationName":"주안역","stationCode":"156"},{"subwayLine":"1호선","stationName":"도화역","stationCode":"157"},{"subwayLine":"1호선","stationName":"제물포역","stationCode":"158"},{"subwayLine":"1호선","stationName":"도원역","stationCode":"159"},{"subwayLine":"1호선","stationName":"동인천역","stationCode":"160"},{"subwayLine":"1호선","stationName":"인천역","stationCode":"161"},{"subwayLine":"4호선","stationName":"진접역","stationCode":"405"},{"subwayLine":"4호선","stationName":"오남역","stationCode":"406"},{"subwayLine":"4호선","stationName":"별내별가람역","stationCode":"408"},{"subwayLine":"4호선","stationName":"당고개역","stationCode":"409"},{"subwayLine":"4호선","stationName":"상계역","stationCode":"410"},{"subwayLine":"4호선","stationName":"노원역","stationCode":"411"},{"subwayLine":"4호선","stationName":"창동역","stationCode":"412"},{"subwayLine":"4호선","stationName":"쌍문역","stationCode":"413"},{"subwayLine":"4호선","stationName":"수유역","stationCode":"414"},{"subwayLine":"4호선","stationName":"미아역","stationCode":"415"},{"subwayLine":"4호선","stationName":"미아사거리역","stationCode":"416"},{"subwayLine":"4호선","stationName":"길음역","stationCode":"417"},{"subwayLine":"4호선","stationName":"성신여대입구역","stationCode":"418"},{"subwayLine":"4호선","stationName":"한성대입구역","stationCode":"419"},{"subwayLine":"4호선","stationName":"혜화역","stationCode":"420"},{"subwayLine":"4호선","stationName":"동대문역","stationCode":"421"},{"subwayLine":"4호선","stationName":"동대문역사문화공원역","stationCode":"422"},{"subwayLine":"4호선","stationName":"충무로역","stationCode":"423"},{"subwayLine":"4호선","stationName":"명동역","stationCode":"424"},{"subwayLine":"4호선","stationName":"회현역","stationCode":"425"},{"subwayLine":"4호선","stationName":"서울역","stationCode":"426"},{"subwayLine":"4호선","stationName":"숙대입구역","stationCode":"427"},{"subwayLine":"4호선","stationName":"삼각지역","stationCode":"428"},{"subwayLine":"4호선","stationName":"신용산역","stationCode":"429"},{"subwayLine":"4호선","stationName":"이촌역","stationCode":"430"},{"subwayLine":"4호선","stationName":"동작역","stationCode":"431"},{"subwayLine":"4호선","stationName":"이수역","stationCode":"432"},{"subwayLine":"4호선","stationName":"사당역","stationCode":"433"},{"subwayLine":"4호선","stationName":"남태령역","stationCode":"434"},{"subwayLine":"4호선","stationName":"선바위역","stationCode":"435"},{"subwayLine":"4호선","stationName":"경마공원역","stationCode":"436"},{"subwayLine":"4호선","stationName":"대공원역","stationCode":"437"},{"subwayLine":"4호선","stationName":"과천역","stationCode":"438"},{"subwayLine":"4호선","stationName":"정부과천청사역","stationCode":"439"},{"subwayLine":"4호선","stationName":"인덕원역","stationCode":"440"},{"subwayLine":"4호선","stationName":"평촌역","stationCode":"441"},{"subwayLine":"4호선","stationName":"범계역","stationCode":"442"},{"subwayLine":"4호선","stationName":"금정역","stationCode":"443"},{"subwayLine":"4호선","stationName":"산본역","stationCode":"444"},{"subwayLine":"4호선","stationName":"수리산역","stationCode":"445"},{"subwayLine":"4호선","stationName":"대야미역","stationCode":"446"},{"subwayLine":"4호선","stationName":"반월역","stationCode":"447"},{"subwayLine":"4호선","stationName":"상록수역","stationCode":"448"},{"subwayLine":"4호선","stationName":"한대앞역","stationCode":"449"},{"subwayLine":"4호선","stationName":"중앙역","stationCode":"450"},{"subwayLine":"4호선","stationName":"고잔역","stationCode":"451"},{"subwayLine":"4호선","stationName":"초지역","stationCode":"452"},{"subwayLine":"4호선","stationName":"안산역","stationCode":"453"},{"subwayLine":"4호선","stationName":"신길온천역","stationCode":"454"},{"subwayLine":"4호선","stationName":"정왕역","stationCode":"455"},{"subwayLine":"4호선","stationName":"오이도역","stationCode":"456"},{"subwayLine":"5호선","stationName":"방화역","stationCode":"510"},{"subwayLine":"5호선","stationName":"개화산역","stationCode":"511"},{"subwayLine":"5호선","stationName":"김포공항역","stationCode":"512"},{"subwayLine":"5호선","stationName":"송정역","stationCode":"513"},{"subwayLine":"5호선","stationName":"마곡역","stationCode":"514"},{"subwayLine":"5호선","stationName":"발산역","stationCode":"515"},{"subwayLine":"5호선","stationName":"우장산역","stationCode":"516"},{"subwayLine":"5호선","stationName":"화곡역","stationCode":"517"},{"subwayLine":"5호선","stationName":"까치산역","stationCode":"518"},{"subwayLine":"5호선","stationName":"신정역","stationCode":"519"},{"subwayLine":"5호선","stationName":"목동역","stationCode":"520"},{"subwayLine":"5호선","stationName":"오목교역","stationCode":"521"},{"subwayLine":"5호선","stationName":"양평역","stationCode":"522"},{"subwayLine":"5호선","stationName":"영등포구청역","stationCode":"523"},{"subwayLine":"5호선","stationName":"영등포시장역","stationCode":"524"},{"subwayLine":"5호선","stationName":"신길역","stationCode":"525"},{"subwayLine":"5호선","stationName":"여의도역","stationCode":"526"},{"subwayLine":"5호선","stationName":"여의나루역","stationCode":"527"},{"subwayLine":"5호선","stationName":"마포역","stationCode":"528"},{"subwayLine":"5호선","stationName":"공덕역","stationCode":"529"},{"subwayLine":"5호선","stationName":"애오개역","stationCode":"530"},{"subwayLine":"5호선","stationName":"충정로역","stationCode":"531"},{"subwayLine":"5호선","stationName":"서대문역","stationCode":"532"},{"subwayLine":"5호선","stationName":"광화문역","stationCode":"533"},{"subwayLine":"5호선","stationName":"종로3가역","stationCode":"534"},{"subwayLine":"5호선","stationName":"을지로4가역","stationCode":"535"},{"subwayLine":"5호선","stationName":"동대문역사문화공원역","stationCode":"536"},{"subwayLine":"5호선","stationName":"청구역","stationCode":"537"},{"subwayLine":"5호선","stationName":"신금호역","stationCode":"538"},{"subwayLine":"5호선","stationName":"행당역","stationCode":"539"},{"subwayLine":"5호선","stationName":"왕십리역","stationCode":"540"},{"subwayLine":"5호선","stationName":"마장역","stationCode":"541"},{"subwayLine":"5호선","stationName":"답십리역","stationCode":"542"},{"subwayLine":"5호선","stationName":"장한평역","stationCode":"543"},{"subwayLine":"5호선","stationName":"군자역","stationCode":"544"},{"subwayLine":"5호선","stationName":"아차산역","stationCode":"545"},{"subwayLine":"5호선","stationName":"광나루역","stationCode":"546"},{"subwayLine":"5호선","stationName":"천호역","stationCode":"547"},{"subwayLine":"5호선","stationName":"강동역","stationCode":"548"},{"subwayLine":"5호선","stationName":"길동역","stationCode":"549"},{"subwayLine":"5호선","stationName":"굽은다리역","stationCode":"550"},{"subwayLine":"5호선","stationName":"명일역","stationCode":"551"},{"subwayLine":"5호선","stationName":"고덕역","stationCode":"552"},{"subwayLine":"5호선","stationName":"상일동역","stationCode":"553"},{"subwayLine":"5호선","stationName":"강일역","stationCode":"555"},{"subwayLine":"6호선","stationName":"응암역","stationCode":"610"},{"subwayLine":"6호선","stationName":"역촌역","stationCode":"611"},{"subwayLine":"6호선","stationName":"불광역","stationCode":"612"},{"subwayLine":"6호선","stationName":"독바위역","stationCode":"613"},{"subwayLine":"6호선","stationName":"연신내역","stationCode":"614"},{"subwayLine":"6호선","stationName":"구산역","stationCode":"615"},{"subwayLine":"6호선","stationName":"새절역","stationCode":"616"},{"subwayLine":"6호선","stationName":"증산역","stationCode":"617"},{"subwayLine":"6호선","stationName":"디지털미디어시티역","stationCode":"618"},{"subwayLine":"6호선","stationName":"월드컵경기장역","stationCode":"619"},{"subwayLine":"6호선","stationName":"마포구청역","stationCode":"620"},{"subwayLine":"6호선","stationName":"망원역","stationCode":"621"},{"subwayLine":"6호선","stationName":"합정역","stationCode":"622"},{"subwayLine":"6호선","stationName":"상수역","stationCode":"623"},{"subwayLine":"6호선","stationName":"광흥창역","stationCode":"624"},{"subwayLine":"6호선","stationName":"대흥역","stationCode":"625"},{"subwayLine":"6호선","stationName":"공덕역","stationCode":"626"},{"subwayLine":"6호선","stationName":"효창공원앞역","stationCode":"627"},{"subwayLine":"6호선","stationName":"삼각지역","stationCode":"628"},{"subwayLine":"6호선","stationName":"녹사평역","stationCode":"629"},{"subwayLine":"6호선","stationName":"이태원역","stationCode":"630"},{"subwayLine":"6호선","stationName":"한강진역","stationCode":"631"},{"subwayLine":"6호선","stationName":"버티고개역","stationCode":"632"},{"subwayLine":"6호선","stationName":"약수역","stationCode":"633"},{"subwayLine":"6호선","stationName":"청구역","stationCode":"634"},{"subwayLine":"6호선","stationName":"신당역","stationCode":"635"},{"subwayLine":"6호선","stationName":"동묘앞역","stationCode":"636"},{"subwayLine":"6호선","stationName":"창신역","stationCode":"637"},{"subwayLine":"6호선","stationName":"보문역","stationCode":"638"},{"subwayLine":"6호선","stationName":"안암역","stationCode":"639"},{"subwayLine":"6호선","stationName":"고려대역","stationCode":"640"},{"subwayLine":"6호선","stationName":"월곡역","stationCode":"641"},{"subwayLine":"6호선","stationName":"상월곡역","stationCode":"642"},{"subwayLine":"6호선","stationName":"돌곶이역","stationCode":"643"},{"subwayLine":"6호선","stationName":"석계역","stationCode":"644"},{"subwayLine":"6호선","stationName":"태릉입구역","stationCode":"645"},{"subwayLine":"6호선","stationName":"화랑대역","stationCode":"646"},{"subwayLine":"6호선","stationName":"봉화산역","stationCode":"647"},{"subwayLine":"6호선","stationName":"신내역","stationCode":"648"},{"subwayLine":"7호선","stationName":"도봉산역","stationCode":"710"},{"subwayLine":"7호선","stationName":"수락산역","stationCode":"711"},{"subwayLine":"7호선","stationName":"마들역","stationCode":"712"},{"subwayLine":"7호선","stationName":"노원역","stationCode":"713"},{"subwayLine":"7호선","stationName":"중계역","stationCode":"714"},{"subwayLine":"7호선","stationName":"하계역","stationCode":"715"},{"subwayLine":"7호선","stationName":"공릉역","stationCode":"716"},{"subwayLine":"7호선","stationName":"태릉입구역","stationCode":"717"},{"subwayLine":"7호선","stationName":"먹골역","stationCode":"718"},{"subwayLine":"7호선","stationName":"중화역","stationCode":"719"},{"subwayLine":"7호선","stationName":"상봉역","stationCode":"720"},{"subwayLine":"7호선","stationName":"면목역","stationCode":"721"},{"subwayLine":"7호선","stationName":"사가정역","stationCode":"722"},{"subwayLine":"7호선","stationName":"용마산역","stationCode":"723"},{"subwayLine":"7호선","stationName":"중곡역","stationCode":"724"},{"subwayLine":"7호선","stationName":"군자역","stationCode":"725"},{"subwayLine":"7호선","stationName":"어린이대공원역","stationCode":"726"},{"subwayLine":"7호선","stationName":"건대입구역","stationCode":"727"},{"subwayLine":"7호선","stationName":"뚝섬유원지역","stationCode":"728"},{"subwayLine":"7호선","stationName":"청담역","stationCode":"729"},{"subwayLine":"7호선","stationName":"강남구청역","stationCode":"730"},{"subwayLine":"7호선","stationName":"학동역","stationCode":"731"},{"subwayLine":"7호선","stationName":"논현역","stationCode":"732"},{"subwayLine":"7호선","stationName":"반포역","stationCode":"733"},{"subwayLine":"7호선","stationName":"고속터미널역","stationCode":"734"},{"subwayLine":"7호선","stationName":"내방역","stationCode":"735"},{"subwayLine":"7호선","stationName":"이수역","stationCode":"736"},{"subwayLine":"7호선","stationName":"남성역","stationCode":"737"},{"subwayLine":"7호선","stationName":"숭실대입구역","stationCode":"738"},{"subwayLine":"7호선","stationName":"상도역","stationCode":"739"},{"subwayLine":"7호선","stationName":"장승배기역","stationCode":"740"},{"subwayLine":"7호선","stationName":"신대방삼거리역","stationCode":"741"},{"subwayLine":"7호선","stationName":"보라매역","stationCode":"742"},{"subwayLine":"7호선","stationName":"신풍역","stationCode":"743"},{"subwayLine":"7호선","stationName":"대림역","stationCode":"744"},{"subwayLine":"7호선","stationName":"남구로역","stationCode":"745"},{"subwayLine":"7호선","stationName":"가산디지털단지역","stationCode":"746"},{"subwayLine":"7호선","stationName":"천왕역","stationCode":"749"},{"subwayLine":"7호선","stationName":"온수역","stationCode":"750"},{"subwayLine":"7호선","stationName":"까치울역","stationCode":"751"},{"subwayLine":"7호선","stationName":"부천종합운동장역","stationCode":"752"},{"subwayLine":"7호선","stationName":"춘의역","stationCode":"753"},{"subwayLine":"7호선","stationName":"신중동역","stationCode":"754"},{"subwayLine":"7호선","stationName":"부천시청역","stationCode":"755"},{"subwayLine":"7호선","stationName":"상동역","stationCode":"756"},{"subwayLine":"7호선","stationName":"삼산체육관역","stationCode":"757"},{"subwayLine":"7호선","stationName":"굴포천역","stationCode":"758"},{"subwayLine":"7호선","stationName":"부평구청역","stationCode":"759"},{"subwayLine":"7호선","stationName":"산곡역","stationCode":"760"},{"subwayLine":"7호선","stationName":"석남역","stationCode":"761"},{"subwayLine":"8호선","stationName":"암사역","stationCode":"810"},{"subwayLine":"8호선","stationName":"천호역","stationCode":"811"},{"subwayLine":"8호선","stationName":"강동구청역","stationCode":"812"},{"subwayLine":"8호선","stationName":"몽촌토성역","stationCode":"813"},{"subwayLine":"8호선","stationName":"잠실역","stationCode":"814"},{"subwayLine":"8호선","stationName":"석촌역","stationCode":"815"},{"subwayLine":"8호선","stationName":"송파역","stationCode":"816"},{"subwayLine":"8호선","stationName":"가락시장역","stationCode":"817"},{"subwayLine":"8호선","stationName":"문정역","stationCode":"818"},{"subwayLine":"8호선","stationName":"장지역","stationCode":"819"},{"subwayLine":"8호선","stationName":"복정역","stationCode":"820"},{"subwayLine":"1호선","stationName":"가산디지털단지역","stationCode":"P142"},{"subwayLine":"1호선","stationName":"독산역","stationCode":"P143"},{"subwayLine":"1호선","stationName":"금천구청역","stationCode":"P144"},{"subwayLine":"1호선","stationName":"광명역","stationCode":"P144-1"},{"subwayLine":"1호선","stationName":"석수역","stationCode":"P145"},{"subwayLine":"1호선","stationName":"관악역","stationCode":"P146"},{"subwayLine":"1호선","stationName":"안양역","stationCode":"P147"},{"subwayLine":"1호선","stationName":"명학역","stationCode":"P148"},{"subwayLine":"1호선","stationName":"금정역","stationCode":"P149"},{"subwayLine":"1호선","stationName":"군포역","stationCode":"P150"},{"subwayLine":"1호선","stationName":"당정역","stationCode":"P151"},{"subwayLine":"1호선","stationName":"의왕역","stationCode":"P152"},{"subwayLine":"1호선","stationName":"성균관대역","stationCode":"P153"},{"subwayLine":"1호선","stationName":"화서역","stationCode":"P154"},{"subwayLine":"1호선","stationName":"수원역","stationCode":"P155"},{"subwayLine":"1호선","stationName":"세류역","stationCode":"P156"},{"subwayLine":"1호선","stationName":"병점역","stationCode":"P157"},{"subwayLine":"1호선","stationName":"서동탄역","stationCode":"P157-1"},{"subwayLine":"1호선","stationName":"세마역","stationCode":"P158"},{"subwayLine":"1호선","stationName":"오산대역","stationCode":"P159"},{"subwayLine":"1호선","stationName":"오산역","stationCode":"P160"},{"subwayLine":"1호선","stationName":"진위역","stationCode":"P161"},{"subwayLine":"1호선","stationName":"송탄역","stationCode":"P162"},{"subwayLine":"1호선","stationName":"서정리역","stationCode":"P163"},{"subwayLine":"1호선","stationName":"평택지제역","stationCode":"P164"},{"subwayLine":"1호선","stationName":"평택역","stationCode":"P165"},{"subwayLine":"1호선","stationName":"성환역","stationCode":"P166"},{"subwayLine":"1호선","stationName":"직산역","stationCode":"P167"},{"subwayLine":"1호선","stationName":"두정역","stationCode":"P168"},{"subwayLine":"1호선","stationName":"천안역","stationCode":"P169"},{"subwayLine":"1호선","stationName":"봉명역","stationCode":"P170"},{"subwayLine":"1호선","stationName":"쌍용역","stationCode":"P171"},{"subwayLine":"1호선","stationName":"아산역","stationCode":"P172"},{"subwayLine":"1호선","stationName":"탕정역","stationCode":"P173"},{"subwayLine":"1호선","stationName":"배방역","stationCode":"P174"},{"subwayLine":"1호선","stationName":"온양온천역","stationCode":"P176"},{"subwayLine":"1호선","stationName":"신창역","stationCode":"P177"},{"subwayLine":"5호선","stationName":"둔촌동역","stationCode":"P549"},{"subwayLine":"5호선","stationName":"올림픽공원역","stationCode":"P550"},{"subwayLine":"5호선","stationName":"방이역","stationCode":"P551"},{"subwayLine":"5호선","stationName":"오금역","stationCode":"P552"},{"subwayLine":"5호선","stationName":"개롱역","stationCode":"P553"},{"subwayLine":"5호선","stationName":"거여역","stationCode":"P554"},{"subwayLine":"5호선","stationName":"마천역","stationCode":"P555"}]


# In[82]:


#stationcode자르기
station_codes = [item['stationCode'] for item in subway]
sub1=station_codes[:100]
sub2=station_codes[100:200]
sub3=station_codes[200:300]
sub4=station_codes[300:]
print(sub1)
print(sub2)
print(sub3)
print(sub4)


# In[ ]:


#일정
'''
day1=sub1[8] day2=sub1[9] day3=sub1[10] 
day4=sub2[8] day5=sub2[9] day6=sub2[10] 
day7=sub3[8] day8=sub3[9] day9=sub3[10] 
day10=sub4[8] sub4[9] sub4[10] 
'''


# In[84]:


#day1~day3 자르기
day1=[]
day2=[]
day3=[]
for i in sub1:
    url_8=f'https://apis.openapi.sk.com/puzzle/subway/congestion/stat/car/stations/{i}?dow=FRI&hh=08'
    url_9=f'https://apis.openapi.sk.com/puzzle/subway/congestion/stat/car/stations/{i}?dow=FRI&hh=09'
    url_10=f'https://apis.openapi.sk.com/puzzle/subway/congestion/stat/car/stations/{i}?dow=FRI&hh=10'
    day1.append(url_8)
    day2.append(url_9)
    day3.append(url_10)
print(day3)
len(day3)


# In[85]:


#day4~day6 자르기
day4=[]
day5=[]
day6=[]
for i in sub2:
    url_8=f'https://apis.openapi.sk.com/puzzle/subway/congestion/stat/car/stations/{i}?dow=FRI&hh=08'
    url_9=f'https://apis.openapi.sk.com/puzzle/subway/congestion/stat/car/stations/{i}?dow=FRI&hh=09'
    url_10=f'https://apis.openapi.sk.com/puzzle/subway/congestion/stat/car/stations/{i}?dow=FRI&hh=10'
    day4.append(url_8)
    day5.append(url_9)
    day6.append(url_10)
print(day4)
len(day4)


# In[86]:


#day7~day9 자르기
day7=[]
day8=[]
day9=[]
for i in sub3:
    url_8=f'https://apis.openapi.sk.com/puzzle/subway/congestion/stat/car/stations/{i}?dow=FRI&hh=08'
    url_9=f'https://apis.openapi.sk.com/puzzle/subway/congestion/stat/car/stations/{i}?dow=FRI&hh=09'
    url_10=f'https://apis.openapi.sk.com/puzzle/subway/congestion/stat/car/stations/{i}?dow=FRI&hh=10'
    day7.append(url_8)
    day8.append(url_9)
    day9.append(url_10)
print(day9)
len(day8)


# In[87]:


#day10 자르기
day10=[]
for i in sub4:
    url_8=f'https://apis.openapi.sk.com/puzzle/subway/congestion/stat/car/stations/{i}?dow=FRI&hh=08'
    url_9=f'https://apis.openapi.sk.com/puzzle/subway/congestion/stat/car/stations/{i}?dow=FRI&hh=09'
    url_10=f'https://apis.openapi.sk.com/puzzle/subway/congestion/stat/car/stations/{i}?dow=FRI&hh=10'
    day10.append(url_8)
    day10.append(url_9)
    day10.append(url_10)
print(day10)
len(day10)
    


# In[95]:


# FIXME
#daY10 부분과 KEY를 각자 파트로 바꾸기
#저장 경로 원하면 바꾸기
key = FIXME
your_day = day3
csv_export_path = 'subway_congestion_dayx.csv'


responses = []

for i in your_day:
    url = i
    headers = {
        "accept": "application/json",
        "appkey": key,
    }
    response = requests.get(url, headers=headers)
    print(response.text)
    responses.append(response.text)


# In[95]:


# data = json.loads(response.text)
data = json.loads(responses)
df_list = []
for once_api_result in data:
    for stat in once_api_result['contents']['stat']:
        for data_row in stat['data']:
            # 'congestionCar' 리스트를 개별 컬럼으로 변환하고, 기존의 데이터에 추가
            data_row.update({f'congestionCar_{i}': v for i, v in enumerate(data_row['congestionCar'])})
            del data_row['congestionCar']
            df_list.append({**stat, **data_row})

df = pd.DataFrame(df_list)

# 'data' 컬럼 삭제
df = df.drop('data', axis=1)

# CSV 파일로 저장
df.to_csv(csv_export_path, index=False)


# %%
