import requests
import re,time
import json

item = 'zhengzhou,henan'
#,后面的可选
url = 'https://free-api.heweather.com/s6/weather/forecast?location=%s&key=a46fd5c4f1b54fda9ee71ba6711f09cd'%(item)
#now	实况天气
#forecast	3-10天预报  
#key 需要自己申请，这个是暂时使用
res = requests.get(url)
time.sleep(2)

#使用json格式获取数据
datalist = res.json()
#获取第一条城市信息
#只查了一个城市时没有意义这句话
data = datalist['HeWeather6'][0]
print(json.dumps(datalist, sort_keys=True, indent=4, separators=(', ', ': ')))

for i in range(3):
    #输出城市信息
    print('城市：',data['basic']['location'])
    print('维度：',data['basic']['lat'],'经度:',data['basic']['lon'])
    print('日期：',data['daily_forecast'][i]['date'])
    print('温度：',data['daily_forecast'][i]['tmp_min'],' ~ ',data['daily_forecast'][i]['tmp_max'])
    print('天气：',data['daily_forecast'][i]['cond_txt_d'],' ~ ',data['daily_forecast'][i]['cond_txt_n'])
    print(data['daily_forecast'][i]['wind_dir'],data['daily_forecast'][i]['wind_sc'],"级")
    print('生活指数:',data['lifestyle']['txt'])
    print("-"*60)