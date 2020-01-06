import requests
import json
import pyaudio
import wave
import requests
import json
import base64
import os
from aip import AipSpeech

def Gettokent():
    baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    #API Key
    client_id = 'SAd15Zc0GYY6Uh49VN5OeDCI'
    #"你的API Key"
    #Secret Key
    client_secret = 'eEpxLlg7ZGj0GcnFEH2qGcavetwBqNTV'
    #"你的Secret Key"

    #拼url
    url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(client_id, client_secret)
    #print(url)
    #获取token
    res = requests.post(url)
    #print(res.text)
    token = json.loads(res.text)["access_token"]
    print(token)
    return token

# 百度
def tts_baidu(text):
    """ 你的 APPID AK SK """
    APP_ID = '18188577'
    API_KEY = 'SAd15Zc0GYY6Uh49VN5OeDCI'
    SECRET_KEY = 'eEpxLlg7ZGj0GcnFEH2qGcavetwBqNTV'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(text = text, options={'vol':5})

    if not isinstance(result,dict):
        with open('audio.mp3','wb') as f:
            f.write(result)
    else:print(result)

def BaiduYuYin(token1,fileurl):
    try:
        RATE = "16000"                  #采样率16KHz
        FORMAT = "wav"                  #wav格式
        CUID = "wate_play"
        DEV_PID = "1536"                #无标点普通话
        token = token1

        # 以字节格式读取文件之后进行编码
        with open(fileurl, "rb") as f:
            speech = base64.b64encode(f.read()).decode('utf8')

        size = os.path.getsize(fileurl)
        headers = {'Content-Type': 'application/json'}
        url = "https://vop.baidu.com/server_api"
        data = {
            "format": FORMAT,
            "rate": RATE,
            "dev_pid": DEV_PID,
            "speech": speech,
            "cuid": CUID,
            "len": size,
            "channel": 1,
            "token": token,
        }
        req = requests.post(url, json.dumps(data), headers)
        result = json.loads(req.text)
        return result["result"][0][:-1]
    except:
        return '识别不清'


if __name__ == '__main__':
    print('程序运行中……')
    fileurl='16k.wav'
    token1=Gettokent()
    res=BaiduYuYin(token1,fileurl)
    print(res)
    tts_baidu('我从哪里来')
