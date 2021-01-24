import subprocess


class Bala:
    def __init__(self, service=None, language='zh-CN', gender=None):
        self.cmd = ['bal4web/bal4web.exe']
        if service is not None:
            ser = ['-s', f'{service}']
            self.cmd += ser
        if language is not None:
            lang = ['-l', f'{language}']
            self.cmd += lang
        if gender is not None:
            gen = ['-g', f'{gender}']
            self.cmd += gen

    def process(self, text, wav):
        wt = ['-w', f'{wav}', '-t', f'{text}']
        stdin = self.cmd + wt
        print(stdin)
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        subprocess.run(stdin, startupinfo=startupinfo)


if __name__ == "__main__":
    test = Bala(service='google', gender='female')
    test.process(text='今天好冷啊', wav='1.wav')
