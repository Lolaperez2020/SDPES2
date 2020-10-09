import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QPushButton, QGraphicsColorizeEffect
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QColor

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.resize(500, 500)
        self.initUi()

    def initUi(self):

        self.color = QGraphicsColorizeEffect()
        self.color.setColor(QColor('black'))

        self.frame = QFrame(self)
        self.frame.setGeometry(100, 100, 100, 100)
        self.frame.setStyleSheet('background-color: black;')
        self.frame.setGraphicsEffect(self.color)

        self.button = QPushButton(self)
        self.button.setGeometry(250, 100, 100, 100)
        self.button.setText('Анимация')
        self.button.clicked.connect(self.Animation)

    def Animation(self):

        self.anim = QPropertyAnimation(self.color, b"color")
        self.anim.setDuration(3000)
        self.anim.setStartValue(QColor('black'))
        self.anim.setEndValue(QColor('red'))
        self.anim.start()


if __name__=="__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())