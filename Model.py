from PyQt5 import Qt, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPainter, QPen, QBrush
from crtlMouvement import *
from PyQt5.QtMultimedia import QSound

class Model(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.setStyleSheet("background-color:#C3C9C5")
        self.__controller = None
        self.__model = None
        self.__view =None
        self.__plateau = [[0,0,0,1,1,1,1,1,1,1],
                    [1,1,1,0,0,0,1,1,0,0],
                    [1,4,3,2,0,0,1,1,0,0],
                    [1,1,1,0,2,0,1,1,0,0],
                    [1,4,1,1,2,4,1,0,0,0],
                    [1,0,1,0,4,0,1,1,0,0],
                    [1,2,0,2,2,2,4,1,1,1],
                    [1,0,0,0,4,0,0,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1]]
        self.__victory = QSound("victoryFF.wav")
        #self.__victory.play()
    def setModel(self, model):
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
    def getPlateau(self):
        return self.__plateau