from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDesktopWidget, QWidget, QVBoxLayout, QSpacerItem, \
    QSizePolicy, QLabel

from books import Books
from library import Library
from location import Location
from signin import Signin
from booking import Booking


class U_Options(QMainWindow):
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
        self.go_to_signin = QPushButton("Actualizar Usuario")
        self.go_to_signin.setFont(QFont("...", 10))
        self.go_to_signin.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; } "
                                        "QPushButton:pressed { background-color: #1c1f26; } ")
        self.go_to_signin.setFixedSize(250, 50)
        self.go_to_signin.clicked.connect(self.activate_signin_window)

        # Botones
        self.go_to_book = QPushButton("Actualizar Libro")
        self.go_to_book.setFont(QFont("...", 10))
        self.go_to_book.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; } "
                                      "QPushButton:pressed { background-color: #1c1f26; } ")
        self.go_to_book.setFixedSize(250, 50)
        self.go_to_book.clicked.connect(self.activate_book_window)

        self.go_to_location = QPushButton("Actualizar Ubicación")
        self.go_to_location.setFont(QFont("...", 10))
        self.go_to_location.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; } "
                                          "QPushButton:pressed { background-color: #1c1f26; } ")
        self.go_to_location.setFixedSize(250, 50)
        self.go_to_location.clicked.connect(self.activate_location_window)

        self.go_to_library = QPushButton("Actualizar Librería")
        self.go_to_library.setFont(QFont("...", 10))
        self.go_to_library.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; } "
                                         "QPushButton:pressed { background-color: #1c1f26; } ")
        self.go_to_library.setFixedSize(250, 50)
        self.go_to_library.clicked.connect(self.activate_library_window)

        self.go_to_booking = QPushButton("Actualizar Reservas")
        self.go_to_booking.setFont(QFont("...", 10))
        self.go_to_booking.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; } "
                                         "QPushButton:pressed { background-color: #1c1f26; } ")
        self.go_to_booking.setFixedSize(250, 50)
        self.go_to_booking.clicked.connect(self.activate_booking_window)

        self.back_button = QPushButton("Atrás")
        self.back_button.setFont(QFont("...", 10))
        self.back_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; } "
                                       "QPushButton:pressed { background-color: #1c1f26; } ")
        self.back_button.setFixedSize(150, 50)
        self.back_button.clicked.connect(self.activate_crud_options)

        # Agrega el título y los botones al layout vertical
        self.vertical1.addWidget(self.icon_label, alignment=Qt.AlignCenter)
        self.vertical1.addWidget(self.options_title)
        self.vertical1.addWidget(self.blank_space)
        self.vertical1.addWidget(self.go_to_signin)
        self.vertical1.addWidget(self.go_to_book)
        self.vertical1.addWidget(self.go_to_location)
        self.vertical1.addWidget(self.go_to_library)
        self.vertical1.addWidget(self.go_to_booking)

        # Agrega el botón de regresar estándo separado de los demás
        self.vertical2.addWidget(self.back_button)

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
    def activate_signin_window(self):
        self.signin_window = Signin(self)
        self.signin_window.show()
        self.close()

    def activate_book_window(self):
        self.book_window = Books(self)
        self.book_window.show()
        self.close()

    def activate_location_window(self):
        self.location_window = Location(self)
        self.location_window.show()
        self.close()

    def activate_library_window(self):
        self.library_window = Library(self)
        self.library_window.show()
        self.close()

    def activate_booking_window(self):
        self.booking_window = Booking(self)
        self.booking_window.show()
        self.close()

    def activate_crud_options(self):
        self.previous_window.show()
        self.close()
