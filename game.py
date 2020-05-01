import random
import sys

from PyQt5 import QtWidgets

from classes.Player import Player
from component.gameWindow import Ui_MainWindow
from task import TaskWindow
from util.commonFunctions import readPlayersBillsAddreses


def initPlayers(initPlayerList):
    initPlayerList = list(initPlayerList)
    result = []
    playerBillsAddresses = readPlayersBillsAddreses('text/playersBillsAddresses.txt')
    if (initPlayerList[0] == 1):
        result.append(Player(0, playerBillsAddresses[0], (255, 0, 0)))
    if (initPlayerList[1] == 1):
        result.append(Player(1, playerBillsAddresses[1], (0, 255, 0)))
    if (initPlayerList[2] == 1):
        result.append(Player(2, playerBillsAddresses[2], (0, 0, 255)))
    if (initPlayerList[3] == 1):
        result.append(Player(3, playerBillsAddresses[3], (255, 255, 0)))
    return result


class GameWindow(QtWidgets.QMainWindow):

    def __init__(self, mainWindow, queue, thread):
        super(GameWindow, self).__init__()
        self.mainWindow = mainWindow
        self.queue = queue
        self.thread = thread

        self.initPlayerList = list(self.mainWindow.numberOfPeople)
        self.playerList = initPlayers(self.initPlayerList)
        self.turn = random.randrange(0, len(self.playerList) - 1)
        self.step = 0

        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.turnLabel.setText(str(self.playerList[self.turn].id + 1))

        self.ui.throwButton.clicked.connect(self.btnThrowClicked)
        self.ui.taskButton.clicked.connect(self.btnTaskClicked)
        self.ui.nextButton.clicked.connect(self.btnNextClicked)

        self.show()
        # self.showFullScreen()

    def btnThrowClicked(self):
        self.step = random.randrange(1, 7)
        self.ui.stepLabelNumber.setText(str(self.step))
        self.ui.stepLabelNumber.show()
        self.ui.stepLabel.show()
        self.ui.stepLine.show()
        self.ui.throwButton.hide()
        self.ui.taskButton.show()

    def btnTaskClicked(self):
        global taskWindow
        taskWindow = TaskWindow(self, self.playerList[self.turn], self.step, self.queue, self.thread)
        taskWindow.show()
        self.hide()
        self.ui.taskButton.hide()
        self.ui.nextButton.show()

    def btnNextClicked(self):
        if self.turn == len(self.playerList) - 1:
            self.turn = 0
        else:
            self.turn = self.turn + 1
        self.initUI()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    global application
    application = GameWindow()
    sys.exit(app.exec())
