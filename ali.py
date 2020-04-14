import json
import threading
import time

import ali_speech
from ali_speech.callbacks import SpeechSynthesizerCallback
from ali_speech.constant import TTSFormat
from ali_speech.constant import TTSSampleRate


class MyCallback(SpeechSynthesizerCallback):
    # 参数name用于指定保存音频的文件
    def __init__(self, name):
        self._name = name
        self._fout = open(name, 'wb')

    def on_binary_data_received(self, raw):
        print('MyCallback.on_binary_data_received: %s' % len(raw))
        self._fout.write(raw)

    def on_completed(self, message):
        print('MyCallback.OnRecognitionCompleted: %s' % message)
        self._fout.close()

    def on_task_failed(self, message):
        print('MyCallback.OnRecognitionTaskFailed-task_id:%s, status_text:%s' % (
            message['header']['task_id'], message['header']['status_text']))
        self._fout.close()

    def on_channel_closed(self):
        print('MyCallback.OnRecognitionChannelClosed')


class Ali:
    def __init__(self, ali_setting, options=None):
        self.client = ali_speech.NlsClient()
        # 设置输出日志信息的级别：DEBUG、INFO、WARNING、ERROR
        self.client.set_log_level('ERROR')
        self.setting = ali_setting
        self.options = options
        ali_speech.NlsClient.set_log_level('ERROR')
        self.token, expire_time = ali_speech.NlsClient.create_token(self.setting.get('access_key'),
                                                                    self.setting.get('access_key_secret'))

    def process(self, text, audio_name):
        callback = MyCallback(audio_name)
        synthesizer = self.client.create_synthesizer(callback)
        synthesizer.set_appkey(self.setting.get('app_key'))
        synthesizer.set_token(self.token)
        synthesizer.set_format(TTSFormat.MP3)
        synthesizer.set_sample_rate(TTSSampleRate.SAMPLE_RATE_16K)
        if self.options is not None:
            synthesizer.set_voice(self.options.get('per'))
            synthesizer.set_speech_rate(self.options.get('spd'))
            synthesizer.set_pitch_rate(self.options.get('pit'))
            synthesizer.set_volume(self.options.get('vol'))
        synthesizer.set_text(text)
        try:
            ret = synthesizer.start()
            if ret < 0:
                return ret
            synthesizer.wait_completed()
        except Exception as e:
            print(e)
        finally:
            synthesizer.close()

    def process_multithread(self, sub, name, sgn=None, sleeptime=1):
        thread_list = []
        for index, i in enumerate(sub):
            audio_name = f"{name}{index + 1}.mp3"
            thread = threading.Thread(target=self.process, args=(i, audio_name))
            thread_list.append(thread)
            thread.start()
            time.sleep(sleeptime)  # 阿里限制请求频率
            if sgn:
                sgn.progress_update.emit(index + 1)
        num = len(sub)
        for thread in thread_list:
            thread.join()
            if sgn:
                num += 1
                sgn.progress_update.emit(num)


if __name__ == "__main__":
    with open('setting.json', 'r') as ff:
        setting = json.load(ff)
        ali_st = setting.get('ali', {})
    my_text = "今天天气不错"
    my_audio_name = '阿里语音.mp3'
    ali = Ali(ali_st)
    ali.process(my_text, my_audio_name)
    # ali.process_multithread(['这是第一句', '今天天气不错', '嘟嘟嘟嘟'], 'audio/')
