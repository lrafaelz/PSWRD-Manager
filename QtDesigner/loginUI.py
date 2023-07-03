import os
import QtDesigner.QTImages_rc
from PyQt5 import uic , QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QPushButton, QCheckBox
from QtDesigner.mainMenuUI import MainMenuWindow

# from mainMenuUI import MainMenuWindow
# from registerUI import RegisterWindow

style_inputTextOK = ("QLineEdit{\n"
"    border: 2px solid rgb(14, 78, 20);\n"
"    border-radius: 5px ; \n"
"    padding: 15px;\n"
"    background-color: rgb(254, 254, 254);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border:2px solid  rgb(254, 254, 254); \n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    color: rgb(000, 000, 000);\n"
"    border:2px solid  rgb(14, 78, 20); \n"
"}")
    
style_inputTextError = ("QLineEdit{\n"
"    border: 2px solid rgb(255, 61, 61);\n"
"    border-radius: 5px ; \n"
"    padding: 15px;\n"
"    background-color: rgb(254, 254, 254);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border:2px solid  rgb(254, 254, 254); \n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    color: rgb(000, 000, 000);\n"
"    border:2px solid  rgb(14, 78, 20); \n"
"}")
    
stylePopupError = ("background-color: rgb(255, 61, 61); border-radius: 8px; position: absolute;")
stylePopupOK = ("background-color: rgb(24, 178, 38); border-radius: 8px; position: absolute;")


#
# CLASS LOGIN
#

class LoginWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        file_path = os.path.abspath("QtDesigner/filesUI/login.ui")
        uic.loadUi(file_path, self)
        #
        # FUNCTIONS
        #
        # pushbutton close popup error
        self.pushButton_closeError.clicked.connect(self.frame_error.hide)
        # hide frame error
        self.frame_error.hide()

        # pushbutton visualizar
        self.viewDFButton.clicked.connect(self.checkFieldsLoginUI)
        # self.finished.connect(self.open_mainMenu)

        # # pushbutton cadastrar
        self.pushButton_newDf.clicked.connect(self.open_registerMenu)
        # if newDataframeUi.isVisible():
        #     newDataframeUi.hide()

          

    #
    # SETUP UI
    #

    def checkFieldsLoginUI(self):
        textUser = ""
        textPassword = ""

        def showMessage(message):
                self.frame_error.show()
                self.label_error.setText(message)

        # checkUser
        if not self.inputText_Email.text():
                textUser = " User empty "
                self.inputText_Email.setStyleSheet(style_inputTextError)
        else:
                textUser = ""
                self.inputText_Email.setStyleSheet(style_inputTextOK)
        
        # checkPassword
        if not self.inputText_Password.text():
                textPassword = " Password empty "
                self.inputText_Password.setStyleSheet(style_inputTextError)
        else:
                textPassword = ""
                self.inputText_Password.setStyleSheet(style_inputTextOK)

        # checkFields
        if textUser + textPassword != "":
                text = textUser + textPassword
                showMessage(text)
                self.frame_error.setStyleSheet(stylePopupError)
        else:
                text = "Login: OK"
                if self.checkbox_saveUser.isChecked():
                    text = text +" | Save User: OK"
                    showMessage(text)
                else:
                    text = text +" | Save User: NO"
                    showMessage(text)
                # Adicionar função para salvar e visualizar o novo banco
                #
                #
                self.frame_error.setStyleSheet(stylePopupOK)
                self.open_mainMenu()

    def open_mainMenu(self):
        mainMenu = MainMenuWindow()
        mainMenu.show()
        self.hide()

    def open_registerMenu(self):
        from QtDesigner.registerUI import RegisterWindow
        register = RegisterWindow()
        register.show()
        self.hide()
