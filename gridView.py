from PyQt5 import Qt, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPainter, QPen, QBrush
from crtlMouvement import *
from PyQt5.QtMultimedia import QSound

class gridView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.setStyleSheet("background-color:#C3C9C5")
        self.__controller = None
        self.__model = None
        #0 = vide
        #1 = bloc
        #2 = caisse
        #3 = perso
        #4 = Ã©toile
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
        self.__victory.play()
        # affichage
        self.getController()
        self.show()

    def paintEvent(self,event):
        painter =QPainter(self)
        print ("test")
        for i in range(len(self.__plateau)):
            for j in range(len(self.__plateau[i])):
                case = self.__plateau[i][j]
                if (case == 1):
                    r = QtCore.QRect(i*50,j*50,50,50)
                    im =QtGui.QPixmap("mur.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r,im)
                    print(i)
                    print(j)
                    print("--")
                if (case == 2):
                    r = QtCore.QRect(i*50,j*50,50,50)
                    im =QtGui.QPixmap("Petite_caisse.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r,im)
                if (case == 3):
                    r = QtCore.QRect(i*50,j*50,50,50)
                    im =QtGui.QPixmap("Fighter_Front.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r,im)
        print("Test")
    def model(self, i, j):
        self.setGeometry(0, 0, 500, 500)
        label = QLabel(self)
        personnage = QPixmap("Fighter_Front.png")
        label.setPixmap(personnage)
        label.move(i, j)

    def caisse(self, i, j):
        self.setGeometry(0, 0, 500, 500)
        label = QLabel(self)
        personnage = QPixmap("Petite_caisse.png")
        label.setPixmap(personnage)
        label.move(i, j)

    def ArriveCaisse(self, i, j):
        self.setGeometry(0, 0, 500, 500)
        label = QLabel(self)
        personnage = QPixmap("etoile.png")
        label.setPixmap(personnage)
        label.move(i, j)

    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setController(self, controller):
        self.__controller = controller
    def getController(self):
        return self.__controller
