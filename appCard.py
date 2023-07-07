import os
import QtDesigner.QTImages_rc
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QFrame


class AppCard(QFrame):
    def __init__(self, matriz_valores, i):
        super().__init__()
        file_path = os.path.abspath("QtDesigner/filesUI/PSWRDCardFrame.ui")
        uic.loadUi(file_path, self)

        self.PSWRDName.setText(matriz_valores[i][0])
        self.PSWRDName.setAlignment(QtCore.Qt.AlignCenter)
        self.PSWRDUser.setText(matriz_valores[i][1])
        self.PSWRDPass.setText(matriz_valores[i][2])

