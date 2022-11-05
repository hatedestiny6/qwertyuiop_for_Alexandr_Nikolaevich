import sys

from PyQt5.QtCore import Qt

from bandzho import Ui_Piano
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_Piano):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setupUi(self)
        self.files = {}
        self.load_mp3('/Strings/banjo_A3_very-long_piano_normal.mp3', 'A3')
        self.load_mp3('/Strings/banjo_A4_very-long_piano_normal.mp3', 'A4')
        self.load_mp3('/Strings/banjo_A5_very-long_piano_normal.mp3', 'A5')
        self.load_mp3('/Strings/banjo_B3_very-long_piano_normal.mp3', 'B3')
        self.load_mp3('/Strings/banjo_B4_very-long_piano_normal.mp3', 'B4')
        self.load_mp3('/Strings/banjo_B5_very-long_piano_normal.mp3', 'B5')
        self.load_mp3('/Strings/banjo_C3_very-long_piano_normal.mp3', 'C3')
        self.load_mp3('/Strings/banjo_C4_very-long_piano_normal.mp3', 'C4')
        self.load_mp3('/Strings/banjo_C5_very-long_piano_normal.mp3', 'C5')
        self.load_mp3('/Strings/banjo_D3_very-long_piano_normal.mp3', 'D3')
        self.load_mp3('/Strings/banjo_D4_very-long_piano_normal.mp3', 'D4')
        self.load_mp3('/Strings/banjo_D5_very-long_piano_normal.mp3', 'D5')
        self.load_mp3('/Strings/banjo_E3_very-long_piano_normal.mp3', 'E3')
        self.load_mp3('/Strings/banjo_E4_very-long_piano_normal.mp3', 'E4')
        self.load_mp3('/Strings/banjo_E5_very-long_piano_normal.mp3', 'E5')
        self.load_mp3('/Strings/banjo_F3_very-long_piano_normal.mp3', 'F3')
        self.load_mp3('/Strings/banjo_F4_very-long_piano_normal.mp3', 'F4')
        self.load_mp3('/Strings/banjo_F5_very-long_piano_normal.mp3', 'F5')
        self.load_mp3('/Strings/banjo_G3_very-long_piano_normal.mp3', 'G3')
        self.load_mp3('/Strings/banjo_G4_very-long_piano_normal.mp3', 'G4')
        self.load_mp3('/Strings/banjo_G5_very-long_piano_normal.mp3', 'G5')
        self.A3.clicked.connect(self.files['A3'].play)
        self.A4.clicked.connect(self.files['A4'].play)
        self.A5.clicked.connect(self.files['A5'].play)
        self.B3.clicked.connect(self.files['B3'].play)
        self.B4.clicked.connect(self.files['B4'].play)
        self.B5.clicked.connect(self.files['B5'].play)
        self.C3.clicked.connect(self.files['C3'].play)
        self.C4.clicked.connect(self.files['C4'].play)
        self.C5.clicked.connect(self.files['C5'].play)
        self.D3.clicked.connect(self.files['D3'].play)
        self.D4.clicked.connect(self.files['D4'].play)
        self.D5.clicked.connect(self.files['D5'].play)
        self.E3.clicked.connect(self.files['E3'].play)
        self.E4.clicked.connect(self.files['E4'].play)
        self.E5.clicked.connect(self.files['E5'].play)
        self.F3.clicked.connect(self.files['F3'].play)
        self.F4.clicked.connect(self.files['F4'].play)
        self.F5.clicked.connect(self.files['F5'].play)
        self.G3.clicked.connect(self.files['G3'].play)
        self.G4.clicked.connect(self.files['G4'].play)
        self.G5.clicked.connect(self.files['G5'].play)

    def load_mp3(self, filename, code):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        self.files[code] = player

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.files['A3'].play()
        if event.key() == Qt.Key_W:
            self.files['A4'].play()
        if event.key() == Qt.Key_E:
            self.files['A5'].play()
        if event.key() == Qt.Key_R:
            self.files['B3'].play()
        if event.key() == Qt.Key_T:
            self.files['B4'].play()
        if event.key() == Qt.Key_Y:
            self.files['B5'].play()
        if event.key() == Qt.Key_U:
            self.files['C3'].play()
        if event.key() == Qt.Key_I:
            self.files['C4'].play()
        if event.key() == Qt.Key_O:
            self.files['C5'].play()
        if event.key() == Qt.Key_P:
            self.files['D3'].play()
        if event.key() == Qt.Key_A:
            self.files['D4'].play()
        if event.key() == Qt.Key_S:
            self.files['D5'].play()
        if event.key() == Qt.Key_D:
            self.files['E3'].play()
        if event.key() == Qt.Key_F:
            self.files['E4'].play()
        if event.key() == Qt.Key_G:
            self.files['E5'].play()
        if event.key() == Qt.Key_H:
            self.files['F3'].play()
        if event.key() == Qt.Key_J:
            self.files['F4'].play()
        if event.key() == Qt.Key_K:
            self.files['F5'].play()
        if event.key() == Qt.Key_L:
            self.files['G3'].play()
        if event.key() == Qt.Key_Z:
            self.files['G4'].play()
        if event.key() == Qt.Key_X:
            self.files['G5'].play()


def exception_hook(cls, exception, traceback):
    sys.__exception_hook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
