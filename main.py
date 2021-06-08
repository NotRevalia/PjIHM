import sys

from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout
from gridView import *
from crtlMouvement import *

controle = crtlMouvement()


app = QApplication(sys.argv)
windows = gridView()
windows.setController(controle)
windows.show()
sys.exit(app.exec_())
