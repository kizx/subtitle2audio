import json
import os
import webbrowser
import time
import threading

import srt
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QLineEdit, QProgressDialog
from PySide2.QtCore import Qt, Signal, QObject
from pydub import AudioSegment

from ali import Ali
from baidu import Baidu


def web(*url):
    for i in url:
        webbrowser.open(i)


def value_change(obj1, obj2):
    obj2.setValue(obj1.value())


class MyQLine(QLineEdit):
    """实现文件拖放功能"""

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().text().endswith('.srt'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        path = e.mimeData().text().replace('file:///', '')
        self.setText(path)


class Stats(QObject):

    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('static/main.ui')

        self.ui.file_path.deleteLater()  # 删除原有的路径框
        self.ui.file_path = MyQLine()  # 新建自己的替换原有的
        self.ui.file_path.setPlaceholderText('浏览或拖拽SRT字幕文件到这里')
        self.ui.horizontalLayout_2.addWidget(self.ui.file_path)
        self.ui.horizontalLayout_2.addWidget(self.ui.file)

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

        self.load_setting()
        self.ui.save_bd.clicked.connect(self.save_setting)
        self.ui.save_ali.clicked.connect(self.save_setting)
        self.ui.file.clicked.connect(self.openfile)
        self.ui.generate.clicked.connect(self.generate)

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

    def save_setting(self):
        sender = self.sender()
        with open('setting.json', 'r+') as f:
            setting = json.load(f)
            if sender.objectName() == 'save_bd':
                app_id = self.ui.app_id_bd.text()
                app_key = self.ui.app_key_bd.text()
                secret_key = self.ui.secret_key_bd.text()
                baidu_setting = {'app_id': app_id, 'app_key': app_key, 'secret_key': secret_key}
                setting['baidu'] = baidu_setting
            if sender.objectName() == 'save_ali':
                app_key = self.ui.app_key_ali.text()
                access_key = self.ui.access_key_ali.text()
                access_key_secret = self.ui.access_key_secret_ali.text()
                ali_setting = {'app_key': app_key, 'access_key': access_key, 'access_key_secret': access_key_secret}
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

    def generate(self):
        try:
            srt_file = self.ui.file_path.text()
            if not srt_file:
                self.note('未找到字幕文件')
                return
            with open(srt_file, encoding='utf-8') as sub:
                subtitle = list(srt.parse(sub))
            file_path = os.path.dirname(srt_file)
            if not os.path.exists(f'{file_path}/audio/'):
                os.mkdir(f'{file_path}/audio/')

            start = time.perf_counter()
            index = self.ui.tabWidget.currentIndex()
            if index == 0:
                self.baidu_process(file_path, subtitle)
            elif index == 1:
                self.ali_process(file_path, subtitle)
            end = time.perf_counter()
            self.note(f"完成！\n共计用时{round(end - start, 2)}秒")
        except Exception as e:
            print(e)
            self.note(str(e))

    def corn(self, api, file_path, subtitle, flag=0):
        audio = AudioSegment.silent(0)
        bf_end = 0

        progress = QProgressDialog("正在操作...", "取消", 0, len(subtitle), self.ui)
        progress.setWindowTitle("请稍等")
        progress.setMinimumDuration(0)
        progress.setWindowModality(Qt.WindowModal)

        for index, i in enumerate(subtitle):
            if progress.wasCanceled():
                QMessageBox.warning(self.ui, "提示", "操作取消")
                break
            else:
                file_name = f'{file_path}/audio/{i.index}.mp3'
                if flag == 0:
                    api.process(i.content, file_name)
                silence_time = i.start.total_seconds() - bf_end
                silence_audio = AudioSegment.silent(silence_time * 1000)
                audio += silence_audio
                audio += AudioSegment.from_mp3(file_name)
                bf_end = audio.duration_seconds
                progress.setValue(index + 1)
        else:
            audio.export(f'{file_path}/输出.mp3', format='mp3')

    def baidu_process(self, file_path, subtitle):
        per = self.ui.per.checkedId()
        spd = self.ui.spd_bd.value()
        vol = self.ui.vol_bd.value()
        pit = self.ui.pit_bd.value()
        options = {'per': per, 'spd': spd, 'vol': vol, 'pit': pit}

        with open('setting.json', 'r') as ff:
            setting = json.load(ff)
            bd_setting = setting.get('baidu', {})

        baidu = Baidu(bd_setting, options)
        self.corn(baidu, file_path, subtitle)

    def ali_process(self, file_path, subtitle):
        per = self.ui.per_ali.checkedButton().objectName()
        spd = self.ui.spd_ali.value()
        vol = self.ui.vol_ali.value()
        pit = self.ui.pit_ali.value()
        options = {'per': per, 'spd': spd, 'vol': vol, 'pit': pit}

        with open('setting.json', 'r') as ff:
            setting = json.load(ff)
            ali_setting = setting.get('ali', {})

        ali = Ali(ali_setting, options)
        sub = [i.content for i in subtitle]
        self.progress = QProgressDialog("正在下载语音文件...", "请稍等", 0, 2 * len(sub), self.ui)
        self.progress.setWindowTitle("操作中")
        self.progress.setMinimumDuration(0)
        self.progress.setWindowModality(Qt.WindowModal)
        self.sgn = MySignal()
        self.sgn.progress_update.connect(self.setprogress)
        ali.process_multithread(sub, f'{file_path}/audio/', self.sgn)
        self.corn(ali, file_path, subtitle, flag=1)

    def setprogress(self, value):
        self.progress.setValue(value)


class MySignal(QObject):
    progress_update = Signal(int)


if __name__ == '__main__':
    app = QApplication()
    app.setWindowIcon(QIcon('static/logo.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
