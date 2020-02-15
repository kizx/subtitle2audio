from aip import AipSpeech
from pydub import AudioSegment
import srt
import sys
import os

""" 填入你的 百度云 APPID AK SK """
APP_ID = '18339246'
API_KEY = 'FpGBWCRoUEtwZ3SYcMvz2SDG'
SECRET_KEY = 'PoxdxWuaRnVZhPElDSMUVqaosXR27G7y'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

"""
spd: 语速 pit: 音调 vol: 音量 
per：0为度小美女声，1为度小宇男声，3为情感合成-度逍遥，4为情感合成-度丫丫
建议先去 https://ai.baidu.com/tech/speech/tts 试听确定合适的参数
"""
options = {'spd': 5, 'pit': 5, 'vol': 5, 'per': 1}


def audio_download(text, file_name):
    result = client.synthesis(text=text, lang='zh', ctp=1, options=options)
    if not isinstance(result, dict):
        with open(file_name, 'wb') as f:
            f.write(result)


def main(srt_file):
    with open(srt_file, encoding='utf-8') as sub:
        subtitle = list(srt.parse(sub))
    audio = AudioSegment.silent(0)
    bf_end = 0
    for i in subtitle:
        file_name = 'audio/' + str(i.index) + '-' + i.content + '.mp3'
        audio_download(i.content, file_name)
        silence_time = i.start.total_seconds() - bf_end
        silence_audio = AudioSegment.silent(silence_time * 1000)
        audio += silence_audio
        audio += AudioSegment.from_mp3(file_name)
        bf_end = audio.duration_seconds
    audio.export('output.mp3', format='mp3')
    print('完成！')


if __name__ == '__main__':
    if not os.path.exists('audio'):
        os.mkdir('audio')
    main(sys.argv[1])
