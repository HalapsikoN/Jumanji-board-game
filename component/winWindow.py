# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ruleWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.move(0, 20)
        self.label.resize(480, 40)
        self.label.setAlignment(Qt.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont('SansSerif', 30))

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.move(0, 70)
        self.label1.resize(480, 40)
        self.label1.setAlignment(Qt.Qt.AlignCenter)
        self.label1.setObjectName("label")
        self.label1.setFont(QtGui.QFont('SansSerif', 25))

        self.playerLabel = QtWidgets.QLabel(self.centralwidget)
        self.playerLabel.move(0, 120)
        self.playerLabel.resize(480, 40)
        self.playerLabel.setAlignment(Qt.Qt.AlignCenter)
        self.playerLabel.setObjectName("label")
        self.playerLabel.setFont(QtGui.QFont('SansSerif', 35))

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.move(0, 170)
        self.label3.resize(480, 40)
        self.label3.setAlignment(Qt.Qt.AlignCenter)
        self.label3.setObjectName("label")
        self.label3.setFont(QtGui.QFont('SansSerif', 30))

        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.move(80, 230)
        self.exitButton.resize(320, 70)
        self.exitButton.setObjectName("pushButton")
        self.exitButton.setFont(QtGui.QFont('SansSerif', 18))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RuleWindow"))
        self.label.setText(_translate("MainWindow", "Поздравляем"))
        self.label1.setText(_translate("MainWindow", "игрока"))
        self.playerLabel.setText(_translate("MainWindow", "0"))
        self.label3.setText(_translate("MainWindow", "с победой!!!"))
        self.exitButton.setText(_translate("MainWindow", "Выход"))
