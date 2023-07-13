import os
import QtDesigner.QTImages_rc
from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGridLayout, QDialog, QFileDialog, QFrame
from PyQt5.QtGui import QClipboard
import styles as st
from authentication.checkfields import Check
from authentication.login import Login
from authentication.user import User
import encryption.encryption as enc
import encryption.decrypto as dec
import encryption.testCards as tc
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
    
    key = None
    
    grid_layout = None
    first_time = 0

    matriz_senhas = []
    PSWRDPath = None

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
                self.key = self.loginWidget.inputText_Password.text()  
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
        self.key = enc.generate_key()
        key = self.key.hex()
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
        self.key = self.registerWidget.inputText_encryptionKey.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(self.key)


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
                        if self.user.verifyUser(self.registerWidget.inputText_email.text()):
                            self.user.createUser() #criar usuario no arquivo users.txt
                            self.registerWidget.close()
                            self.open_mainMenuUI()
                        else:
                            showMessage("Email já existente")
                            self.registerWidget.frame_error.setStyleSheet(st.stylePopupError)
    
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

        self.refreshAppCards()

        self.mainMenuButtonSetup()

    def fillUserInfo(self):
        self.mainMenuWidget.label_bancoName.setText(self.user.getFolderName().strip(".txt"))
        self.mainMenuWidget.label_email.setText(self.user.getEmail())
        

    def refreshAppCards(self):
        import os.path
        if self.mainMenuWidget.widget_gridApps.layout() is not None:
            for child in self.grid_layout.findChildren(QFrame):
                child.setParent(None)
            self.mainMenuWidget.widget_gridApps.layout().removeItem(self.grid_layout)
        self.grid_layout = QGridLayout()
        print(self.matriz_senhas)
        # Definir o número máximo de frames por linha
        max_frames_por_linha = 3           

        # Lista de frames
        frames = []
        if os.path.isfile(self.user.getFolderPath()) and self.first_time == 0:
            print(self.user.getFolderPath())
            self.matriz_senhas = dec.decrypto(self.user.getFolderPath(), self.key)
            print(self.matriz_senhas)
            self.first_time = 1

        # Adicionar frames ao layout de grid
        from appCard import AppCard
        from appAdd import AppAdd
        frame = AppAdd(self)
        self.grid_layout.addWidget(frame, 0, 0)
        linha = 0
        for i in range(len(self.matriz_senhas)):    
            frame = AppCard(self.matriz_senhas, i, self)
            frames.append(frame)

            # Calcular a posição do frame na grade
            linha = (i+1) // max_frames_por_linha
            coluna = (i+1) % max_frames_por_linha

            # Adicionar o frame ao layout de grid
            self.grid_layout.addWidget(frame, linha, coluna)
        empty_frame = QFrame()
        empty_frame.setFixedSize(238, 272)
        self.grid_layout.addWidget(empty_frame, linha+1, 0)
        self.grid_layout.addWidget(empty_frame, linha+1, 1)
        self.grid_layout.addWidget(empty_frame, linha+1, 2)

        self.mainMenuWidget.widget_gridApps.setLayout(self.grid_layout)


    def backToLoginUI(self):
        import encryption.encrypto as enc
        self.PSWRDPath = self.user.folderPath
        self.fileName = self.user.folderName
        enc.encrypto(self.matriz_senhas, self.PSWRDPath, self.fileName, self.key) # adadasda
        self.user.logout()
        self.login.resetData()
        
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
        # self.mainMenuWidget.pushButton_addNewPSWRD.clicked.connect(self.onAddButton)

        # pushbutton visualizar senhas
        self.mainMenuWidget.pushButton_passwords.setEnabled(False)

        # pushbutton visualizar notas guardadas
        self.mainMenuWidget.pushButton_notes.clicked.connect(self.showNotesButton)

        # pushbutton visualizar senhas wifi guardadas
        self.mainMenuWidget.pushButton_wifiPass.clicked.connect(self.showWifiPassButton)

        self.mainMenuWidget.pushButton_blockPSWRDs.clicked.connect(self.backToLoginUI)

    def showNotesButton(self):
           print("show notes widget")

    def showWifiPassButton(self):
           print("show wifi pass widget")

############################################################################################################

    def addNewPSWRD(self, appName, appUser, appPass):
        self.matriz_senhas.append([appName, appUser, appPass])
        # print(self.matriz_senhas)
        self.refreshAppCards()

    def addFromEdit(self, position, appName, appUser, appPass):
        print(position, appName, appUser, appPass)
        self.matriz_senhas[position] = [appName, appUser, appPass]
        self.refreshAppCards()
    
    def removePSWRD(self, position):
        if(len(self.matriz_senhas) != 0):
            self.matriz_senhas.pop(position)
            self.refreshAppCards()
            self.mainMenuWidget.deleteLater()
            self.open_mainMenuUI()

    

############################################################################################################

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
