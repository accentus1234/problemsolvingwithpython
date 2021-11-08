from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplications, QMainWindow
import sys

def window():
    app = QApplications(sys.argv)
    win = QMainWindow
    win.setGeometry(200, 200, 200, 200)
    win.setWindowTitle("Will\'s Test")

    label = QtWidgets.QLabel(win)
    label.setText("My first label")
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())