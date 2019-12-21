# coding=utf-8 ##

import requests as re
import chardet
# res=re.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')
# res.encoding='utf-8'
# text=res.text
# print(text)

# with open("douban.txt","w") as f:
#     f.write(text)

# with open('douban.txt','r',encoding='UTF-8') as f:
#     data = f.readline()

#     data1 = '离离原上草，一岁一枯荣'.encode('gbk')
   
# print(data)

import requests as re 

res=re.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')

res.encoding='utf-8'
text=res.text
with open("douban.html","w",encoding='UTF-8') as f:
    f.write(text)