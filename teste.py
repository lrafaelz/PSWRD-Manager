from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QGridLayout, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Criar um QGridLayout para posicionar os frames
        layout = QGridLayout()

        # Criar um frame para a barra lateral
        sidebar_frame = QFrame()
        sidebar_frame.setStyleSheet("background-color: red")  # Apenas para visualização
        layout.addWidget(sidebar_frame, 0, 0)  # Adicionar na posição (0, 0)

        # Criar um QVBoxLayout para conter os frames em sequência
        frames_layout = QVBoxLayout()

        # Array de frames
        frames = []

        # Adicionar frames ao array
        frames.append(QFrame())
        frames.append(QFrame())
        frames.append(QFrame())

        # Adicionar cada frame ao QVBoxLayout
        for frame in frames:
            frame_layout = QVBoxLayout()

            # Criar um QPushButton para cada frame
            button = QPushButton("Botão")
            frame_layout.addWidget(button)

            frame.setLayout(frame_layout)  # Definir o layout no frame

            frames_layout.addWidget(frame)

        # Criar um frame para conter os frames em sequência
        container_frame = QFrame()
        container_frame.setStyleSheet("background-color: green")  # Apenas para visualização
        container_frame.setLayout(frames_layout)

        # Adicionar o container_frame ao QGridLayout
        layout.addWidget(container_frame, 0, 1)  # Adicionar na posição (0, 1)

        # Criar um QWidget e definir o QGridLayout como seu layout
        widget = QFrame()
        widget.setLayout(layout)

        # Definir o QWidget como o central widget da janela
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
