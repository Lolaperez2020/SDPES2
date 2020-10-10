# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


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
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(28, 28, 28, 255), stop:1 rgba(86, 86, 86, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cmd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cmd_btn.setGeometry(QtCore.QRect(10, 40, 41, 41))
        self.cmd_btn.setStyleSheet("image:url(:/image/terminal_blue.png);\n"
"background-color: rgb(40, 40, 40);\n"
"border-radius:20px;")
        self.cmd_btn.setText("")
        self.cmd_btn.setObjectName("cmd_btn")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 30, 61, 571))
        self.listWidget.setStyleSheet("background-color:rgb(40, 40, 40);\n"
"border-style: solid;\n"
"border-width:0px;")
        self.listWidget.setObjectName("listWidget")
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
        self.listWidget_2.setGeometry(QtCore.QRect(0, 0, 801, 30))
        self.listWidget_2.setStyleSheet("background-color:rgb(20, 20, 20);\n"
"border-style: solid;\n"
"border-width:0px;")
        self.listWidget_2.setObjectName("listWidget_2")
        self.cmd_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.cmd_btn_2.setGeometry(QtCore.QRect(10, 90, 41, 41))
        self.cmd_btn_2.setStyleSheet("image:url(:/image/weather.png);\n"
"background-color: rgb(40, 40, 40);\n"
"border-radius:20px;")
        self.cmd_btn_2.setText("")
        self.cmd_btn_2.setObjectName("cmd_btn_2")
        self.cmd_btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.cmd_btn_3.setGeometry(QtCore.QRect(10, 140, 41, 41))
        self.cmd_btn_3.setStyleSheet("image:url(:/image/unnamed.png);\n"
"background-color: rgb(40, 40, 40);\n"
"border-radius:20px;")
        self.cmd_btn_3.setText("")
        self.cmd_btn_3.setObjectName("cmd_btn_3")
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
        self.temp_image.setGeometry(QtCore.QRect(220, 52, 47, 51))
        self.temp_image.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
        self.temp_image.setText("")
        self.temp_image.setObjectName("temp_image")
        self.weather_stat_image = QtWidgets.QLabel(self.centralwidget)
        self.weather_stat_image.setGeometry(QtCore.QRect(380, 70, 151, 141))
        self.weather_stat_image.setText("")
        self.weather_stat_image.setObjectName("weather_stat_image")
        self.listWidget_2.raise_()
        self.listWidget.raise_()
        self.exit_btn.raise_()
        self.full_screen_btn.raise_()
        self.tray_btn.raise_()
        self.cmd_btn.raise_()
        self.cmd_btn_2.raise_()
        self.cmd_btn_3.raise_()
        self.temperature.raise_()
        self.temp_image.raise_()
        self.weather_stat_image.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cmd_btn_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><img src=\":/image/terminal_blue.png\"/></p></body></html>"))
        self.temperature.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:36pt;\">0</span></p></body></html>"))
