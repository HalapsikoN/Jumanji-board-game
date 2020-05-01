import random
import sys

from PyQt5 import QtWidgets

from classes.Message import *
from component.optionWindow import Ui_MainWindow


class OptionWindow(QtWidgets.QMainWindow):
    def __init__(self, mainWindow, queue):
        super(OptionWindow, self).__init__()
        self.mainWindow = mainWindow
        self.queue = queue
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.addItem("2", [1, 0, 1, 0])
        self.ui.comboBox.addItem("3", [1, 1, 1, 0])
        self.ui.comboBox.addItem("4", [1, 1, 1, 1])
        self.ui.comboBox.setCurrentIndex(self.ui.comboBox.findData(self.mainWindow.numberOfPeople))
        self.queue.put(Message(OPTION_CHOOSE, self.ui.comboBox.currentData()))

        self.ui.comboBox.currentIndexChanged.connect(self.comboBoxChanged)

        self.ui.autoButton.clicked.connect(self.btnAutoClicked)

        self.ui.chooseButton.clicked.connect(self.btnChooseClicked)

        self.ui.backButton.clicked.connect(self.btnBackClicked)

        self.show()
        # self.showFullScreen()

    def comboBoxChanged(self):
        self.queue.put(Message(OPTION_CHOOSE, self.ui.comboBox.currentData()))

    def btnAutoClicked(self):
        self.ui.comboBox.setCurrentIndex(random.randrange(3))

    def btnChooseClicked(self):
        self.queue.put(Message(CLEAR))
        self.queue.put(Message(START_UP_FUNCTION))

        self.mainWindow.numberOfPeople = self.ui.comboBox.currentData()
        self.mainWindow.show()
        self.close()

    def btnBackClicked(self):
        self.queue.put(Message(CLEAR))
        self.queue.put(Message(START_UP_FUNCTION))

        self.mainWindow.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    global ex
    ex = OptionWindow()
    sys.exit(app.exec())
