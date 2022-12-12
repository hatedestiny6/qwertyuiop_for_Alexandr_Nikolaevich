import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QDialog, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sqlite3

from library import Ui_Form
from dialog import Ui_Dialog


class Information(QDialog, Ui_Dialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.title = data[1]
        self.author = data[2]
        self.year = str(data[3])
        self.genre = data[4]
        self.image = data[5]

        self.show()

    def show(self):
        pixmap = QPixmap(self.image)
        self.image_output.setPixmap(pixmap)
        self.labelTitle.setText(self.title)
        self.labelAuthor.setText(self.author)
        self.labelYear.setText(self.year)
        self.labelGenre.setText(self.genre)


class Main(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.con = sqlite3.connect('library.db')

        self.library = {}

        self.comboBox.addItems(['Автор', 'Название'])
        self.goBtn.clicked.connect(self.search)

    def search(self):
        if self.comboBox.currentText() == 'Автор':
            self.search_name()
        else:
            self.search_title()

    def search_title(self):
        cur = self.con.cursor()
        text = self.searchLine.text()
        sql = f"SELECT * FROM books WHERE title LIKE '%{text}%'"
        data = cur.execute(sql).fetchall()

        self.library = {}

        self.output.clear()

        for i in data:
            btn = QPushButton(i[1])
            btn.clicked.connect(self.show_information)

            self.library[btn] = i

            listWidgetItem = QListWidgetItem()
            listWidgetItem.setSizeHint(btn.sizeHint())
            self.output.addItem(listWidgetItem)
            self.output.setItemWidget(listWidgetItem, btn)
            self.output.scrollToItem(listWidgetItem)

    def search_name(self):
        cur = self.con.cursor()
        text = self.searchLine.text()
        sql = f"SELECT * FROM books WHERE author LIKE '%{text}%'"
        data = cur.execute(sql).fetchall()

        self.library = {}

        self.output.clear()

        for i in data:
            btn = QPushButton(i[1])
            btn.clicked.connect(self.show_information)

            self.library[btn] = i

            listWidgetItem = QListWidgetItem()
            listWidgetItem.setSizeHint(btn.sizeHint())
            self.output.addItem(listWidgetItem)
            self.output.setItemWidget(listWidgetItem, btn)
            self.output.scrollToItem(listWidgetItem)

    def show_information(self):
        dlg = Information(tuple(self.library[self.sender()]), self)
        dlg.exec()


def exception_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.excepthook = exception_hook
    ex.show()
    sys.exit(app.exec_())
