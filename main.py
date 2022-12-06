import math
import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'C:\Users\79082\PycharmProjects\pythonProject9\venv\untitled.ui', self)
        self.run()

    def run(self):
        self.pushButton.clicked.connect(self.hello)

    def hello(self):
        self.n = QListWidget(self)
        self.n.addItem('')
        s = self.lineEdit_2.text() + ' ' + self.lineEdit.text()
        self.listWidget_2.addItem(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
