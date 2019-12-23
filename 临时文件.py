import requests
import re,time
import json

item = 'zhengzhou'
ii=input('输入查询的城市：')
if ii!='':
    item=ii
    
url = 'https://free-api.heweather.com/s6/weather/forecast?location=%s&key=c3fe7421ef4c4cdd85b2965e563af7ae'%(item)
#now	实况天气
#forecast	3-10天预报  
#账号 hah007@126.com
res = requests.get(url)
time.sleep(2)

#使用json格式获取数据
datalist = res.json()
# print(datalist)
#获取第一条城市信息
data = datalist['HeWeather6'][0]
# print(json.dumps(datalist, sort_keys=True, indent=4, separators=(', ', ': ')))
for i in range(3):
    #输出城市信息
    print('城市：',data['basic']['location'])
    print('纬度：',data['basic']['lat'],'经度:',data['basic']['lon'])
    print('日期：',data['daily_forecast'][i]['date'])
    print('温度：',data['daily_forecast'][i]['tmp_min'],' ~ ',data['daily_forecast'][i]['tmp_max'])
    print('天气：',data['daily_forecast'][i]['cond_txt_d'],' ~ ',data['daily_forecast'][i]['cond_txt_n'])
    print(data['daily_forecast'][i]['wind_dir'],data['daily_forecast'][i]['wind_sc'],"级")
    print("-"*60)
