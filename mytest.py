import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   w.setWindowTitle("PyQt6")
   w.show()
   sys.exit(app.exec())

if __name__ == '__main__':
   window()
