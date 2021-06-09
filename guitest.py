r"""
Various tests for the PyQt5 modules and submodules.
"""
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QProgressBar, QPushButton
import sys
import time

ProgLim = 100

class External(QThread):
    """Runs a counter thread"""
    countChanged = pyqtSignal(int)

    def run(self):
        count = 0
        while count < ProgLim:
            count += 1
            self.countChanged.emit(count)

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

        # Progress bar
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(0,100,300,20)
        self.pbar.setMaximum(ProgLim)

    def clicked(self):
        """Function that is executed when the button is clicked"""
        self.label.setText("Button was pressed...\nNo longer french :(")
        self.b1.setText("Button (no longer in french)")
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start
        self.update()


    def update(self):
        """Update label size"""
        self.label.adjustSize()
        self.b1.adjustSize()

    def onCountChanged(self, value):
        self.pbar.setValue(value)

def wdwProg():
    """Draw window with appropriate exit parameters"""
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
