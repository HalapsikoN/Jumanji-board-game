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
        self.label.move(80, 20)
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont('SansSerif', 20))

        self.playerLabel = QtWidgets.QLabel(self.centralwidget)
        self.playerLabel.move(262, 20)
        self.playerLabel.setObjectName("label")
        self.playerLabel.setFont(QtGui.QFont('SansSerif', 20))

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.move(290, 20)
        self.label3.setObjectName("label")
        self.label3.setFont(QtGui.QFont('SansSerif', 20))

        self.task = QtWidgets.QLabel(self.centralwidget)
        self.task.move(40, 50)
        self.task.resize(400, 160)
        self.task.setWordWrap(True)
        self.task.setAlignment(Qt.Qt.AlignCenter)
        self.task.setObjectName("label2")
        self.task.setFont(QtGui.QFont('SansSerif', 16))

        self.doneButton = QtWidgets.QPushButton(self.centralwidget)
        self.doneButton.move(30, 230)
        self.doneButton.resize(210, 70)
        self.doneButton.setObjectName("pushButton")
        self.doneButton.setFont(QtGui.QFont('SansSerif', 18))

        self.skipButton = QtWidgets.QPushButton(self.centralwidget)
        self.skipButton.move(250, 230)
        self.skipButton.resize(210, 70)
        self.skipButton.setObjectName("pushButton")
        self.skipButton.setFont(QtGui.QFont('SansSerif', 18))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RuleWindow"))
        self.label.setText(_translate("MainWindow", "Задание для:"))
        self.task.setText(_translate("MainWindow", "Текст  задания..."))
        self.label3.setText(_translate("MainWindow", "игрока"))
        self.playerLabel.setText(_translate("MainWindow", "0"))
        self.doneButton.setText(_translate("MainWindow", "Выполнил"))
        self.skipButton.setText(_translate("MainWindow", "Не выполнил"))
