import sys

from PyQt5 import QtWidgets
from QtDesigner.loginUI import LoginWindow
# from QtDesigner.mainMenuUI import MainMenuWindow
# from QtDesigner.registerUI import RegisterWindow


if __name__ == "__main__":
        # instance app
        app = QtWidgets.QApplication([])
        loginMenu = LoginWindow()
        loginMenu.show()
        # mainMenu = MainMenuWindow()
        # mainMenu.show()
        # registerMenu = RegisterWindow()
        # registerMenu.show()
        app.exec_()