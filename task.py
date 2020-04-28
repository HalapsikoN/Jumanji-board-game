import sys
from PyQt5 import QtWidgets
from component.taskWindow import Ui_MainWindow
from util.commonFunctions import readCurrenLine
from win import WinWindow

class TaskWindow(QtWidgets.QMainWindow):

    def __init__(self, mainWindow, player, step):
        super(TaskWindow, self).__init__()
        self.mainWindow = mainWindow
        self.player=player
        self.step=step
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.playerLabel.setText(str(self.player.id+1))
        self.ui.task.setText(readCurrenLine('text/task.txt', self.player.stripList[self.player.currentPosition]))
        self.ui.doneButton.clicked.connect(self.btnDoneClicked)
        self.ui.skipButton.clicked.connect(self.btnSkipClicked)

        self.show()
        # self.showFullScreen()

    def btnDoneClicked(self):
        self.player.currentPosition+=self.step
        if self.player.currentPosition>=(len(self.player.stripList)):
            self.mainWindow.close()
            global winWindow
            winWindow=WinWindow(self.player)
            winWindow.show()
            self.close()
        else:
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
