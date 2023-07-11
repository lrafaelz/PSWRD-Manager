import os
import typing
import QtDesigner.QTImages_rc
from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QFrame, QApplication, QDialog, QWidget
import styles as st
from mainWindow import MainWindow

class AppAdd(QFrame):

    addPSWRDModal = None

    pname = None
    puser = None
    ppass = None

    MainWindow = None

    def __init__(self, parent):
        super().__init__()
        file_path = os.path.abspath("QtDesigner/filesUI/frame_addPWSRDButton.ui")
        uic.loadUi(file_path, self)

        self.MainWindow = parent

        self.pushButton_addNewPSWRD.clicked.connect(self.AddPSWRDModalSetup)

    def AddPSWRDModalSetup(self):
        self.addPSWRDModal = QDialog()
        file_path = os.path.abspath("QtDesigner/filesUI/addPSWRD.ui")
        uic.loadUi(file_path, self.addPSWRDModal)

        self.addPSWRDModal.show()

        self.modalSetup()

    def modalSetup(self):
        self.addPSWRDModal.spinBox_symbols.setEnabled(False)
        self.addPSWRDModal.spinBox_uppercase.setEnabled(False)  
        self.addPSWRDModal.spinBox_numbers.setEnabled(False)
        self.addPSWRDModal.spinBox_lowercase.setEnabled(False)
        self.addPSWRDModal.pushButton_generate.setEnabled(False)

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.addPSWRDModal.checkBox_generate.stateChanged.connect(self.generatePassword)

        self.addPSWRDModal.pushButton_save.clicked.connect(self.checkFieldsSavePSWRD)

        self.addPSWRDModal.pushButton_generate.clicked.connect(self.writePassword)

    def generatePassword(self, estado):
            if estado == Qt.Checked:
                print("generate password")
                self.addPSWRDModal.spinBox_symbols.setEnabled(True)
                self.addPSWRDModal.spinBox_uppercase.setEnabled(True)  
                self.addPSWRDModal.spinBox_numbers.setEnabled(True)
                self.addPSWRDModal.spinBox_lowercase.setEnabled(True)
                self.addPSWRDModal.pushButton_generate.setEnabled(True)
                self.timer.start(500)
            else:
                self.modalSetup()

    def writePassword(self):
        from generator.requirement import Requirement
        from generator.temporary_password import TemporaryPassword
        self.addPSWRDModal.Input_appPSWRD.setText(TemporaryPassword().getValue(Requirement(self.addPSWRDModal.spinBox_uppercase.value(), self.addPSWRDModal.spinBox_symbols.value(),
                                                       self.addPSWRDModal.spinBox_numbers.value(), self.addPSWRDModal.spinBox_symbols.value())))
        
    def checkFieldsSavePSWRD(self):
        teste = ''
        # checkAppName
        if not self.addPSWRDModal.Input_appName.text():
            self.addPSWRDModal.Input_appPSWRD.setStyleSheet(st.style_modalInputTextError)
        else:
            teste += 'OK'
            self.pname = self.addPSWRDModal.Input_appName.text()
            self.addPSWRDModal.Input_appName.setStyleSheet(st.style_modalInputTextOK)

        # checkUsername
        if not self.addPSWRDModal.Input_appUsername.text():
            self.addPSWRDModal.Input_appUsername.setStyleSheet(st.style_modalInputTextError)
        else:
            teste += 'OK'
            self.puser = self.addPSWRDModal.Input_appUsername.text()
            self.addPSWRDModal.Input_appUsername.setStyleSheet(st.style_modalInputTextOK)

        # checkPassword
        if not self.addPSWRDModal.Input_appPSWRD.text():
            self.addPSWRDModal.Input_appPSWRD.setStyleSheet(st.style_modalInputTextError)
        else:
            teste += 'OK'
            self.ppass = self.addPSWRDModal.Input_appPSWRD.text()
            self.addPSWRDModal.Input_appPSWRD.setStyleSheet(st.style_modalInputTextOK)

        if teste == 'OKOKOK':
              self.addPSWRDModal.close()
              self.savePSWRD()
            #   MainWindow.refreashAppCards(self.MainWindow)
        
    def savePSWRD(self):
        MainWindow.addNewPSWRD(self.MainWindow, self.pname, self.puser, self.ppass)
        