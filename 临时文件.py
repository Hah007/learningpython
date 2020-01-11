import gevent,time,requests, bs4,csv
from bs4 import BeautifulSoup

url = 'http://www.mtime.com/top/tv/top100/'
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

r = requests.get(url, headers=headers)

print(r.status_code)
bs = bs4.BeautifulSoup(r.text, 'html.parser')
bs = bs.find('ul', id="asyncRatingRegion")

for item in bs.find_all('li'):
    num = item.find(class_="number").text
    data_all = item.find('div', class_="mov_con")
    name=data_all.find('h2',class_="px14 pb6").text
    
    if item.find('p',class_="mt3") != None:
        remarks=item.find('p',class_="mt3").text
    else:
        remarks=''
    datas=item.find_all('p')
    for data in datas:
        if data.text[:2]=='导演':
            director=data.text[3:].strip()
        elif data.text[:2]=='主演':
            actor=data.text[3:].strip()
    
    print(num,name,director,actor,remarks)

    # print(num,name)
    # for data in data_all:
    #     if data.text[:2]=='导演':
    #         director=data.text[3:].strip()
    #     elif data.text[:2]=='主演':
    #         actor=data.text[3:].strip()
    #     else:
    #         remarks = data.text.strip()
    

    # for data_a in data_all:
    #     print(data_a)
    #     # name=data_a.find('a').text
    #     datas=data_a.find_all('p')
   

    # director = titles.find('导演： ',class_="c_fff").text
    # performer= item.find('主演： ',class_="c_fff").text
    # comment = item.find('p',class_="mt3").text
    # print(num,name,director)
