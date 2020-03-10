import json
import os
import webbrowser

import srt
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QLineEdit
from pydub import AudioSegment

from ali import Ali
from baidu import Baidu


def web(*url):
    for i in url:
        webbrowser.open(i)


def value_change(obj, obje):
    obje.setValue(obj.value())


class Stats:

    def __init__(self):
        self.ui = QUiLoader().load('static/main.ui')

        self.ui.secret_key_bd.setEchoMode(QLineEdit.Password)
        self.ui.access_key_secret_ali.setEchoMode(QLineEdit.Password)

        self.ui.per.setId(self.ui.per_0, 0)
        self.ui.per.setId(self.ui.per_1, 1)
        self.ui.per.setId(self.ui.per_3, 3)
        self.ui.per.setId(self.ui.per_4, 4)

        self.ui.baiduapi.clicked.connect(
            lambda: web('https://console.bce.baidu.com/ai/?fromai=1#/ai/speech/overview/index'))
        self.ui.baiduai.clicked.connect(lambda: web('https://ai.baidu.com/tech/speech/tts'))
        self.ui.aliapi.clicked.connect(
            lambda: web('https://nls-portal.console.aliyun.com/applist',
                        'https://usercenter.console.aliyun.com/#/manage/ak'))
        self.ui.aliai.clicked.connect(lambda: web('https://ai.aliyun.com/nls/tts'))

        self.ui.save_bd.clicked.connect(self.save_bd)
        self.ui.save_ali.clicked.connect(self.save_ali)
        self.ui.file.clicked.connect(self.openfile)
        self.ui.file_ali.clicked.connect(self.openfile)
        self.ui.generate.clicked.connect(self.baidu_process)
        self.ui.generate_ali.clicked.connect(self.ali_process)
        self.load_setting()

        self.ui.spd_bd.valueChanged.connect(lambda: value_change(self.ui.spd_bd, self.ui.spd_spin_bd))
        self.ui.spd_spin_bd.valueChanged.connect(lambda: value_change(self.ui.spd_spin_bd, self.ui.spd_bd))
        self.ui.pit_bd.valueChanged.connect(lambda: value_change(self.ui.pit_bd, self.ui.pit_spin_bd))
        self.ui.pit_spin_bd.valueChanged.connect(lambda: value_change(self.ui.pit_spin_bd, self.ui.pit_bd))
        self.ui.vol_bd.valueChanged.connect(lambda: value_change(self.ui.vol_bd, self.ui.vol_spin_bd))
        self.ui.vol_spin_bd.valueChanged.connect(lambda: value_change(self.ui.vol_spin_bd, self.ui.vol_bd))

        self.ui.spd_ali.valueChanged.connect(lambda: value_change(self.ui.spd_ali, self.ui.spd_spin_ali))
        self.ui.spd_spin_ali.valueChanged.connect(lambda: value_change(self.ui.spd_spin_ali, self.ui.spd_ali))
        self.ui.pit_ali.valueChanged.connect(lambda: value_change(self.ui.pit_ali, self.ui.pit_spin_ali))
        self.ui.pit_spin_ali.valueChanged.connect(lambda: value_change(self.ui.pit_spin_ali, self.ui.pit_ali))
        self.ui.vol_ali.valueChanged.connect(lambda: value_change(self.ui.vol_ali, self.ui.vol_spin_ali))
        self.ui.vol_spin_ali.valueChanged.connect(lambda: value_change(self.ui.vol_spin_ali, self.ui.vol_ali))

    def note(self, info):
        QMessageBox.information(self.ui, "提示", info)

    def save_bd(self):
        app_id = self.ui.app_id_bd.text()
        app_key = self.ui.app_key_bd.text()
        secret_key = self.ui.secret_key_bd.text()
        baidu_setting = {'app_id': app_id, 'app_key': app_key, 'secret_key': secret_key}
        with open('setting.json', 'r+') as f:
            setting = json.load(f)
            setting['baidu'] = baidu_setting
            f.seek(0)
            f.truncate()
            json.dump(setting, f, indent=2)
            self.note('保存设置成功')

    def save_ali(self):
        app_key = self.ui.app_key_ali.text()
        access_key = self.ui.access_key_ali.text()
        access_key_secret = self.ui.access_key_secret_ali.text()
        ali_setting = {'app_key': app_key, 'access_key': access_key, 'access_key_secret': access_key_secret}
        with open('setting.json', 'r+') as f:
            setting = json.load(f)
            setting['ali'] = ali_setting
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
            ali_setting = setting.get('ali', {})

        self.ui.app_id_bd.setText(baidu_setting.get('app_id', ''))
        self.ui.app_key_bd.setText(baidu_setting.get('app_key', ''))
        self.ui.secret_key_bd.setText(baidu_setting.get('secret_key', ''))

        self.ui.app_key_ali.setText(ali_setting.get('app_key', ''))
        self.ui.access_key_ali.setText(ali_setting.get('access_key', ''))
        self.ui.access_key_secret_ali.setText(ali_setting.get('access_key_secret', ''))

    def openfile(self):
        file, _ = QFileDialog.getOpenFileName(self.ui, '选择字幕文件', './', "Srt File(*.srt)")
        if file:
            self.ui.file_path.setText(file)
            self.ui.file_path_ali.setText(file)

    def baidu_process(self):
        try:
            per = self.ui.per.checkedId()
            spd = self.ui.spd_bd.value()
            vol = self.ui.vol_bd.value()
            pit = self.ui.pit_bd.value()
            options = {'per': per, 'spd': spd, 'vol': vol, 'pit': pit}

            srt_file = self.ui.file_path.text()
            if not srt_file:
                self.note('未找到字幕文件')
                return
            with open(srt_file, encoding='utf-8') as sub:
                subtitle = list(srt.parse(sub))

            with open('setting.json', 'r') as ff:
                setting = json.load(ff)
                bd_setting = setting.get('baidu', {})

            file_path = os.path.dirname(srt_file)
            if not os.path.exists(f'{file_path}/audio/'):
                os.mkdir(f'{file_path}/audio/')
            audio = AudioSegment.silent(0)
            bf_end = 0
            step = 50 / len(subtitle)
            pbar = 0
            baidu = Baidu(bd_setting, options)
            for i in subtitle:
                file_name = f'{file_path}/audio/{i.index}-{i.content}.mp3'
                baidu.process(i.content, file_name)
                pbar += step
                self.ui.progressBar.setValue(pbar)
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

    # 直接复制粘贴上面的是不是不太优雅
    def ali_process(self):
        try:
            per = self.ui.per_ali.checkedButton().objectName()
            spd = self.ui.spd_ali.value()
            vol = self.ui.vol_ali.value()
            pit = self.ui.pit_ali.value()
            options = {'per': per, 'spd': spd, 'vol': vol, 'pit': pit}

            srt_file = self.ui.file_path_ali.text()
            if not srt_file:
                self.note('未找到字幕文件')
                return
            with open(srt_file, encoding='utf-8') as sub:
                subtitle = list(srt.parse(sub))

            with open('setting.json', 'r') as ff:
                setting = json.load(ff)
                ali_setting = setting.get('ali', {})

            file_path = os.path.dirname(srt_file)
            if not os.path.exists(f'{file_path}/audio/'):
                os.mkdir(f'{file_path}/audio/')
            audio = AudioSegment.silent(0)
            bf_end = 0
            step = 50 / len(subtitle)
            pbar = 0
            ali = Ali(ali_setting, options)
            for i in subtitle:
                pbar += step
                self.ui.progressBar_ali.setValue(pbar)
                file_name = f'{file_path}/audio/{i.index}-{i.content}.mp3'
                ali.process(i.content, file_name)
                pbar += step
                self.ui.progressBar_ali.setValue(pbar)
                silence_time = i.start.total_seconds() - bf_end
                silence_audio = AudioSegment.silent(silence_time * 1000)
                audio += silence_audio
                audio += AudioSegment.from_mp3(file_name)
                bf_end = audio.duration_seconds
            else:
                audio.export(f'{srt_file}.mp3', format='mp3')
                self.note("完成！输出文件在字幕文件夹下")
        except Exception as e:
            print(e)
            self.note(str(e))


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('static/logo.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
