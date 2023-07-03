import os
import QtDesigner.QTImages_rc
from PyQt5 import uic , QtWidgets, QtCore, QtGui


class CardSenha():
        
        def __init__(self, matriz_valores, i):
                file_path = os.path.abspath("QtDesigner/filesUI/mainMenu.ui")
                mainMenu = uic.loadUi(file_path, self)
                newFrame = QtWidgets.QFrame(mainMenu.frame_12)

                iconUser = QtGui.QIcon()
                iconUser.addPixmap(QtGui.QPixmap(":/User/Images/User.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                iconLocker = QtGui.QIcon()
                iconLocker.addPixmap(QtGui.QPixmap(":/Locker/Images/Locker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

                newFrame.setMinimumSize(QtCore.QSize(238, 272))
                newFrame.setMaximumSize(QtCore.QSize(238, 272))
                newFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                newFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                newFrame.setObjectName(newFrame)

                mainMenu.gridLayout_2.addWidget(newFrame, 0, 1, 1, 1)

                # PSWRD1 (PSWRDx...)
                if(i > 5):
                        newPSWRD = QtWidgets.QFrame(newFrame)
                else:
                        print("precisa referenciar o frame correto")
                        # newPSWRD = QtWidgets.QFrame(mainMenu.) # não queria fazer uma concatenação de if/else
                newPSWRD.setGeometry(QtCore.QRect(22, 16, 194, 240))
                newPSWRD.setMinimumSize(QtCore.QSize(194, 240))
                newPSWRD.setMaximumSize(QtCore.QSize(194, 240))
                newPSWRD.setStyleSheet("    background-color: rgb(254, 254, 254);\n"
                "    font: 75 13pt \"Inter\";\n"
                "\n"
                "    border-radius: 20px;")
                newPSWRD.setFrameShape(QtWidgets.QFrame.StyledPanel)
                newPSWRD.setFrameShadow(QtWidgets.QFrame.Raised)
                newPSWRD.setObjectName(newPSWRD)

                newPSWRDLayout = QtWidgets.QVBoxLayout(newPSWRD)
                newPSWRDLayout.setContentsMargins(0, 0, 0, 0)
                newPSWRDLayout.setSpacing(0)
                newPSWRDLayout.setObjectName(newPSWRDLayout)

                newPSWRDIcon = QtWidgets.QPushButton(newPSWRD)
                newPSWRDIcon.setEnabled(True)
                newPSWRDIcon.setMinimumSize(QtCore.QSize(194, 105))
                newPSWRDIcon.setMaximumSize(QtCore.QSize(194, 105))

                font = QtGui.QFont()
                font.setFamily("Inter")
                font.setPointSize(13)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)

                newPSWRDIcon.setFont(font)
                newPSWRDIcon.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
                newPSWRDIcon.setStyleSheet("QPushButton{\n"
                "    background-color: rgb(254, 254, 254);\n"
                "    font: 75 13pt \"Inter\";\n"
                "}\n"
                "\n"
                "QPushButton:hover{\n"
                "    background-color: rgb(235, 235, 235);\n"
                "}\n"
                "\n"
                "QPushButton:hover:pressed{\n"
                "    background-color: rgb(255, 255, 255);\n"
                "}\n"
                "\n"
                "")

                newPSWRDIcon.setText("")
                newPSWRDIcon.setIcon(mainMenu.icon4) # adicionar icon
                newPSWRDIcon.setIconSize(QtCore.QSize(80, 80))
                newPSWRDIcon.setCheckable(False)
                newPSWRDIcon.setAutoRepeat(False)
                newPSWRDIcon.setAutoExclusive(False)
                newPSWRDIcon.setObjectName(newPSWRDIcon)

                newPSWRDLayout.addWidget(newPSWRDIcon)

                newPSWRDName = QtWidgets.QLabel(newPSWRD)

                font = QtGui.QFont()
                font.setFamily("Inter")
                font.setPointSize(13)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)

                newPSWRDName.setFont(font)
                newPSWRDName.setAutoFillBackground(False)
                newPSWRDName.setStyleSheet("background-color: rgba(0,0,0,0%)")
                newPSWRDName.setFrameShape(QtWidgets.QFrame.NoFrame)
                newPSWRDName.setFrameShadow(QtWidgets.QFrame.Plain)
                newPSWRDName.setObjectName(newPSWRDName)

                newPSWRDLayout.addWidget(newPSWRDName)

                newPSWRDUser = QtWidgets.QPushButton(newPSWRD)
                newPSWRDUser.setEnabled(True)
                newPSWRDUser.setMinimumSize(QtCore.QSize(194, 60))
                newPSWRDUser.setMaximumSize(QtCore.QSize(194, 60))

                font = QtGui.QFont()
                font.setFamily("Inter")
                font.setPointSize(8)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)

                newPSWRDUser.setFont(font)
                newPSWRDUser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
                newPSWRDUser.setAutoFillBackground(False)
                newPSWRDUser.setStyleSheet("QPushButton{\n"
                "    background-color: rgb(254, 254, 254);\n"
                "    font: 75 8pt \"Inter\";\n"
                "}\n"
                "QPushButton:hover{\n"
                "    background-color: rgb(235, 235, 235);\n"
                "}\n"
                "QPushButton:hover:pressed{\n"
                "    background-color: rgb(255, 255, 255);\n"
                "}\n"
                "")

                newPSWRDUser.setIcon(iconUser)
                newPSWRDUser.setIconSize(QtCore.QSize(30, 30))
                newPSWRDUser.setCheckable(False)
                newPSWRDUser.setAutoRepeat(False)
                newPSWRDUser.setAutoExclusive(False)
                newPSWRDUser.setObjectName(f"PSWRDUser{i}")

                # PSWRDPass
                newPSWRDPass = QtWidgets.QPushButton(newPSWRD)
                newPSWRDPass.setEnabled(True)
                newPSWRDPass.setMinimumSize(QtCore.QSize(194, 60))
                newPSWRDPass.setMaximumSize(QtCore.QSize(194, 60))

                font = QtGui.QFont()
                font.setFamily("Inter")
                font.setPointSize(8)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)

                newPSWRDPass.setFont(font)
                newPSWRDPass.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
                newPSWRDPass.setStyleSheet("QPushButton{\n"
                "    background-color: rgb(254, 254, 254);\n"
                "    font: 75 8pt \"Inter\";\n"
                "}\n"
                "QPushButton:hover{\n"
                "    background-color: rgb(235, 235, 235);\n"
                "}\n"
                "QPushButton:hover:pressed{\n"
                "    background-color: rgb(255, 255, 255);\n"
                "}\n"
                "")

                newPSWRDPass.setIcon(iconLocker)
                newPSWRDPass.setIconSize(QtCore.QSize(30, 30))
                newPSWRDPass.setCheckable(False)
                newPSWRDPass.setAutoRepeat(False)
                newPSWRDPass.setAutoExclusive(False)
                newPSWRDPass.setObjectName(f"PSWRDPass{i}")

                newPSWRDLayout.addWidget(newPSWRDPass)

                # textos do card
                texto_PWRDName = "<html><head/><body><p align=\"center\">" + matriz_valores[i][0] + "</p></body></html>"
                newPSWRDName.setText(mainMenu._translate("MainWindow", texto_PWRDName))
                self.PSWRDUser.setText(mainMenu._translate("MainWindow", matriz_valores[i][1]))
                self.PSWRDPass.setText(mainMenu._translate("MainWindow", matriz_valores[i][2]))