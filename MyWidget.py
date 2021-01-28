from PySide2.QtWidgets import QLineEdit, QPlainTextEdit

from MySignal import mysgn


class MyQLine(QLineEdit):
    """实现文件拖放功能"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().text().endswith('.srt'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        path = e.mimeData().text().replace('file:///', '')
        self.setText(path)


class MyQPlainTextEdit(QPlainTextEdit):
    """实现文件拖放功能"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().text().endswith('.srt'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        path = e.mimeData().text().replace('file:///', '')
        super().dropEvent(e)
        mysgn.drop_srt.emit(path)


class MyTXTLine(QLineEdit):
    """实现文件拖放功能"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().text().endswith('.txt'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        path = e.mimeData().text().replace('file:///', '')
        self.setText(path)


class MyTXText(QPlainTextEdit):
    """实现文件拖放功能"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().text().endswith('.txt'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        path = e.mimeData().text().replace('file:///', '')
        super().dropEvent(e)
        mysgn.drop_txt.emit(path)
