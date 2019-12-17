import requests
import re
#key = input('\n输入你的key：')
#需要去注册图灵机器人，申请一个key
key='c72a56d85ebd431a891c4e751a4ac047'
while True:
    info = input('\n可爱的我：')
    url = 'http://www.tuling123.com/openapi/api?key='+ key + '&info=' + info
    res = requests.get(url).text 
    reg = r'"text":"(.*?)"'
    reg = re.compile(reg,re.S)
    imagesList = re.findall(reg,res)
    print(*imagesList,sep = '\n')
