#coding=utf-8

'''
Descroption:Word文档转换txt
Author:hah007
Prompt:code in python3.7 env
'''

import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = '6973858@qq.com'
password = 'zntuizltafjjbhjg'
receiver = '6973858@qq.com'

def caipu_spider():
    res_foods = requests.get('http://www.xiachufang.com/explore/')
    # 获取数据
    bs_foods = BeautifulSoup(res_foods.text,'html.parser')
    tag_name = bs_foods.find_all('p',class_='name')

    list_foods = bs_foods.find_all('div',class_='info pure-u')
    list_all = ''
    num=0
    for food in list_foods:
        num=num+1
        tag_a = food.find('a')
        name = tag_a.text.strip()
        url = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p',class_='ing ellipsis')
        ingredients = tag_p.text.strip()
        food_info = '''
        序号: %s
        菜名: %s
        链接: %s
        原料: %s
        '''%(num,name,url,ingredients)
        list_all=list_all+food_info
    return(list_all)
    

def send_email(list_all):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    qqmail.login(account,password)
    content= '本周的热门菜谱如下：'+list_all
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '每周热门菜谱'
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header('6973858@qq.com')
    message['To'] = Header('6973858@qq.com')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

def job():
    print('开始一次任务')
    list_all = caipu_spider()
    # print(list_all)
    send_email(list_all)
    print('任务完成')

if __name__ == '__main__':
    print('程序运行中……')
    schedule.every().friday.at("18:00").do(job)#部署每周五的18：00执行函数的任务
    while True:
        schedule.run_pending()
        time.sleep(1)