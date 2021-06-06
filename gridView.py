from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPainter, QPen


class gridView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.setStyleSheet("background-color:#C3C9C5")
        self.setFixedSize(1057,1057)
        self.__window = QWidget()
        self.__gridLayout =QGridLayout()
        self.gridButton = []
        self.__controller = None
        self.__model = None
        for i in range(0,1057,906):
            for j in range(0,1057,151):
                self.mur(i,j)
        for i in range(0,1057,151):
            self.mur2(i)
        for i in range(0, 1057, 151):
            self.mur3(i)
        self.mur4(151,302)
        self.mur4(302, 302)
        self.ArriveCaisse()
        self.caisse(453,151)
        self.model(453,453)
        self.show()


    def mur(self,i,j):
        label = QLabel(self)
        murs= QPixmap("mur.jpg")
        label.setPixmap(murs)
        label.move(i,j)
    def mur2(self,i):
        label = QLabel(self)
        murs= QPixmap("mur.jpg")
        label.setPixmap(murs)
        label.move(i,0)
    def mur3(self,i):
        label = QLabel(self)
        murs= QPixmap("mur.jpg")
        label.setPixmap(murs)
        label.move(i,849)
    def mur4(self,i,j):
        label = QLabel(self)
        murs= QPixmap("mur.jpg")
        label.setPixmap(murs)
        label.move(i,j)
    def model(self,i,j):
        self.setGeometry(0, 0, 500, 500)
        label = QLabel(self)
        personnage = QPixmap("Fighter_Front.png")
        label.setPixmap(personnage)
        label.move(i,j)
    def caisse(self,i,j):
        self.setGeometry(0, 0, 500, 500)
        label = QLabel(self)
        personnage = QPixmap("Petite_caisse.png")
        label.setPixmap(personnage)
        label.move(i, j)
    def ArriveCaisse(self):
        self.setGeometry(0, 0, 500, 500)
        label = QLabel(self)
        personnage = QPixmap("gris.png")
        label.setPixmap(personnage)
        label.move(151, 151)





    def setModel(self,model):
        self.__model = model


    def getModel(self):
        return self.__model
    def setController(self,controller):
        self.__controller = controller