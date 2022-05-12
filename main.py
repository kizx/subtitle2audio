import json
import os
import threading
import time
import webbrowser

import srt
from PySide2.QtCore import Qt, QUrl
from PySide2.QtGui import QIcon, QDesktopServices
from PySide2.QtWidgets import *
from pydub import AudioSegment

from MySignal import mysgn
from ali import Ali
from baidu import Baidu
from mainwindow import Ui_MainWindow
from xfyun import XF
from azurepy import Azu

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


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 自定义信号
        self.sgn = mysgn
        self.sgn.drop_srt.connect(self.dropsrt)
        self.sgn.drop_txt.connect(self.droptxt)
        # 动态导入ui 自定义控件
        # loader = QUiLoader()
        # loader.registerCustomWidget(MyQLine)
        # loader.registerCustomWidget(MyQPlainTextEdit)
        # loader.registerCustomWidget(MyTXTLine)
        # loader.registerCustomWidget(MyTXText)
        # # self.ui = loader.load('mainwindow.ui')
        # 百度发音人id设置
        self.ui.per.setId(self.ui.per_0, 0)
        self.ui.per.setId(self.ui.per_1, 1)
        self.ui.per.setId(self.ui.per_3, 3)
        self.ui.per.setId(self.ui.per_4, 4)
        # 打开网页链接
        self.ui.baiduapi.clicked.connect(
            lambda: web('https://ai.baidu.com/tech/speech/tts'))
        self.ui.aliapi.clicked.connect(
            lambda: web('https://nls-portal.console.aliyun.com/applist',
                        'https://usercenter.console.aliyun.com/'))
        self.ui.aliai.clicked.connect(lambda: web('https://ai.aliyun.com/nls/tts'))
        self.ui.xfai.clicked.connect(lambda: web('https://www.xfyun.cn/services/online_tts'))
        self.ui.xfapi.clicked.connect(lambda: web('https://console.xfyun.cn/app/myapp'))
        self.ui.azuai.clicked.connect(lambda: web('https://azure.microsoft.com/zh-cn/services/cognitive-services/text-to-speech/?cdn=disable#overview'))
        self.ui.azuapi.clicked.connect(lambda: web('https://portal.azure.com/#home'))
        # 保存设置
        self.load_setting()
        self.ui.save_bd.clicked.connect(self.save_setting)
        self.ui.save_ali.clicked.connect(self.save_setting)
        self.ui.save_xf.clicked.connect(self.save_setting)
        self.ui.save_azu.clicked.connect(self.save_setting)
        # 字幕文件
        self.ui.open_srt.clicked.connect(self.opensrt)
        self.ui.edit_srt.clicked.connect(self.editsrt)
        self.ui.save_srt.clicked.connect(self.savesrt)
        self.ui.srt_path.textChanged.connect(self.preprocess)
        # TXT文件
        self.ui.open_txt.clicked.connect(self.opentxt)
        self.ui.edit_txt.clicked.connect(self.edittxt)
        self.ui.save_txt.clicked.connect(self.savetxt)
        self.ui.txt_path.textChanged.connect(self.pretxtprocess)
        # 下载合成
        self.ui.download.clicked.connect(self.download)
        self.ui.generate.clicked.connect(self.generate)
        # 菜单
        self.ui.opendir.triggered.connect(self.opendir)
        self.ui.about.triggered.connect(self.about)

        self.file_path = ''
        self.subtitle = []
        self.subtxt = []
        self.sub = []

    def note(self, info):
        QMessageBox.information(self, "提示", info)

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
            if sender.objectName() == 'save_xf':
                app_id = self.ui.app_id_xf.text()
                api_secret = self.ui.api_secret_xf.text()
                api_key = self.ui.api_key_xf.text()
                xf_setting = {'app_id': app_id, 'api_secret': api_secret, 'api_key': api_key}
                setting['xf'] = xf_setting
            if sender.objectName() == 'save_azu':
                azutoken = self.ui.azu_token.text()
                azuregion = self.ui.azu_region.text()                    
                azu_setting = {'token': azutoken, 'region': azuregion}
                setting['azu'] = azu_setting
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
            xf_setting = setting.get('xf', {})
            azu_setting = setting.get('azu', {})

        self.ui.app_id_bd.setText(baidu_setting.get('app_id', ''))
        self.ui.app_key_bd.setText(baidu_setting.get('app_key', ''))
        self.ui.secret_key_bd.setText(baidu_setting.get('secret_key', ''))

        self.ui.app_key_ali.setText(ali_setting.get('app_key', ''))
        self.ui.access_key_ali.setText(ali_setting.get('access_key', ''))
        self.ui.access_key_secret_ali.setText(ali_setting.get('access_key_secret', ''))

        self.ui.app_id_xf.setText(xf_setting.get('app_id', ''))
        self.ui.api_secret_xf.setText(xf_setting.get('api_secret', ''))
        self.ui.api_key_xf.setText(xf_setting.get('api_key', ''))
        
        self.ui.azu_token.setText(azu_setting.get('token', ''))
        self.ui.azu_region.setText(azu_setting.get('region', ''))


    def opensrt(self):
        """打开字幕文件路径"""
        file, _ = QFileDialog.getOpenFileName(self, '选择字幕文件', './', "Srt File(*.srt)")
        if file:
            self.ui.srt_path.setText(file)

    def dropsrt(self, path):
        """字幕文本拖放触发事件"""
        self.ui.srt_path.setText(path)

    def editsrt(self):
        """修改字幕"""
        self.subtitle = list(srt.parse(self.ui.srt_text.toPlainText()))
        self.note('修改成功！')

    def savesrt(self):
        """保存字幕"""
        with open(self.ui.srt_path.text(), 'w', encoding='utf-8') as f:
            f.write(self.ui.srt_text.toPlainText())
        self.note('保存字幕成功！')

    def opentxt(self):
        """打开TXT文件路径"""
        file, _ = QFileDialog.getOpenFileName(self, '选择字幕文件', './', "TXT File(*.txt)")
        if file:
            self.ui.txt_path.setText(file)

    def droptxt(self, path):
        """字幕文本拖放触发事件"""
        self.ui.txt_path.setText(path)

    def edittxt(self):
        """修改TXT"""
        self.subtxt = self.ui.txt_text.toPlainText().split('\n')
        self.note('修改成功！')

    def savetxt(self):
        """保存TXT"""
        with open(self.ui.txt_path.text(), 'w', encoding='utf-8') as f:
            f.write(self.ui.txt_text.toPlainText())
        self.note('保存TXT成功！')

    def opendir(self):
        """打开输出目录"""
        path = self.file_path
        if path:
            QDesktopServices.openUrl(QUrl('file:///' + path))
        else:
            self.note('未找到文件')

    def about(self):
        html = """<html><head><meta name="qrichtext" content="1" /><style type="text/css"> p, li { white-space: 
        pre-wrap; } </style></head><body style=" font-family:'SimSun'; font-size:9pt; font-weight:400; 
        font-style:normal;"> <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; 
        -qt-block-indent:0; text-indent:0px;">当前版本：V3.0.0</p> <p style=" margin-top:0px; margin-bottom:0px; 
        margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">开源地址：<a 
        href="https://github.com/kizx/subtitle2audio"><span style=" text-decoration: underline; 
        color:#0000ff;">https://github.com/kizx/subtitle2audio</span></a></p> <p style=" margin-top:0px; 
        margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">下载地址：<a 
        href="https://www.2bboy.com/archives/210.html"><span style=" text-decoration: underline; 
        color:#0000ff;">https://www.2bboy.com/archives/210.html</span></a></p></body></html> """
        QMessageBox.about(self, '关于', html)

    @trybug
    def preprocess(self):
        """字幕预处理"""
        srt_file = self.ui.srt_path.text()
        if not srt_file:
            self.note('未找到字幕文件')
            return 0
        with open(srt_file, encoding='utf-8') as sub:
            self.subtitle = list(srt.parse(sub))
            for index, i in enumerate(self.subtitle[:]):  # 删除空字幕块
                if i.content.isspace() or i.content == '':
                    self.subtitle.remove(i)
        self.ui.srt_text.setPlainText(srt.compose(self.subtitle))  # 显示字幕
        self.file_path = os.path.dirname(srt_file)
        if not os.path.exists(f'{self.file_path}/audio/'):
            os.mkdir(f'{self.file_path}/audio/')
        return 1

    def pretxtprocess(self):
        """TXT预处理"""
        txt_file = self.ui.txt_path.text()
        if not txt_file:
            self.note('未找到TXT文件')
            return 0
        with open(txt_file, encoding="utf-8") as f:
            lines = f.readlines()
        self.subtxt = []
        for line in lines:
            line = line.strip()
            if line:
                self.subtxt.append(line)
        self.ui.txt_text.setPlainText('\n'.join(self.subtxt))
        self.file_path = os.path.dirname(txt_file)
        if not os.path.exists(f'{self.file_path}/audio/'):
            os.mkdir(f'{self.file_path}/audio/')
        return 1

    @trybug
    def download(self):
        """下载"""
        start = time.perf_counter()
        sub_type = self.ui.subtab.currentIndex()
        if sub_type == 0:
            self.sub = [i.content for i in self.subtitle]
        elif sub_type == 1:
            self.sub = self.subtxt
        index = self.ui.tabWidget.currentIndex()
        if index == 0:
            self.baidu_process()
        elif index == 1:
            self.ali_process()
        elif index == 2:
            self.xf_process()
        elif index == 3:
            self.azu_process()
        end = time.perf_counter()
        self.note(f"完成！\n共计用时{round(end - start, 2)}秒")

    @trybug
    def generate(self):
        """合成"""
        start = time.perf_counter()
        index = self.ui.tabWidget.currentIndex()
        if index == 4:
            self.corn(wav=1)
        else:
            self.corn()
        end = time.perf_counter()
        self.note(f"完成！\n共计用时{round(end - start, 2)}秒")
        self.opendir()

    def corn(self, wav=0):
        file_path = self.file_path
        subtitle = self.sub
        audio = AudioSegment.silent(0)
        bf_end = 0

        self.statusBar().showMessage(f'正在操作中...')
        progress = QProgressDialog("正在操作...", "取消", 0, len(subtitle), self)
        progress.setWindowTitle("请稍等")
        progress.setMinimumDuration(0)
        progress.setWindowModality(Qt.WindowModal)

        for index, i in enumerate(subtitle):
            if progress.wasCanceled():
                QMessageBox.warning(self, "提示", "操作取消")
                break
            else:
                if wav == 0:
                    file_name = f'{file_path}/audio/{index + 1}.mp3'
                else:
                    file_name = f'{file_path}/audio/{index + 1}.wav'
                self.statusBar().showMessage(f'正在合并第{index + 1}句：{i}')
                if self.ui.subtab.currentIndex() == 0:
                    silence_time = self.subtitle[index].start.total_seconds() - bf_end
                elif self.ui.subtab.currentIndex() == 1:
                    silence_time = self.ui.silence_time.value()
                else:
                    silence_time = 1
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
            self.statusBar().showMessage('下载完成', 5000)

    def baidu_process(self):
        file_path = self.file_path
        subtitle = self.sub
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
            file_name = f'{file_path}/audio/{index + 1}.mp3'
            self.statusBar().showMessage(f'正在下载第{index + 1}句：{i}')
            baidu.process(i, file_name)

        self.statusBar().showMessage(f'下载完成！')

    def ali_process(self):
        file_path = self.file_path
        subtitle = self.sub
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
                file_name = f'{file_path}/audio/{index + 1}.mp3'
                self.statusBar().showMessage(f'正在下载第{index + 1}句：{i}')
                ali.process(i, file_name)

    def xf_process(self):
        file_path = self.file_path
        subtitle = self.sub
        per = self.ui.per_xf.checkedButton().objectName()
        if per == 'tsvcn':
            per = self.ui.xfvcn.text()
            if per == '':
                self.note('特色发音人参数为空')
                return
        spd = self.ui.spd_xf.value()
        vol = self.ui.vol_xf.value()
        pit = self.ui.pit_xf.value()
        options = {'per': per, 'spd': spd, 'vol': vol, 'pit': pit}

        with open('setting.json', 'r') as ff:
            setting = json.load(ff)
            xf_setting = setting.get('xf', {})

        xf = XF(xf_setting, options)
        for index, i in enumerate(subtitle):
            file_name = f'{file_path}/audio/{index + 1}.mp3'
            self.statusBar().showMessage(f'正在下载第{index + 1}句：{i}')
            xf.process(i, file_name)
        self.statusBar().showMessage(f'下载完成！')
        
    def azu_process(self):
        file_path = self.file_path
        subtitle = self.sub
        per = self.ui.per_azu.checkedButton().accessibleDescription()
        spd = self.ui.spd_azu.value()
        vol = self.ui.vol_azu.value()
        pit = self.ui.pit_azu.value()
        options = {'per': per, 'spd': spd, 'vol': vol, 'pit': pit}

        with open('setting.json', 'r') as ff:
             setting = json.load(ff)
             azu_setting = setting.get('azu', {})

        azu = Azu(azu_setting, options)
        is_multi = self.ui.azu_multi.isChecked()
        if is_multi:  # 多线程
            sleeptime = self.ui.sleeptime_2.value()
            self.process_multithread(azu, subtitle, f'{file_path}/audio/', sleeptime=sleeptime)
        else:  # 单线程
            for index, i in enumerate(subtitle):
                 file_name = f'{file_path}/audio/{index + 1}.mp3'
                 self.statusBar().showMessage(f'正在下载第{index + 1}句：{i}')
                 azu.process(i, file_name)
        self.statusBar().showMessage(f'下载完成！')
    # def bal_process(self):
    #     file_path = self.file_path
    #     subtitle = self.sub
    #     service = self.ui.service.checkedButton().property('service')
    #     gender = self.ui.gender.checkedButton().objectName()
    #     language = self.ui.language.checkedButton().property('language')
    #     bala = Bala(service=service, language=language, gender=gender)
    #     is_multi = self.ui.bal_multi.isChecked()
    #     if is_multi:
    #         self.process_multithread(bala, subtitle, f'{file_path}/audio/', sleeptime=0.2, wav=1)
    #     else:
    #         for index, i in enumerate(subtitle):
    #             file_name = f'{file_path}/audio/{index + 1}.wav'
    #             self.ui.statusBar().showMessage(f'正在下载第{index + 1}句：{i}')
    #             bala.process(i, file_name)

    def setprogress(self, value):
        self.progress.setValue(value)

    def process_multithread(self, api, sub, name, sleeptime=1.0, wav=0):
        self.progress = QProgressDialog("正在下载语音文件...", "取消", 0, len(sub), self)
        self.progress.setWindowTitle("下载中")
        self.progress.setMinimumDuration(0)
        self.progress.setWindowModality(Qt.WindowModal)
        self.sgn.progress_update.connect(self.setprogress)
        thread_list = []
        for index, i in enumerate(sub):
            if self.progress.wasCanceled():
                QMessageBox.warning(self, "提示", "操作取消")
                return 0
            if wav:
                audio_name = f"{name}{index + 1}.wav"
            else:
                audio_name = f"{name}{index + 1}.mp3"
            thread = threading.Thread(target=api.process, args=(i, audio_name))
            self.statusBar().showMessage(f'正在下载第{index + 1}句：{i}')
            thread_list.append(thread)
            thread.start()
            time.sleep(sleeptime)  # 限制请求频率
            self.sgn.progress_update.emit(index + 1)
        for index, thread in enumerate(thread_list):
            self.sgn.progress_update.emit(index + 1)
            thread.join()


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('static/logo.png'))
    mainwindow = MainWindow()
    mainwindow.show()
    app.exec_()
