import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import main_UI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.cmd_btn.clicked.connect(self.term)
        self.exit_btn.clicked.connect(self.kill)

    def term(self):
        print('jjj')

    def kill(self):
        print('h')
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
