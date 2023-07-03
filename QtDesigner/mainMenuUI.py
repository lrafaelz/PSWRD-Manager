import os
from PyQt5 import uic , QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QPushButton, QCheckBox
import QtDesigner.QTImages_rc


class MainMenuWindow(QtWidgets.QMainWindow):
        def __init__(self):
                super().__init__()
                file_path = os.path.abspath("QtDesigner/filesUI/mainMenu.ui")
                uic.loadUi(file_path, self)
                                #
                # FUNCTIONS
                #
                # pushbutton close popup error
                file_path = os.path.abspath("encryption/texto.txt") # Alterar para rodar
                # caminho_arquivo = "encryption/texto.txt" # Alterar para rodar
                matriz_valores = []
                with open(file_path, 'r') as arquivo:
                        for linha in arquivo:
                                valores = linha.strip().split(',')
                                matriz_valores.append(valores)
                print(matriz_valores)
                from cardSenha import CardSenha
                for(i) in range(len(matriz_valores)):
                        PSWRDCards = []
                        if(i<5):
                                PSWRDCards.append(matriz_valores,i)
                                
                self.pushButton_closeError.clicked.connect(self.frame_error.hide)
                # hide frame error
                self.frame_error.hide()

                # pushbutton adicionar nova senha
                self.pushButton_addNewPSWRD.clicked.connect(self.onAddWidget)

        n = 0
        
        def onAddWidget(self):

                layout = self.frame_addNewPSWRD.layout()
                newLayout = QGridLayout(self.frame_addNewPSWRD)
                buttonText = "teste"
                button = QPushButton(buttonText, self.frame_addNewPSWRD)
                newLayout.addWidget(button)


        def editPSWRD(self):
               print("editPSWRD")
        