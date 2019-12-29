# coding=utf-8

"""
Description: 提取相关联的单词
Author：hah007
Prompt: code in Python3.7
"""
#网址：http://ictclas.nlpir.org/nlpir/
#验证码暂时需要手工确认

import requests,json
url = 'http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
headers = {
    'origin':'http://ictclas.nlpir.org',
    'referer':'http://ictclas.nlpir.org/nlpir/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }
words = input('请输入你想查询的词汇：')
data = {'content':words}
res = requests.post(url,data=data,headers=headers)
data=res.text
# 以上，为上一步的代码

data1=json.loads(data)
print(data1)
# print(data1['vjson']))
# 把json数据转换为字典
print('关联词及关联度：')
for i in data1['w2vlist']:
    print(i)
print('*'*10+'\n')
for v in range(3):
    print('二级关联词 %s 及关联度：\n' %v)
    vi='v'+str(v)
    for i in data1['vjson'][vi]:
        print(i)
