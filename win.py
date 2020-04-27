import sys
from PyQt5 import QtWidgets, QtCore
from component.winWindow import Ui_MainWindow
from Player import Player


class WinWindow(QtWidgets.QMainWindow):

    def __init__(self, player):
        super(WinWindow, self).__init__()
        self.player=player
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.playerLabel.setText(str(self.player.id+1))
        self.ui.exitButton.clicked.connect(self.btnExitClicked)

        self.show()
        # self.showFullScreen()

    def btnExitClicked(self):
        QtCore.QCoreApplication.instance().quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    global ex
    ex = WinWindow()
    sys.exit(app.exec())
