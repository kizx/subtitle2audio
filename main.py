import json
import os
import threading
import time
import webbrowser

import srt
from PySide2.QtCore import Qt, Signal, QObject, QUrl
from PySide2.QtGui import QIcon, QDesktopServices
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QProgressDialog
from pydub import AudioSegment

from MyWidget import MyQLine
from ali import Ali
from baidu import Baidu
from bala import Bala


def web(*url):
    for i in url:
        webbrowser.open(i)


def trybug(fun):
    def wrapped(self):
        try:
            fun(self)
        except Exception as e:
            print('错误：', e)
            self.note(str(e))

    return wrapped


class MainWindow(QObject):

    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        loader.registerCustomWidget(MyQLine)
        self.ui = loader.load('mainwindow.ui')

        self.ui.per.setId(self.ui.per_0, 0)
        self.ui.per.setId(self.ui.per_1, 1)
        self.ui.per.setId(self.ui.per_3, 3)
        self.ui.per.setId(self.ui.per_4, 4)

        self.ui.baiduapi.clicked.connect(
            lambda: web('https://ai.baidu.com/tech/speech/tts'))
        self.ui.baiduai.clicked.connect(lambda: web('https://developer.baidu.com/vcast'))
        self.ui.aliapi.clicked.connect(
            lambda: web('https://nls-portal.console.aliyun.com/applist',
                        'https://usercenter.console.aliyun.com/#/manage/ak'))
        self.ui.aliai.clicked.connect(lambda: web('https://ai.aliyun.com/nls/tts'))

        self.load_setting()
        self.ui.save_bd.clicked.connect(self.save_setting)
        self.ui.save_ali.clicked.connect(self.save_setting)
        self.ui.file.clicked.connect(self.openfile)
        self.ui.download.clicked.connect(self.download)
        self.ui.generate.clicked.connect(self.generate)

        self.ui.openfile.triggered.connect(self.openfile)
        self.ui.opensrt.triggered.connect(self.opensrt)
        self.ui.opendir.triggered.connect(self.opendir)
        self.ui.about.triggered.connect(self.about)

        self.file_path = ''
        self.subtitle = ''

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

    def opensrt(self):
        path = self.ui.file_path.text()
        if path:
            QDesktopServices.openUrl(QUrl('file:///' + path))
        else:
            self.note('未找到字幕文件')

    def opendir(self):
        path = self.ui.file_path.text()
        file_path = os.path.dirname(path)
        if file_path:
            QDesktopServices.openUrl(QUrl('file:///' + file_path))
        else:
            self.note('未找到文件')

    def about(self):
        html = """<html><head><meta name="qrichtext" content="1" /><style type="text/css"> p, li { white-space: 
        pre-wrap; } </style></head><body style=" font-family:'SimSun'; font-size:9pt; font-weight:400; 
        font-style:normal;"> <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; 
        -qt-block-indent:0; text-indent:0px;">当前版本：V2.4.2</p> <p style=" margin-top:0px; margin-bottom:0px; 
        margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">开源地址：<a 
        href="https://github.com/kizx/subtitle2audio"><span style=" text-decoration: underline; 
        color:#0000ff;">https://github.com/kizx/subtitle2audio</span></a></p> <p style=" margin-top:0px; 
        margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">下载地址：<a 
        href="https://www.2bboy.com/archives/151.html"><span style=" text-decoration: underline; 
        color:#0000ff;">https://www.2bboy.com/archives/151.html</span></a></p></body></html> """
        QMessageBox.about(self.ui, '关于', html)

    def preprocess(self):
        """字幕预处理"""
        srt_file = self.ui.file_path.text()
        if not srt_file:
            self.note('未找到字幕文件')
            return 0
        with open(srt_file, encoding='utf-8') as sub:
            self.subtitle = list(srt.parse(sub))
            for index, i in enumerate(self.subtitle[:]):  # 删除空字幕块
                if i.content.isspace() or i.content == '':
                    self.subtitle.remove(i)
        self.file_path = os.path.dirname(srt_file)
        if not os.path.exists(f'{self.file_path}/audio/'):
            os.mkdir(f'{self.file_path}/audio/')
        return 1

    @trybug
    def download(self):
        ok = self.preprocess()
        if not ok:
            return
        start = time.perf_counter()
        index = self.ui.tabWidget.currentIndex()
        if index == 0:
            self.baidu_process()
        elif index == 1:
            self.ali_process()
        elif index == 2:
            self.bal_process()
        end = time.perf_counter()
        self.note(f"完成！\n共计用时{round(end - start, 2)}秒")

    @trybug
    def generate(self):
        ok = self.preprocess()
        if not ok:
            return
        start = time.perf_counter()
        index = self.ui.tabWidget.currentIndex()
        if index == 2:
            self.corn(wav=1)
        else:
            self.corn()
        end = time.perf_counter()
        self.note(f"完成！\n共计用时{round(end - start, 2)}秒")

    def corn(self, wav=0):
        file_path = self.file_path
        subtitle = self.subtitle
        audio = AudioSegment.silent(0)
        bf_end = 0

        self.ui.statusBar().showMessage(f'正在操作中...')
        progress = QProgressDialog("正在操作...", "取消", 0, len(subtitle), self.ui)
        progress.setWindowTitle("请稍等")
        progress.setMinimumDuration(0)
        progress.setWindowModality(Qt.WindowModal)

        for index, i in enumerate(subtitle):
            if progress.wasCanceled():
                QMessageBox.warning(self.ui, "提示", "操作取消")
                break
            else:
                if wav == 0:
                    file_name = f'{file_path}/audio/{i.index}.mp3'
                else:
                    file_name = f'{file_path}/audio/{i.index}.wav'
                self.ui.statusBar().showMessage(f'正在合并第{i.index}句：{i.content}')
                silence_time = i.start.total_seconds() - bf_end
                silence_audio = AudioSegment.silent(silence_time * 1000)
                audio += silence_audio
                if wav == 0:
                    audio += AudioSegment.from_mp3(file_name)
                else:
                    audio += AudioSegment.from_wav(file_name)
                bf_end = audio.duration_seconds
                progress.setValue(index + 1)
        else:
            if wav == 0:
                audio.export(f'{file_path}/输出.mp3', format='mp3')
            else:
                audio.export(f'{file_path}/输出.wav', format='wav')
            self.ui.statusBar().showMessage('下载完成', 5000)

    def baidu_process(self):
        file_path = self.file_path
        subtitle = self.subtitle
        per = self.ui.per.checkedId()
        spd = self.ui.spd_bd.value()
        vol = self.ui.vol_bd.value()
        pit = self.ui.pit_bd.value()
        options = {'per': per, 'spd': spd, 'vol': vol, 'pit': pit}

        with open('setting.json', 'r') as ff:
            setting = json.load(ff)
            bd_setting = setting.get('baidu', {})

        baidu = Baidu(bd_setting, options)
        for index, i in enumerate(subtitle):
            file_name = f'{file_path}/audio/{i.index}.mp3'
            self.ui.statusBar().showMessage(f'正在下载第{i.index}句：{i.content}')
            baidu.process(i.content, file_name)

    def ali_process(self):
        file_path = self.file_path
        subtitle = self.subtitle
        per = self.ui.per_ali.checkedButton().objectName()
        spd = self.ui.spd_ali.value()
        vol = self.ui.vol_ali.value()
        pit = self.ui.pit_ali.value()
        options = {'per': per, 'spd': spd, 'vol': vol, 'pit': pit}

        with open('setting.json', 'r') as ff:
            setting = json.load(ff)
            ali_setting = setting.get('ali', {})

        ali = Ali(ali_setting, options)
        is_multi = self.ui.ali_multi.isChecked()
        if is_multi:  # 多线程
            sleeptime = self.ui.sleeptime.value()
            self.process_multithread(ali, subtitle, f'{file_path}/audio/', sleeptime=sleeptime)
        else:  # 单线程
            for index, i in enumerate(subtitle):
                file_name = f'{file_path}/audio/{i.index}.mp3'
                self.ui.statusBar().showMessage(f'正在下载第{i.index}句：{i.content}')
                ali.process(i.content, file_name)

    def bal_process(self):
        file_path = self.file_path
        subtitle = self.subtitle
        service = self.ui.service.checkedButton().property('service')
        gender = self.ui.gender.checkedButton().objectName()
        language = self.ui.language.checkedButton().property('language')
        bala = Bala(service=service, language=language, gender=gender)
        is_multi = self.ui.bal_multi.isChecked()
        if is_multi:
            self.process_multithread(bala, subtitle, f'{file_path}/audio/', sleeptime=0.2, wav=1)
        else:
            for index, i in enumerate(subtitle):
                file_name = f'{file_path}/audio/{i.index}.wav'
                self.ui.statusBar().showMessage(f'正在下载第{i.index}句：{i.content}')
                bala.process(i.content, file_name)

    def setprogress(self, value):
        self.progress.setValue(value)

    def process_multithread(self, api, sub, name, sleeptime=1.0, wav=0):
        self.progress = QProgressDialog("正在下载语音文件...", "取消", 0, len(sub), self.ui)
        self.progress.setWindowTitle("下载中")
        self.progress.setMinimumDuration(0)
        self.progress.setWindowModality(Qt.WindowModal)
        self.sgn = MySignal()
        self.sgn.progress_update.connect(self.setprogress)
        thread_list = []
        for index, i in enumerate(sub):
            if self.progress.wasCanceled():
                QMessageBox.warning(self.ui, "提示", "操作取消")
                return 0
            if wav:
                audio_name = f"{name}{i.index}.wav"
            else:
                audio_name = f"{name}{i.index}.mp3"
            thread = threading.Thread(target=api.process, args=(i.content, audio_name))
            self.ui.statusBar().showMessage(f'正在下载第{i.index}句：{i.content}')
            thread_list.append(thread)
            thread.start()
            time.sleep(sleeptime)  # 限制请求频率
            self.sgn.progress_update.emit(index + 1)
        for index, thread in enumerate(thread_list):
            self.sgn.progress_update.emit(index + 1)
            thread.join()


class MySignal(QObject):
    progress_update = Signal(int)


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('static/logo.png'))
    mainwindow = MainWindow()
    mainwindow.ui.show()
    app.exec_()
