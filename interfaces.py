r"""
FILE CONTAINS:
    - CLI interfaces for any of the submenus (FOR WHEN CLI MODE IS CHOSEN).
    - GUI interfaces for any of the submenus (FOR WHEN GUI MODE IS CHOSEN).
    - Customizable elements for any of the interfaces (for "localization" in a sense).
"""

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QProgressBar, QPushButton
import sys
import time
import os
import linecache

#   /==== C L I   S E C T I O N ====/

def infcPlanner(file,view):
    """I pull up (the directory)"""
    print("Oh my god this shit doesn't work!!!")
    # That's because you haven't done anything with it yet idjit
    return 'stuff' # Return stuff 

#   /==== G U I   S E C T I O N====/

ProgLim = 100

if linecache.getline('config.txt', 2).capitalize()[0] == "P":
    TiPl = "Planner"
else: TiPl = "Timetable"

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
        # Splash Label
        self.label = QLabel(self)
        self.label.setText("Welcome to the PythonPlanner GUI!")
        self.label.move(25, 25)
        self.label.adjustSize()

        # Title label
        self.labelTitle = QLabel(self)
        if TiPl[0] == "T":
            self.labelTitle.setText("You are in Timetable mode.")
        elif TiPl[0] == "P":
            self.labelTitle.setText("You are in Planner mode.")
        else: self.labelTitle.setText("Broken code, please fix arigatou")
        self.labelTitle.move(50, 35)
        self.labelTitle.adjustSize()

        # Button
        self.b1 = QPushButton(self)
        self.b1.setText("Clear config file")
        self.b1.adjustSize()
        self.b1.clicked.connect(self.btnClearClicked) # Action when clicked

        # Progress bar
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(0,200,300,20)
        self.pbar.setMaximum(ProgLim)

    def btnClearClicked(self):
        """Function that is executed when the button is clicked"""
        self.label.setText("Clearing config file...")
        self.b1.setText("Clearing...")
        self.update()
        os.remove("config.txt")
        self.label.setText("Config file cleared!")
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
