# 小说楼：https://www.xslou.com/
# 小说楼登录：https://www.xslou.com/login.php
# 小说楼的排行榜：https://www.xslou.com/top/allvisit_1/
# 小说楼推荐：https://www.xslou.com/modules/article/uservote.php?id=

import requests , json
from bs4 import BeautifulSoup 

login_url = 'https://www.xslou.com/login.php'
hot_url = 'https://www.xslou.com/top/allvisit_1/'
urge_url = 'https://www.xslou.com/modules/article/uservote.php?id='
session = requests.session()  
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def sign_in():
    data = {'username':input('请输入你的账号:'),
            'password':input('请输入你的密码:'),
            'action':'login'}
    result = session.post(login_url, headers=headers, data=data)
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    cookies_str = json.dumps(cookies_dict)
    f = open('xslou_cookies.txt', 'w')
    f.write(cookies_str)
    f.close()
    # 以上5行代码，是cookies存储。

def cookies_read():
    cookies_txt = open('xslou_cookies.txt', 'r')
    cookies_dict = json.loads(cookies_txt.read())
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    return (cookies)
    # 以上4行代码，是cookies读取。

def get_bookids():
    result = requests.get(hot_url, headers=headers)
    result.encoding = 'gbk'
    bs = BeautifulSoup(result.text,'html.parser')
    uls = bs.find_all('span',class_='up2')
    books = {}
    for li in uls:
        book_name = li.find('a').text
        link = li.find('a')['href']
        id_list = list(filter(str.isdigit,link))
        book_id = ''.join(id_list)
        books[book_id] = book_name
    return books

def urge(book_id):
    url = urge_url+book_id
    result = session.get(url, headers=headers, cookies=session.cookies)
    result.encoding = 'gbk'
    if result.status_code == 200:
        bs = BeautifulSoup(result.text,'html.parser')
        urge_info = bs.find('div',class_='blocktitle').get_text()
        urge_info2 = bs.find('div',class_='blockcontent').get_text()
        print(urge_info)
        print(urge_info2)

if __name__ == '__main__':
    try:
        session.cookies = cookies_read()
    except FileNotFoundError:
        sign_in()
        session.cookies = cookies_read()

    books = get_bookids()
    print('--------热门书籍--------')
    for k,v in books.items():
        print(k,':',v)
    book_id = input('请输入想要推荐的书籍id：')
    urge(book_id)

