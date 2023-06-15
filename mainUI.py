import QtDesigner.QTImages_rc
from PyQt5 import uic , QtWidgets
#
# Styles
#

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

class LoginWindow(object):

    #
    # SETUP UI
    #

    def checkFieldsLoginUI(self):
        textUser = ""
        textPassword = ""

        def showMessage(message):
                loginUi.frame_error.show()
                loginUi.label_error.setText(message)

        # checkUser
        if not loginUi.inputText_Email.text():
                textUser = " User empty "
                loginUi.inputText_Email.setStyleSheet(style_inputTextError)
        else:
                textUser = ""
                loginUi.inputText_Email.setStyleSheet(style_inputTextOK)
        
        # checkPassword
        if not loginUi.inputText_Password.text():
                textPassword = " Password empty "
                loginUi.inputText_Password.setStyleSheet(style_inputTextError)
        else:
                textPassword = ""
                loginUi.inputText_Password.setStyleSheet(style_inputTextOK)

        # checkFields
        if textUser + textPassword != "":
                text = textUser + textPassword
                showMessage(text)
                loginUi.frame_error.setStyleSheet(stylePopupError)
        else:
                text = "Login: OK"
                if loginUi.checkbox_saveUser.isChecked():
                    text = text +" | Save User: OK"
                    showMessage(text)
                else:
                    text = text +" | Save User: NO"
                    showMessage(text)
                # Adicionar função para salvar e visualizar o novo banco
                #
                #
                loginUi.frame_error.setStyleSheet(stylePopupOK)
 
    def openLoginUI(self):
        print("openLoginUI")
        loginUi.show()
        if newDataframeUi.isVisible():
            newDataframeUi.hide()
        self.setupLoginUI()

    def setupLoginUI(self):
        #
        # FUNCTIONS
        #
        # pushbutton close popup error
        loginUi.pushButton_closeError.clicked.connect(loginUi.frame_error.hide)
        # hide frame error
        loginUi.frame_error.hide()

        # pushbutton visualizar
        loginUi.viewDFButton.clicked.connect(self.checkFieldsLoginUI)

        # pushbutton cadastrar
        loginUi.pushButton_newDf.clicked.connect(register.openNewDfUI)



# 
# CLASS REGISTER
#

class RegisterWindow(object):
    
    #
    # SETUP UI
    #

    def checkFieldsRegisterUI(self):
        textEmail = ""
        textDfName = ""
        textDfPath = ""

        def showMessage(message):
                newDataframeUi.frame_error.show()
                newDataframeUi.label_error.setText(message)

        # checkEmail
        if not newDataframeUi.inputText_email.text():
                textEmail = " Email empty "
                newDataframeUi.inputText_email.setStyleSheet(style_inputTextError)
        else:
                textEmail = ""
                newDataframeUi.inputText_email.setStyleSheet(style_inputTextOK)
        
        # checkDfName
        if not newDataframeUi.inputText_dfName.text():
                textDfName = " Df name empty "
                newDataframeUi.inputText_dfName.setStyleSheet(style_inputTextError)
        else:
                textDfName = ""
                newDataframeUi.inputText_dfName.setStyleSheet(style_inputTextOK)

        # checkDfPath
        if not newDataframeUi.inputText_dfPath.text():
                textDfPath = " Df name empty "
                newDataframeUi.inputText_dfPath.setStyleSheet(style_inputTextError)
        else:
                textDfPath = ""
                newDataframeUi.inputText_dfPath.setStyleSheet(style_inputTextOK)

        # checkFields
        if textEmail + textDfName + textDfPath != "":
                text = textEmail + textDfName + textDfPath
                showMessage(text)
                newDataframeUi.frame_error.setStyleSheet(stylePopupError)
        else:
                text = "Register: OK"
                showMessage(text)
                newDataframeUi.frame_error.setStyleSheet(stylePopupOK)
                # Adicionar função para salvar e visualizar o novo banco
                #
                #
    def openNewDfUI(self):
        print("openNewDf")
        loginUi.hide()
        newDataframeUi.show()
        self.setupRegisterUI()
        


    def setupRegisterUI(self):
        #
        # FUNCTIONS
        #

        # pushbutton close popup error
        newDataframeUi.pushButton_closeError.clicked.connect(newDataframeUi.frame_error.hide)
        newDataframeUi.frame_error.hide()

        # pushbutton adicionar novo banco
        newDataframeUi.pushButton_addNewDf.clicked.connect(self.checkFieldsRegisterUI)

        # pushbutton voltar
        newDataframeUi.pushButton_back.clicked.connect(login.openLoginUI)


if __name__ == "__main__":
    # instance app
    app = QtWidgets.QApplication([])
    # loading Ui
    loginUi = uic.loadUi('QtDesigner/login.ui')
    newDataframeUi = uic.loadUi('QtDesigner/newDF.ui')

    # instance classes
    login = LoginWindow()
    register = RegisterWindow()

    # functions
    login.openLoginUI()
    # newDataframeUi.hide()
    app.exec_()
 
