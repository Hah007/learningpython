# 本地Chrome浏览器设置方法
from selenium import webdriver # 从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options
import time # 调用time模块

#手动输入评论
comm_text=input('请输入评论：(回车默认‘selenium自动评论测试-001’)')
if comm_text=='':
    comm_text='selenium自动评论测试-001'

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('disable-infobars')

driver = webdriver.Chrome(chrome_options=chrome_options) # 设置引擎为Chrome，真实地打开一个Chrome浏览器
url='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
driver.get(url) # 访问页面
time.sleep(2) # 暂停两秒，等待浏览器缓冲

name = driver.find_element_by_id('user_login') # 找到【用户名】下面的输入框位置
name.send_keys('hah007') # 输入用户名

password= driver.find_element_by_id('user_pass') # 找到【密码】下面的输入框位置
password.send_keys('iamhah007')
button = driver.find_element_by_id('wp-submit') # 找到【登录】按钮
button.click() # 点击【登录】按钮
time.sleep(4)

# 获取到该文章对应的a标签（超链接），并点击链接进入文章详情页
article_link = driver.find_element_by_partial_link_text('未来已来（四）——Python学习进阶图谱')
article_link.click()
#评论区
comm = driver.find_element_by_id('comment') # 找到【评论】下面的输入框位置
comm.send_keys('selenium自动评论测试-001') # 输入评论
comm_bu=driver.find_element_by_id('submit') # 找到【发表评论】按钮
comm_bu.click()

time.sleep(4)
driver.close() # 关闭浏览器



