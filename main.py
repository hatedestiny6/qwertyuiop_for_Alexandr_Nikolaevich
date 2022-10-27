import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()
        # положение нло
        self.x = 0
        self.y = 0
        # шаг
        self.delta = 10
        # пропорции иконки нло
        self.ufo_x = 64
        self.ufo_y = 64
        # файл нло
        self.ufo_name = 'ufo.png'
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('НЛО')

        self.pixmap = QPixmap(self.ufo_name)

        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.y -= self.delta

            if self.y <= -20:
                self.y = 420 - self.ufo_y

            self.lbl.move(self.x, self.y)

        if event.key() == Qt.Key_Down:
            self.y += self.delta

            if self.y >= 360:
                self.y = -10

            self.lbl.move(self.x, self.y)

        if event.key() == Qt.Key_Right:
            self.x += self.delta

            if self.x >= 350:
                self.x = -10

            self.lbl.move(self.x, self.y)

        if event.key() == Qt.Key_Left:
            self.x -= self.delta

            if self.x < -10:
                self.x = 400 - self.ufo_x

            self.lbl.move(self.x, self.y)

        print(self.lbl.pos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
