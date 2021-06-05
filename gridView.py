from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QImage, QIcon





class gridView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.setFixedSize(500,500)
        self.__window = QWidget()
        self.__gridLayout =QGridLayout()
        self.grifButton = []
        self.__controller = None
        self.__model = None
        self.mur()
        self.model()
        self.show()
    def mur(self):
        label = QLabel(self)
        murs= QPixmap("mur.jpg")
        label.setPixmap(murs)
    def model(self):
        self.setGeometry(0, 0, 500, 500)
        label = QLabel(self)
        personnage = QPixmap("Fighter_Front.png")
        label.setPixmap(personnage)


    def setModel(self,model):
        self.__model = model


    def getModel(self):
        return self.__model
    def setController(self,controller):
        self.__controller = controller