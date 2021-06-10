from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPainter, QPen
from PyQt5.QtMultimedia import QSound
from gridView import *

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

    def checkD(self,a,b):
        plateau = self.__model.getPlateau()
        if(plateau[a][b+1]==2):
            plateau[a][b+1]=0
            plateau[a][b+2]=2
            print("Caisse")
        if(plateau[a][b+1]==1):
            self.__son=QSound("quack.wav")
            self.__son.play()
            print("Mur")

    def checkH(self,a,b):
        plateau = self.__model.getPlateau()
        if (plateau[a-1][b] == 2):
            plateau[a-1][b]=0
            plateau[a-2][b]=2
            print("Caisse")
        if (plateau[a-1][b] == 1):
            self.__son = QSound("quack.wav")
            self.__son.play()
            print("Mur")

    def checkG(self,a,b):
        plateau = self.__model.getPlateau()
        if(plateau[a][b-1]==2):
            plateau[a][b-1]=0
            plateau[a][b-2]=2
            print("Caisse")
        if(plateau[a][b-1]==1):
            self.__son=QSound("quack.wav")
            self.__son.play()
            print("Mur")

    def checkB(self,a,b):
        plateau = self.__model.getPlateau()
        if(plateau[a+1][b]==2):
            plateau[a+1][b]=0
            plateau[a+2][b]=2
            print("Caisse")
        if(plateau[a+1][b]==1):
            self.__son=QSound("quack.wav")
            self.__son.play()
            print("Mur")


