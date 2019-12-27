import requests
from bs4 import BeautifulSoup
import random
#访问主页，请求cookies
res=requests.get('https://www.kuaidi100.com');
cookies_dict = requests.utils.dict_from_cookiejar(res.cookies)
# 把cookies转化成字典。
cookieValue='csrftoken='+cookies_dict['csrftoken']+';'
cookieValue=cookieValue+'WWWID='+cookies_dict['WWWID']
print(cookieValue);
id=input('请输入快递单号:')
headers={
#'Host':'www.kuaidi100.com',#cookies的获取来源
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
'Referer': 'https://www.kuaidi100.com/',
'Cookie': cookieValue
}
params={
	'resultv2':'1',
	'text':id
}
data1={
	"comCode":"",
	 "num":"",
	 "auto":[
		{"comCode":"","id":"","noCount":None,"noPre":"","startTime":""},
		{"comCode":"", "id":"","noCount":None,"noPre":"","startTime":""}]
	}
res=requests.post('https://www.kuaidi100.com/autonumber/autoComNum',data=data1,headers=headers,params=params)
if len(res.json()['auto'])>1:
	print('根据快递单号找到'+str(len(res.json()['auto']))+'家快递公司')
	comCodeList=[]
	count=0
	for j in res.json()['auto']:
		count=count+1
		print(str(count)+': '+j['comCode'])
		comCodeList.append(j['comCode'])
	comCode=comCodeList[int(input('请输入快递公司序号：'))-1]
else:
	comCode=res.json()['auto'][0]['comCode']
url='https://www.kuaidi100.com/query'
tmp=random.random()
print(str(tmp))
params={
	'type':comCode,
	'postid':id,
	'temp':tmp,
	'phone':''
}
res=requests.get(url,headers=headers,params=params)
print(res.status_code)
m=res.json()['data']
for i in m:
	print(i['time'],i['context'])
