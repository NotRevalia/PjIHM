import sys

from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QMainWindow, QAction, QStatusBar
from PyQt5 import QtGui
from gridView import *
from Model import *
from crtlMouvement import *
from PyQt5.QtMultimedia import QSound


class MainWinddow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.setWindowIcon(QIcon("images/logo.png"))
        self.__musicG = QSound("son/Wii.wav")
        self.__model = Model(self)
        self.__view = gridView()
        self.__controller = crtlMouvement()
        self.__view.setModel(self.__model)
        self.__view.setController(self.__controller)
        self.__model.setView(self.__view)
        self.__controller.setView(self.__view)
        self.__controller.setModel(self.__model)
        self.setCentralWidget(self.__view)
        self.menuBarGame()
        self.StatusBarGame()
        self.__view.setFocus()
        self.__musicG.play()
        self.show()

    def menuBarGame(self):
        self.bar = self.menuBar()
        self.setMenuBar(self.bar)
        self.Jeu = self.bar.addMenu("Jeu")

        self.quitGame = QAction("Quit",self)
        self.quitGame.setShortcut("Ctrl+Q")
        self.Jeu.addAction(self.quitGame)
        self.quitGame.triggered.connect(self.boutonQ)

        self.restartGame = QAction("Restart",self)
        self.restartGame.setShortcut("Ctrl+R")
        self.Jeu.addAction(self.restartGame)
        self.restartGame.triggered.connect(self.boutonR)


    def boutonR(self):
        self.close()
        self.__musicG.stop()
        self.__model = Model(self)
        self.__view = gridView()
        self.__controller = crtlMouvement()
        self.__view.setModel(self.__model)
        self.__view.setController(self.__controller)
        self.__model.setView(self.__view)
        self.__controller.setView(self.__view)
        self.__controller.setModel(self.__model)
        self.setCentralWidget(self.__view)
        self.__view.setFocus()
        self.__musicG.play()
        self.show()

    def boutonQ(self):
        sys.exit(app.exec_())

    def StatusBarGame(self):
        self.Bar = QStatusBar()
        self.setStatusBar(self.Bar)
        self.Bar.showMessage("Nombre de pas : " + str(self.__model.getPas()))

    def updatePas(self):
        self.Bar.showMessage("Nombre de pas : " + str(self.__model.getPas()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWinddow()
    sys.exit(app.exec_())


