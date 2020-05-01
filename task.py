import sys

from PyQt5 import QtWidgets

from classes.Message import *
from component.taskWindow import Ui_MainWindow
from util.commonFunctions import readCurrenLine
from win import WinWindow


class TaskWindow(QtWidgets.QMainWindow):

    def __init__(self, mainWindow, player, step, queue, thread):
        super(TaskWindow, self).__init__()
        self.mainWindow = mainWindow
        self.player = player
        self.step = step
        self.queue = queue
        self.thread = thread
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.playerLabel.setText(str(self.player.id + 1))
        self.ui.task.setText(readCurrenLine('text/task.txt'))
        self.ui.doneButton.clicked.connect(self.btnDoneClicked)
        self.ui.skipButton.clicked.connect(self.btnSkipClicked)

        self.show()
        # self.showFullScreen()

    def btnDoneClicked(self):
        print(self.player)
        self.player.lastPosition = self.player.currentPosition
        self.player.currentPosition += self.step
        if self.player.currentPosition >= (len(self.player.stripList)):
            self.queue.put(Message(CLEAR))

            self.mainWindow.close()
            global winWindow
            winWindow = WinWindow(self.player, self.queue, self.thread)
            winWindow.show()
            self.close()
        else:
            self.queue.put(Message(SET_NEW_POINT, self.player))

            self.mainWindow.show()
            self.close()

    def btnSkipClicked(self):
        self.mainWindow.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    global ex
    ex = TaskWindow()
    sys.exit(app.exec())
