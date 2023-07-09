import os
import QtDesigner.QTImages_rc
from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QApplication, QDialog
import styles as st


class AppCard(QFrame):

    editPSWRDModal = None

    def __init__(self, matriz_valores, i):
        super().__init__()
        file_path = os.path.abspath("QtDesigner/filesUI/PSWRDCardFrame.ui")
        uic.loadUi(file_path, self)

        self.PSWRDName.setText(matriz_valores[i][0])
        self.PSWRDName.setAlignment(QtCore.Qt.AlignCenter)
        self.PSWRDUser.setText(matriz_valores[i][1])
        self.PSWRDPass.setText(matriz_valores[i][2])

        self.buttonSetup()

    def buttonSetup(self):
        self.PSWRDIcon.clicked.connect(self.editPSWRD)

        self.PSWRDUser.clicked.connect(self.userCopy)

        self.PSWRDPass.clicked.connect(self.passCopy)

    def editPSWRD(self):
        self.editPSWRDModal = QDialog()
        file_path = os.path.abspath("QtDesigner/filesUI/editPSWRD.ui")
        uic.loadUi(file_path, self.editPSWRDModal)

        self.editPSWRDModal.show()

        self.editPSWRDSetup()


    def userCopy(self):
        user = self.PSWRDUser.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(user)
    
    def passCopy(self):
        password = self.PSWRDPass.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(password)


    def editPSWRDSetup(self):
        self.editPSWRDModal.checkBox_symbol.setEnabled(False)
        self.editPSWRDModal.checkBox_uppercase.setEnabled(False)  
        self.editPSWRDModal.checkBox_number.setEnabled(False)
        self.editPSWRDModal.spinBox_caracter.setEnabled(False)
        self.editPSWRDModal.pushButton_generate.setEnabled(False)

        self.editPSWRDModal.checkBox_generate.stateChanged.connect(self.generatePassword)

        self.editPSWRDModal.pushButton_save.clicked.connect(self.checkFieldsSavePSWRD)


    def generatePassword(self, estado):
        if estado == Qt.Checked:
            print("generate password")
            self.editPSWRDModal.checkBox_symbol.setEnabled(True)
            self.editPSWRDModal.checkBox_uppercase.setEnabled(True)  
            self.editPSWRDModal.checkBox_number.setEnabled(True)
            self.editPSWRDModal.spinBox_caracter.setEnabled(True)
            self.editPSWRDModal.pushButton_generate.setEnabled(True)
        else:
            self.AddPSWRDSetup()

    def checkFieldsSavePSWRD(self):
        teste = ''
        # checkAppName
        if not self.editPSWRDModal.Input_appName.text():
            self.editPSWRDModal.Input_appPSWRD.setStyleSheet(st.style_modalInputTextError)
        else:
            teste += 'OK'
            self.editPSWRDModal.Input_appName.setStyleSheet(st.style_modalInputTextOK)

        # checkUsername
        if not self.editPSWRDModal.Input_appUsername.text():
            self.editPSWRDModal.Input_appUsername.setStyleSheet(st.style_modalInputTextError)
        else:
            teste += 'OK'
            self.editPSWRDModal.Input_appUsername.setStyleSheet(st.style_modalInputTextOK)

        # checkPassword
        if not self.editPSWRDModal.Input_appPSWRD.text():
            self.editPSWRDModal.Input_appPSWRD.setStyleSheet(st.style_modalInputTextError)
        else:
            teste += 'OK'
            self.editPSWRDModal.Input_appPSWRD.setStyleSheet(st.style_modalInputTextOK)

        if teste == 'OKOKOK':
              self.editPSWRDModal.close()
              self.savePSWRD()
              self.refreashAppCards()
        
    def savePSWRD():
        print("savePSWRD")



