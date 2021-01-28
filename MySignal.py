from PySide2.QtCore import Signal, QObject


class MySignal(QObject):
    progress_update = Signal(int)
    drop_srt = Signal(str)
    drop_txt = Signal(str)


mysgn = MySignal()
