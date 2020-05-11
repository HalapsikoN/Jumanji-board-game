# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt

from util.commonFunctions import setStyle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        xbutton = 140

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.move(0, 5)
        self.label.resize(480, 60)
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont('SansSerif', 40))
        self.label.setAlignment(Qt.Qt.AlignCenter)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.move(xbutton, 80)
        self.pushButton.resize(200, 50)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(QtGui.QFont('SansSerif', 20))

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.move(xbutton, 140)
        self.pushButton2.resize(200, 50)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.setFont(QtGui.QFont('SansSerif', 20))

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.move(xbutton, 200)
        self.pushButton3.resize(200, 50)
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton3.setFont(QtGui.QFont('SansSerif', 20))

        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.move(xbutton, 260)
        self.pushButton4.resize(200, 50)
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton4.setFont(QtGui.QFont('SansSerif', 20))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        setStyle(self, 'style/main.stylesheet')

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Jumanji"))
        self.pushButton.setText(_translate("MainWindow", "Играть"))
        self.pushButton2.setText(_translate("MainWindow", "Настройки"))
        self.pushButton3.setText(_translate("MainWindow", "Правила"))
        self.pushButton4.setText(_translate("MainWindow", "Выход"))
