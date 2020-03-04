import json
import os
import webbrowser

import srt
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QLineEdit
from pydub import AudioSegment

from baidu import baidu


def web(url):
    webbrowser.open(url)


class Stats:

    def __init__(self):
        self.ui = QUiLoader().load('main.ui')
        self.ui.secret_key.setEchoMode(QLineEdit.Password)
        self.ui.per.setId(self.ui.per_0, 0)
        self.ui.per.setId(self.ui.per_1, 1)
        self.ui.per.setId(self.ui.per_3, 3)
        self.ui.per.setId(self.ui.per_4, 4)
        self.ui.baiduapi.clicked.connect(
            lambda: web('https://console.bce.baidu.com/ai/?fromai=1#/ai/speech/overview/index'))
        self.ui.baiduai.clicked.connect(lambda: web('https://ai.baidu.com/tech/speech/tts'))
        self.ui.save.clicked.connect(self.save)
        self.ui.file.clicked.connect(self.openfile)
        self.ui.generate.clicked.connect(self.generate)
        self.load_setting()

    def note(self, info):
        QMessageBox.information(self.ui, "提示", info)

    def save(self):
        app_id = self.ui.app_id.text()
        app_key = self.ui.app_key.text()
        secret_key = self.ui.secret_key.text()
        baidu_setting = {'app_id': app_id, 'app_key': app_key, 'secret_key': secret_key}
        with open('setting.json', 'r+') as f:
            setting = json.load(f)
            setting['baidu'] = baidu_setting
            f.seek(0)
            f.truncate()
            json.dump(setting, f, indent=2)
            self.note('保存设置成功')

    def load_setting(self):
        if not os.path.exists('setting.json'):
            with open('setting.json', 'w') as f:
                f.write('{}')
        with open('setting.json', 'r') as f:
            setting = json.load(f)
            baidu_setting = setting.get('baidu', {})
            app_id = baidu_setting.get('app_id', '')
            app_key = baidu_setting.get('app_key', '')
            secret_key = baidu_setting.get('secret_key', '')
        self.ui.app_id.setText(app_id)
        self.ui.app_key.setText(app_key)
        self.ui.secret_key.setText(secret_key)

    def openfile(self):
        file, _ = QFileDialog.getOpenFileName(self.ui, '选择字幕文件', './', "Srt File(*.srt)")
        if file:
            self.ui.file_path.setText(file)

    def generate(self):
        try:
            per = self.ui.per.checkedId()
            spd = self.ui.spd.value()
            vol = self.ui.vol.value()
            pit = self.ui.pit.value()
            srt_file = self.ui.file_path.text()
            if not srt_file:
                self.note('未找到字幕文件')
                return
            with open(srt_file, encoding='utf-8') as sub:
                subtitle = list(srt.parse(sub))
            options = {'per': per, 'spd': spd, 'vol': vol, 'pit': pit}
            file_path = os.path.dirname(srt_file)
            if not os.path.exists(f'{file_path}/audio/'):
                os.mkdir(f'{file_path}/audio/')
            audio = AudioSegment.silent(0)
            bf_end = 0
            step = 50 / len(subtitle)
            pbar = 0
            for i in subtitle:
                pbar += step
                self.ui.progressBar.setValue(pbar)
                file_name = f'{file_path}/audio/{i.index}-{i.content}.mp3'
                baidu(i.content, options, file_name)
                silence_time = i.start.total_seconds() - bf_end
                silence_audio = AudioSegment.silent(silence_time * 1000)
                audio += silence_audio
                audio += AudioSegment.from_mp3(file_name)
                bf_end = audio.duration_seconds
                pbar += step
                self.ui.progressBar.setValue(pbar)
            else:
                audio.export(f'{srt_file}.mp3', format='mp3')
                self.note("完成！输出文件在字幕文件夹下")
        except Exception as e:
            print(e)
            self.note(str(e))


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('logo.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
