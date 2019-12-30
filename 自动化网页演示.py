# 本地Chrome浏览器设置方法
from selenium import webdriver # 从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options
import time # 调用time模块
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('disable-infobars')

driver = webdriver.Chrome(chrome_options=chrome_options) # 设置引擎为Chrome，真实地打开一个Chrome浏览器

driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 暂停两秒，等待浏览器缓冲

teacher = driver.find_element_by_id('teacher') # 找到【请输入你喜欢的老师】下面的输入框位置
teacher.send_keys('必须是吴枫呀') # 输入文字
assistant = driver.find_element_by_name('assistant') # 找到【请输入你喜欢的助教】下面的输入框位置
assistant.send_keys('都喜欢') # 输入文字
button = driver.find_element_by_class_name('sub') # 找到【提交】按钮
button.click() # 点击【提交】按钮
time.sleep(2)
#查找Python之禅所在的标签
#方法一：
# contents = driver.find_elements_by_class_name('content') 
# for con in contents:
#     title=con.find_element_by_tag_name('h1').text
#     kp=con.find_element_by_tag_name('p').text
#     print('标题：\n'+title)
#     print('内容：\n'+kp)

#查找Python之禅所在的标签
#方法二：
page_all = driver.page_source # 获取页面信息，selenium的page_source方法可以直接返回页面源码
bs = BeautifulSoup(page_all,'html.parser')  # 使用bs解析网页
contents = bs.find_all(class_="content") # 找到Python之禅中文版和英文版所在的元素
for con in contents:
    title=con.find('h1').text
    kp=con.find('p').text.replace('  ','') 
    print('标题：\n'+title)
    print('内容：\n'+kp)

driver.close() # 关闭浏览器