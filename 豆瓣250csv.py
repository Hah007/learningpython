import requests, bs4
import csv

#准备csv文件
fl=open('douban250.csv','w', newline='',encoding='utf-8')
writer=csv.writer(fl)
writer.writerow(['序号 ', '电影名', '评分', '推荐语', '播放地址'])



headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
for x in range(10):
    try:
        url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
        res = requests.get(url, headers=headers)
        res.raise_for_status()
    except Exception as e:
        print('爬取错误')
        exit()
    else:
        print('爬取成功')
        
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span',class_="rating_num").text
        url_movie = titles.find('a')['href']

        if titles.find('span',class_="inq") != None:
            tes = titles.find('span',class_="inq").text
            print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
        else:
            print(num + '.' + title + '——' + comment + '\n' +'\n' + url_movie)

        
        writer.writerow([num,title,comment,tes,url_movie])

fl.close()
        