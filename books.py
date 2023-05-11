from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QLabel, QLineEdit, QFormLayout, \
    QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem


class Books(QMainWindow):
    def __init__(self, previous):
        super().__init__()

        # Icono de la ventana
        self.setWindowIcon(QtGui.QIcon("icon.svg"))

        self.previous_window = previous
        # Titulo de la ventana
        self.setWindowTitle("Libros")

        self.setStyleSheet("background-color: #2a2d37; color: #c0c5ce;")

        # Tamaño de la ventana
        self.width = 1280
        self.height = 720

        # Asignar tamaño a la ventana
        self.resize(self.width, self.height)

        # Centrar ventanas
        self.screen = self.frameGeometry()
        self.center = QDesktopWidget().availableGeometry().center()
        self.screen.moveCenter(self.center)
        self.move(self.screen.topLeft())

        self.horizontal_layout = QHBoxLayout()

        # Establecer layout
        self.form_layout = QFormLayout()
        
        # Logo
        self.icon = QPixmap("icon.svg").scaledToHeight(72)
        self.icon_label = QLabel()
        self.icon_label.setPixmap(self.icon)
        self.icon_label.setAlignment(Qt.AlignCenter)

        # Texto
        self.books_text = QLabel()
        self.books_text.setText("Libros")
        self.books_text.setFont(QFont("...", 14))
        self.books_text.setAlignment(Qt.AlignCenter)

        self.blank_space = QLabel("\n")

        self.isbn_text = QLabel()
        self.isbn_text.setText("ISBN:")
        self.isbn_text.setFont(QFont("...", 10))
        self.isbn_input = QLineEdit()
        self.isbn_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.isbn_input.setFont(QFont("...", 10))
        self.isbn_input.setFixedWidth(200)

        self.name_text = QLabel()
        self.name_text.setText("Nombre:")
        self.name_text.setFont(QFont("...", 10))
        self.name_input = QLineEdit()
        self.name_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.name_input.setFont(QFont("...", 10))
        self.name_input.setFixedWidth(200)

        self.author_text = QLabel()
        self.author_text.setText("Autor:")
        self.author_text.setFont(QFont("...", 10))
        self.author_input = QLineEdit()
        self.author_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                        "border-radius: 10px;")
        self.author_input.setFont(QFont("...", 10))
        self.author_input.setFixedWidth(200)

        self.year_text = QLabel()
        self.year_text.setText("Año:")
        self.year_text.setFont(QFont("...", 10))
        self.year_input = QLineEdit()
        self.year_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.year_input.setFont(QFont("...", 10))
        self.year_input.setFixedWidth(200)

        self.genre_text = QLabel()
        self.genre_text.setText("Género:")
        self.genre_text.setFont(QFont("...", 10))
        self.genre_input = QLineEdit()
        self.genre_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                       "border-radius: 10px;")
        self.genre_input.setFont(QFont("...", 10))
        self.genre_input.setFixedWidth(200)

        self.quantity_text = QLabel()
        self.quantity_text.setText("Cantidad:")
        self.quantity_text.setFont(QFont("...", 10))
        self.quantity_input = QLineEdit()
        self.quantity_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                          "border-radius: 10px;")
        self.quantity_input.setFont(QFont("...", 10))
        self.quantity_input.setFixedWidth(200)

        self.reserve_text = QLabel()
        self.reserve_text.setText("Reserva:")
        self.reserve_text.setFont(QFont("...", 10))
        self.reserve_input = QLineEdit()
        self.reserve_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                         "border-radius: 10px;")
        self.reserve_input.setFont(QFont("...", 10))
        self.reserve_input.setFixedWidth(200)

        self.remaining_time_text = QLabel()
        self.remaining_time_text.setText("Tiempo Restante:")
        self.remaining_time_text.setFont(QFont("...", 10))
        self.remaining_time_input = QLineEdit()
        self.remaining_time_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                                "border-radius: 10px;")
        self.remaining_time_input.setFont(QFont("...", 10))
        self.remaining_time_input.setFixedWidth(200)

        # Boton
        self.back_button = QPushButton("Atrás")
        self.back_button.setFont(QFont("...", 10))
        self.back_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                       "QPushButton:pressed { background-color: #1c1f26; }")
        self.back_button.setFixedSize(100, 50)
        self.back_button.clicked.connect(self.activate_options_window)

        self.search_button = QPushButton("Buscar")
        self.search_button.setFont(QFont("...", 10))
        self.search_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #1c1f26; }")
        self.search_button.setFixedSize(100, 50)

        # Botón para cerrar sesión
        self.sign_out_button = QPushButton("Cerrar Sesión")
        self.sign_out_button.setFont(QFont("...", 10))
        self.sign_out_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                           "QPushButton:pressed { background-color: #1c1f26; }")
        self.sign_out_button.setFixedSize(150, 50)
        self.sign_out_button.clicked.connect(self.sign_out)

        # Agregar contenido
        self.form_layout.addRow(self.icon_label)
        self.form_layout.addRow(self.books_text)
        self.form_layout.addRow(self.blank_space)
        self.form_layout.addRow(self.isbn_text, self.isbn_input)
        self.form_layout.addRow(self.name_text, self.name_input)
        self.form_layout.addRow(self.author_text, self.author_input)
        self.form_layout.addRow(self.year_text, self.year_input)
        self.form_layout.addRow(self.genre_text, self.genre_input)
        self.form_layout.addRow(self.quantity_text, self.quantity_input)
        self.form_layout.addRow(self.reserve_text, self.reserve_input)
        self.form_layout.addRow(self.remaining_time_text, self.remaining_time_input)

        # Para que se muestre el boton
        self.horizontal_layout.addWidget(self.back_button)
        self.horizontal_layout.addWidget(self.search_button)

        self.widget1 = QWidget()
        self.widget1.setLayout(self.form_layout)

        self.button_widget = QWidget()
        self.button_widget.setLayout(self.horizontal_layout)

        # Crea un QVBoxLayout para contener los QFormLayouts centrados y los espaciadores
        self.main_layout = QVBoxLayout()
        #self.main_layout.addWidget(self.sign_out_button, alignment=Qt.AlignRight)
        self.main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.main_layout.addWidget(self.widget1, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.button_widget, alignment=Qt.AlignCenter)
        self.main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Establecer el widget central
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.central_widget)

    def activate_options_window(self):
        self.previous_window.show()
        self.close()

    def sign_out(self):
        pass
