from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPainter, QPen

class crtlMouvement(QWidget):
    def __init__(self):
        self.__y = 500
        self.__i = 500
        self.__views = []
        self.__model = None
        self.__controller = None

    def keyPressEvent(self,event):
        print(event.key)
        KeyLeft = 16777234
        KeyUp = 16777235
        KeyRight = 16777236
        KeyDown = 16777237

        if (event.key == KeyLeft):
            self.__i = self.__i + 100
            #if gridView.caisse(i,j) == gridView.model(i,j):
                #gridView.caisse(i+100,j)
                #gridView.modele(i,j)

            #self.show()3
            print("bouge vers la gauche")

        if (event.key == KeyUp):
            print("bouge vers le Haut")
        if (event.key == KeyRight):
            print("bouge vers la droite")
        if (event.key == KeyDown):
            print("bouge vers le bas")


    def setModel(self,model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setController(self, controller):
        self.__controller = controller
    def getController(self):
        return self.__controller