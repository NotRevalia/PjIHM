from PyQt5.QtWidgets import QWidget ,QMainWindow,QGridLayout,QPushButton
from PyQt5.QtGui import QPixmap,QImage,QIcon

class gridView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.setFixedSize(500,500)
        self.__window = QWidget()
        self.__gridLayout =QGridLayout()
        self.grifButton = []
        model = QImage("Fighter_Front.png",'png')
        self.__model = model
        self.__controller = None
    def setModel(self,model):
        self.__model = model


    def setController(self,controller):
        self.__controller = controller

    def display(self):
        assert self.__model is not None


