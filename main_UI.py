# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(28, 28, 28, 255), stop:1 rgba(86, 86, 86, 255))

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(24)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:rgb(10, 10, 10)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.settings_btn = QtWidgets.QPushButton(self.centralwidget)
        self.settings_btn.setGeometry(QtCore.QRect(10, 550, 41, 41))
        self.settings_btn.setIcon(QtGui.QIcon('images/settings_icon.png'))
        self.settings_btn.setIconSize(QtCore.QSize(40, 40))
        self.settings_btn.setStyleSheet("background-color: rgb(40, 40, 40);\n"
                                     "border-radius:20px;")
        self.settings_btn.setText("")
        self.settings_btn.setObjectName("settings_btn")

        self.icons_btn = QtWidgets.QPushButton(self.centralwidget)
        self.icons_btn.setGeometry(QtCore.QRect(10, 40, 41, 41))
        self.icons_btn.setIcon(QtGui.QIcon('images/exe_ico.png'))
        self.icons_btn.setIconSize(QtCore.QSize(40, 40))
        self.icons_btn.setStyleSheet("background-color: rgb(40, 40, 40);\n"
                                   "border-radius:20px;")
        self.icons_btn.setText("")
        self.icons_btn.setObjectName("icons_btn")

        self.cmd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cmd_btn.setGeometry(QtCore.QRect(10, 90, 41, 41))
        self.cmd_btn.setIcon(QtGui.QIcon('images/terminal_blue.png'))
        self.cmd_btn.setIconSize(QtCore.QSize(40, 40))
        self.cmd_btn.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-radius:20px;")
        self.cmd_btn.setText("")
        self.cmd_btn.setObjectName("cmd_btn")

        self.side_menu_bg = QtWidgets.QListWidget(self.centralwidget)
        self.side_menu_bg.setGeometry(QtCore.QRect(0, 30, 61, 571))
        self.side_menu_bg.setStyleSheet("background-color:rgb(40, 40, 40);\n"
"border-style: solid;\n"
"border-width:0px;")
        self.side_menu_bg.setObjectName("listWidget")

        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(770, 5, 20, 20))
        self.exit_btn.setStyleSheet("background-color: rgb(255, 100, 100);\n"
"border-radius:10px;")
        self.exit_btn.setText("")
        self.exit_btn.setObjectName("exit_btn")

        self.full_screen_btn = QtWidgets.QPushButton(self.centralwidget)
        self.full_screen_btn.setGeometry(QtCore.QRect(745, 5, 20, 20))
        self.full_screen_btn.setStyleSheet("background-color: rgb(255, 255, 100);\n"
"border-radius:10px;")
        self.full_screen_btn.setText("")
        self.full_screen_btn.setObjectName("full_screen_btn")

        self.tray_btn = QtWidgets.QPushButton(self.centralwidget)
        self.tray_btn.setGeometry(QtCore.QRect(720, 5, 20, 20))
        self.tray_btn.setStyleSheet("background-color: rgb(100, 255, 100);\n"
"border-radius:10px;")
        self.tray_btn.setText("")
        self.tray_btn.setObjectName("tray_btn")

        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 30, 801, 600))
        self.listWidget_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(28, 28, 28, 255), stop:1 rgba(86, 86, 86, 255));\n"
"border-style: solid;\n"
"border-width:0px;")
        self.listWidget_2.setObjectName("listWidget_2")

        self.weather_btn = QtWidgets.QPushButton(self.centralwidget)
        self.weather_btn.setGeometry(QtCore.QRect(10, 140, 41, 41))
        self.weather_btn.setIcon(QtGui.QIcon('images/weather.png'))
        self.weather_btn.setIconSize(QtCore.QSize(40, 40))
        self.weather_btn.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-radius:20px;")
        self.weather_btn.setText("")
        self.weather_btn.setObjectName("cmd_btn_2")

        self.speed_btn = QtWidgets.QPushButton(self.centralwidget)
        self.speed_btn.setGeometry(QtCore.QRect(10, 190, 41, 41))
        self.speed_btn.setIcon(QtGui.QIcon('images/speed.png'))
        self.speed_btn.setIconSize(QtCore.QSize(40, 40))
        self.speed_btn.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-radius:20px;")
        self.speed_btn.setText("")
        self.speed_btn.setObjectName("cmd_btn_3")

        self.temperature = QtWidgets.QLabel(self.centralwidget)
        self.temperature.setGeometry(QtCore.QRect(90, 50, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.temperature.setFont(font)
        self.temperature.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                       "color:rgba(19, 87, 255, 1);\n"
                                       "border-radius:0px;")
        self.temperature.setObjectName("temperature")
        self.temp_image = QtWidgets.QLabel(self.centralwidget)
        self.temp_image.setGeometry(QtCore.QRect(220, 52, 50, 50))
        self.temp_image.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
        self.temp_image.setText("")

        px = QtGui.QPixmap('images/cel.png').scaled(50, 50)
        self.temp_image.setPixmap(px)
        # self.temp_image.setIconSize(QtCore.QSize(40, 40))

        self.temp_image.setObjectName("temp_image")
        self.weather_stat_image = QtWidgets.QLabel(self.centralwidget)
        self.weather_stat_image.setGeometry(QtCore.QRect(380, 70, 151, 141))
        self.weather_stat_image.setText("")
        self.weather_stat_image.setObjectName("weather_stat_image")

        self.layout_weather_bg = QtWidgets.QListWidget(self.centralwidget)
        self.layout_weather_bg.setGeometry(QtCore.QRect(61, 30, 739, 570))
        self.layout_weather_bg.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                        "border-style: solid;\n"
                                        "border-width:0px;")
        self.layout_weather_bg.setObjectName("listWidget")

        self.listWidget_2.raise_()
        self.side_menu_bg.raise_()
        self.exit_btn.raise_()
        self.full_screen_btn.raise_()
        self.tray_btn.raise_()
        self.cmd_btn.raise_()
        self.weather_btn.raise_()
        self.speed_btn.raise_()
        self.icons_btn.raise_()
        self.layout_weather_bg.raise_()
        self.temperature.raise_()
        self.temp_image.raise_()
        self.weather_stat_image.raise_()
        self.settings_btn.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
