# 直接运行代码就好
import requests
import time
# 引用requests模块

name = '周杰伦'
# 这个歌手可以修改

headers = {
    'origin': 'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
}
# 伪装请求头
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
# 这是请求歌曲评论的url
#url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
# 这个是歌曲主页
for x in range(2):
    # 封装参数
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'remoteplace': 'txt.yqq.lyric',
        'searchid': '91671855062495018',
        'aggr': '0',
        'catZhida': '1',
        'lossless': '0',
        'sem': '1',
        't': '7',
        'p': str(x+1),
        'n': '5',
        'w': name,
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
        }
    # 将参数封装为字典
    res_music = requests.get(url, headers=headers, params=params)
    # 调用get方法，下载这个字典
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    Lyric_music = json_music['data']['lyric']['list']
    # 一层一层地取字典，获取歌单列表
    for Lyric in Lyric_music:
        # list_music是一个列表，music是它里面的元素
        print(Lyric['content'].replace('\\n','\n'))
        print('-----------------------------------')
        

    # 暂停1秒
    time.sleep(1)


