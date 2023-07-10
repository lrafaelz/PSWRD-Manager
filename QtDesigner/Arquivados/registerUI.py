import os
from PyQt5 import uic , QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QPushButton, QCheckBox
from QtDesigner.mainMenuUI import MainMenuWindow


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

class RegisterWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super().__init__()
                file_path = os.path.abspath("QtDesigner/filesUI/newDF.ui")
                uic.loadUi(file_path, self)
                #
                # FUNCTIONS
                #
                print("open_registerMenu")

                # pushbutton close popup error
                self.pushButton_closeError.clicked.connect(self.frame_error.hide)
                self.frame_error.hide()

                # pushbutton adicionar novo banco
                self.pushButton_addNewDf.clicked.connect(self.checkFieldsRegisterUI)

                # pushbutton voltar
                self.pushButton_back.clicked.connect(self.openLoginMenu)

        def checkFieldsRegisterUI(self):
                textEmail = ""
                textDfName = ""
                textDfPath = ""

                def showMessage(message):
                        self.frame_error.show()
                        self.label_error.setText(message)

                # checkEmail
                if not self.inputText_email.text():
                        textEmail = " Email empty "
                        self.inputText_email.setStyleSheet(style_inputTextError)
                else:
                        textEmail = ""
                        self.inputText_email.setStyleSheet(style_inputTextOK)
                
                # checkDfName
                if not self.inputText_dfName.text():
                        textDfName = " Df name empty "
                        self.inputText_dfName.setStyleSheet(style_inputTextError)
                else:
                        textDfName = ""
                        self.inputText_dfName.setStyleSheet(style_inputTextOK)

                # checkDfPath
                if not self.inputText_dfPath.text():
                        textDfPath = " Df name empty "
                        self.inputText_dfPath.setStyleSheet(style_inputTextError)
                else:
                        textDfPath = ""
                        self.inputText_dfPath.setStyleSheet(style_inputTextOK)

                # checkFields
                if textEmail + textDfName + textDfPath != "":
                        text = textEmail + textDfName + textDfPath
                        showMessage(text)
                        self.frame_error.setStyleSheet(stylePopupError)
                else:
                        text = "Register: OK"
                        showMessage(text)
                        # Adicionar função para salvar e visualizar o novo banco
                        #


        def openLoginMenu(self):
                from QtDesigner.loginUI import LoginWindow
                self.loginMenu = LoginWindow()
                self.loginMenu.show()
                self.hide()


        def openNewDfUI(self):
                print("openNewDf")
                mainMenu = MainMenuWindow()
                mainMenu.show()
                self.hide()