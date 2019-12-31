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

def weather_spider():
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url='http://www.weather.com.cn/weather/101180101.shtml'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    tem1= soup.find(class_='tem')
    weather1= soup.find(class_='wea')
    #爬取明日天气预报 
    # text= soup.find(class_='sky skyid lv1')
    # tem1=text.find(class_='tem')
    # weather1= text.find(class_='wea')
    # tem=tem1.text
    # weather=weather1.text
    tem=tem1.text
    weather=weather1.text
    return tem,weather

def send_email(tem,weather):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    qqmail.login(account,password)
    content= '郑州'+tem+weather
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今日天气预报'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

def job():
    print('开始一次任务')
    tem,weather = weather_spider()
    send_email(tem,weather)
    print('任务完成')

if __name__ == '__main__':
    schedule.every().day.at("23:35").do(job) 
    while True:
        schedule.run_pending()
        time.sleep(1)