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
        MainWindow.setObjectName("OptionWindow")
        MainWindow.resize(480, 320)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.move(0, 0)
        self.label.resize(480, 60)
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont('SansSerif', 20))
        self.label.setAlignment(Qt.Qt.AlignCenter)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.move(195, 70)
        self.comboBox.resize(90, 50)
        self.comboBox.setFont(QtGui.QFont('SansSerif', 16))
        self.comboBox.setObjectName("comboBox")

        self.randomButton = QtWidgets.QPushButton(self.centralwidget)
        self.randomButton.move(150, 130)
        self.randomButton.resize(180, 50)
        self.randomButton.setObjectName("pushButton")
        self.randomButton.setFont(QtGui.QFont('SansSerif', 20))

        self.autoButton = QtWidgets.QPushButton(self.centralwidget)
        self.autoButton.move(150, 190)
        self.autoButton.resize(180, 50)
        self.autoButton.setObjectName("pushButton")
        self.autoButton.setFont(QtGui.QFont('SansSerif', 20))

        self.chooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseButton.move(60, 250)
        self.chooseButton.resize(180, 50)
        self.chooseButton.setObjectName("pushButton2")
        self.chooseButton.setFont(QtGui.QFont('SansSerif', 20))

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.move(250, 250)
        self.backButton.resize(180, 50)
        self.backButton.setObjectName("pushButton3")
        self.backButton.setFont(QtGui.QFont('SansSerif', 20))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        setStyle(self, 'style/main.stylesheet')

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("OptionWindow", "OptionWindow"))
        self.label.setText(_translate("OptionWindow", "Выберите количество игроков:"))
        self.randomButton.setText(_translate("OptionWindow", "Случайно"))
        self.chooseButton.setText(_translate("OptionWindow", "Сохранить"))
        self.autoButton.setText(_translate("OptionWindow", "Авто"))
        self.backButton.setText(_translate("OptionWindow", "Назад"))
