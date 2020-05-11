# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ruleWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt

from util.commonFunctions import setStyle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("RuleWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.move(0, 0)
        self.label.resize(480, 30)
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont('SansSerif', 20))
        self.label.setAlignment(Qt.Qt.AlignCenter)

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.move(20, 30)
        self.label2.setStyleSheet("")
        self.label2.setObjectName("label2")
        self.label2.setWordWrap(True)
        self.label2.setFont(QtGui.QFont('SansSerif', 14))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.move(150, 250)
        self.pushButton.resize(180, 50)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(QtGui.QFont('SansSerif', 20))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        setStyle(self, 'style/main.stylesheet')

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("RuleWindow", "RuleWindow"))
        self.label.setText(_translate("RuleWindow", "Правила:"))
        self.label2.setText(_translate("RuleWindow", ""))
        self.pushButton.setText(_translate("RuleWindow", "Назад"))
