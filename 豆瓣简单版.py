#encoding=utf-8
import bs4
from bs4 import BeautifulSoup
import requests

movieInfo = []
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='

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

    bs = BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        #查找序号
        title = titles.find('span', class_="title").text
        #查找电影名
        tes = titles.find('span',class_="inq").text
        #查找推荐语
        comment = titles.find('span',class_="rating_num").text
        #查找评分
        url_movie = titles.find('a')['href']
        # print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
        movieInfo.append((num,title, comment,tes,url_movie))

for mov in movieInfo:
    print(mov)
# for x in range(10):
#     url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
#     try:
#         user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'
#         response = requests.get(url,headers={'User-Agent':user_agent})
#         response.raise_for_status()     # 如果返回的状态码不是200，则抛出异常
#         response.encoding = response.apparent_encoding      # 根据响应信息判断网页的编码格式，便于response.text知道如何解码
#     except Exception as e:
#         print('爬取错误')
#     else:
#         print('爬取成功')
#         return response.text