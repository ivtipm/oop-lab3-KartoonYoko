# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_authorization.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_authorization(object):
    def setupUi(self, Form_authorization):
        Form_authorization.setObjectName("Form_authorization")
        Form_authorization.resize(334, 289)
        Form_authorization.setMinimumSize(QtCore.QSize(334, 289))
        Form_authorization.setMaximumSize(QtCore.QSize(334, 289))
        Form_authorization.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form_authorization.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_name = QtWidgets.QLineEdit(Form_authorization)
        self.lineEdit_name.setGeometry(QtCore.QRect(80, 130, 171, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label = QtWidgets.QLabel(Form_authorization)
        self.label.setGeometry(QtCore.QRect(110, 110, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form_authorization)
        self.label_2.setGeometry(QtCore.QRect(120, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form_authorization)
        self.pushButton.setGeometry(QtCore.QRect(110, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form_authorization)
        QtCore.QMetaObject.connectSlotsByName(Form_authorization)

    def retranslateUi(self, Form_authorization):
        _translate = QtCore.QCoreApplication.translate
        Form_authorization.setWindowTitle(_translate("Form_authorization", "Окно авторизации"))
        self.label.setText(_translate("Form_authorization", "Введите свое имя:"))
        self.label_2.setText(_translate("Form_authorization", "Welcome"))
        self.pushButton.setText(_translate("Form_authorization", "Войти"))
