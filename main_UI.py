# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import os


class ButtonExecutable(QtWidgets.QPushButton):
    def setpath(self, path):
        self.path = path
        self.clicked.connect(self.execute)

    def execute(self):
        try:
            os.startfile(self.path)
        except NameError:
            pass
        except FileNotFoundError:
            pass

    def set_style(self):
        self.width, self.height = 70, 70
        self.pos_x, self.pos_y = 100, 100
        self.setGeometry(QtCore.QRect(self.pos_x, self.pos_y, self.width, self.height))
        self.setStyleSheet("background-color:rgba(200, 200, 200, 1);\n"
                           "border-radius:10px;")
        # self.setIcon(QtGui.QIcon(icon))
        # self.setIconSize(QtCore.QSize(40, 40))

    def set_pos(self, x, y):
        self.pos_x, self.pos_y = x, y
        self.setGeometry(QtCore.QRect(self.pos_x, self.pos_y, self.width, self.height))
        self.update()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.size = 800, 600
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.size[0], self.size[1])
        MainWindow.setMinimumSize(QtCore.QSize(self.size[0], self.size[1]))
        MainWindow.setMaximumSize(QtCore.QSize(self.size[0], self.size[1]))
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
        self.side_menu_bg.setGeometry(QtCore.QRect(0, 30, 60, 570))
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
        self.listWidget_2.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(28, 28, 28, 255), stop:1 rgba(86, 86, 86, 255));\n"
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

        self.ege_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ege_btn.setGeometry(QtCore.QRect(10, 240, 41, 41))
        self.ege_btn.setIcon(QtGui.QIcon('images/ege.png'))
        self.ege_btn.setIconSize(QtCore.QSize(40, 40))
        self.ege_btn.setStyleSheet("background-color: rgb(40, 40, 40);\n"
                                     "border-radius:20px;")
        self.ege_btn.setText("")
        self.ege_btn.setObjectName("ege_btn")

        self.temperature = QtWidgets.QLabel(self.centralwidget)
        self.temperature.setGeometry(QtCore.QRect(100, 50, 50, 51))
        self.font = QtGui.QFont()
        self.font.setFamily("Berlin Sans FB Demi")
        self.font.setPointSize(16)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.temperature.setFont(self.font)
        self.temperature.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                       "color:rgba(19, 87, 255, 1);\n"
                                       "border-radius:0px;")
        self.temperature.setObjectName("temperature")
        self.temp_image = QtWidgets.QLabel(self.centralwidget)
        self.temp_image.setGeometry(QtCore.QRect(150, 52, 50, 50))
        self.temp_image.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
        self.temp_image.setText("")

        px = QtGui.QPixmap('images/cel.png').scaled(50, 50)
        self.temp_image.setPixmap(px)
        # self.temp_image.setIconSize(QtCore.QSize(40, 40))

        self.temp_image.setObjectName("temp_image")
        self.weather_stat_image = QtWidgets.QLabel(self.centralwidget)
        self.weather_stat_image.setGeometry(QtCore.QRect(530, 40, 151, 141))
        self.weather_stat_image.setText("")
        self.weather_stat_image.setObjectName("weather_stat_image")

        self.layout_weather_bg = QtWidgets.QListWidget(self.centralwidget)
        self.layout_weather_bg.setGeometry(QtCore.QRect(61, 30, 739, 570))
        self.layout_weather_bg.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                             "border-style: solid;\n"
                                             "border-width:0px;")
        self.layout_weather_bg.setObjectName("listWidget")

        self.wind_image = QtWidgets.QLabel(self.centralwidget)
        self.wind_image.setGeometry(QtCore.QRect(100, 100, 80, 50))
        self.wind_image.setText("")
        self.wind_image.setObjectName("weather_stat_image")
        self.wind_image.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                      "border-style: solid;\n"
                                      "border-width:0px;")
        px = QtGui.QPixmap('images/wind.png').scaled(75, 50)
        self.wind_image.setPixmap(px)

        self.wind_scale = QtWidgets.QLabel(self.centralwidget)
        self.wind_scale.setGeometry(QtCore.QRect(180, 100, 130, 50))
        self.wind_scale.setText("")
        self.wind_scale.setObjectName("weather_stat_image")
        self.wind_scale.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                      "border-style: solid;\n"
                                      "color:rgba(150, 230, 255, 1);\n"
                                      "border-width:0px;")
        self.wind_scale.setFont(font)

        self.humid_image = QtWidgets.QLabel(self.centralwidget)
        self.humid_image.setGeometry(QtCore.QRect(155, 170, 80, 50))
        self.humid_image.setText("")
        self.humid_image.setObjectName("weather_stat_image")
        self.humid_image.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                       "border-style: solid;\n"
                                       "border-width:0px;")
        px = QtGui.QPixmap('images/drop.png').scaled(50, 70)
        self.humid_image.setPixmap(px)

        self.humid_scale = QtWidgets.QLabel(self.centralwidget)
        self.humid_scale.setGeometry(QtCore.QRect(100, 170, 60, 50))
        self.humid_scale.setText("")
        self.humid_scale.setObjectName("weather_stat_image")
        self.humid_scale.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                       "border-style: solid;\n"
                                       "color:rgba(19, 87, 255, 1);\n"
                                       "border-width:0px;")
        self.humid_scale.setFont(font)

        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(80, 50, 160, 30))
        self.add_btn.setIconSize(QtCore.QSize(40, 40))
        self.add_btn.setStyleSheet("background-color: rgb(80, 235, 80);\n"
                                   "border-radius:15px;")
        self.add_btn.setText("Add Button")
        self.add_btn.setObjectName("add_btn")

        self.del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_btn.setGeometry(QtCore.QRect(260, 50, 160, 30))
        self.del_btn.setIconSize(QtCore.QSize(40, 40))
        self.del_btn.setStyleSheet("background-color: rgb(235, 80, 80);\n"
                                   "border-radius:15px;")
        self.del_btn.setText("Delete Button")
        self.del_btn.setObjectName("del_btn")

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
        self.wind_image.raise_()
        self.wind_scale.raise_()
        self.humid_scale.raise_()
        self.humid_image.raise_()
        self.add_btn.raise_()
        self.del_btn.raise_()
        self.ege_btn.raise_()

        self.ege_temp()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def ege_temp(self):
        self.rus_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rus_btn.setGeometry(QtCore.QRect(80, 50, 130, 60))
        self.rus_btn.setStyleSheet("background-color: rgb(80, 235, 80);\n"
                                   "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255,241,78,1), stop:1 rgba(52,240,255,1));\n"
                                   "border-radius:25px;")
        self.rus_btn.setFont(self.font)
        self.rus_btn.setText("Russian")
        self.rus_btn.setObjectName("https://rus-ege.sdamgia.ru/")
        self.rus_btn.raise_()

        self.physics_btn = QtWidgets.QPushButton(self.centralwidget)
        self.physics_btn.setGeometry(QtCore.QRect(80, 130, 130, 60))
        self.physics_btn.setStyleSheet("background-color: rgb(80, 235, 80);\n"
                                       "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255,5,27,1), stop:1 rgba(52,240,255,1));\n"
                                       "border-radius:25px;")
        self.physics_btn.setFont(self.font)
        self.physics_btn.setText("Physics")
        self.physics_btn.setObjectName("https://phys-ege.sdamgia.ru/")
        self.physics_btn.raise_()

        self.math_btn = QtWidgets.QPushButton(self.centralwidget)
        self.math_btn.setGeometry(QtCore.QRect(80, 210, 130, 60))
        self.math_btn.setStyleSheet("background-color: rgba(80, 235, 80, 1);\n"
                                    "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(47,57,186,1), stop:1 rgba(52,240,255,1));\n"
                                    "border-radius:25px;")
        self.math_btn.setFont(self.font)
        self.math_btn.setText("Math")
        self.math_btn.setObjectName("https://math-ege.sdamgia.ru/")
        self.math_btn.raise_()
