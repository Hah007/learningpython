import requests

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#封装headers
link = requests.get('https://www.shanbay.com/api/v1/vocabtest/category/',headers=headers)
#先用requests下载链接。
js_link = link.json()

kemu=int(input('''请输入你选择的词库编号，按Enter确认
1，GMAT  2，考研  3，高考  4，四级  5，六级
6，英专  7，托福  8，GRE  9，雅思  10，任意
>'''))

url='https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='
relurl=url+list[kemu]
#返回正确的网址
res=requests.get(relurl,headers=headers)
words=res.json()
danci = []
#新增一个list，用于统计用户认识的单词
words_knows = []
#创建一个空的列表，用于记录用户认识的单词。
not_knows = []
#创建一个空的列表，用于记录用户不认识的单词。
print ('测试现在开始。如果你认识这个单词，请输入Y，否则直接敲Enter：')
n=0
for x in words['data']:
    #启动一个循环，循环的次数等于单词的数量。
    n=n+1
    print ("\n第"+str(n)+'个：'+x['content'])
    #加一个\n，用于换行。
    answer = input('认识请敲Y，否则敲Enter：')
    #让用户输入自己是否认识。
    if answer == 'Y':
    #如果用户认识：
        danci.append(x['content'])
        words_knows.append(x)
        #就把这个单词，追加进列表words_knows。
    else:
    #否则
        not_knows.append(x)
        #就把这个单词，追加进列表not_knows。


print ('\n在上述'+str(len(words['data']))+'个单词当中，有'+str(len(danci))+'个是你觉得自己认识的，它们是：')
print(danci)

print ('现在我们来检测一下，你有没有真正掌握它们：')
wrong_words = []
right_num = 0
for y in words_knows:
    print('\n\n'+'A:'+y['definition_choices'][0]['definition'])
    #我们改用A、B、C、D，不再用rank值，下同
    print('B:'+y['definition_choices'][1]['definition'])
    print('C:'+y['definition_choices'][2]['definition'])
    print('D:'+y['definition_choices'][3]['definition'])
    xuanze = input('请选择单词\"'+y['content']+'\"的正确翻译（输入字母即可）：')
    dic = {'A':y['definition_choices'][0]['rank'],'B':y['definition_choices'][1]['rank'],'C':y['definition_choices'][2]['rank'],'D':y['definition_choices'][3]['rank']} 
    #我们创建一个字典，搭建起A、B、C、D和四个rank值的映射关系。
    if dic[xuanze] == y['rank']:
    #此时dic[xuanze]的内容，其实就是rank值，此时的代码含义已经和之前的版本相同了。
        right_num += 1
    else:
        wrong_words.append(y)

    