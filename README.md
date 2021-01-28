# [subtitle2audio](https://github.com/kizx/subtitle2audio)

字幕朗读，由字幕或文本生成语音 | Subtitle reading, generated audio from subtitles  
更多说明见 [我的博客](https://www.2bboy.com/archives/210.html)

![](https://www.2bboy.com/usr/uploads/2021/01/2091177316.png)

## 使用

[下载地址](https://github.com/kizx/subtitle2audio/releases)  
使用前需自行注册获取相关密钥

## 打包

pydub库修改`audio_segment.py`和`utils.py`中subprocess.Popen()参数

```
shell=True, stdin=subprocess.PIPE
```

打包命令

```
pyinstaller -w -F -i ./static/logo.ico -n 字幕朗读器 main.py
```

## 更新日志

v1.0 接入百度语音，命令行启动  
v1.1 引入 flask，添加 web 界面  
v2.0 使用qt界面  
v2.1 添加阿里云语音接口  
v2.2 修复无响应假死，阿里云改用多线程  
v2.4 添加新的语音库  
v3.0 添加TXT文本转换，修复阿里云语音，添加讯飞云语音，删除bal语音
