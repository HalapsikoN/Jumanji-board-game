from PyQt5 import QtWidgets, QtCore
from component.mainWindow import Ui_MainWindow
from rule import RuleWindow
from option import OptionWindow
from stripLight import ledWork
from game import GameWindow
import sys
import queue
import threading


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

        # self.setWindowTitle('Icon')
        # self.setWindowIcon(QIcon('web.png'))
        # btn = QPushButton('Quit', self)

        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.clicked.connect(QCoreApplication.instance().quit)
        # btn.resize(btn.sizeHint())
        # btn.move(50, 50)

    def btnPlayClicked(self):
        # print(event.is_set())
        # event.set()
        # print(self.numberOfPeople)
        # print(event.is_set())
        global game
        game = GameWindow(application)
        game.show()
        self.close()

    def btnOptionClicked(self):
        global options
        options = OptionWindow(application)
        options.show()
        self.close()

    def btnRuleClicked(self):
        global rules
        rules = RuleWindow(application)
        rules.show()
        self.close()

    def btnQuitClicked(self):
        event.set()
        thread.join()
        QtCore.QCoreApplication.instance().quit()



if __name__ == '__main__':
    global queue
    global event
    global thread

    queue = queue.Queue(maxsize=10)
    event = threading.Event()
    thread = threading.Thread(target=ledWork, args=(queue, event))
    thread.start()

    app = QtWidgets.QApplication([])
    global application
    application = MenuWindow()
    sys.exit(app.exec())
