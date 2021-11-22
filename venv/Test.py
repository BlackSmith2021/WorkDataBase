from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.addItem("Staff")





app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
app.exec_()
