from gevent import monkey
#从gevent库里导入monkey模块。
monkey.patch_all()
#monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步。
import gevent,time,requests, bs4,csv
#导入gevent、time、requests
from gevent.queue import Queue
#从gevent库里导入queue模块

start = time.time()

# #准备csv文件
fl=open('mtime250tv.csv','w', newline='',encoding='utf-8')
writer=csv.writer(fl)
writer.writerow(['序号 ', '电视剧名', '导演', '主演', '简介'])

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url_list = ['http://www.mtime.com/top/tv/top100/']
url_1='http://www.mtime.com/top/tv/top100/index-{page}.html'
for x in range(2,11):
    url = url_1.format( page=x)
    url_list.append(url)
work = Queue()
#创建队列对象，并赋值给work。
for url in url_list:
#遍历url_list
    work.put_nowait(url)
    #用put_nowait()函数可以把网址都放进队列里。
def crawler():
    while not work.empty():
    #当队列不是空的时候，就执行下面的程序。
        url = work.get_nowait()
        #用get_nowait()函数可以把队列里的网址都取出。
        r = requests.get(url, headers=headers)
        #用requests.get()函数抓取网址。
        print(url,work.qsize(),r.status_code)
        #打印网址、队列长度、抓取请求的状态码。
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
            writer.writerow([num,name,director,actor,remarks])
            print('记录+1......')
            

tasks_list  = [ ]
#创建空的任务列表
for x in range(5):
#相当于创建了5个爬虫
    task = gevent.spawn(crawler)
    #用gevent.spawn()函数创建执行crawler()函数的任务。
    tasks_list.append(task)
    #往任务列表添加任务。
gevent.joinall(tasks_list)
#用gevent.joinall方法，执行任务列表里的所有任务，就是让爬虫开始爬取网站。
end = time.time()
print(end-start)
    
