import http.client
import json
import threading
import time

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


def get_token(access_key, access_key_secret):
    # 创建AcsClient实例
    client = AcsClient(
        access_key,
        access_key_secret,
        "cn-shanghai"
    )
    # 创建request，并设置参数
    request = CommonRequest()
    request.set_method('POST')
    request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
    request.set_version('2019-02-28')
    request.set_action_name('CreateToken')
    response = client.do_action_with_exception(request)
    return json.loads(response)["Token"]["Id"]


def processPOSTRequest(appkey, token, text, audioSaveFile, options):
    host = 'nls-gateway.cn-shanghai.aliyuncs.com'
    url = 'https://' + host + '/stream/v1/tts'
    # 设置HTTPS Headers。
    httpHeaders = {
        'Content-Type': 'application/json'
    }
    # 设置HTTPS Body。
    body = {
        'appkey': appkey,
        'token': token,
        'text': text,
        'format': 'mp3',
        'voice': options.get('per'),  # 发音人
        'volume': options.get('vol'),  # 音量
        'speech_rate': options.get('spd'),  # 语速
        'pitch_rate': options.get('pit')  # 语调
    }
    body = json.dumps(body)
    # print('The POST request body content: ' + body)
    # Python 3.x请使用http.client。
    conn = http.client.HTTPSConnection(host)
    conn.request(method='POST', url=url, body=body, headers=httpHeaders)
    # 处理服务端返回的响应。
    response = conn.getresponse()
    # print(response.status, response.reason)
    contentType = response.getheader('Content-Type')
    body = response.read()
    if 'audio/mpeg' == contentType:
        with open(audioSaveFile, mode='wb') as f:
            f.write(body)
        print(text, 'Save succeed!')
    else:
        print('The POST request failed: ' + str(body))
    conn.close()


class Ali:
    def __init__(self, ali_setting, options):
        self.setting = ali_setting
        self.options = options
        self.appKey = self.setting.get("app_key")
        self.access_key = self.setting.get("access_key")
        self.access_key_secret = self.setting.get("access_key_secret")
        self.token = get_token(self.access_key, self.access_key_secret)

    def process(self, text, audio_name):
        audioSaveFile = audio_name
        processPOSTRequest(self.appKey, self.token, text, audioSaveFile, self.options)

    def process_multithread(self, sub, name, sgn=None, sleeptime=1):
        thread_list = []
        for index, i in enumerate(sub):
            audio_name = f"{name}{index + 1}.mp3"
            thread = threading.Thread(target=self.process, args=(i, audio_name))
            thread_list.append(thread)
            thread.start()
            time.sleep(sleeptime)  # 阿里限制请求频率
            if sgn:
                sgn.progress_update.emit(index + 1)
        num = len(sub)
        for thread in thread_list:
            thread.join()
            if sgn:
                num += 1
                sgn.progress_update.emit(num)


if __name__ == "__main__":
    with open('setting.json', 'r') as ff:
        setting = json.load(ff)
        ali_st = setting.get('ali', {})
    my_text = "今天天气不错"
    my_audio_name = '阿里语音.mp3'
    ops = {
        'per': 'xiaoyun',
        'vol': 50,
        'spd': 0,
        'pit': 0
    }
    ali = Ali(ali_st, ops)
    ali.process(my_text, my_audio_name)
    # ali.process_multithread(['这是第一句', '今天天气不错', '嘟嘟嘟嘟'], '')
