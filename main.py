import sys
import os
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import main_UI
from PyQt5.QtCore import Qt
import weather_module


class MainWindow(QMainWindow, main_UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint) # окно находится всегда на верху

        self.all_widget_list = [self.temperature, self.temp_image, self.weather_stat_image, self.layout_weather_bg]
        self.weather_list_widgets = [self.temperature, self.temp_image, self.weather_stat_image, self.layout_weather_bg]
        self.speed_list_widgets = []
        self.launch_list_widgets = []
        self.settings_list_widgets = []
        self.hide_other(self.launch_list_widgets)

        self.cmd_btn.clicked.connect(self.term)
        self.exit_btn.clicked.connect(self.kill)
        self.tray_btn.clicked.connect(self.hide_window)
        self.weather_btn.clicked.connect(self.weather_set)
        self.speed_btn.clicked.connect(self.speed_set)
        self.icons_btn.clicked.connect(self.launch_set)
        self.settings_btn.clicked.connect(self.settings_set)

    def day_time(self, time=None):
        if time is not None:
            if '7' <= time <= '18':
                return True
            else:
                return False
        else:
            return None

    def weather_set(self):
        weather = weather_module.get_weather_stat()
        self.temperature.setText('<html><head/><body><p align="right"><span style=" font-size:36pt;">'
                                 + str(weather[0]) + '</span></p></body></html>')
        if weather[1] == 'Clouds':
            self.weather_stat_image.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
            self.weather_stat_image.setText("")
            px = QtGui.QPixmap('images/suncloud.png').scaled(150, 100)
            self.weather_stat_image.setPixmap(px)
            self.layout_weather_bg.setStyleSheet("background-color:rgba(65, 112, 252, 0.1);\n"
                                                 "border-style: solid;\n"
                                                 "border-width:0px;")
        elif weather[1] == 'Clear':
            if self.day_time(weather[4]):
                self.weather_stat_image.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
                self.weather_stat_image.setText("")
                px = QtGui.QPixmap('images/sun_clear.png').scaled(100, 100)
                self.weather_stat_image.setPixmap(px)
                self.layout_weather_bg.setStyleSheet("background-color:rgba(255, 205, 112, 0.1);\n"
                                                     "border-style: solid;\n"
                                                     "border-width:0px;")
            else:
                self.weather_stat_image.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
                self.weather_stat_image.setText("")
                px = QtGui.QPixmap('images/moon_clear.png').scaled(100, 100)
                self.weather_stat_image.setPixmap(px)
                self.layout_weather_bg.setStyleSheet("background-color:rgba(65, 112, 252, 0.1);\n"
                                                     "border-style: solid;\n"
                                                     "border-width:0px;")
        self.hide_other(self.weather_list_widgets)

    def settings_set(self):
        self.hide_other(self.settings_list_widgets)

    def speed_set(self):
        self.hide_other(self.speed_list_widgets)

    def launch_set(self):
        self.hide_other(self.launch_list_widgets)

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)

    def hide_other(self, temp_list):
        for c in self.all_widget_list:
            if c not in temp_list:
                c.hide()
            else:
                c.show()

    def term(self):
        os.startfile('C:\Windows\System32\cmd.exe')

    def kill(self):
        exit()

    def hide_window(self):
        self.showMinimized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
