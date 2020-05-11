import sys

from PyQt5 import QtWidgets, QtCore

from classes.Message import *
from component.winWindow import Ui_MainWindow


class WinWindow(QtWidgets.QMainWindow):

    def __init__(self, player, queue, thread):
        super(WinWindow, self).__init__()
        self.player = player
        self.queue = queue
        self.thread = thread
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.queue.put(Message(PARTY, self.player))
        self.ui.playerLabel.setText(str(self.player.id + 1))
        self.ui.exitButton.clicked.connect(self.btnExitClicked)

        self.show()
        self.showFullScreen()

    def btnExitClicked(self):
        self.queue.put(Message(EXIT))
        self.thread.join()
        QtCore.QCoreApplication.instance().quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    global ex
    ex = WinWindow()
    sys.exit(app.exec())
