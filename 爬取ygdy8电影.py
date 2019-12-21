#encoding=utf-8
import bs4
from bs4 import BeautifulSoup
import requests
from urllib.request import quote

movieInfo = []

#电影名称
name=input('输入想下载的电影名字(回车‘误杀瞒天记’)：')
if name=='':
    name='误杀瞒天记'
else:
    pass
print('本次爬取的电影是：'+name)
movie_name=quote(name.encode('gbk'))
#转码为gbk
url = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword=' +movie_name
print(url)

try:
    header = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
    res = requests.get(url,timeout = 30,headers=header)
    res.raise_for_status()
    # print(r.text)
except Exception as e:
    print('爬取错误')
else:
    print('爬取成功')
res.encoding='gbk'
#解析下载页面
soup_movie=BeautifulSoup(res.text,'html.parser')

urlpart = soup_movie.find(class_="co_content8").find_all('table')
#print(urlpart)
if urlpart:
    urlpart = urlpart[0].find('a')['href']
    urlmovie= 'https://www.ygdy8.com/' + urlpart
    print('下载页面是：'+urlmovie)
    res1=requests.get(urlmovie)
    res1.encoding='gbk'
    movie_url=BeautifulSoup(res1.text,'html.parser')
    if movie_url.find('div',id="Zoom").find('table')==None:
        print('没有网址，需要磁力下载！')
        down_url=movie_url.find('div',id="Zoom").find('span').find('a')['href']
    else:
        print('有具体网址，可以直接下载！')
        down_url=movie_url.find('div',id="Zoom").find('span').find('table').find('a')['href']

    #解析具体下载页面
    
    # .find('table').find('a')['href']
    #有部分页面不一致('table')部分没有
    print('下载地址:'+down_url)
else:
    print('没有找到电影：'+name)
     
