import sys

from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QMainWindow, QAction
from gridView import *
from Model import *
from crtlMouvement import *

class MainWinddow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sokoban")
        self.setWindowIcon(QIcon("logo.png"))
        self.__model = Model()
        self.__view = gridView()
        self.__controller = crtlMouvement()
        self.__view.setModel(self.__model)
        self.__view.setController(self.__controller)
        self.__model.setView(self.__view)
        self.__controller.setView(self.__view)
        self.__controller.setModel(self.__model)
        self.setCentralWidget(self.__view)
        self.menuBarGame()
        self.__view.setFocus()
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
        self.__model = Model()
        self.__view = gridView()
        self.__controller = crtlMouvement()
        self.__view.setModel(self.__model)
        self.__view.setController(self.__controller)
        self.__model.setView(self.__view)
        self.__controller.setView(self.__view)
        self.__controller.setModel(self.__model)
        self.setCentralWidget(self.__view)
        self.__view.setFocus()
        self.show()

    def boutonQ(self):
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWinddow()
    sys.exit(app.exec_())


