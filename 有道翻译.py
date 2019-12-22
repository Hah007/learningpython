import requests
import chardet
import json
import time,random,hashlib
 
def get_md5(string):
    string = string.encode('utf-8')
    md5 = hashlib.md5(string).hexdigest()
    return md5

def translate(keyword):
    ts = str(int(time.time()*1000))
    #ts是13位时间戳
    salt = ts + str(random.randint(0, 9))
    #salt是ts+一位随机数
    bv = get_md5("5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36")
    #bv是浏览器User-Agent，需要进行MD5计算
    sign = get_md5("fanyideskweb" + keyword + salt + "n%A-rKaT5fb[Gy?;N5@Tj")
    #sign是四个字符串组成后进行MD5的结果
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    #有道翻译的网站   
    data = {
        'i': keyword,
        'from': 'AUTO',
        'to': 'AUTO',
        'doctype': 'json',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt':salt,
        'sign':sign,
        'ts':ts,
        'bv':bv,
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'TypoResult': 'false'
    }
 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        ' AppleWebKit/537.36 (KHTML, like Gecko)'
        ' Chrome/73.0.3683.86 Safari/537.36'
    }
 
    response = requests.post(url, data=data, headers=headers)
    html = response.content  # 读取返回的对象
    code = chardet.detect(html)  # 自行判断编码格式
    data = html.decode(code.get('encoding', 'utf-8'))  # 解码
    json_data = json.loads(data)  # 解析载入json数据
    print('翻译的结果为：' + json_data['translateResult'][0][0]['tgt'])
    return()

if __name__ == '__main__':
    while True:
        keyword= input('请输入要翻译的内容：')
        if (keyword=='q' or keyword=='Q'):
            print('翻译结束，欢迎下次再使用！')
            print('*'*20)
            break
        translate(keyword)
        print('='*20)   
    

