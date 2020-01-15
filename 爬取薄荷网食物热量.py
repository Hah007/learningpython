from gevent import monkey
monkey.patch_all()
import gevent,requests, bs4, csv,time
from gevent.queue import Queue

start = time.time()

# #准备csv文件
fl=open('food_calorie.csv','w', newline='',encoding='utf-8')
writer=csv.writer(fl)
writer.writerow(['序号','食物名称 ', '链接地址', '热量'])

work = Queue()
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

#前3个常见食物分类的前3页的食物记录的网址：
url_1 = 'http://www.boohee.com/food/group/{type}?page={page}'
for x in range(1, 4):
    for y in range(1, 4):
        real_url = url_1.format(type=x, page=y)
        work.put_nowait(real_url)
      
#第11个常见食物分类的前3页的食物记录的网址：
url_2 = 'http://www.boohee.com/food/view_menu?page={page}'
for x in range(1,4):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)

#请写出crawler函数和启动协程的代码：
def crawler():
    while not work.empty():
    #当队列不是空的时候，就执行下面的程序。
        global Number
        Number=0
        url = work.get_nowait()
        #用get_nowait()函数可以把队列里的网址都取出。
        res = requests.get(url, headers=headers)
        #用requests.get()函数抓取网址。
        print(url,work.qsize(),res.status_code)
        #打印网址、队列长度、抓取请求的状态码。
        #用requests.get获取网页源代码。
        bs_res = bs4.BeautifulSoup(res.text, 'html.parser')
        #用BeautifulSoup解析网页源代码。
        foods = bs_res.find_all('li', class_='item clearfix')
        #用find_all提取出<li class="item clearfix">标签的内容。
        for food in foods:
        #遍历foods
            food_name = food.find_all('a')[1]['title']
            #用find_all在<li class="item clearfix">标签下，提取出第2个<a>元素title属性的值，也就是食物名称。
            food_url = 'http://www.boohee.com' + food.find_all('a')[1]['href']
            #用find_all在<li class="item clearfix">元素下，提取出第2个<a>元素href属性的值，跟'http://www.boohee.com'组合在一起，就是食物详情页的链接。
            food_calorie = food.find('p').text
            #用find在<li class="item clearfix">标签下，提取<p>元素，再用text方法留下纯文本，也提取出了食物的热量。              
            Number+=1
            print(Number,food_name,food_calorie)
            #打印食物的名称和热量。
            writer.writerow([Number,food_name,food_url,food_calorie])
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