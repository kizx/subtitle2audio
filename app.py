from flask import Flask, render_template, url_for, redirect, request
import json
import os
from pydub import AudioSegment
import srt
from baidu import baidu

app = Flask(__name__)


@app.route('/')
def index():
    with open('setting.json', 'r') as f:
        setting = json.load(f)
        baidu = setting.get('baidu', {})
    return render_template('sub2audio.html', baidu=baidu)


@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))


@app.route('/sub2audio/save/<api>', methods=['POST'])
def save(api):
    with open('setting.json', 'r+') as f:
        setting = json.load(f)
        setting[api] = request.form
        f.seek(0)
        f.truncate()
        json.dump(setting, f, indent=2)
        app.logger.debug('保存设置成功')
    return redirect(url_for('index'))


@app.route('/sub2audio/generate/<api>', methods=['POST'])
def generate(api):
    if not os.path.exists('output'):
        os.mkdir('output')
    if api == 'baidu':
        options = request.form
        f = request.files.get('file')
        file_path = os.path.join('output', f.filename)
        f.save(file_path)
        main(file_path, options)
    return '生成成功，生成文件在output文件夹下'


def main(srt_file, options):
    if not os.path.exists('output/audio'):
        os.mkdir('output/audio')
    with open(srt_file, encoding='utf-8') as sub:
        subtitle = list(srt.parse(sub))
    audio = AudioSegment.silent(0)
    bf_end = 0
    for i in subtitle:
        file_name = 'output/audio/' + str(i.index) + '-' + i.content + '.mp3'
        baidu(i.content, file_name, options)
        silence_time = i.start.total_seconds() - bf_end
        silence_audio = AudioSegment.silent(silence_time * 1000)
        audio += silence_audio
        audio += AudioSegment.from_mp3(file_name)
        bf_end = audio.duration_seconds
    audio.export(f'{srt_file}.mp3', format='mp3')
    app.logger.debug('完成')


if __name__ == '__main__':
    if not os.path.exists('setting.json'):
        with open('setting.json', 'w') as f:
            f.write('{}')
    app.debug = True
    app.run()
