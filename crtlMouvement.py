from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPainter, QPen

class crtlMouvement(QWidget):
    def __init__(self):
        super().__init__()
        self.__y = 500
        self.__i = 500
        self.__views = []
        self.__model = None
        self.__controller = None
        self.__view =None

    def setModel(self,model):
        self.__model = model
    def getModel(self):
        return self.__model
    def setController(self, controller):
        self.__controller = controller
    def getController(self):
        return self.__controller
    def setView (self,view):
        self.__view = view
    def getView (self):
        return self.__view