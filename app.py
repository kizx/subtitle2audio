from flask import Flask, render_template, url_for, redirect, request
import json
import os

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


if __name__ == '__main__':
    if not os.path.exists('setting.json'):
        with open('setting.json', 'w') as f:
            f.write('{}')
    app.debug = True
    app.run()
