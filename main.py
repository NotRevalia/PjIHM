import sys

from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout
from gridView import *
from Model import *
from crtlMouvement import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = Model()
    view = gridView()
    controller =crtlMouvement()
    view.setModel(model)
    view.setController(controller)
    model.setView(view)
    controller.setView(view)
    controller.setModel(model)
    sys.exit(app.exec_())
