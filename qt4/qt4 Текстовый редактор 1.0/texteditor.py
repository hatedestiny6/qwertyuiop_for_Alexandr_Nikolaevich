# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'texteditor.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 402)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 151, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filename_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.filename_input.setObjectName("filename_input")
        self.verticalLayout.addWidget(self.filename_input)
        self.create_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.create_btn.setObjectName("create_btn")
        self.verticalLayout.addWidget(self.create_btn)
        self.save_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)
        self.open_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_btn.setObjectName("open_btn")
        self.verticalLayout.addWidget(self.open_btn)
        self.data_input = QtWidgets.QTextEdit(self.centralwidget)
        self.data_input.setGeometry(QtCore.QRect(170, 10, 361, 361))
        self.data_input.setObjectName("data_input")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create_btn.setText(_translate("MainWindow", "?????????????? ??????????"))
        self.save_btn.setText(_translate("MainWindow", "?????????????????? ????????"))
        self.open_btn.setText(_translate("MainWindow", "?????????????? ????????"))
