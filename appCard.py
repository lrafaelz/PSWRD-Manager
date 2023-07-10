import os
import QtDesigner.QTImages_rc
from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QFrame, QApplication, QDialog
import styles as st
from mainWindow import MainWindow


class AppCard(QFrame):

    editPSWRDModal = None

    pname = None
    puser = None
    ppass = None
    pposition = None

    MainWindow = None


    def __init__(self, matriz_valores, i, parent):
        super().__init__()
        file_path = os.path.abspath("QtDesigner/filesUI/PSWRDCardFrame.ui")
        uic.loadUi(file_path, self)

        self.pname = matriz_valores[i][0]
        self.puser = matriz_valores[i][1]
        self.ppass = matriz_valores[i][2]
        self.pposition = i
        self.MainWindow = parent
        self.PSWRDName.setText(self.pname)
        self.PSWRDName.setAlignment(QtCore.Qt.AlignCenter)
        self.PSWRDUser.setText(self.puser)
        self.PSWRDPass.setText(self.ppass)

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
        self.editPSWRDModal.Input_appName.setText(self.pname)
        self.editPSWRDModal.Input_appUsername.setText(self.puser)
        self.editPSWRDModal.Input_appPSWRD.setText(self.ppass)

        self.editPSWRDModal.spinBox_symbols.setEnabled(False)
        self.editPSWRDModal.spinBox_uppercase.setEnabled(False)  
        self.editPSWRDModal.spinBox_numbers.setEnabled(False)
        self.editPSWRDModal.spinBox_lowercase.setEnabled(False)
        self.editPSWRDModal.pushButton_generate.setEnabled(False)

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.editPSWRDModal.checkBox_generate.stateChanged.connect(self.generatePassword)

        self.editPSWRDModal.pushButton_save.clicked.connect(self.checkFieldsSavePSWRD)

        self.editPSWRDModal.pushButton_generate.clicked.connect(self.writePassword)

        self.editPSWRDModal.pushButton_erase.clicked.connect(self.erasePSWRD)


    def generatePassword(self, estado):
            if estado == Qt.Checked:
                print("generate password")
                self.editPSWRDModal.spinBox_symbols.setEnabled(True)
                self.editPSWRDModal.spinBox_uppercase.setEnabled(True)  
                self.editPSWRDModal.spinBox_numbers.setEnabled(True)
                self.editPSWRDModal.spinBox_lowercase.setEnabled(True)
                self.editPSWRDModal.pushButton_generate.setEnabled(True)
                self.timer.start(500)
            else:
                self.AddPSWRDSetup()

    def writePassword(self):
        from generator.requirement import Requirement
        from generator.temporary_password import TemporaryPassword
        self.editPSWRDModal.Input_appPSWRD.setText(TemporaryPassword().getValue(Requirement(self.editPSWRDModal.spinBox_uppercase.value(), self.editPSWRDModal.spinBox_symbols.value(),
                                                    self.editPSWRDModal.spinBox_numbers.value(), self.editPSWRDModal.spinBox_symbols.value())))

    def checkFieldsSavePSWRD(self):
        teste = ''
        # checkAppName
        if not self.editPSWRDModal.Input_appName.text():
            self.editPSWRDModal.Input_appPSWRD.setStyleSheet(st.style_modalInputTextError)
        else:
            teste += 'OK'
            self.editPSWRDModal.Input_appName.setStyleSheet(st.style_modalInputTextOK)
            self.pname = self.editPSWRDModal.Input_appName.text()

        # checkUsername
        if not self.editPSWRDModal.Input_appUsername.text():
            self.editPSWRDModal.Input_appUsername.setStyleSheet(st.style_modalInputTextError)
        else:
            teste += 'OK'
            self.editPSWRDModal.Input_appUsername.setStyleSheet(st.style_modalInputTextOK)
            self.puser = self.editPSWRDModal.Input_appUsername.text()

        # checkPassword
        if not self.editPSWRDModal.Input_appPSWRD.text():
            self.editPSWRDModal.Input_appPSWRD.setStyleSheet(st.style_modalInputTextError)
        else:
            teste += 'OK'
            self.editPSWRDModal.Input_appPSWRD.setStyleSheet(st.style_modalInputTextOK)
            self.ppass = self.editPSWRDModal.Input_appPSWRD.text()

        if teste == 'OKOKOK':
              self.editPSWRDModal.close()
              self.savePSWRD()
            #   MainWindow.refreashAppCards(self.MainWindow)
        
    def savePSWRD(self):
        MainWindow.addFromEdit(self.MainWindow, self.pposition, self.pname, self.puser, self.ppass)
    
    def erasePSWRD(self):
        self.setParent(None)
        self.editPSWRDModal.close()
        MainWindow.removePSWRD(self.MainWindow, self.pposition)



