from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
import sys

class MyWindow(QMainWindow):

    def __init__(self):
        """Set up window size, title, and features"""
        super(MyWindow, self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Planner")
        self.initUI()

    def initUI(self):
        """Makes window features"""
        # Label
        self.label = QLabel(self)
        self.label.setText("Label oh yeah woo")
        self.label.move(50, 50)
        self.label.adjustSize()

        # Button
        self.b1 = QPushButton(self)
        self.b1.setText("Button (but in french)")
        self.b1.adjustSize()
        self.b1.clicked.connect(self.clicked) # Action when clicked

    def clicked(self):
        """Function that is executed when the button is clicked"""
        self.label.setText("Button was pressed...\nNo longer french :(")
        self.b1.setText("Button (no longer in french)")
        self.update()

    def update(self):
        """Update label size"""
        self.label.adjustSize()
        self.b1.adjustSize()

def window():
    """Draw window with appropriate exit parameters"""
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())