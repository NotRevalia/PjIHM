from PyQt5 import Qt, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPainter, QPen, QBrush
from PyQt5.QtMultimedia import QSound

class gridView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.setStyleSheet("background-color:#C3C9C5")
        self.setFixedSize(450,450)
        self.__controller = None
        self.__model = None
        self.show()

    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setController(self, controller):
        self.__controller = controller
    def getController(self):
        return self.__controller
    def paintEvent(self,event):
        painter = QPainter(self)
        plateau = self.__model.getPlateau()
        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                case = plateau[j][i]
                if (case == 1):
                    r = QtCore.QRect(i*50,j*50,50,50)
                    im =QtGui.QPixmap("mur.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r,im)
                if (case == 2):
                    r = QtCore.QRect(i*50,j*50,50,50)
                    im =QtGui.QPixmap("Petite_caisse.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r,im)
                if (case == 3):
                    r = QtCore.QRect(i*50,j*50,36,50)
                    im =QtGui.QPixmap("Fighter_Front.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r,im)
                if (case == 4):
                    r = QtCore.QRect(i * 50, j * 50, 50, 50)
                    im = QtGui.QPixmap("etoile.png")
                    im = im.scaled(r.size())
                    painter.drawPixmap(r, im)

    def keyPressEvent(self,event):
        actions = [(-1,0),(0,-1),(1,0),(0,1)]
        value=event.key() - 16777234
        print(value)
        if value == 0:
            print("Gauche")
        if value == 1:
            print("Haut")
        if value == 2:
            print("Gauche")
        if value == 3:
            print("bas")
