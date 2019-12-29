from selenium import webdriver # 从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options
import time # 调用time模块
from bs4 import BeautifulSoup 

chrome_options = Options()
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('disable-infobars')

driver = webdriver.Chrome(chrome_options=chrome_options) # 设置引擎为Chrome，真实地打开一个Chrome浏览器
url='https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html'
driver.get(url) # 访问页面
time.sleep(2) # 暂停两秒，等待浏览器缓冲

comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') # 使用class_name找到评论
print(len(comments)) # 打印获取到的评论个数
for comment in comments: # 循环
    sweet = comment.find_element_by_tag_name('p') # 找到评论
    print ('评论：%s\n ---\n'%sweet.text) # 打印评论

nextpage=driver.find_element_by_class_name('js_get_more_hot')
nextpage.click()
time.sleep(2) # 暂停两秒，等待浏览器缓冲

print('*******下一页**********') 
# comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') # 使用class_name找到评论
# for comment in comments: # 循环
#     sweet = comment.find_element_by_tag_name('p') # 找到评论
#     print ('评论：%s\n ---\n'%sweet.text) # 打印评论

# BeautifulSoup解析
pageSource = driver.page_source # 获取Elements中渲染完成的网页源代码
soup = BeautifulSoup(pageSource,'html.parser')  # 使用bs解析网页
comments = soup.find('ul',class_='js_hot_list').find_all('li',class_='js_cmt_li') # 使用bs提取元素
for comment in comments: # 循环
    sweet = comment.find('p') # 提取评论
    print ('评论：%s\n ---\n'%sweet.text) # 打印评论

driver.close() # 关闭浏览器

