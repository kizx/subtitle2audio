from aip import AipSpeech
import json


def baidu(text, file_name, options):
    with open('setting.json', 'r') as f:
        setting = json.load(f)
        baidu = setting.get('baidu', {})
    client = AipSpeech(baidu.get('app_id', ''), baidu.get(
        'app_key', ''), baidu.get('secret_key', ''))
    result = client.synthesis(text=text, lang='zh', ctp=1, options=options)
    if not isinstance(result, dict):
        with open(file_name, 'wb') as f:
            f.write(result)
    return result


if __name__ == '__main__':
    options = {'spd': 5, 'pit': 5, 'vol': 5, 'per': 1}
    result = baidu('百度你好', '百度你好.mp3', options)
