import sys  # send arguments to application
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window(): # Function to launch application
    app = QApplication(sys.argv) # initializes a Qt application and allows it to handle command-line arguments
    win = QMainWindow() # create a desktop window

    win.setGeometry(600, 40, 700, 650) # top left coordinate, width, height
    win.setWindowTitle("TestApp")
    win.setWindowIcon(QIcon("test.jpg"))
    win.setToolTip("CurrPage")

    lbl_API_Key = QtWidgets.QLabel(win) # create a label
    lbl_API_Key.setText('API Key :')
    lbl_API_Key.move(40, 50)

    lbl_Secret = QtWidgets.QLabel(win) # create a label
    lbl_Secret.setText('Secret :')
    lbl_Secret.move(40, 90)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150, 50)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150, 90)

    win.show() # Show the desktop window
    sys.exit(app.exec_()) # send argument to close app when close button clicked

window()