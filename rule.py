import sys

from PyQt5 import QtWidgets

from component.ruleWindow import Ui_MainWindow


class RuleWindow(QtWidgets.QMainWindow):

    def __init__(self, mainWindow):
        super(RuleWindow, self).__init__()
        self.mainWindow = mainWindow
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        file = open('text/rules.txt', 'r', encoding='utf-8')
        rules = file.read()
        self.ui.label2.setText(rules)
        self.ui.label2.adjustSize()

        self.ui.pushButton.clicked.connect(self.btnBackClicked)

        self.show()
        self.showFullScreen()

    def btnBackClicked(self):
        self.mainWindow.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    global ex
    ex = RuleWindow()
    sys.exit(app.exec())
