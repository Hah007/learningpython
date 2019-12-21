import requests
from bs4 import  BeautifulSoup
from urllib.request import quote


play_html='https://y.qq.com/n/yqq/song/001qvvgF38HVc4.html'
# play_html='https://y.gtimg.cn/music/icon/v1/pc/nsvip6.png?max_age=2592000'

res2=requests.get(play_html)
# res2.encoding='utf-8'
# print(res2.text)
bs_res= BeautifulSoup(res2.text,'html.parser')

bs_json=res2.json()
print(bs_json)
# Lyrics=bs_json['']
# print(Lyrics)