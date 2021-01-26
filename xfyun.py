import _thread as thread
import base64
import datetime
import hashlib
import hmac
import json
import os
import ssl
from datetime import datetime
from time import mktime
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time

import websocket

STATUS_FIRST_FRAME = 0  # 第一帧的标识
STATUS_CONTINUE_FRAME = 1  # 中间帧标识
STATUS_LAST_FRAME = 2  # 最后一帧的标识


# 收到websocket错误的处理
def on_error(ws, error):
    print("on_error:", error)


# 收到websocket关闭的处理
def on_close(ws):
    print("### closed ###")


class XF:
    def __init__(self, xf_setting, options=None):
        self.APPID = xf_setting.get('app_id')
        self.APIKey = xf_setting.get('api_key')
        self.APISecret = xf_setting.get('api_secret')
        if options is None:
            options = {'per': 'xiaoyan', 'spd': 50, 'vol': 50, 'pit': 50}
        self.options = options

        self.CommonArgs = {"app_id": self.APPID}
        self.BusinessArgs = {"aue": "lame",
                             "auf": "audio/L16;rate=16000",
                             "vcn": self.options.get('per'),
                             "speed": self.options.get('spd'),
                             "volume": self.options.get('vol'),
                             "pitch": self.options.get('pit'),
                             "tte": "utf8",
                             "sfl": 1}

    def process(self, text, file_name):
        Data = {"status": 2, "text": str(base64.b64encode(text.encode('utf-8')), "UTF8")}

        def on_message(ws, message):
            try:
                message = json.loads(message)
                code = message["code"]
                sid = message["sid"]
                audio = message["data"]["audio"]
                audio = base64.b64decode(audio)
                status = message["data"]["status"]
                # print(message)
                if status == STATUS_LAST_FRAME:
                    # print("ws is closed")
                    ws.close()
                if code != 0:
                    errMsg = message["message"]
                    print("sid:%s call error:%s code is:%s" % (sid, errMsg, code))
                else:
                    with open(file_name, 'ab') as f:
                        f.write(audio)
            except Exception as e:
                print("receive msg,but parse exception:", e)

        def on_open(ws):
            def run(*args):
                d = {"common": self.CommonArgs,
                     "business": self.BusinessArgs,
                     "data": Data,
                     }
                d = json.dumps(d)
                # print("开始发送文本数据：", text)
                ws.send(d)
                if os.path.exists(file_name):
                    os.remove(file_name)

            thread.start_new_thread(run, ())

        websocket.enableTrace(False)
        wsUrl = self.create_url()
        wss = websocket.WebSocketApp(wsUrl,
                                     on_message=on_message,
                                     on_error=on_error,
                                     on_close=on_close)
        wss.on_open = on_open
        wss.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def create_url(self):
        url = 'wss://tts-api.xfyun.cn/v2/tts'
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))
        # 拼接字符串
        signature_origin = "host: " + "ws-api.xfyun.cn" + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + "/v2/tts " + "HTTP/1.1"
        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
            self.APIKey, "hmac-sha256", "host date request-line", signature_sha)
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": "ws-api.xfyun.cn"
        }
        # 拼接鉴权参数，生成url
        url = url + '?' + urlencode(v)
        return url


if __name__ == "__main__":
    with open('setting.json', 'r') as ff:
        setting = json.load(ff)
        xf_st = setting.get('xf', {})
    xf = XF(xf_st)
    xf.process('今天不学习 明天变垃圾', '讯飞.mp3')
