from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDesktopWidget, QWidget, QVBoxLayout, QSpacerItem, \
    QSizePolicy, QLabel

from c_options import C_Options
from r_options import R_Options
from u_options import U_Options
from d_options import D_Options

class CRUD_Options(QMainWindow):
    def __init__(self, previous):
        super().__init__()

        # Icono de la ventana
        self.setWindowIcon(QtGui.QIcon("icon.svg"))

        # Guardar en una variable la ventana anterior
        self.previous_window = previous

        # Titulo de la ventana
        self.setWindowTitle("CommunityBooks")

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

        # Establecer los layout que contendrán los botones
        self.vertical1 = QVBoxLayout()
        self.vertical2 = QVBoxLayout()

        # Logo
        self.icon = QPixmap("icon.svg").scaledToHeight(72)
        self.icon_label = QLabel()
        self.icon_label.setPixmap(self.icon)

        # Título
        self.options_title = QLabel()
        self.options_title.setText("Eliga la Opción")
        self.options_title.setFont(QFont("...", 14))
        self.options_title.setAlignment(Qt.AlignCenter)

        self.blank_space = QLabel("\n")

        # Definir los botones
        self.go_to_create = QPushButton("Crear")
        self.go_to_create.setFont(QFont("...", 10))
        self.go_to_create.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; } "
                                        "QPushButton:pressed { background-color: #1c1f26; } ")
        self.go_to_create.setFixedSize(250, 50)
        self.go_to_create.clicked.connect(self.activate_create_window)

        # Botones
        self.go_to_read = QPushButton("Leer")
        self.go_to_read.setFont(QFont("...", 10))
        self.go_to_read.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; } "
                                      "QPushButton:pressed { background-color: #1c1f26; } ")
        self.go_to_read.setFixedSize(250, 50)
        self.go_to_read.clicked.connect(self.activate_read_window)

        self.go_to_update = QPushButton("Actualizar")
        self.go_to_update.setFont(QFont("...", 10))
        self.go_to_update.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; } "
                                          "QPushButton:pressed { background-color: #1c1f26; } ")
        self.go_to_update.setFixedSize(250, 50)
        self.go_to_update.clicked.connect(self.activate_update_window)

        self.go_to_delete = QPushButton("Eliminar")
        self.go_to_delete.setFont(QFont("...", 10))
        self.go_to_delete.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; } "
                                         "QPushButton:pressed { background-color: #1c1f26; } ")
        self.go_to_delete.setFixedSize(250, 50)
        self.go_to_delete.clicked.connect(self.activate_delete_window)

        self.sign_out_button = QPushButton("Cerrar Sesión")
        self.sign_out_button.setFont(QFont("...", 10))
        self.sign_out_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; } "
                                         "QPushButton:pressed { background-color: #1c1f26; } ")
        self.sign_out_button.setFixedSize(150, 50)
        self.sign_out_button.clicked.connect(self.sign_out)

        # Agrega el título y los botones al layout vertical
        self.vertical1.addWidget(self.icon_label, alignment=Qt.AlignCenter)
        self.vertical1.addWidget(self.options_title)
        self.vertical1.addWidget(self.blank_space)
        self.vertical1.addWidget(self.go_to_create)
        self.vertical1.addWidget(self.go_to_read)
        self.vertical1.addWidget(self.go_to_update)
        self.vertical1.addWidget(self.go_to_delete)

        # Agrega el botón de regresar estándo separado de los demás
        self.vertical2.addWidget(self.sign_out_button)

        # Centrar los objetos
        # Se crea y define el layout con base a los botones que agregamos en el layout vertical
        self.options_widget = QWidget()
        self.options_widget.setLayout(self.vertical1)
        self.login_widget = QWidget()
        self.login_widget.setLayout(self.vertical2)

        # Se crea y define el layout principal, el cual permitirá centrar los layouts anteriores.
        self.main_layout = QVBoxLayout()
        self.main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.main_layout.addWidget(self.options_widget, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.login_widget, alignment=Qt.AlignCenter)
        self.main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Crea el widget principal y establece el layout principal como su layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)

        # Establece el widget principal como el widget central de la ventana
        self.setCentralWidget(self.central_widget)

    # Programar los botones
    def activate_create_window(self):
        self.c_options_window = C_Options(self)
        self.c_options_window.show()
        self.close()

    def activate_read_window(self):
        self.r_options_window = R_Options(self)
        self.r_options_window.show()
        self.close()

    def activate_update_window(self):
        self.u_options_window = U_Options(self)
        self.u_options_window.show()
        self.close()

    def activate_delete_window(self):
        self.d_options_window = D_Options(self)
        self.d_options_window.show()
        self.close()

    def sign_out(self):
        self.previous_window.show()
        self.close()
