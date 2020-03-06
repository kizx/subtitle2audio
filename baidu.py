import json

from aip import AipSpeech


class Baidu:
    def __init__(self, baidu_setting, options=None):
        if options is None:
            options = {'spd': 5, 'pit': 5, 'vol': 5, 'per': 1}
        self.setting = baidu_setting
        self.options = options
        self.client = AipSpeech(self.setting.get('app_id', ''), self.setting.get('app_key', ''),
                                self.setting.get('secret_key', ''))

    def process(self, text, file_name):
        result = self.client.synthesis(text=text, lang='zh', ctp=1, options=self.options)
        if not isinstance(result, dict):
            with open(file_name, 'wb') as f:
                f.write(result)
        return result


if __name__ == '__main__':
    with open('setting.json', 'r') as ff:
        setting = json.load(ff)
        bd_st = setting.get('baidu', {})
    baidu = Baidu(bd_st)
    baidu.process('百度你好', '百度语音.mp3')
