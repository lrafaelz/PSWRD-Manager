import os
import QtDesigner.QTImages_rc
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGridLayout, QDialog, QFileDialog
from PyQt5.QtGui import QClipboard
import styles as st
from authentication.checkfields import Check
from authentication.login import Login
from authentication.user import User
import encryption.testCards as tc
import encryption.encryption as  enc


# Carregar o arquivo mainWindow.ui
file_path = os.path.abspath("QtDesigner/filesUI/mainWindow.ui")
Ui_MainWindow, QtBaseClass = uic.loadUiType(file_path)

class MainWindow(QMainWindow, Ui_MainWindow):
    
    user = User()
    login = Login()
    # Criar um layout vertical para receber telas
    mainLayout = QVBoxLayout()

    # variaveis para receber os widgets
    loginWidget = None
    registerWidget = None
    mainMenuWidget = None
    addPSWRDModal = None
    editPSWDModal = None

    matriz_senhas = []

##############################################################################################################

    def __init__(self): # loginMenu initialization
        super().__init__()
        self.setupUi(self)

        self.loginInit()

        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        # Configurar o layout como o layout central da janela principal
        centralWidget = QWidget()
        centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralWidget)

        self.loginButtonSetup()

    def loginInit(self): # loginMenu initialization
        # Carregar o widget loginWindowWidget.ui
        self.loginWidget = QWidget()
        file_path = os.path.abspath("QtDesigner/filesUI/loginWindowWidget.ui")
        uic.loadUi(file_path, self.loginWidget)

        # Adicionar o widget ao layout
        self.mainLayout.addWidget(self.loginWidget)

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
        if not Check.SyntaxEmail(self.loginWidget.inputText_Email.text()):
                textUser = "Email invalid"
                self.loginWidget.inputText_Email.setStyleSheet(st.style_inputTextError)

        else:
                textUser = ""
                self.loginWidget.inputText_Email.setStyleSheet(st.style_inputTextOK)
        
        # checkPassword
        if not Check.SyntaxKey(self.loginWidget.inputText_Password.text()):
                textPassword = "/Key invalid"
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
                # Adicionar função para salvar e visualizar o novo banco
                self.login.updateData(self.loginWidget.inputText_Email.text(), self.loginWidget.inputText_Password.text())  
                if(self.login.authorizeLogin(self.loginWidget.inputText_Email.text(), self.loginWidget.inputText_Password.text())):
                    self.user.setEmail(self.login.getInputEmail())
                    self.user.setFolderName(self.login.getInputName())
                    self.user.setFolderPath(self.login.getInputPath())
                    self.user.setFullPath(self.login.getFullPath())
                    text = "Login: OK"
                    self.login.resetData()
                    showMessage(text)
                    self.loginWidget.frame_error.setStyleSheet(st.stylePopupOK)
                    self.open_mainMenuUI()
                else:
                    text = "Email e/ou Key inválidas."
                    showMessage(text)
                    self.loginWidget.frame_error.setStyleSheet(st.stylePopupError)


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
        
        self.generateKey()

        self.registerButtonSetup()

        
    def generateKey(self):
        key = enc.generate_key()
        self.registerWidget.inputText_encryptionKey.setText(key)

    def registerButtonSetup(self):
        self.registerWidget.frame_error.hide()
        self.registerWidget.pushButton_closeError.clicked.connect(self.registerWidget.frame_error.hide)

        self.registerWidget.pushButton_findPath.clicked.connect(self.findPath)

        self.registerWidget.pushButton_copyKey.clicked.connect(self.copyKey)

        # pushbutton adicionar novo banco
        self.registerWidget.pushButton_addNewDf.clicked.connect(self.checkFieldsRegisterUI)

        # pushbutton voltar
        self.registerWidget.pushButton_back.clicked.connect(self.openLoginUI)

    def copyKey(self):
        key = self.registerWidget.inputText_encryptionKey.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(key)


    def findPath(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select Folder")
        self.registerWidget.inputText_dfPath.setText(folder_path)
        print(folder_path)
        # return folder_path

    def checkFieldsRegisterUI(self):
                textEmail = ""
                textDfName = ""
                textDfPath = ""
                
                def showMessage(message):
                        self.registerWidget.frame_error.show()
                        self.registerWidget.label_error.setText(message)
                # checkEmail
                #if not self.registerWidget.inputText_email.text():     
                if not Check.SyntaxEmail(self.registerWidget.inputText_email.text()):
                        textEmail = "Email Invalid"
                        self.registerWidget.inputText_email.setStyleSheet(st.style_inputTextError)
                else:
                        print("entrou no email")
                        self.user.setEmail(self.registerWidget.inputText_email.text()) 
                        textEmail = ""
                        self.registerWidget.inputText_email.setStyleSheet(st.style_inputTextOK)
                
                # checkDfName
                if not Check.SyntaxFileName(self.registerWidget.inputText_dfName.text()):
                        textDfName = "/FileName Invalid/"
                        self.registerWidget.inputText_dfName.setStyleSheet(st.style_inputTextError)
                else:
                        self.user.setFolderName(self.registerWidget.inputText_dfName.text())
                        textDfName = ""
                        self.registerWidget.inputText_dfName.setStyleSheet(st.style_inputTextOK)

                # checkDfPath
                if not Check.SyntaxFilePath(self.registerWidget.inputText_dfPath.text()):
                        textDfPath = "Path Invalid"
                        self.registerWidget.inputText_dfPath.setStyleSheet(st.style_inputTextError)
                else:
                        self.user.setFolderPath(self.registerWidget.inputText_dfPath.text())
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
                        self.user.createUser() #criar usuario no arquivo users.txt
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
        self.loginWidget.hide()
        # self.loginWidget.close()
        self.mainLayout.addWidget(self.mainMenuWidget)

        # Configurar o layout como o layout central da janela principal
        centralWidget = QWidget()
        centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralWidget)

        self.fillUserInfo()

        self.refreashAppCards()

        self.mainMenuButtonSetup()

    def fillUserInfo(self):
        self.mainMenuWidget.label_bancoName.setText(self.user.getFolderName().strip(".txt"))
        self.mainMenuWidget.label_email.setText(self.user.getEmail())
        

    def refreashAppCards(self):
        # Criar o layout de grid
        grid_layout = QGridLayout()

        # Definir o número máximo de frames por linha
        max_frames_por_linha = 3

        # Lista de frames
        frames = []
        self.matriz_senhas = tc.getTestCards()
        print(self.matriz_senhas)

        # Adicionar frames ao layout de grid
        from appCard import AppCard
        for i in range(len(self.matriz_senhas)):
            frame = AppCard(self.matriz_senhas, i)
            frames.append(frame)

            # Calcular a posição do frame na grade
            linha = (i+1) // max_frames_por_linha
            coluna = (i+1) % max_frames_por_linha

            # Adicionar o frame ao layout de grid
            grid_layout.addWidget(frame, linha, coluna)

        # Configurar o frame_gridApps como o central widget da janela
        # self.setCentralWidget(frame_gridApps)
        self.mainMenuWidget.widget_gridApps.setLayout(grid_layout)

    def backToLoginUI(self):
        # import encryption.encrypto as enc
        # enc.encrypto(self.matriz_senhas)
        self.mainMenuWidget.close()
        self.loginWidget.show()
        self.loginWidget.inputText_Email.clear()
        self.loginWidget.inputText_Password.clear()
        self.loginWidget.frame_error.hide()

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

        self.mainMenuWidget.pushButton_blockPSWRDs.clicked.connect(self.backToLoginUI)
     
    def onAddButton(self):
        self.addPSWRDModal = QDialog()
        file_path = os.path.abspath("QtDesigner/filesUI/addPSWRD.ui")
        uic.loadUi(file_path, self.addPSWRDModal)

        self.addPSWRDModal.show()

        self.AddPSWRDSetup()

    def showNotesButton(self):
           print("show notes widget")

    def showWifiPassButton(self):
           print("show wifi pass widget")

############################################################################################################

    def AddPSWRDSetup(self):
        self.addPSWRDModal.spinBox_symbols.setEnabled(False)
        self.addPSWRDModal.spinBox_uppercase.setEnabled(False)  
        self.addPSWRDModal.spinBox_numbers.setEnabled(False)
        self.addPSWRDModal.spinBox_lowercase.setEnabled(False)
        self.addPSWRDModal.pushButton_generate.setEnabled(False)

        self.addPSWRDModal.checkBox_generate.stateChanged.connect(self.generatePassword)

        self.addPSWRDModal.pushButton_save.clicked.connect(self.checkFieldsSavePSWRD)


    def generatePassword(self, estado):
        if estado == Qt.Checked:
            print("generate password")
            self.addPSWRDModal.spinBox_symbols.setEnabled(True)
            self.addPSWRDModal.spinBox_uppercase.setEnabled(True)  
            self.addPSWRDModal.spinBox_numbers.setEnabled(True)
            self.addPSWRDModal.spinBox_lowercase.setEnabled(True)
            self.addPSWRDModal.pushButton_generate.setEnabled(True)

            self.addPSWRDModal.pushButton_generate.clicked.connect(self.writePassword)
        else:
            self.AddPSWRDSetup()

    def writePassword(self):
        import generator.requirement as rq
        import generator.temporary_password as tp
        # from generator.requirement import Requirement
        # from generator.temporary_password import TemporaryPassword
        requisitos = rq(self.addPSWRDModal.spinBox_uppercase.value(), self.addPSWRDModal.spinBox_lowercase.value(), 
                                 self.addPSWRDModal.spinBox_numbers.value(), self.addPSWRDModal.spinBox_symbols.value())
        self.addPSWRDModal.Input_appPSWRD.setText(tp(requisitos).getValue())
        

        
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

############################################################################################################






if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()