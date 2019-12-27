# -*- coding: utf-8 -*-
import requests
# 引用requests库
import csv
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

def get_content(url):
    try:
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'
        response = requests.get(url,headers={'User-Agent':user_agent})
        response.raise_for_status()     # 如果返回的状态码不是200，则抛出异常
        # response.encoding = response.apparent_encoding      # 根据响应信息判断网页的编码格式，便于response.text知道如何解码
        rscode = response.encoding
        #研究结论：本项目encoding 比 apparent_encoding 准确
       
    except Exception as e:
        print('爬取错误')
    else:
        print('爬取成功')
        # print(response.text)
        return response.text,rscode

def parser_content(content):
    bs_foods = BeautifulSoup(content,'html.parser')

    # 解析数据
    list_foods = bs_foods.find_all('div',class_='info pure-u')
    # 查找最小父级标签

    list_all = []
    # 创建一个空列表，用于存储信息

    for food in list_foods:

        tag_a = food.find('a')
        # 提取第0个父级标签中的<a>标签
        name = tag_a.text[17:-13]
        # 菜名，使用[17:-13]切掉了多余的信息
        URL = 'http://www.xiachufang.com'+tag_a['href']
        # 获取URL
        tag_p = food.find('p',class_='ing ellipsis')
        # 提取第0个父级标签中的<p>标签
        ingredients = tag_p.text[1:-1]
        # 食材，使用[1:-1]切掉了多余的信息
        list_all.append([name,URL,ingredients])
        # 将菜名、URL、食材，封装为列表，添加进list_all
    # print(list_all)
    return list_all
    

def save_csv(list,rscode):
    with open('caipu22.csv','w',encoding=rscode) as f:
        writer = csv.writer(f)
        writer.writerow('热门菜谱')
        writer.writerows(list)
    print('csv文件保存成功......')

if __name__ == '__main__':
    url='http://www.xiachufang.com/explore/'
    content,rscode = get_content(url)
    print(rscode)
    food=parser_content(content)
    save_csv(food,rscode)