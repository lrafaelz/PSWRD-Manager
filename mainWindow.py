import os
import QtDesigner.QTImages_rc
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGridLayout, QDialog
import styles as st

# Carregar o arquivo mainWindow.ui
file_path = os.path.abspath("QtDesigner/filesUI/mainWindow.ui")
Ui_MainWindow, QtBaseClass = uic.loadUiType(file_path)

class MainWindow(QMainWindow, Ui_MainWindow):
    
    # Criar um layout vertical para receber telas
    mainLayout = QVBoxLayout()

    # variaveis para receber os widgets
    loginWidget = None
    registerWidget = None
    mainMenuWidget = None
    addPSWRDModal = None

    decryptoKey = None

##############################################################################################################

    def __init__(self): # loginMenu initialization
        super().__init__()
        self.setupUi(self)

        # Carregar o widget loginWindowWidget.ui
        self.loginWidget = QWidget()
        file_path = os.path.abspath("QtDesigner/filesUI/loginWindowWidget.ui")
        uic.loadUi(file_path, self.loginWidget)

        # Adicionar o widget ao layout
        self.mainLayout.addWidget(self.loginWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        # Configurar o layout como o layout central da janela principal
        centralWidget = QWidget()
        centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralWidget)

        self.loginButtonSetup()

    def loginButtonSetup(self):
        self.loginWidget.pushButton_closeError.clicked.connect(self.loginWidget.frame_error.hide)
        self.loginWidget.frame_error.hide()

        self.loginWidget.pushButton_newDf.clicked.connect(self.open_registerUI)
        
        self.loginWidget.viewDFButton.clicked.connect(self.checkFieldsLoginUI)


    # script checkFields
    def checkFieldsLoginUI(self):
        textUser = ""
        textPassword = ""

        def showMessage(message):
                self.loginWidget.frame_error.show()
                self.loginWidget.label_error.setText(message)

        # checkUser
        if not self.loginWidget.inputText_Email.text():
                textUser = " User empty "
                self.loginWidget.inputText_Email.setStyleSheet(st.style_inputTextError)
        else:
                textUser = ""
                self.loginWidget.inputText_Email.setStyleSheet(st.style_inputTextOK)
        
        # checkPassword
        if not self.loginWidget.inputText_Password.text():
                textPassword = " Password empty "
                self.loginWidget.inputText_Password.setStyleSheet(st.style_inputTextError)
        else:
                textPassword = ""
                self.loginWidget.inputText_Password.setStyleSheet(st.style_inputTextOK)

        # checkFields
        if textUser + textPassword != "":
                text = textUser + textPassword
                showMessage(text)
                self.loginWidget.frame_error.setStyleSheet(st.stylePopupError)
        else:
                text = "Login: OK"
                if self.loginWidget.checkbox_saveUser.isChecked():
                    text = text +" | Save User: OK"
                    showMessage(text)
                else:
                    text = text +" | Save User: NO"
                    showMessage(text)
                # Adicionar função para salvar e visualizar o novo banco
                #
                #
                self.loginWidget.frame_error.setStyleSheet(st.stylePopupOK)
                self.open_mainMenuUI()

############################################################################################################

    def open_registerUI(self):
        self.registerWidget = QWidget()
        file_path = os.path.abspath("QtDesigner/filesUI/registerWindowWidget.ui")
        uic.loadUi(file_path, self.registerWidget)

        # Adicionar o widget ao layout
        self.loginWidget.hide()
        self.mainLayout.addWidget(self.registerWidget)

        # Configurar o layout como o layout central da janela principal
        centralWidget = QWidget()
        centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralWidget)

        self.registerButtonSetup()

    def registerButtonSetup(self):
        self.registerWidget.frame_error.hide()
        self.registerWidget.pushButton_closeError.clicked.connect(self.registerWidget.frame_error.hide)

        # pushbutton adicionar novo banco
        self.registerWidget.pushButton_addNewDf.clicked.connect(self.checkFieldsRegisterUI)

        # pushbutton voltar
        self.registerWidget.pushButton_back.clicked.connect(self.openLoginUI)

    def checkFieldsRegisterUI(self):
                textEmail = ""
                textDfName = ""
                textDfPath = ""

                def showMessage(message):
                        self.registerWidget.frame_error.show()
                        self.registerWidget.label_error.setText(message)

                # checkEmail
                if not self.registerWidget.inputText_email.text():
                        textEmail = " Email empty "
                        self.registerWidget.inputText_email.setStyleSheet(st.style_inputTextError)
                else:
                        textEmail = ""
                        self.registerWidget.inputText_email.setStyleSheet(st.style_inputTextOK)
                
                # checkDfName
                if not self.registerWidget.inputText_dfName.text():
                        textDfName = " Df name empty "
                        self.registerWidget.inputText_dfName.setStyleSheet(st.style_inputTextError)
                else:
                        textDfName = ""
                        self.registerWidget.inputText_dfName.setStyleSheet(st.style_inputTextOK)

                # checkDfPath
                if not self.registerWidget.inputText_dfPath.text():
                        textDfPath = " Df name empty "
                        self.registerWidget.inputText_dfPath.setStyleSheet(st.style_inputTextError)
                else:
                        textDfPath = ""
                        self.registerWidget.inputText_dfPath.setStyleSheet(st.style_inputTextOK)

                # checkFields
                if textEmail + textDfName + textDfPath != "":
                        text = textEmail + textDfName + textDfPath
                        showMessage(text)
                        self.registerWidget.frame_error.setStyleSheet(st.stylePopupError)
                else:
                        text = "Register: OK"
                        showMessage(text)
                        self.registerWidget.frame_error.setStyleSheet(st.stylePopupOK)

                        # Adicionar função para salvar e visualizar o novo banco
                        self.registerWidget.close()
                        self.open_mainMenuUI()
    
    def openLoginUI(self):
        self.registerWidget.hide()
        self.loginWidget.show()

############################################################################################################

    def open_mainMenuUI(self):
        self.mainMenuWidget = QWidget()
        file_path = os.path.abspath("QtDesigner/filesUI/mainMenuWidget.ui")
        self.mainMenuWidget = uic.loadUi(file_path)
        
        # Adicionar o widget ao layout
        # self.loginWidget.hide() # caso formos utilizar um timer para bloquear o banco de senhas
        self.loginWidget.close() # Poupar memória na solução sem timer
        self.mainLayout.addWidget(self.mainMenuWidget)

        # Configurar o layout como o layout central da janela principal
        centralWidget = QWidget()
        centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralWidget)

        self.refreashAppCards()

        self.mainMenuButtonSetup()

    def refreashAppCards(self):
        # Criar o layout de grid
        grid_layout = QGridLayout()

        # Definir o número máximo de frames por linha
        max_frames_por_linha = 3

        # Lista de frames
        frames = []
        import encryption.testCards as tc
        matriz_valores = tc.getTestCards()
        print(matriz_valores)

        # Adicionar frames ao layout de grid
        from appCard import AppCard
        for i in range(len(matriz_valores)):
            frame = AppCard(matriz_valores, i)
            frames.append(frame)

            # Calcular a posição do frame na grade
            linha = (i+1) // max_frames_por_linha
            coluna = (i+1) % max_frames_por_linha

            # Adicionar o frame ao layout de grid
            grid_layout.addWidget(frame, linha, coluna)

        # Configurar o frame_gridApps como o central widget da janela
        # self.setCentralWidget(frame_gridApps)
        self.mainMenuWidget.widget_gridApps.setLayout(grid_layout)

    def mainMenuButtonSetup(self):
        self.mainMenuWidget.pushButton_closeError.clicked.connect(self.mainMenuWidget.frame_error.hide)
        # hide frame error
        self.mainMenuWidget.frame_error.hide()

        # pushbutton adicionar nova senha
        self.mainMenuWidget.pushButton_addNewPSWRD.clicked.connect(self.onAddButton)

        # pushbutton visualizar senhas
        self.mainMenuWidget.pushButton_passwords.setEnabled(False)

        # pushbutton visualizar notas guardadas
        self.mainMenuWidget.pushButton_notes.clicked.connect(self.showNotesButton)

        # pushbutton visualizar senhas wifi guardadas
        self.mainMenuWidget.pushButton_wifiPass.clicked.connect(self.showWifiPassButton)
     

    def onAddButton(self):
        self.addPSWRDModal = QDialog()
        file_path = os.path.abspath("QtDesigner/filesUI/addPSWRD.ui")
        uic.loadUi(file_path, self.addPSWRDModal)

        self.addPSWRDModal.show()

        self.AddPSWRDSetup()

    def AddPSWRDSetup(self):
        self.addPSWRDModal.checkBox_symbol.setEnabled(False)
        self.addPSWRDModal.checkBox_uppercase.setEnabled(False)  
        self.addPSWRDModal.checkBox_number.setEnabled(False)
        self.addPSWRDModal.spinBox_caracter.setEnabled(False)
        self.addPSWRDModal.pushButton_generate.setEnabled(False)

        self.addPSWRDModal.checkBox_generate.stateChanged.connect(self.generatePassword)

        self.addPSWRDModal.pushButton_save.clicked.connect(self.checkFieldsSavePSWRD)


    def generatePassword(self, estado):
        if estado == Qt.Checked:
            print("generate password")
            self.addPSWRDModal.checkBox_symbol.setEnabled(True)
            self.addPSWRDModal.checkBox_uppercase.setEnabled(True)  
            self.addPSWRDModal.checkBox_number.setEnabled(True)
            self.addPSWRDModal.spinBox_caracter.setEnabled(True)
            self.addPSWRDModal.pushButton_generate.setEnabled(True)
        else:
            self.AddPSWRDSetup()

    def checkFieldsSavePSWRD(self):
        teste = ''
        # checkAppName
        if not self.addPSWRDModal.Input_appName.text():
            self.addPSWRDModal.Input_appPSWRD.setStyleSheet(st.style_modalInputTextError)
        else:
            teste += 'OK'
            self.addPSWRDModal.Input_appName.setStyleSheet(st.style_modalInputTextOK)

        # checkUsername
        if not self.addPSWRDModal.Input_appUsername.text():
            self.addPSWRDModal.Input_appUsername.setStyleSheet(st.style_modalInputTextError)
        else:
            teste += 'OK'
            self.addPSWRDModal.Input_appUsername.setStyleSheet(st.style_modalInputTextOK)

        # checkPassword
        if not self.addPSWRDModal.Input_appPSWRD.text():
            self.addPSWRDModal.Input_appPSWRD.setStyleSheet(st.style_modalInputTextError)
        else:
            teste += 'OK'
            self.addPSWRDModal.Input_appPSWRD.setStyleSheet(st.style_modalInputTextOK)

        if teste == 'OKOKOK':
              self.addPSWRDModal.close()
              self.addNewPSWRD()
              self.refreashAppCards()
        
        
    def addNewPSWRD(self):
          pass

    def showNotesButton(self):
           print("show notes widget")

    def showWifiPassButton(self):
           print("show wifi pass widget")


############################################################################################################

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()