# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.move(150, 50)
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont('SansSerif', 20))

        self.turnLabel = QtWidgets.QLabel(self.centralwidget)
        self.turnLabel.move(220, 50)
        self.turnLabel.setObjectName("label_4")
        self.turnLabel.setFont(QtGui.QFont('SansSerif', 20))

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.move(210, 80)
        self.line.resize(40, 5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.move(255, 50)
        self.label3.setFont(QtGui.QFont('SansSerif', 20))
        self.label3.setObjectName("label_3")

        self.stepLabel = QtWidgets.QLabel(self.centralwidget)
        self.stepLabel.move(100, 110)
        self.stepLabel.setFont(QtGui.QFont('SansSerif', 20))
        self.stepLabel.setObjectName("label_2")
        self.stepLabel.hide()

        self.stepLine = QtWidgets.QFrame(self.centralwidget)
        self.stepLine.move(340, 140)
        self.stepLine.resize(40, 5)
        self.stepLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.stepLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stepLine.setObjectName("line_3")
        self.stepLine.hide()

        self.stepLabelNumber = QtWidgets.QLabel(self.centralwidget)
        self.stepLabelNumber.move(350, 110)
        self.stepLabelNumber.setFont(QtGui.QFont('SansSerif', 20))
        self.stepLabelNumber.setObjectName("label_6")
        self.stepLabelNumber.hide()

        self.throwButton = QtWidgets.QPushButton(self.centralwidget)
        self.throwButton.move(60, 170)
        self.throwButton.resize(360, 120)
        self.throwButton.setObjectName("pushButton")
        self.throwButton.setFont(QtGui.QFont('SansSerif', 30))

        self.taskButton = QtWidgets.QPushButton(self.centralwidget)
        self.taskButton.move(60, 170)
        self.taskButton.resize(360, 120)
        self.taskButton.setObjectName("pushButton_2")
        self.taskButton.setFont(QtGui.QFont('SansSerif', 30))
        self.taskButton.hide()

        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.move(60, 170)
        self.nextButton.resize(360, 120)
        self.nextButton.setFont(QtGui.QFont('SansSerif', 30))
        self.nextButton.setObjectName("pushButton_3")
        self.nextButton.hide()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ход:"))
        self.throwButton.setText(_translate("MainWindow", "Бросить кости"))
        self.stepLabel.setText(_translate("MainWindow", "Количество шагов:"))
        self.label3.setText(_translate("MainWindow", "игрока"))
        self.turnLabel.setText(_translate("MainWindow", "0"))
        self.taskButton.setText(_translate("MainWindow", "Задание"))
        self.nextButton.setText(_translate("MainWindow", "Следующий игрок"))
        self.stepLabelNumber.setText(_translate("MainWindow", "0"))
