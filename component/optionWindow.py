# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ruleWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from util.commonFunctions import setStyle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("OptionWindow")
        MainWindow.resize(480, 320)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.move(100, 20)
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont('SansSerif', 16))

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.move(195, 80)
        self.comboBox.resize(90, 50)
        self.comboBox.setFont(QtGui.QFont('SansSerif', 16))
        self.comboBox.setObjectName("comboBox")

        self.autoButton = QtWidgets.QPushButton(self.centralwidget)
        self.autoButton.move(150, 140)
        self.autoButton.resize(180, 50)
        self.autoButton.setObjectName("pushButton")

        self.chooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseButton.move(60, 250)
        self.chooseButton.resize(180, 50)
        self.chooseButton.setObjectName("pushButton2")

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.move(250, 250)
        self.backButton.resize(180, 50)
        self.backButton.setObjectName("pushButton3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        setStyle(self, 'style/option.stylesheet')

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("OptionWindow", "OptionWindow"))
        self.label.setText(_translate("OptionWindow", "Choose the number of people:"))
        self.autoButton.setText(_translate("OptionWindow", "Auto"))
        self.chooseButton.setText(_translate("OptionWindow", "Choose"))
        self.backButton.setText(_translate("OptionWindow", "Back"))
