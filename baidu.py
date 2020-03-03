import json

from aip import AipSpeech


def baidu(text, options, file_name=''):
    with open('setting.json', 'r') as f:
        setting = json.load(f)
        baidu_setting = setting.get('baidu', {})
    client = AipSpeech(baidu_setting.get('app_id', ''), baidu_setting.get(
        'app_key', ''), baidu_setting.get('secret_key', ''))
    result = client.synthesis(text=text, lang='zh', ctp=1, options=options)
    if not isinstance(result, dict):
        if file_name:
            with open(file_name, 'wb') as f:
                f.write(result)
    return result


if __name__ == '__main__':
    opt = {'spd': 5, 'pit': 5, 'vol': 5, 'per': 1}
    baidu('百度你好', opt, '百度你好.mp3')
