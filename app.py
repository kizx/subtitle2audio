from flask import Flask, render_template, url_for, redirect, request
import json
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('sub2audio.html')


@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))


@app.route('/sub2audio/save/<api>', methods=['POST'])
def save(api):
    if not os.path.exists('setting.json'):
        with open('setting.json', 'w') as f:
            f.write('{}')
    with open('setting.json', 'r+') as f:
        setting = json.load(f)
        setting[api] = request.form
        f.seek(0)
        json.dump(setting, f, indent=4)
        print(setting)
        print('写入个人设置成功')
    return request.form


if __name__ == '__main__':
    app.debug = True
    app.run()
