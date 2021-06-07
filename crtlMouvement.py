from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPainter, QPen

class crtlMouvement(QWidget):
    def mouvement(self,event):
        key = event.key()
        print(key)