import queue
import sys
import threading

from PyQt5 import QtWidgets, QtCore

from classes.Message import *
from component.mainWindow import Ui_MainWindow
from element.stripLight import ledWork
from game import GameWindow
from option import OptionWindow
from rule import RuleWindow


class MenuWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MenuWindow, self).__init__()
        self.numberOfPeople = [1, 1, 1, 1]
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.btnPlayClicked)
        self.ui.pushButton2.clicked.connect(self.btnOptionClicked)
        self.ui.pushButton3.clicked.connect(self.btnRuleClicked)
        self.ui.pushButton4.clicked.connect(self.btnQuitClicked)

        self.show()
        # self.showFullScreen()

    def btnPlayClicked(self):
        queue.put(Message(CLEAR))
        global game
        game = GameWindow(application, queue, thread)
        game.show()
        self.close()

    def btnOptionClicked(self):
        queue.put(Message(CLEAR))

        global options
        options = OptionWindow(application, queue)
        options.show()
        self.close()

    def btnRuleClicked(self):
        global rules
        rules = RuleWindow(application)
        rules.show()
        self.close()

    def btnQuitClicked(self):
        queue.put(Message(EXIT))
        thread.join()

        QtCore.QCoreApplication.instance().quit()


if __name__ == '__main__':
    global queue
    global event
    global thread

    queue = queue.Queue()
    event = threading.Event()
    thread = threading.Thread(target=ledWork, args=(queue, event))
    thread.start()

    app = QtWidgets.QApplication([])
    global application
    application = MenuWindow()
    sys.exit(app.exec())
