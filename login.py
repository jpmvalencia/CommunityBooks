from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLineEdit, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QMessageBox

from createconsult import Create_Consult


class Login(QMainWindow):
    def __init__(self):
        super().__init__()

        # Icono de la ventana
        self.setWindowIcon(QtGui.QIcon("icon.svg"))

        # Titulo de la ventana
        self.setWindowTitle("CommunityBooks")

        self.user = "admin"
        self.psswd = "admin"

        # Color de fondo y color de letras
        self.setStyleSheet("background-color: #2a2d37; color: #c0c5ce;")

        # Establecer propiedades de ancho y alto
        self.width = 1280
        self.height = 720

        # Establecer el tamaño de la ventana
        self.resize(self.width, self.height)

        # Centrar la ventana
        self.screen = self.frameGeometry()
        self.center = QDesktopWidget().availableGeometry().center()
        self.screen.moveCenter(self.center)
        self.move(self.screen.topLeft())

        # Definir los textos, inputs y botones
        # Logo
        self.icon = QPixmap("icon.svg").scaledToHeight(128)
        self.icon_label = QLabel()
        self.icon_label.setPixmap(self.icon)
        
        # Título
        self.login_text = QLabel()
        self.login_text.setText("Inicio de Sesión")
        self.login_text.setFont(QFont("...", 14))

        self.blank_space = QLabel("\n")

        # Input para el usuario
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Usuario")
        self.user_input.setStyleSheet("border: none; background-color: #1c1f26; border-radius: 10px; padding: 7px;")
        self.user_input.setFont(QFont("...", 10))
        self.user_input.setFixedSize(200, 50)

        # Input para la contraseña
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setStyleSheet("border: none; background-color: #1c1f26; border-radius: 10px; "
                                          "padding: 7px;")
        self.password_input.setFont(QFont("...", 10))
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedSize(200, 50)
        self.entered_psswd = self.password_input.text()

        # Botón para ingresar
        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.setFont(QFont("...", 10))
        self.login_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; } "
                                        "QPushButton:pressed { background-color: #1c1f26; } ")
        self.login_button.setFixedSize(150, 50)
        self.login_button.clicked.connect(self.activate_options_window)

        # Agregar los objetos
        self.container = QWidget()
        self.lay = QVBoxLayout(self.container)
        self.lay.addWidget(self.icon_label, alignment=Qt.AlignCenter)
        self.lay.addWidget(self.login_text, alignment=Qt.AlignCenter)
        self.lay.addWidget(self.blank_space)
        self.lay.addWidget(self.user_input, alignment=Qt.AlignCenter)
        self.lay.addWidget(self.password_input, alignment=Qt.AlignCenter)
        self.lay.addWidget(self.login_button, alignment=Qt.AlignCenter)
        self.container.setFixedSize(self.container.sizeHint())

        self.central_widget = QWidget()

        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.addWidget(self.container, 1, 1)

        # Establece el widget principal como el widget central de la ventana
        self.setCentralWidget(self.central_widget)

    # Programar los botones
    def activate_options_window(self):
        self.error_message = QMessageBox()
        self.error_message.setIcon(QMessageBox.Warning)
        self.error_message.setWindowTitle("Datos Incorrectos")
        self.error_message.setText("Los datos ingresados son incorrectos.")
        self.error_message.setStandardButtons(QMessageBox.Ok)
        self.error_message.buttonClicked.connect(self.activate_message)

        self.true_values = True

        if self.user_input.text() == self.user:
            if self.password_input.text() == self.psswd:
                self.user_input.setText("")
                self.password_input.setText("")
                self.options_window = Create_Consult(self)
                self.options_window.show()
                self.hide()
            else:
                self.error_message.exec()
        else:
            self.error_message.exec()

    def activate_message(self):
        self.error_message.close()


if __name__ == '__main__':
    app = QApplication([])
    login = Login()
    login.show()
    app.exec_()
