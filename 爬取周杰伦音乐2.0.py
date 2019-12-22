# 直接运行代码就好
import requests
import openpyxl
import time
# 引用requests模块

name='周杰伦'
#这个歌手可以修改

#准备excel表格
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='music'
sheet['A1']='歌曲名'
sheet['B1']='所属专辑'
sheet['C1']='播放时长'
sheet['D1']='播放链接'
sheet['E1']='下载地址'

headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
# 伪装请求头

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
####
####仅爬取两页，可以修改后爬取多页
####
for x in range(2):
    #封装参数
    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.song_next',
    'searchid':'64405487069162918',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':str(x+1),
    'n':'20',
    'w':name,
    'g_tk':'5381',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'    
    }
    # 将参数封装为字典
    res_music = requests.get(url,headers=headers,params=params)
    # 调用get方法，下载这个字典
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
    # list_music是一个列表，music是它里面的元素
        name=music['name']
        # 以name为键，查找歌曲名，把歌曲名赋值给nam
        album=music['album']['name']
        # 查找专辑名，把专辑名赋给album
        time1=music['interval']
        # 查找播放时长，把时长赋值给time
        link1='https://y.qq.com/n/yqq/song/' + str(music['mid']) + '.html'
        # 查找播放链接，把链接赋值给link
        link2=music['url']
        sheet.append([name,album,time1,link1,link2])
        # 把name、album、time和link写成列表，用append函数多行写入Excel

        print('歌曲名：' + name + '\n' + '所属专辑:' + album +'\n' + '播放时长:' + str(time1) + '\n' + '播放链接:'+ link1+'播放地址：'+link2+'\n')
        
    
    #暂停1秒
    time.sleep(1)
    
wb.save('Jay.xlsx')

