import pathlib
import time

import requests
file_path = r'这里替换成缓存文件的**路径**'

def init():
    path = pathlib.Path('\history.csv')
    print(path.is_file())

    if path.is_file()==True:
        files = open(file_path+'\history.csv')

        print('**温馨提示**：查询到历史记录，可复制粘贴单号查询：'+'\n',files.read())
        check()
    else:
        print('**温馨提示**：未查询到历史记录，请输入单号查询。\n')
        check()

def info(comp_type,num):

    url = 'https://m.kuaidi100.com/query?type={}&postid={}'.format(comp_type,num)
    result = requests.get(url)
    for n in range(0,len(result.json()['data'])):
        print(result.json()['data'][n]['time']+'\t',result.json()['data'][n]['context'])

    now = time.strftime("%Y.%m.%d\t%H:%M:%S")
    with open(file_path+'\history.csv','a+') as ff:
        ff.write(now+'\t'+comp_type+'\t'+num+'\n')

def check():

    num = input('\n请输入快递单号：')
    # num = '1'
    auto_url = 'http://m.kuaidi100.com/autonumber/auto?num={}'.format(num)
    auto_org = requests.get(auto_url)
    if auto_org.json() == []:

        print('\n**温馨提示**：单号有误或未录入，请核对单号或稍后再尝试！\n')
    else:
        print(auto_org.json)
        comp_type = auto_org.json()['comCode']
        print('\n快递类型：',comp_type)
        print('快递单号：',num+'\n')
        info(comp_type,num)

init()

# import requests
# from bs4 import BeautifulSoup
# import random
# # 访问主页，请求cookies
# res = requests.get('https://www.kuaidi100.com')
# cookies_dict = requests.utils.dict_from_cookiejar(res.cookies)
# # 把cookies转化成字典。
# cookieValue = 'csrftoken='+cookies_dict['csrftoken']+';'
# cookieValue = cookieValue+'WWWID='+cookies_dict['WWWID']
# print(cookieValue)
# id = input('请输入快递单号:')
# headers = {
#     # 'Host':'www.kuaidi100.com',#cookies的获取来源
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#     'Referer': 'https://www.kuaidi100.com/',
#     'Cookie': cookieValue
# }
# params = {
#     'resultv2': '1',
#     'text': id
# }
# data1 = {
#     "comCode": "",
#     "num": "",
#     "auto": [
#         {"comCode": "", "id": "", "noCount": None, "noPre": "", "startTime": ""},
#         {"comCode": "", "id": "", "noCount": None, "noPre": "", "startTime": ""}]
# }
# res = requests.post('https://www.kuaidi100.com/autonumber/autoComNum',
#                     data=data1, headers=headers, params=params)
# if len(res.json()['auto']) > 1:
#     print('根据快递单号找到'+str(len(res.json()['auto']))+'家快递公司')
#     comCodeList = []
#     count = 0
#     for j in res.json()['auto']:
#         count = count+1
#         print(str(count)+': '+j['comCode'])
#         comCodeList.append(j['comCode'])
#     comCode = comCodeList[int(input('请输入快递公司序号：'))-1]
# else:
#     comCode = res.json()['auto'][0]['comCode']

# url = 'https://www.kuaidi100.com/query'
# tmp = random.random()
# print(str(tmp))
# params = {
#     'type': comCode,
#     'postid': id,
#     'temp': tmp,
#     'phone': ''
# }
# res = requests.get(url, headers=headers, params=params)
# print(res.status_code)
# m = res.json()['data']
# for i in m:
#     print(i['time'], i['context'])
