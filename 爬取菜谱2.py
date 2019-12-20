import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_foods = requests.get('http://www.xiachufang.com/explore/')
# 获取数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 解析数据
# list_foods = bs_foods.find_all('div',class_ = 'info pure-u')     #找到我们需要提取数据的最小父级标签
# list_all = []       #创建空列表
# for food in list_foods:            #因为有多个层级的标签，需要使用循环进行操作
# 	tag_a = list_foods[0].find('a')      #我们只提取第一个数据，所以别忘记加入角标[0],再接着寻找正确的标签
# 	name = tag_a.text.strip()       #获取菜名
# 	url = 'http://www.xiachufang.com'+tag_a['href']       #获取网址链接
# 	tag_p = food.find('p',class_ = 'ing ellipsis')       #提取食材信息
# 	shi_c = tag_p.text.strip()         #得到食材的信息
# 	list_all.append([name,url,shi_c])         #将菜名，链接，食材添加到列表中
# print(list_all)


tag_name = bs_foods.find_all('p',class_='name')

# 查找包含菜名和URL的<p>标签
tag_ingredients = bs_foods.find_all('p',class_='ing ellipsis')

# 查找包含食材的<p>标签
list_all = []
# 创建一个空列表，用于存储信息
for x in range(len(tag_name)):
# 启动一个循环，次数等于菜名的数量
    
    list_food = [tag_name[x].text.strip(),'http://www.xiachufang.com'+tag_name[x].find('a')['href'],tag_ingredients[x].text.strip()]
    # 提取信息，封装为列表。注意此处[18:-14]切片和之前不同，是因为此处使用的是<p>标签，而之前是<a>
    list_all.append(list_food)
    # 将信息添加进list_all
for li in list_all:
    print(li)
# 打印