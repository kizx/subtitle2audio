# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from MyWidget import MyQLine
from MyWidget import MyQPlainTextEdit
from MyWidget import MyTXTLine
from MyWidget import MyTXText


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1097, 611)
        self.openfile = QAction(MainWindow)
        self.openfile.setObjectName(u"openfile")
        self.about = QAction(MainWindow)
        self.about.setObjectName(u"about")
        self.opensrt = QAction(MainWindow)
        self.opensrt.setObjectName(u"opensrt")
        self.opendir = QAction(MainWindow)
        self.opendir.setObjectName(u"opendir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_20 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.subtab = QTabWidget(self.groupBox)
        self.subtab.setObjectName(u"subtab")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_14 = QVBoxLayout(self.tab_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, -1, -1, -1)
        self.label_3 = QLabel(self.tab_9)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.srt_path = MyQLine(self.tab_9)
        self.srt_path.setObjectName(u"srt_path")
        self.srt_path.setMinimumSize(QSize(0, 25))
        self.srt_path.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.srt_path)

        self.open_srt = QToolButton(self.tab_9)
        self.open_srt.setObjectName(u"open_srt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.open_srt.sizePolicy().hasHeightForWidth())
        self.open_srt.setSizePolicy(sizePolicy1)
        self.open_srt.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_2.addWidget(self.open_srt)


        self.verticalLayout_14.addLayout(self.horizontalLayout_2)

        self.srt_text = MyQPlainTextEdit(self.tab_9)
        self.srt_text.setObjectName(u"srt_text")
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(10)
        self.srt_text.setFont(font)

        self.verticalLayout_14.addWidget(self.srt_text)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.edit_srt = QPushButton(self.tab_9)
        self.edit_srt.setObjectName(u"edit_srt")
        self.edit_srt.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_21.addWidget(self.edit_srt)

        self.save_srt = QPushButton(self.tab_9)
        self.save_srt.setObjectName(u"save_srt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.save_srt.sizePolicy().hasHeightForWidth())
        self.save_srt.setSizePolicy(sizePolicy2)
        self.save_srt.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_21.addWidget(self.save_srt)


        self.verticalLayout_14.addLayout(self.horizontalLayout_21)

        self.subtab.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.verticalLayout_15 = QVBoxLayout(self.tab_10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(5, -1, -1, -1)
        self.label_14 = QLabel(self.tab_10)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_22.addWidget(self.label_14)

        self.txt_path = MyTXTLine(self.tab_10)
        self.txt_path.setObjectName(u"txt_path")
        self.txt_path.setMinimumSize(QSize(0, 25))
        self.txt_path.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.txt_path)

        self.open_txt = QToolButton(self.tab_10)
        self.open_txt.setObjectName(u"open_txt")
        sizePolicy1.setHeightForWidth(self.open_txt.sizePolicy().hasHeightForWidth())
        self.open_txt.setSizePolicy(sizePolicy1)
        self.open_txt.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_22.addWidget(self.open_txt)


        self.verticalLayout_15.addLayout(self.horizontalLayout_22)

        self.txt_text = MyTXText(self.tab_10)
        self.txt_text.setObjectName(u"txt_text")
        self.txt_text.setFont(font)

        self.verticalLayout_15.addWidget(self.txt_text)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, -1, 10, -1)
        self.label_19 = QLabel(self.tab_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_19)

        self.silence_time = QDoubleSpinBox(self.tab_10)
        self.silence_time.setObjectName(u"silence_time")
        sizePolicy1.setHeightForWidth(self.silence_time.sizePolicy().hasHeightForWidth())
        self.silence_time.setSizePolicy(sizePolicy1)
        self.silence_time.setMinimumSize(QSize(80, 25))
        self.silence_time.setDecimals(1)
        self.silence_time.setSingleStep(0.100000000000000)
        self.silence_time.setValue(1.000000000000000)

        self.horizontalLayout_24.addWidget(self.silence_time)

        self.label_20 = QLabel(self.tab_10)
        self.label_20.setObjectName(u"label_20")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy3)

        self.horizontalLayout_24.addWidget(self.label_20)


        self.verticalLayout_15.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.edit_txt = QPushButton(self.tab_10)
        self.edit_txt.setObjectName(u"edit_txt")
        self.edit_txt.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_23.addWidget(self.edit_txt)

        self.save_txt = QPushButton(self.tab_10)
        self.save_txt.setObjectName(u"save_txt")
        sizePolicy2.setHeightForWidth(self.save_txt.sizePolicy().hasHeightForWidth())
        self.save_txt.setSizePolicy(sizePolicy2)
        self.save_txt.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_23.addWidget(self.save_txt)


        self.verticalLayout_15.addLayout(self.horizontalLayout_23)

        self.subtab.addTab(self.tab_10, "")

        self.verticalLayout_5.addWidget(self.subtab)


        self.horizontalLayout_20.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tabWidget = QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy4)
        self.tabWidget.setAcceptDrops(False)
        self.baidu = QWidget()
        self.baidu.setObjectName(u"baidu")
        self.verticalLayout_3 = QVBoxLayout(self.baidu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_4 = QGroupBox(self.baidu)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout = QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.lable_app_id = QLabel(self.groupBox_4)
        self.lable_app_id.setObjectName(u"lable_app_id")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lable_app_id)

        self.app_id_bd = QLineEdit(self.groupBox_4)
        self.app_id_bd.setObjectName(u"app_id_bd")
        self.app_id_bd.setClearButtonEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.app_id_bd)

        self.lable_app_key = QLabel(self.groupBox_4)
        self.lable_app_key.setObjectName(u"lable_app_key")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lable_app_key)

        self.app_key_bd = QLineEdit(self.groupBox_4)
        self.app_key_bd.setObjectName(u"app_key_bd")
        self.app_key_bd.setClearButtonEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.app_key_bd)

        self.lable_secret_key = QLabel(self.groupBox_4)
        self.lable_secret_key.setObjectName(u"lable_secret_key")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lable_secret_key)

        self.secret_key_bd = QLineEdit(self.groupBox_4)
        self.secret_key_bd.setObjectName(u"secret_key_bd")
        self.secret_key_bd.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.secret_key_bd.setClearButtonEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.secret_key_bd)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.baiduapi = QPushButton(self.groupBox_4)
        self.baiduapi.setObjectName(u"baiduapi")
        sizePolicy1.setHeightForWidth(self.baiduapi.sizePolicy().hasHeightForWidth())
        self.baiduapi.setSizePolicy(sizePolicy1)
        self.baiduapi.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.baiduapi)

        self.save_bd = QPushButton(self.groupBox_4)
        self.save_bd.setObjectName(u"save_bd")
        sizePolicy1.setHeightForWidth(self.save_bd.sizePolicy().hasHeightForWidth())
        self.save_bd.setSizePolicy(sizePolicy1)
        self.save_bd.setMinimumSize(QSize(100, 30))
        self.save_bd.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.save_bd)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.person = QGroupBox(self.baidu)
        self.person.setObjectName(u"person")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.person.sizePolicy().hasHeightForWidth())
        self.person.setSizePolicy(sizePolicy5)
        self.horizontalLayout_5 = QHBoxLayout(self.person)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.per_1 = QRadioButton(self.person)
        self.per = QButtonGroup(MainWindow)
        self.per.setObjectName(u"per")
        self.per.addButton(self.per_1)
        self.per_1.setObjectName(u"per_1")
        self.per_1.setChecked(True)

        self.horizontalLayout_5.addWidget(self.per_1)

        self.per_0 = QRadioButton(self.person)
        self.per.addButton(self.per_0)
        self.per_0.setObjectName(u"per_0")
        self.per_0.setChecked(False)

        self.horizontalLayout_5.addWidget(self.per_0)

        self.per_3 = QRadioButton(self.person)
        self.per.addButton(self.per_3)
        self.per_3.setObjectName(u"per_3")

        self.horizontalLayout_5.addWidget(self.per_3)

        self.per_4 = QRadioButton(self.person)
        self.per.addButton(self.per_4)
        self.per_4.setObjectName(u"per_4")

        self.horizontalLayout_5.addWidget(self.per_4)


        self.verticalLayout_3.addWidget(self.person)

        self.groupBox_3 = QGroupBox(self.baidu)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_5)

        self.spd_bd = QSlider(self.groupBox_3)
        self.spd_bd.setObjectName(u"spd_bd")
        self.spd_bd.setMaximum(9)
        self.spd_bd.setValue(5)
        self.spd_bd.setOrientation(Qt.Horizontal)
        self.spd_bd.setTickPosition(QSlider.TicksBothSides)

        self.horizontalLayout_14.addWidget(self.spd_bd)

        self.spd_spin_bd = QSpinBox(self.groupBox_3)
        self.spd_spin_bd.setObjectName(u"spd_spin_bd")
        self.spd_spin_bd.setMinimumSize(QSize(45, 0))
        self.spd_spin_bd.setMaximum(9)
        self.spd_spin_bd.setValue(5)

        self.horizontalLayout_14.addWidget(self.spd_spin_bd)


        self.verticalLayout_11.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy6)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_6)

        self.pit_bd = QSlider(self.groupBox_3)
        self.pit_bd.setObjectName(u"pit_bd")
        self.pit_bd.setMaximum(9)
        self.pit_bd.setValue(5)
        self.pit_bd.setOrientation(Qt.Horizontal)
        self.pit_bd.setTickPosition(QSlider.TicksBothSides)

        self.horizontalLayout_15.addWidget(self.pit_bd)

        self.pit_spin_bd = QSpinBox(self.groupBox_3)
        self.pit_spin_bd.setObjectName(u"pit_spin_bd")
        self.pit_spin_bd.setMinimumSize(QSize(45, 0))
        self.pit_spin_bd.setMaximum(9)
        self.pit_spin_bd.setValue(5)

        self.horizontalLayout_15.addWidget(self.pit_spin_bd)


        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_16.addWidget(self.label_7)

        self.vol_bd = QSlider(self.groupBox_3)
        self.vol_bd.setObjectName(u"vol_bd")
        self.vol_bd.setMaximum(15)
        self.vol_bd.setPageStep(10)
        self.vol_bd.setValue(5)
        self.vol_bd.setOrientation(Qt.Horizontal)
        self.vol_bd.setTickPosition(QSlider.TicksBothSides)

        self.horizontalLayout_16.addWidget(self.vol_bd)

        self.vol_spin_bd = QSpinBox(self.groupBox_3)
        self.vol_spin_bd.setObjectName(u"vol_spin_bd")
        self.vol_spin_bd.setMinimumSize(QSize(45, 0))
        self.vol_spin_bd.setMaximum(15)
        self.vol_spin_bd.setValue(5)

        self.horizontalLayout_16.addWidget(self.vol_spin_bd)


        self.verticalLayout_11.addLayout(self.horizontalLayout_16)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.baidu, "")
        self.ali = QWidget()
        self.ali.setObjectName(u"ali")
        self.verticalLayout_4 = QVBoxLayout(self.ali)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_6 = QGroupBox(self.ali)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setLabelAlignment(Qt.AlignCenter)
        self.lable_app_id_2 = QLabel(self.groupBox_6)
        self.lable_app_id_2.setObjectName(u"lable_app_id_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lable_app_id_2)

        self.app_key_ali = QLineEdit(self.groupBox_6)
        self.app_key_ali.setObjectName(u"app_key_ali")
        self.app_key_ali.setClearButtonEnabled(False)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.app_key_ali)

        self.access_key_ali = QLineEdit(self.groupBox_6)
        self.access_key_ali.setObjectName(u"access_key_ali")
        self.access_key_ali.setClearButtonEnabled(False)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.access_key_ali)

        self.lable_secret_key_2 = QLabel(self.groupBox_6)
        self.lable_secret_key_2.setObjectName(u"lable_secret_key_2")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lable_secret_key_2)

        self.access_key_secret_ali = QLineEdit(self.groupBox_6)
        self.access_key_secret_ali.setObjectName(u"access_key_secret_ali")
        self.access_key_secret_ali.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.access_key_secret_ali.setClearButtonEnabled(False)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.access_key_secret_ali)

        self.lable_app_key_2 = QLabel(self.groupBox_6)
        self.lable_app_key_2.setObjectName(u"lable_app_key_2")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lable_app_key_2)


        self.verticalLayout_13.addLayout(self.formLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.aliai = QPushButton(self.groupBox_6)
        self.aliai.setObjectName(u"aliai")
        sizePolicy1.setHeightForWidth(self.aliai.sizePolicy().hasHeightForWidth())
        self.aliai.setSizePolicy(sizePolicy1)
        self.aliai.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_7.addWidget(self.aliai)

        self.aliapi = QPushButton(self.groupBox_6)
        self.aliapi.setObjectName(u"aliapi")
        sizePolicy1.setHeightForWidth(self.aliapi.sizePolicy().hasHeightForWidth())
        self.aliapi.setSizePolicy(sizePolicy1)
        self.aliapi.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_7.addWidget(self.aliapi)

        self.save_ali = QPushButton(self.groupBox_6)
        self.save_ali.setObjectName(u"save_ali")
        sizePolicy1.setHeightForWidth(self.save_ali.sizePolicy().hasHeightForWidth())
        self.save_ali.setSizePolicy(sizePolicy1)
        self.save_ali.setMinimumSize(QSize(100, 30))
        self.save_ali.setCheckable(False)
        self.save_ali.setAutoDefault(False)
        self.save_ali.setFlat(False)

        self.horizontalLayout_7.addWidget(self.save_ali)


        self.verticalLayout_13.addLayout(self.horizontalLayout_7)


        self.verticalLayout_4.addWidget(self.groupBox_6)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.PerTab = QTabWidget(self.ali)
        self.PerTab.setObjectName(u"PerTab")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.PerTab.sizePolicy().hasHeightForWidth())
        self.PerTab.setSizePolicy(sizePolicy7)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout = QGridLayout(self.tab_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Sicheng = QRadioButton(self.tab_1)
        self.per_ali = QButtonGroup(MainWindow)
        self.per_ali.setObjectName(u"per_ali")
        self.per_ali.addButton(self.Sicheng)
        self.Sicheng.setObjectName(u"Sicheng")

        self.gridLayout.addWidget(self.Sicheng, 1, 1, 1, 1)

        self.Aiqi = QRadioButton(self.tab_1)
        self.per_ali.addButton(self.Aiqi)
        self.Aiqi.setObjectName(u"Aiqi")

        self.gridLayout.addWidget(self.Aiqi, 1, 2, 1, 1)

        self.Ruoxi = QRadioButton(self.tab_1)
        self.per_ali.addButton(self.Ruoxi)
        self.Ruoxi.setObjectName(u"Ruoxi")

        self.gridLayout.addWidget(self.Ruoxi, 0, 2, 1, 1)

        self.Siqi = QRadioButton(self.tab_1)
        self.per_ali.addButton(self.Siqi)
        self.Siqi.setObjectName(u"Siqi")

        self.gridLayout.addWidget(self.Siqi, 0, 3, 1, 1)

        self.Aijia = QRadioButton(self.tab_1)
        self.per_ali.addButton(self.Aijia)
        self.Aijia.setObjectName(u"Aijia")

        self.gridLayout.addWidget(self.Aijia, 1, 3, 1, 1)

        self.Xiaogang = QRadioButton(self.tab_1)
        self.per_ali.addButton(self.Xiaogang)
        self.Xiaogang.setObjectName(u"Xiaogang")

        self.gridLayout.addWidget(self.Xiaogang, 0, 1, 1, 1)

        self.Xiaoyun = QRadioButton(self.tab_1)
        self.per_ali.addButton(self.Xiaoyun)
        self.Xiaoyun.setObjectName(u"Xiaoyun")
        self.Xiaoyun.setChecked(True)

        self.gridLayout.addWidget(self.Xiaoyun, 0, 0, 1, 1)

        self.Sijia = QRadioButton(self.tab_1)
        self.per_ali.addButton(self.Sijia)
        self.Sijia.setObjectName(u"Sijia")

        self.gridLayout.addWidget(self.Sijia, 1, 0, 1, 1)

        self.Aicheng = QRadioButton(self.tab_1)
        self.per_ali.addButton(self.Aicheng)
        self.Aicheng.setObjectName(u"Aicheng")

        self.gridLayout.addWidget(self.Aicheng, 2, 0, 1, 1)

        self.Aida = QRadioButton(self.tab_1)
        self.per_ali.addButton(self.Aida)
        self.Aida.setObjectName(u"Aida")

        self.gridLayout.addWidget(self.Aida, 2, 1, 1, 1)

        self.Ninger = QRadioButton(self.tab_1)
        self.per_ali.addButton(self.Ninger)
        self.Ninger.setObjectName(u"Ninger")

        self.gridLayout.addWidget(self.Ninger, 2, 2, 1, 1)

        self.Ruilin = QRadioButton(self.tab_1)
        self.per_ali.addButton(self.Ruilin)
        self.Ruilin.setObjectName(u"Ruilin")

        self.gridLayout.addWidget(self.Ruilin, 2, 3, 1, 1)

        self.PerTab.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Yina = QRadioButton(self.tab_2)
        self.per_ali.addButton(self.Yina)
        self.Yina.setObjectName(u"Yina")

        self.gridLayout_2.addWidget(self.Yina, 2, 1, 1, 1)

        self.Aishuo = QRadioButton(self.tab_2)
        self.per_ali.addButton(self.Aishuo)
        self.Aishuo.setObjectName(u"Aishuo")

        self.gridLayout_2.addWidget(self.Aishuo, 2, 3, 1, 1)

        self.Aiya = QRadioButton(self.tab_2)
        self.per_ali.addButton(self.Aiya)
        self.Aiya.setObjectName(u"Aiya")

        self.gridLayout_2.addWidget(self.Aiya, 0, 1, 1, 1)

        self.Aiyue = QRadioButton(self.tab_2)
        self.per_ali.addButton(self.Aiyue)
        self.Aiyue.setObjectName(u"Aiyue")

        self.gridLayout_2.addWidget(self.Aiyue, 1, 1, 1, 1)

        self.Aimei = QRadioButton(self.tab_2)
        self.per_ali.addButton(self.Aimei)
        self.Aimei.setObjectName(u"Aimei")

        self.gridLayout_2.addWidget(self.Aimei, 0, 3, 1, 1)

        self.Sijing = QRadioButton(self.tab_2)
        self.per_ali.addButton(self.Sijing)
        self.Sijing.setObjectName(u"Sijing")

        self.gridLayout_2.addWidget(self.Sijing, 2, 2, 1, 1)

        self.Aijing = QRadioButton(self.tab_2)
        self.per_ali.addButton(self.Aijing)
        self.Aijing.setObjectName(u"Aijing")

        self.gridLayout_2.addWidget(self.Aijing, 1, 2, 1, 1)

        self.Siyue = QRadioButton(self.tab_2)
        self.per_ali.addButton(self.Siyue)
        self.Siyue.setObjectName(u"Siyue")

        self.gridLayout_2.addWidget(self.Siyue, 0, 0, 1, 1)

        self.Aina = QRadioButton(self.tab_2)
        self.per_ali.addButton(self.Aina)
        self.Aina.setObjectName(u"Aina")

        self.gridLayout_2.addWidget(self.Aina, 2, 0, 1, 1)

        self.Xiaomei = QRadioButton(self.tab_2)
        self.per_ali.addButton(self.Xiaomei)
        self.Xiaomei.setObjectName(u"Xiaomei")

        self.gridLayout_2.addWidget(self.Xiaomei, 1, 3, 1, 1)

        self.Aixia = QRadioButton(self.tab_2)
        self.per_ali.addButton(self.Aixia)
        self.Aixia.setObjectName(u"Aixia")

        self.gridLayout_2.addWidget(self.Aixia, 0, 2, 1, 1)

        self.Aiyu = QRadioButton(self.tab_2)
        self.per_ali.addButton(self.Aiyu)
        self.Aiyu.setObjectName(u"Aiyu")

        self.gridLayout_2.addWidget(self.Aiyu, 1, 0, 1, 1)

        self.PerTab.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Sitong = QRadioButton(self.tab_3)
        self.per_ali.addButton(self.Sitong)
        self.Sitong.setObjectName(u"Sitong")

        self.gridLayout_3.addWidget(self.Sitong, 0, 0, 1, 1)

        self.Xiaobei = QRadioButton(self.tab_3)
        self.per_ali.addButton(self.Xiaobei)
        self.Xiaobei.setObjectName(u"Xiaobei")

        self.gridLayout_3.addWidget(self.Xiaobei, 0, 1, 1, 1)

        self.Aitong = QRadioButton(self.tab_3)
        self.per_ali.addButton(self.Aitong)
        self.Aitong.setObjectName(u"Aitong")

        self.gridLayout_3.addWidget(self.Aitong, 0, 2, 1, 1)

        self.Aiwei = QRadioButton(self.tab_3)
        self.per_ali.addButton(self.Aiwei)
        self.Aiwei.setObjectName(u"Aiwei")

        self.gridLayout_3.addWidget(self.Aiwei, 0, 3, 1, 1)

        self.Aibao = QRadioButton(self.tab_3)
        self.per_ali.addButton(self.Aibao)
        self.Aibao.setObjectName(u"Aibao")

        self.gridLayout_3.addWidget(self.Aibao, 1, 0, 1, 1)

        self.PerTab.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Andy = QRadioButton(self.tab_4)
        self.per_ali.addButton(self.Andy)
        self.Andy.setObjectName(u"Andy")

        self.gridLayout_4.addWidget(self.Andy, 0, 2, 1, 1)

        self.William = QRadioButton(self.tab_4)
        self.per_ali.addButton(self.William)
        self.William.setObjectName(u"William")

        self.gridLayout_4.addWidget(self.William, 2, 0, 1, 1)

        self.Emily = QRadioButton(self.tab_4)
        self.per_ali.addButton(self.Emily)
        self.Emily.setObjectName(u"Emily")

        self.gridLayout_4.addWidget(self.Emily, 1, 0, 1, 1)

        self.Harry = QRadioButton(self.tab_4)
        self.per_ali.addButton(self.Harry)
        self.Harry.setObjectName(u"Harry")

        self.gridLayout_4.addWidget(self.Harry, 0, 0, 1, 1)

        self.Abby = QRadioButton(self.tab_4)
        self.per_ali.addButton(self.Abby)
        self.Abby.setObjectName(u"Abby")

        self.gridLayout_4.addWidget(self.Abby, 0, 1, 1, 1)

        self.Wendy = QRadioButton(self.tab_4)
        self.per_ali.addButton(self.Wendy)
        self.Wendy.setObjectName(u"Wendy")

        self.gridLayout_4.addWidget(self.Wendy, 1, 3, 1, 1)

        self.Eric = QRadioButton(self.tab_4)
        self.per_ali.addButton(self.Eric)
        self.Eric.setObjectName(u"Eric")

        self.gridLayout_4.addWidget(self.Eric, 0, 3, 1, 1)

        self.Olivia = QRadioButton(self.tab_4)
        self.per_ali.addButton(self.Olivia)
        self.Olivia.setObjectName(u"Olivia")

        self.gridLayout_4.addWidget(self.Olivia, 2, 1, 1, 1)

        self.Luna = QRadioButton(self.tab_4)
        self.per_ali.addButton(self.Luna)
        self.Luna.setObjectName(u"Luna")

        self.gridLayout_4.addWidget(self.Luna, 1, 1, 1, 1)

        self.Luca = QRadioButton(self.tab_4)
        self.per_ali.addButton(self.Luca)
        self.Luca.setObjectName(u"Luca")

        self.gridLayout_4.addWidget(self.Luca, 1, 2, 1, 1)

        self.Lydia = QRadioButton(self.tab_4)
        self.per_ali.addButton(self.Lydia)
        self.Lydia.setObjectName(u"Lydia")

        self.gridLayout_4.addWidget(self.Lydia, 2, 2, 1, 1)

        self.PerTab.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_7 = QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.Shanshan = QRadioButton(self.tab_5)
        self.per_ali.addButton(self.Shanshan)
        self.Shanshan.setObjectName(u"Shanshan")

        self.gridLayout_7.addWidget(self.Shanshan, 0, 0, 1, 1)

        self.Xiaoyue = QRadioButton(self.tab_5)
        self.per_ali.addButton(self.Xiaoyue)
        self.Xiaoyue.setObjectName(u"Xiaoyue")

        self.gridLayout_7.addWidget(self.Xiaoyue, 0, 1, 1, 1)

        self.Qingqing = QRadioButton(self.tab_5)
        self.per_ali.addButton(self.Qingqing)
        self.Qingqing.setObjectName(u"Qingqing")

        self.gridLayout_7.addWidget(self.Qingqing, 0, 2, 1, 1)

        self.Cuijie = QRadioButton(self.tab_5)
        self.per_ali.addButton(self.Cuijie)
        self.Cuijie.setObjectName(u"Cuijie")

        self.gridLayout_7.addWidget(self.Cuijie, 0, 3, 1, 1)

        self.Xiaoze = QRadioButton(self.tab_5)
        self.per_ali.addButton(self.Xiaoze)
        self.Xiaoze.setObjectName(u"Xiaoze")

        self.gridLayout_7.addWidget(self.Xiaoze, 1, 0, 1, 2)

        self.PerTab.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_8 = QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.Tomoka = QRadioButton(self.tab_6)
        self.per_ali.addButton(self.Tomoka)
        self.Tomoka.setObjectName(u"Tomoka")

        self.gridLayout_8.addWidget(self.Tomoka, 0, 0, 1, 1)

        self.Tomoya = QRadioButton(self.tab_6)
        self.per_ali.addButton(self.Tomoya)
        self.Tomoya.setObjectName(u"Tomoya")

        self.gridLayout_8.addWidget(self.Tomoya, 0, 1, 1, 1)

        self.Tomoya_2 = QRadioButton(self.tab_6)
        self.per_ali.addButton(self.Tomoya_2)
        self.Tomoya_2.setObjectName(u"Tomoya_2")

        self.gridLayout_8.addWidget(self.Tomoya_2, 1, 0, 1, 2)

        self.PerTab.addTab(self.tab_6, "")

        self.verticalLayout_6.addWidget(self.PerTab)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)

        self.groupBox_5 = QGroupBox(self.ali)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy6.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy6)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.spd_ali = QSlider(self.groupBox_5)
        self.spd_ali.setObjectName(u"spd_ali")
        self.spd_ali.setMinimum(-500)
        self.spd_ali.setMaximum(500)
        self.spd_ali.setSingleStep(100)
        self.spd_ali.setPageStep(10)
        self.spd_ali.setValue(0)
        self.spd_ali.setOrientation(Qt.Horizontal)
        self.spd_ali.setTickPosition(QSlider.TicksBothSides)

        self.horizontalLayout_10.addWidget(self.spd_ali)

        self.spd_spin_ali = QSpinBox(self.groupBox_5)
        self.spd_spin_ali.setObjectName(u"spd_spin_ali")
        self.spd_spin_ali.setMinimumSize(QSize(55, 0))
        self.spd_spin_ali.setMinimum(-500)
        self.spd_spin_ali.setMaximum(500)
        self.spd_spin_ali.setSingleStep(10)

        self.horizontalLayout_10.addWidget(self.spd_spin_ali)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")
        sizePolicy6.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy6)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_10)

        self.pit_ali = QSlider(self.groupBox_5)
        self.pit_ali.setObjectName(u"pit_ali")
        self.pit_ali.setMinimum(-500)
        self.pit_ali.setMaximum(500)
        self.pit_ali.setSingleStep(100)
        self.pit_ali.setPageStep(50)
        self.pit_ali.setValue(0)
        self.pit_ali.setOrientation(Qt.Horizontal)
        self.pit_ali.setTickPosition(QSlider.TicksBothSides)

        self.horizontalLayout_12.addWidget(self.pit_ali)

        self.pit_spin_ali = QSpinBox(self.groupBox_5)
        self.pit_spin_ali.setObjectName(u"pit_spin_ali")
        self.pit_spin_ali.setMinimumSize(QSize(55, 0))
        self.pit_spin_ali.setMinimum(-500)
        self.pit_spin_ali.setMaximum(500)
        self.pit_spin_ali.setSingleStep(10)

        self.horizontalLayout_12.addWidget(self.pit_spin_ali)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.vol_ali = QSlider(self.groupBox_5)
        self.vol_ali.setObjectName(u"vol_ali")
        self.vol_ali.setMaximum(100)
        self.vol_ali.setSingleStep(10)
        self.vol_ali.setPageStep(10)
        self.vol_ali.setValue(50)
        self.vol_ali.setOrientation(Qt.Horizontal)
        self.vol_ali.setTickPosition(QSlider.TicksBothSides)

        self.horizontalLayout_13.addWidget(self.vol_ali)

        self.vol_spin_ali = QSpinBox(self.groupBox_5)
        self.vol_spin_ali.setObjectName(u"vol_spin_ali")
        self.vol_spin_ali.setMinimumSize(QSize(55, 0))
        self.vol_spin_ali.setMaximum(100)
        self.vol_spin_ali.setValue(50)

        self.horizontalLayout_13.addWidget(self.vol_spin_ali)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.ali_multi = QCheckBox(self.ali)
        self.ali_multi.setObjectName(u"ali_multi")
        self.ali_multi.setChecked(True)

        self.horizontalLayout_8.addWidget(self.ali_multi)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.ali)
        self.label_2.setObjectName(u"label_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy8)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.sleeptime = QDoubleSpinBox(self.ali)
        self.sleeptime.setObjectName(u"sleeptime")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.sleeptime.sizePolicy().hasHeightForWidth())
        self.sleeptime.setSizePolicy(sizePolicy9)
        self.sleeptime.setMinimum(0.500000000000000)
        self.sleeptime.setMaximum(10.000000000000000)
        self.sleeptime.setSingleStep(0.050000000000000)
        self.sleeptime.setValue(1.000000000000000)

        self.horizontalLayout_8.addWidget(self.sleeptime)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.tabWidget.addTab(self.ali, "")
        self.xf = QWidget()
        self.xf.setObjectName(u"xf")
        self.verticalLayout_8 = QVBoxLayout(self.xf)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_7 = QGroupBox(self.xf)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_8 = QLabel(self.groupBox_7)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.app_id_xf = QLineEdit(self.groupBox_7)
        self.app_id_xf.setObjectName(u"app_id_xf")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.app_id_xf)

        self.label_12 = QLabel(self.groupBox_7)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.api_secret_xf = QLineEdit(self.groupBox_7)
        self.api_secret_xf.setObjectName(u"api_secret_xf")
        self.api_secret_xf.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.api_secret_xf)

        self.label_13 = QLabel(self.groupBox_7)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.api_key_xf = QLineEdit(self.groupBox_7)
        self.api_key_xf.setObjectName(u"api_key_xf")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.api_key_xf)


        self.verticalLayout_7.addLayout(self.formLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.xfai = QPushButton(self.groupBox_7)
        self.xfai.setObjectName(u"xfai")
        sizePolicy1.setHeightForWidth(self.xfai.sizePolicy().hasHeightForWidth())
        self.xfai.setSizePolicy(sizePolicy1)
        self.xfai.setMinimumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.xfai)

        self.xfapi = QPushButton(self.groupBox_7)
        self.xfapi.setObjectName(u"xfapi")
        sizePolicy1.setHeightForWidth(self.xfapi.sizePolicy().hasHeightForWidth())
        self.xfapi.setSizePolicy(sizePolicy1)
        self.xfapi.setMinimumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.xfapi)

        self.save_xf = QPushButton(self.groupBox_7)
        self.save_xf.setObjectName(u"save_xf")
        sizePolicy1.setHeightForWidth(self.save_xf.sizePolicy().hasHeightForWidth())
        self.save_xf.setSizePolicy(sizePolicy1)
        self.save_xf.setMinimumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.save_xf)


        self.verticalLayout_7.addLayout(self.horizontalLayout)


        self.verticalLayout_8.addWidget(self.groupBox_7)

        self.tabWidget_2 = QTabWidget(self.xf)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_9 = QGridLayout(self.tab_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.xiaoyan = QRadioButton(self.tab_7)
        self.per_xf = QButtonGroup(MainWindow)
        self.per_xf.setObjectName(u"per_xf")
        self.per_xf.addButton(self.xiaoyan)
        self.xiaoyan.setObjectName(u"xiaoyan")
        self.xiaoyan.setChecked(True)

        self.gridLayout_9.addWidget(self.xiaoyan, 0, 0, 1, 1)

        self.aisjiuxu = QRadioButton(self.tab_7)
        self.per_xf.addButton(self.aisjiuxu)
        self.aisjiuxu.setObjectName(u"aisjiuxu")

        self.gridLayout_9.addWidget(self.aisjiuxu, 0, 1, 1, 1)

        self.aisxping = QRadioButton(self.tab_7)
        self.per_xf.addButton(self.aisxping)
        self.aisxping.setObjectName(u"aisxping")

        self.gridLayout_9.addWidget(self.aisxping, 0, 2, 1, 1)

        self.aisjinger = QRadioButton(self.tab_7)
        self.per_xf.addButton(self.aisjinger)
        self.aisjinger.setObjectName(u"aisjinger")

        self.gridLayout_9.addWidget(self.aisjinger, 0, 3, 1, 1)

        self.aisbabyxu = QRadioButton(self.tab_7)
        self.per_xf.addButton(self.aisbabyxu)
        self.aisbabyxu.setObjectName(u"aisbabyxu")

        self.gridLayout_9.addWidget(self.aisbabyxu, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_9 = QVBoxLayout(self.tab_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_18 = QLabel(self.tab_8)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)

        self.verticalLayout_9.addWidget(self.label_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.tsvcn = QRadioButton(self.tab_8)
        self.per_xf.addButton(self.tsvcn)
        self.tsvcn.setObjectName(u"tsvcn")
        sizePolicy1.setHeightForWidth(self.tsvcn.sizePolicy().hasHeightForWidth())
        self.tsvcn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_19.addWidget(self.tsvcn)

        self.xfvcn = QLineEdit(self.tab_8)
        self.xfvcn.setObjectName(u"xfvcn")
        sizePolicy2.setHeightForWidth(self.xfvcn.sizePolicy().hasHeightForWidth())
        self.xfvcn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_19.addWidget(self.xfvcn)


        self.verticalLayout_9.addLayout(self.horizontalLayout_19)

        self.tabWidget_2.addTab(self.tab_8, "")

        self.verticalLayout_8.addWidget(self.tabWidget_2)

        self.groupBox_8 = QGroupBox(self.xf)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_17 = QLabel(self.groupBox_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_17)

        self.spd_xf = QSlider(self.groupBox_8)
        self.spd_xf.setObjectName(u"spd_xf")
        self.spd_xf.setMaximum(100)
        self.spd_xf.setSingleStep(10)
        self.spd_xf.setPageStep(10)
        self.spd_xf.setValue(50)
        self.spd_xf.setOrientation(Qt.Horizontal)
        self.spd_xf.setTickPosition(QSlider.TicksBothSides)

        self.horizontalLayout_6.addWidget(self.spd_xf)

        self.vol_spin_ali_2 = QSpinBox(self.groupBox_8)
        self.vol_spin_ali_2.setObjectName(u"vol_spin_ali_2")
        self.vol_spin_ali_2.setMinimumSize(QSize(55, 0))
        self.vol_spin_ali_2.setMaximum(100)
        self.vol_spin_ali_2.setValue(50)

        self.horizontalLayout_6.addWidget(self.vol_spin_ali_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_15 = QLabel(self.groupBox_8)
        self.label_15.setObjectName(u"label_15")
        sizePolicy6.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy6)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_15)

        self.pit_xf = QSlider(self.groupBox_8)
        self.pit_xf.setObjectName(u"pit_xf")
        self.pit_xf.setMaximum(100)
        self.pit_xf.setSingleStep(10)
        self.pit_xf.setPageStep(10)
        self.pit_xf.setValue(50)
        self.pit_xf.setOrientation(Qt.Horizontal)
        self.pit_xf.setTickPosition(QSlider.TicksBothSides)

        self.horizontalLayout_9.addWidget(self.pit_xf)

        self.vol_spin_ali_3 = QSpinBox(self.groupBox_8)
        self.vol_spin_ali_3.setObjectName(u"vol_spin_ali_3")
        self.vol_spin_ali_3.setMinimumSize(QSize(55, 0))
        self.vol_spin_ali_3.setMaximum(100)
        self.vol_spin_ali_3.setValue(50)

        self.horizontalLayout_9.addWidget(self.vol_spin_ali_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_16 = QLabel(self.groupBox_8)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_18.addWidget(self.label_16)

        self.vol_xf = QSlider(self.groupBox_8)
        self.vol_xf.setObjectName(u"vol_xf")
        self.vol_xf.setMaximum(100)
        self.vol_xf.setSingleStep(10)
        self.vol_xf.setPageStep(10)
        self.vol_xf.setValue(50)
        self.vol_xf.setOrientation(Qt.Horizontal)
        self.vol_xf.setTickPosition(QSlider.TicksBothSides)

        self.horizontalLayout_18.addWidget(self.vol_xf)

        self.vol_spin_ali_4 = QSpinBox(self.groupBox_8)
        self.vol_spin_ali_4.setObjectName(u"vol_spin_ali_4")
        self.vol_spin_ali_4.setMinimumSize(QSize(55, 0))
        self.vol_spin_ali_4.setMaximum(100)
        self.vol_spin_ali_4.setValue(50)

        self.horizontalLayout_18.addWidget(self.vol_spin_ali_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)


        self.verticalLayout_16.addLayout(self.verticalLayout_2)


        self.verticalLayout_8.addWidget(self.groupBox_8)

        self.tabWidget.addTab(self.xf, "")
        self.azure = QWidget()
        self.azure.setObjectName(u"azure")
        self.groupBox_9 = QGroupBox(self.azure)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(10, 10, 562, 132))
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_21 = QLabel(self.groupBox_9)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_21)

        self.azu_region = QLineEdit(self.groupBox_9)
        self.azu_region.setObjectName(u"azu_region")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.azu_region)

        self.label_22 = QLabel(self.groupBox_9)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_22)

        self.azu_token = QLineEdit(self.groupBox_9)
        self.azu_token.setObjectName(u"azu_token")
        self.azu_token.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.azu_token)


        self.verticalLayout_17.addLayout(self.formLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.azuai = QPushButton(self.groupBox_9)
        self.azuai.setObjectName(u"azuai")
        sizePolicy1.setHeightForWidth(self.azuai.sizePolicy().hasHeightForWidth())
        self.azuai.setSizePolicy(sizePolicy1)
        self.azuai.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_11.addWidget(self.azuai)

        self.azuapi = QPushButton(self.groupBox_9)
        self.azuapi.setObjectName(u"azuapi")
        sizePolicy1.setHeightForWidth(self.azuapi.sizePolicy().hasHeightForWidth())
        self.azuapi.setSizePolicy(sizePolicy1)
        self.azuapi.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_11.addWidget(self.azuapi)

        self.save_azu = QPushButton(self.groupBox_9)
        self.save_azu.setObjectName(u"save_azu")
        sizePolicy1.setHeightForWidth(self.save_azu.sizePolicy().hasHeightForWidth())
        self.save_azu.setSizePolicy(sizePolicy1)
        self.save_azu.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_11.addWidget(self.save_azu)


        self.verticalLayout_17.addLayout(self.horizontalLayout_11)

        self.groupBox_10 = QGroupBox(self.azure)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(81, 385, 491, 71))
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_24 = QLabel(self.groupBox_10)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_24)

        self.spd_azu = QSlider(self.groupBox_10)
        self.spd_azu.setObjectName(u"spd_azu")
        self.spd_azu.setMaximum(100)
        self.spd_azu.setSingleStep(10)
        self.spd_azu.setPageStep(10)
        self.spd_azu.setValue(50)
        self.spd_azu.setOrientation(Qt.Horizontal)
        self.spd_azu.setTickPosition(QSlider.TicksBothSides)

        self.horizontalLayout_17.addWidget(self.spd_azu)

        self.vol_spin_ali_5 = QSpinBox(self.groupBox_10)
        self.vol_spin_ali_5.setObjectName(u"vol_spin_ali_5")
        self.vol_spin_ali_5.setMinimumSize(QSize(55, 0))
        self.vol_spin_ali_5.setMaximum(100)
        self.vol_spin_ali_5.setValue(50)

        self.horizontalLayout_17.addWidget(self.vol_spin_ali_5)


        self.verticalLayout_19.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_25 = QLabel(self.groupBox_10)
        self.label_25.setObjectName(u"label_25")
        sizePolicy6.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy6)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_25)

        self.pit_azu = QSlider(self.groupBox_10)
        self.pit_azu.setObjectName(u"pit_azu")
        self.pit_azu.setMaximum(100)
        self.pit_azu.setSingleStep(10)
        self.pit_azu.setPageStep(10)
        self.pit_azu.setValue(50)
        self.pit_azu.setOrientation(Qt.Horizontal)
        self.pit_azu.setTickPosition(QSlider.TicksBothSides)

        self.horizontalLayout_25.addWidget(self.pit_azu)

        self.vol_spin_ali_6 = QSpinBox(self.groupBox_10)
        self.vol_spin_ali_6.setObjectName(u"vol_spin_ali_6")
        self.vol_spin_ali_6.setMinimumSize(QSize(55, 0))
        self.vol_spin_ali_6.setMaximum(100)
        self.vol_spin_ali_6.setValue(50)

        self.horizontalLayout_25.addWidget(self.vol_spin_ali_6)


        self.verticalLayout_19.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_26 = QLabel(self.groupBox_10)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_26.addWidget(self.label_26)

        self.vol_azu = QSlider(self.groupBox_10)
        self.vol_azu.setObjectName(u"vol_azu")
        self.vol_azu.setMaximum(100)
        self.vol_azu.setSingleStep(10)
        self.vol_azu.setPageStep(10)
        self.vol_azu.setValue(50)
        self.vol_azu.setOrientation(Qt.Horizontal)
        self.vol_azu.setTickPosition(QSlider.TicksBothSides)

        self.horizontalLayout_26.addWidget(self.vol_azu)

        self.vol_spin_ali_7 = QSpinBox(self.groupBox_10)
        self.vol_spin_ali_7.setObjectName(u"vol_spin_ali_7")
        self.vol_spin_ali_7.setMinimumSize(QSize(55, 0))
        self.vol_spin_ali_7.setMaximum(100)
        self.vol_spin_ali_7.setValue(50)

        self.horizontalLayout_26.addWidget(self.vol_spin_ali_7)


        self.verticalLayout_19.addLayout(self.horizontalLayout_26)


        self.verticalLayout_18.addLayout(self.verticalLayout_19)

        self.gridWidget = QWidget(self.azure)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setGeometry(QRect(20, 155, 531, 161))
        self.gridLayout_5 = QGridLayout(self.gridWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.radioButton_5 = QRadioButton(self.gridWidget)
        self.per_azu = QButtonGroup(MainWindow)
        self.per_azu.setObjectName(u"per_azu")
        self.per_azu.addButton(self.radioButton_5)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout_5.addWidget(self.radioButton_5, 2, 0, 1, 1)

        self.radioButton = QRadioButton(self.gridWidget)
        self.per_azu.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.gridLayout_5.addWidget(self.radioButton, 7, 0, 1, 1)

        self.radioButton_10 = QRadioButton(self.gridWidget)
        self.per_azu.addButton(self.radioButton_10)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.gridLayout_5.addWidget(self.radioButton_10, 4, 1, 1, 1)

        self.radioButton_9 = QRadioButton(self.gridWidget)
        self.per_azu.addButton(self.radioButton_9)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.gridLayout_5.addWidget(self.radioButton_9, 4, 0, 1, 1)

        self.radioButton_4 = QRadioButton(self.gridWidget)
        self.per_azu.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_5.addWidget(self.radioButton_4, 6, 0, 1, 1)

        self.radioButton_6 = QRadioButton(self.gridWidget)
        self.per_azu.addButton(self.radioButton_6)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout_5.addWidget(self.radioButton_6, 1, 1, 1, 1)

        self.radioButton_7 = QRadioButton(self.gridWidget)
        self.per_azu.addButton(self.radioButton_7)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout_5.addWidget(self.radioButton_7, 2, 1, 1, 1)

        self.radioButton_8 = QRadioButton(self.gridWidget)
        self.per_azu.addButton(self.radioButton_8)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout_5.addWidget(self.radioButton_8, 6, 1, 1, 1)

        self.radioButton_2 = QRadioButton(self.gridWidget)
        self.per_azu.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_5.addWidget(self.radioButton_2, 1, 0, 1, 1)

        self.radioButton_11 = QRadioButton(self.gridWidget)
        self.per_azu.addButton(self.radioButton_11)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setChecked(False)

        self.gridLayout_5.addWidget(self.radioButton_11, 7, 1, 1, 1)

        self.layoutWidget = QWidget(self.azure)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 310, 531, 31))
        self.horizontalLayout_27 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.azu_multi = QCheckBox(self.layoutWidget)
        self.azu_multi.setObjectName(u"azu_multi")
        self.azu_multi.setChecked(True)

        self.horizontalLayout_27.addWidget(self.azu_multi)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy8.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy8)

        self.horizontalLayout_27.addWidget(self.label_4)

        self.sleeptime_2 = QDoubleSpinBox(self.layoutWidget)
        self.sleeptime_2.setObjectName(u"sleeptime_2")
        sizePolicy9.setHeightForWidth(self.sleeptime_2.sizePolicy().hasHeightForWidth())
        self.sleeptime_2.setSizePolicy(sizePolicy9)
        self.sleeptime_2.setMinimum(0.500000000000000)
        self.sleeptime_2.setMaximum(10.000000000000000)
        self.sleeptime_2.setSingleStep(0.050000000000000)
        self.sleeptime_2.setValue(1.000000000000000)

        self.horizontalLayout_27.addWidget(self.sleeptime_2)

        self.label_23 = QLabel(self.azure)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 380, 51, 61))
        self.label_23.setScaledContents(False)
        self.label_23.setWordWrap(True)
        self.lineEdit = QLineEdit(self.azure)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 350, 113, 21))
        self.label = QLabel(self.azure)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 350, 81, 16))
        self.tabWidget.addTab(self.azure, "")

        self.verticalLayout_10.addWidget(self.tabWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.download = QPushButton(self.groupBox_2)
        self.download.setObjectName(u"download")
        sizePolicy2.setHeightForWidth(self.download.sizePolicy().hasHeightForWidth())
        self.download.setSizePolicy(sizePolicy2)
        self.download.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_4.addWidget(self.download)

        self.generate = QPushButton(self.groupBox_2)
        self.generate.setObjectName(u"generate")
        sizePolicy2.setHeightForWidth(self.generate.sizePolicy().hasHeightForWidth())
        self.generate.setSizePolicy(sizePolicy2)
        self.generate.setMinimumSize(QSize(0, 45))

        self.horizontalLayout_4.addWidget(self.generate)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_20.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1097, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.opendir)
        self.menu_2.addAction(self.about)

        self.retranslateUi(MainWindow)
        self.spd_spin_bd.valueChanged.connect(self.spd_bd.setValue)
        self.vol_spin_bd.valueChanged.connect(self.vol_bd.setValue)
        self.pit_ali.valueChanged.connect(self.pit_spin_ali.setValue)
        self.vol_spin_ali_2.valueChanged.connect(self.spd_xf.setValue)
        self.vol_spin_ali_3.valueChanged.connect(self.pit_xf.setValue)
        self.vol_xf.valueChanged.connect(self.vol_spin_ali_4.setValue)
        self.vol_ali.valueChanged.connect(self.vol_spin_ali.setValue)
        self.pit_bd.valueChanged.connect(self.pit_spin_bd.setValue)
        self.pit_spin_ali.valueChanged.connect(self.pit_ali.setValue)
        self.spd_xf.valueChanged.connect(self.vol_spin_ali_2.setValue)
        self.pit_spin_bd.valueChanged.connect(self.pit_bd.setValue)
        self.spd_bd.valueChanged.connect(self.spd_spin_bd.setValue)
        self.pit_xf.valueChanged.connect(self.vol_spin_ali_3.setValue)
        self.vol_spin_ali.valueChanged.connect(self.vol_ali.setValue)
        self.vol_spin_ali_4.valueChanged.connect(self.vol_xf.setValue)
        self.vol_bd.valueChanged.connect(self.vol_spin_bd.setValue)
        self.spd_ali.valueChanged.connect(self.spd_spin_ali.setValue)
        self.spd_spin_ali.valueChanged.connect(self.spd_ali.setValue)

        self.subtab.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(3)
        self.save_ali.setDefault(False)
        self.PerTab.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5b57\u5e55\u6717\u8bfb\u5668", None))
        self.openfile.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(tooltip)
        self.openfile.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u5b57\u5e55\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.openfile.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u5b57\u5e55\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.openfile.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#if QT_CONFIG(tooltip)
        self.about.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#endif // QT_CONFIG(tooltip)
        self.opensrt.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u5b57\u5e55", None))
#if QT_CONFIG(tooltip)
        self.opensrt.setToolTip(QCoreApplication.translate("MainWindow", u"\u7528\u6587\u672c\u7f16\u8f91\u5668\u6253\u5f00\u5b57\u5e55\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.opensrt.setStatusTip(QCoreApplication.translate("MainWindow", u"\u7528\u6587\u672c\u7f16\u8f91\u5668\u6253\u5f00\u5b57\u5e55\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
        self.opendir.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8f93\u51fa\u6587\u4ef6\u5939", None))
#if QT_CONFIG(statustip)
        self.opendir.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8f93\u51fa\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(statustip)
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u5e55\u6587\u4ef6", None))
        self.srt_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u652f\u6301\u62d6\u62fdSRT\u5b57\u5e55\u6587\u4ef6\u5230\u8fd9\u91cc", None))
#if QT_CONFIG(statustip)
        self.open_srt.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4e00\u4e2aSRT\u5b57\u5e55\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
        self.open_srt.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(statustip)
        self.srt_text.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u7f16\u8f91\u5b57\u5e55", None))
#endif // QT_CONFIG(statustip)
        self.srt_text.setPlainText("")
#if QT_CONFIG(statustip)
        self.edit_srt.setStatusTip(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u540e\u4fee\u6539\u624d\u4f1a\u751f\u6548", None))
#endif // QT_CONFIG(statustip)
        self.edit_srt.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u4fee\u6539", None))
#if QT_CONFIG(statustip)
        self.save_srt.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4f1a\u8986\u76d6\u6e90\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
        self.save_srt.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5b57\u5e55", None))
        self.subtab.setTabText(self.subtab.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"SRT\u5b57\u5e55", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"TXT\u6587\u4ef6", None))
        self.txt_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u652f\u6301\u62d6\u62fdTXT\u6587\u672c\u5230\u8fd9\u91cc", None))
#if QT_CONFIG(statustip)
        self.open_txt.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4e00\u4e2aSRT\u5b57\u5e55\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
        self.open_txt.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(statustip)
        self.txt_text.setStatusTip(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u7f16\u8f91\u5b57\u5e55", None))
#endif // QT_CONFIG(statustip)
        self.txt_text.setPlainText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u4e24\u53e5\u8bdd\u95f4\u9694\u65f6\u95f4", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
#if QT_CONFIG(statustip)
        self.edit_txt.setStatusTip(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u540e\u4fee\u6539\u624d\u4f1a\u751f\u6548", None))
#endif // QT_CONFIG(statustip)
        self.edit_txt.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u4fee\u6539", None))
#if QT_CONFIG(statustip)
        self.save_txt.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4f1a\u8986\u76d6\u6e90\u6587\u4ef6", None))
#endif // QT_CONFIG(statustip)
        self.save_txt.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6587\u672c", None))
        self.subtab.setTabText(self.subtab.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"TXT\u6587\u672c", None))
        self.groupBox_2.setTitle("")
        self.groupBox_4.setTitle("")
        self.lable_app_id.setText(QCoreApplication.translate("MainWindow", u"App ID", None))
        self.lable_app_key.setText(QCoreApplication.translate("MainWindow", u"App Key", None))
        self.lable_secret_key.setText(QCoreApplication.translate("MainWindow", u"Secret Key", None))
        self.baiduapi.setText(QCoreApplication.translate("MainWindow", u"\u524d\u5f80\u5b98\u7f51", None))
#if QT_CONFIG(statustip)
        self.save_bd.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5fc5\u987b\u5148\u4fdd\u5b58", None))
#endif // QT_CONFIG(statustip)
        self.save_bd.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.person.setTitle(QCoreApplication.translate("MainWindow", u"\u53d1\u97f3\u4eba", None))
        self.per_1.setText(QCoreApplication.translate("MainWindow", u"\u5ea6\u5c0f\u5b87\uff08\u6807\u51c6\u7537\u58f0\uff09", None))
        self.per_0.setText(QCoreApplication.translate("MainWindow", u"\u5ea6\u5c0f\u7f8e\uff08\u6807\u51c6\u5973\u58f0\uff09", None))
        self.per_3.setText(QCoreApplication.translate("MainWindow", u"\u5ea6\u900d\u9065\uff08\u60c5\u611f\u7537\u58f0\uff09", None))
        self.per_4.setText(QCoreApplication.translate("MainWindow", u"\u5ea6\u4e2b\u4e2b\uff08\u60c5\u611f\u5973\u58f0\uff09", None))
        self.groupBox_3.setTitle("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u901f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u8c03", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u91cf", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.baidu), QCoreApplication.translate("MainWindow", u"\u767e\u5ea6\u4e91", None))
        self.groupBox_6.setTitle("")
        self.lable_app_id_2.setText(QCoreApplication.translate("MainWindow", u"App Key", None))
        self.app_key_ali.setText("")
        self.lable_secret_key_2.setText(QCoreApplication.translate("MainWindow", u"Access Key Secret", None))
        self.lable_app_key_2.setText(QCoreApplication.translate("MainWindow", u"AccessKey ID", None))
#if QT_CONFIG(tooltip)
        self.aliai.setToolTip(QCoreApplication.translate("MainWindow", u"\u524d\u5f80\u5b98\u7f51\u8bd5\u542c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.aliai.setStatusTip(QCoreApplication.translate("MainWindow", u"\u524d\u5f80\u5b98\u7f51\u8bd5\u542c", None))
#endif // QT_CONFIG(statustip)
        self.aliai.setText(QCoreApplication.translate("MainWindow", u"\u5728\u7ebf\u8bd5\u542c", None))
#if QT_CONFIG(tooltip)
        self.aliapi.setToolTip(QCoreApplication.translate("MainWindow", u"\u9700\u8981\u5728\u4e24\u4e2a\u9875\u9762\u5206\u522b\u83b7\u53d6\u4ee5\u4e0a\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.aliapi.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9700\u8981\u5728\u4e24\u4e2a\u9875\u9762\u5206\u522b\u83b7\u53d6\u4ee5\u4e0a\u4fe1\u606f", None))
#endif // QT_CONFIG(statustip)
        self.aliapi.setText(QCoreApplication.translate("MainWindow", u"\u524d\u5f80\u63a7\u5236\u53f0", None))
#if QT_CONFIG(statustip)
        self.save_ali.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5fc5\u987b\u5148\u4fdd\u5b58", None))
#endif // QT_CONFIG(statustip)
        self.save_ali.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(tooltip)
        self.PerTab.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.PerTab.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bf4\u660e\uff1aCE\u8868\u793a\u652f\u6301\u4e2d\u82f1\u6587\u6df7\u5408\uff0cC\u8868\u793a\u53ea\u652f\u6301\u4e2d\u6587\uff0cE\u8868\u793a\u53ea\u652f\u6301\u82f1\u6587", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.PerTab.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Sicheng.setText(QCoreApplication.translate("MainWindow", u"\u601d\u8bda \u6807\u51c6\u7537\u58f0CE", None))
        self.Aiqi.setText(QCoreApplication.translate("MainWindow", u"\u827e\u742a \u6e29\u67d4\u5973\u58f0CE", None))
        self.Ruoxi.setText(QCoreApplication.translate("MainWindow", u"\u82e5\u516e \u6e29\u67d4\u5973\u58f0CE", None))
        self.Siqi.setText(QCoreApplication.translate("MainWindow", u"\u601d\u742a \u6e29\u67d4\u5973\u58f0CE", None))
        self.Aijia.setText(QCoreApplication.translate("MainWindow", u"\u827e\u4f73 \u6807\u51c6\u5973\u58f0CE", None))
        self.Xiaogang.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u521a \u6807\u51c6\u7537\u58f0CE", None))
        self.Xiaoyun.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u4e91 \u6807\u51c6\u5973\u58f0CE", None))
        self.Sijia.setText(QCoreApplication.translate("MainWindow", u"\u601d\u4f73 \u6807\u51c6\u5973\u58f0CE", None))
        self.Aicheng.setText(QCoreApplication.translate("MainWindow", u"\u827e\u8bda \u6807\u51c6\u7537\u58f0CE", None))
        self.Aida.setText(QCoreApplication.translate("MainWindow", u"\u827e\u8fbe \u6807\u51c6\u7537\u58f0CE", None))
        self.Ninger.setText(QCoreApplication.translate("MainWindow", u"\u5b81\u513f \u6807\u51c6\u5973\u58f0C", None))
        self.Ruilin.setText(QCoreApplication.translate("MainWindow", u"\u745e\u7433 \u6807\u51c6\u5973\u58f0C", None))
        self.PerTab.setTabText(self.PerTab.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u901a\u7528\u573a\u666f", None))
        self.Yina.setText(QCoreApplication.translate("MainWindow", u"\u4f0a\u5a1c \u6d59\u666e\u5973\u58f0C", None))
        self.Aishuo.setText(QCoreApplication.translate("MainWindow", u"\u827e\u7855 \u81ea\u7136\u7537\u58f0CE", None))
        self.Aiya.setText(QCoreApplication.translate("MainWindow", u"\u827e\u96c5 \u4e25\u5389\u5973\u58f0CE", None))
        self.Aiyue.setText(QCoreApplication.translate("MainWindow", u"\u827e\u60a6 \u6e29\u67d4\u5973\u58f0CE", None))
        self.Aimei.setText(QCoreApplication.translate("MainWindow", u"\u827e\u7f8e \u751c\u7f8e\u5973\u58f0CE", None))
        self.Sijing.setText(QCoreApplication.translate("MainWindow", u"\u601d\u5a67 \u4e25\u5389\u5973\u58f0C", None))
        self.Aijing.setText(QCoreApplication.translate("MainWindow", u"\u827e\u5a67 \u4e25\u5389\u5973\u58f0CE", None))
        self.Siyue.setText(QCoreApplication.translate("MainWindow", u"\u601d\u60a6 \u6e29\u67d4\u5973\u58f0CE", None))
        self.Aina.setText(QCoreApplication.translate("MainWindow", u"\u827e\u5a1c \u6d59\u666e\u5973\u58f0C", None))
        self.Xiaomei.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u7f8e \u751c\u7f8e\u5973\u58f0CE", None))
        self.Aixia.setText(QCoreApplication.translate("MainWindow", u"\u827e\u590f \u4eb2\u548c\u5973\u58f0CE", None))
        self.Aiyu.setText(QCoreApplication.translate("MainWindow", u"\u827e\u96e8 \u81ea\u7136\u5973\u58f0CE", None))
        self.PerTab.setTabText(self.PerTab.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u5ba2\u670d\u573a\u666f", None))
        self.Sitong.setText(QCoreApplication.translate("MainWindow", u"\u601d\u5f64 \u513f\u7ae5\u97f3C", None))
        self.Xiaobei.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u5317 \u841d\u8389\u5973\u58f0C", None))
        self.Aitong.setText(QCoreApplication.translate("MainWindow", u"\u827e\u5f64 \u513f\u7ae5\u97f3C", None))
        self.Aiwei.setText(QCoreApplication.translate("MainWindow", u"\u827e\u8587 \u841d\u8389\u5973\u58f0C", None))
        self.Aibao.setText(QCoreApplication.translate("MainWindow", u"\u827e\u5b9d \u841d\u8389\u5973\u58f0C", None))
        self.PerTab.setTabText(self.PerTab.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u7ae5\u58f0\u573a\u666f", None))
        self.Andy.setText(QCoreApplication.translate("MainWindow", u"Andy \u7f8e\u97f3\u7537\u58f0E", None))
        self.William.setText(QCoreApplication.translate("MainWindow", u"William \u82f1\u97f3\u7537\u58f0E", None))
        self.Emily.setText(QCoreApplication.translate("MainWindow", u"Emily \u82f1\u97f3\u5973\u58f0E", None))
        self.Harry.setText(QCoreApplication.translate("MainWindow", u"Harry \u82f1\u97f3\u7537\u58f0E", None))
        self.Abby.setText(QCoreApplication.translate("MainWindow", u"Abby \u7f8e\u97f3\u5973\u58f0E", None))
        self.Wendy.setText(QCoreApplication.translate("MainWindow", u"Wendy \u82f1\u97f3\u5973\u58f0E", None))
        self.Eric.setText(QCoreApplication.translate("MainWindow", u"Eric \u82f1\u97f3\u7537\u58f0E", None))
        self.Olivia.setText(QCoreApplication.translate("MainWindow", u"Olivia \u82f1\u97f3\u5973\u58f0E", None))
        self.Luna.setText(QCoreApplication.translate("MainWindow", u"Luna \u82f1\u97f3\u5973\u58f0E", None))
        self.Luca.setText(QCoreApplication.translate("MainWindow", u"Luca \u82f1\u97f3\u7537\u58f0E", None))
        self.Lydia.setText(QCoreApplication.translate("MainWindow", u"Lydia \u82f1\u4e2d\u53cc\u8bed\u5973\u58f0CE", None))
        self.PerTab.setTabText(self.PerTab.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u82f1\u6587\u573a\u666f", None))
        self.Shanshan.setText(QCoreApplication.translate("MainWindow", u"\u59d7\u59d7 \u7ca4\u8bed\u5973\u58f0CE", None))
        self.Xiaoyue.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u73a5 \u56db\u5ddd\u8bdd\u5973\u58f0CE", None))
        self.Qingqing.setText(QCoreApplication.translate("MainWindow", u"\u9752\u9752 \u53f0\u6e7e\u8bdd\u5973\u58f0", None))
        self.Cuijie.setText(QCoreApplication.translate("MainWindow", u"\u7fe0\u59d0 \u4e1c\u5317\u8bdd\u5973\u58f0", None))
        self.Xiaoze.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u6cfd \u6e56\u5357\u91cd\u53e3\u97f3\u7537\u58f0", None))
        self.PerTab.setTabText(self.PerTab.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u65b9\u8a00\u573a\u666f", None))
        self.Tomoka.setText(QCoreApplication.translate("MainWindow", u"\u667a\u9999 \u65e5\u8bed\u5973\u751f", None))
        self.Tomoya.setText(QCoreApplication.translate("MainWindow", u"\u667a\u4e5f \u65e5\u8bed\u7537\u58f0", None))
        self.Tomoya_2.setText(QCoreApplication.translate("MainWindow", u"Annie \u7f8e\u8bed\u5973\u58f0", None))
        self.PerTab.setTabText(self.PerTab.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u6587\u5b66\u573a\u666f", None))
        self.groupBox_5.setTitle("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u901f", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u8c03", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u91cf", None))
        self.ali_multi.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u591a\u7ebf\u7a0b\u52a0\u901f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7ebf\u7a0b\u4f11\u7720\u65f6\u95f4", None))
#if QT_CONFIG(statustip)
        self.sleeptime.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8d8a\u5c0f\u8d8a\u5feb\uff0c\u592a\u5feb\u4f1a\u88ab\u963f\u91cc\u9650\u5236\u53d1\u751f\u4e0b\u8f7d\u9519\u8bef", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ali), QCoreApplication.translate("MainWindow", u"\u963f\u91cc\u4e91", None))
        self.groupBox_7.setTitle("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"APPID", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"APISecret", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"APIKey", None))
        self.xfai.setText(QCoreApplication.translate("MainWindow", u"\u5728\u7ebf\u8bd5\u542c", None))
        self.xfapi.setText(QCoreApplication.translate("MainWindow", u"\u524d\u5f80\u63a7\u5236\u53f0", None))
#if QT_CONFIG(statustip)
        self.save_xf.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5fc5\u987b\u5148\u4fdd\u5b58", None))
#endif // QT_CONFIG(statustip)
        self.save_xf.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.xiaoyan.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u71d5 \u751c\u7f8e\u5973\u751f", None))
        self.aisjiuxu.setText(QCoreApplication.translate("MainWindow", u"\u8bb8\u4e45 \u4eb2\u5207\u7537\u58f0", None))
        self.aisxping.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u840d \u77e5\u6027\u5973\u58f0", None))
        self.aisjinger.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u5a67 \u4eb2\u5207\u5973\u58f0", None))
        self.aisbabyxu.setText(QCoreApplication.translate("MainWindow", u"\u8bb8\u5c0f\u5b9d \u53ef\u7231\u7ae5\u58f0", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u53d1\u97f3\u4eba", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u7279\u8272\u53d1\u8a00\u4eba\u9700\u624b\u52a8\u5728\u63a7\u5236\u53f0\u6dfb\u52a0\uff0c\u6dfb\u52a0\u540e\u70b9\u51fb\u64cd\u4f5c\uff0c\u5c06\u53c2\u6570\u586b\u5165\u4e0b\u9762", None))
        self.tsvcn.setText(QCoreApplication.translate("MainWindow", u"\u7279\u8272\u53d1\u97f3\u4eba\u53c2\u6570\uff08vcn/voice_name\uff09", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u7279\u8272\u53d1\u97f3\u4eba", None))
        self.groupBox_8.setTitle("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u901f", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u8c03", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u91cf", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.xf), QCoreApplication.translate("MainWindow", u"\u8baf\u98de", None))
        self.groupBox_9.setTitle("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"region", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"token", None))
        self.azuai.setText(QCoreApplication.translate("MainWindow", u"\u5728\u7ebf\u8bd5\u542c", None))
        self.azuapi.setText(QCoreApplication.translate("MainWindow", u"\u524d\u5f80\u63a7\u5236\u53f0", None))
#if QT_CONFIG(statustip)
        self.save_azu.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5fc5\u987b\u5148\u4fdd\u5b58", None))
#endif // QT_CONFIG(statustip)
        self.save_azu.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.groupBox_10.setTitle("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u901f", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u8c03", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u91cf", None))
#if QT_CONFIG(accessibility)
        self.radioButton_5.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"zh-CN-XiaomoNeural", None))
#endif // QT_CONFIG(accessibility)
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u6653\u58a8 \u591a\u79cd\u89d2\u8272\u626e\u6f14", None))
#if QT_CONFIG(accessibility)
        self.radioButton.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"zh-CN-YunyangNeural", None))
#endif // QT_CONFIG(accessibility)
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u626c \u65b0\u95fb\u4f18\u5316", None))
#if QT_CONFIG(accessibility)
        self.radioButton_10.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"zh-CN-XiaoshuangNeural", None))
#endif // QT_CONFIG(accessibility)
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"\u6653\u53cc \u513f\u7ae5 \u6545\u4e8b\uff0c\u804a\u5929\u4f18\u5316", None))
#if QT_CONFIG(accessibility)
        self.radioButton_9.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"zh-CN-XiaoruiNeural", None))
#endif // QT_CONFIG(accessibility)
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"\u6653\u745e", None))
#if QT_CONFIG(accessibility)
        self.radioButton_4.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"zh-CN-XiaoyouNeural", None))
#endif // QT_CONFIG(accessibility)
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6653\u60a0 \u513f\u7ae5\u8bed\u97f3\u6545\u4e8b\u4f18\u5316", None))
#if QT_CONFIG(accessibility)
        self.radioButton_6.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"zh-CN-XiaohanNeural", None))
#endif // QT_CONFIG(accessibility)
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\u6653\u6db5", None))
#if QT_CONFIG(accessibility)
        self.radioButton_7.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"zh-CN-XiaoqiuNeural", None))
#endif // QT_CONFIG(accessibility)
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"\u6653\u79cb \u53d9\u4e8b\u4f18\u5316", None))
#if QT_CONFIG(accessibility)
        self.radioButton_8.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"zh-CN-YunxiNeural", None))
#endif // QT_CONFIG(accessibility)
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u6eaa \u6700\u5e38\u89c1\u8425\u9500\u53f7\u7528", None))
#if QT_CONFIG(accessibility)
        self.radioButton_2.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"zh-CN-XiaochenNeural", None))
#endif // QT_CONFIG(accessibility)
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6653\u8fb0 \u81ea\u53d1\u5bf9\u8bdd\u4f18\u5316", None))
#if QT_CONFIG(accessibility)
        self.radioButton_11.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"zh-CN-YunyeNeural", None))
#endif // QT_CONFIG(accessibility)
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u91ce \u6545\u4e8b\u4f18\u5316", None))
        self.azu_multi.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u591a\u7ebf\u7a0b\u52a0\u901f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7ebf\u7a0b\u4f11\u7720\u65f6\u95f4", None))
#if QT_CONFIG(statustip)
        self.sleeptime_2.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8d8a\u5c0f\u8d8a\u5feb\uff0c\u592a\u5feb\u4f1a\u88ab\u963f\u91cc\u9650\u5236\u53d1\u751f\u4e0b\u8f7d\u9519\u8bef", None))
#endif // QT_CONFIG(statustip)
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u6682\u672a\u5b9e\u73b0\u8c03\u8282\u529f\u80fd", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5355\u72ec\u4e0b\u8f7d\u4e00\u884c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.azure), QCoreApplication.translate("MainWindow", u"azure", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u"\u5148\u70b9\u4e0b\u8f7d", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"\u518d\u70b9\u5408\u6210", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

