import sys

from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout
from gridView import *



app = QApplication(sys.argv)

windows = gridView()
windows.show()
sys.exit(app.exec_())
