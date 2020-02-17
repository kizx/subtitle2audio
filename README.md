# [subtitle2audio](https://github.com/kizx/subtitle2audio)

字幕朗读，由字幕生成音频 | Subtitle reading, generated audio from subtitles  
更多细节见[我的博客](https://www.2bboy.com/archives/151.html)

![](https://pan.2bboy.com/img/2020/02/0217145126.jpg)

## 使用

- 安装 ffmpeg

1. 下载解压[ffmpeg](https://ffmpeg.zeranoe.com/builds/)
2. 将解压的 ffmpeg/bin 路径添加到系统环境变量

- 安装依赖

  ```
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

- 启动  
  `flask run`  
   浏览器打开 http://127.0.0.1:5000/ 获取并填写相关 key 后点击生成，所有生成的文件在 output 文件夹内。

## 更新日志

v1.0 接入百度语音，命令行启动  
v1.1 引入 flask，添加 web 界面
