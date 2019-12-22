import requests
import openpyxl
from bs4 import  BeautifulSoup
from urllib.request import quote

name='周杰伦'

artist_name=quote(name.encode('utf'))
#转到歌手页面
url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&\
searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w='+artist_name+'&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
# print(url)
#获取页面信息
res_music=requests.get(url)
# be_music=BeautifulSoup(res_music.text,'html.parser')
#解析网页
json_music = res_music.json()
# 使用json()方法，将response对象，转为列表/字典
list_music = json_music['data']['song']['list']
# 一层一层地取字典，获取歌单列表
#准备excel文件
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='music'
sheet['A1']='歌曲名'
sheet['B1']='所属专辑'
sheet['C1']='播放时长'
sheet['D1']='播放链接'
sheet['E1']='下载地址'

for music in list_music:
# list_music是一个列表，music是它里面的元素
    print(music['name'])
    # 以name为键，查找歌曲名
    
    print('所属专辑：'+music['album']['name'])
    # 查找专辑名
    print('播放时长：'+str(music['interval'])+'秒')
    # 查找播放时长
    # 查找播放链接
    play_html='https://y.qq.com/n/yqq/song/'+music['mid']+'.html'
    print('播放链接：'+play_html)
    #下载地址
    print('下载地址：'+music['url']+'\n')
    