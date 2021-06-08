from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPainter, QPen
from crtlMouvement import *

class gridView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.setStyleSheet("background-color:#C3C9C5")
        self.setFixedSize(1000, 1000)
        self.__window = QWidget()
        self.__gridLayout = QGridLayout()
        self.gridButton = []
        self.__controller = None
        self.__model = None
        # placement des murs
        for i in range(0, 1000, 900):
            for j in range(0, 1000, 100):
                self.mur(i, j)
        for i in range(0, 1000, 100):
            self.mur(i, 0)
        for i in range(0, 1000, 100):
            self.mur(i, 900)
        for i in range(100, 1000, 100):
            self.mur(i, 800)
        for i in range(100, 1000, 100):
            self.mur(800, i)
            self.mur(700, i)
        for i in range(100, 600, 100):
            self.mur(600, i)
        self.mur(100, 300)
        self.mur(300, 400)
        self.mur(200, 300)
        self.mur(100, 100)
        self.mur(200, 100)
        self.mur(200, 400)
        self.mur(200, 500)
        # placement des etoile ou il faut mettre les caisse
        self.ArriveCaisse(100, 200)
        self.ArriveCaisse(300, 600)
        self.ArriveCaisse(100, 400)
        self.ArriveCaisse(400, 700)
        self.ArriveCaisse(600, 600)
        self.ArriveCaisse(400, 500)
        self.ArriveCaisse(500, 400)
        # placement des caisse
        self.caisse(400, 400)
        self.caisse(400, 300)
        self.caisse(100, 600)
        self.caisse(300, 600)
        self.caisse(400, 600)
        self.caisse(500, 600)
        self.caisse(300, 200)
        self.model(200, 200)
        # affichage
        self.getController()
        self.show()

    def mur(self, i, j):
        label = QLabel(self)
        murs = QPixmap("mur.png")
        label.setPixmap(murs)
        label.move(i, j)

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
