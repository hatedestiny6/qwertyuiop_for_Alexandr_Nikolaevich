# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Change_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 277)
        self.yearEdit = QtWidgets.QLineEdit(Dialog)
        self.yearEdit.setGeometry(QtCore.QRect(100, 80, 281, 21))
        self.yearEdit.setObjectName("yearEdit")
        self.nameEdit = QtWidgets.QLineEdit(Dialog)
        self.nameEdit.setGeometry(QtCore.QRect(100, 30, 281, 31))
        self.nameEdit.setObjectName("nameEdit")
        self.lengthEdit = QtWidgets.QLineEdit(Dialog)
        self.lengthEdit.setGeometry(QtCore.QRect(100, 160, 281, 21))
        self.lengthEdit.setObjectName("lengthEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 51, 21))
        self.label_3.setObjectName("label_3")
        self.changeButton = QtWidgets.QPushButton(Dialog)
        self.changeButton.setGeometry(QtCore.QRect(270, 200, 111, 41))
        self.changeButton.setObjectName("changeButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.label_2.setObjectName("label_2")
        self.statusLabel = QtWidgets.QLabel(Dialog)
        self.statusLabel.setGeometry(QtCore.QRect(20, 210, 181, 21))
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 47, 21))
        self.label_4.setObjectName("label_4")
        self.genreEdit = QtWidgets.QComboBox(Dialog)
        self.genreEdit.setGeometry(QtCore.QRect(100, 120, 281, 21))
        self.genreEdit.setObjectName("genreEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "????????"))
        self.changeButton.setText(_translate("Dialog", "??????????????????????????????"))
        self.label.setText(_translate("Dialog", "????????????????"))
        self.label_2.setText(_translate("Dialog", "?????? ??????????????"))
        self.label_4.setText(_translate("Dialog", "??????????"))
