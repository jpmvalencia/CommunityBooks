from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QLabel, QLineEdit, QFormLayout, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem, QMessageBox

import os
import pandas as pd


class Books(QMainWindow):
    def __init__(self, previous):
        super().__init__()

        # Icono de la ventana
        self.setWindowIcon(QtGui.QIcon("icon.svg"))

        # Guardar en una variable la ventana anterior
        self.previous_window = previous

        # Titulo de la ventana
        self.setWindowTitle("Registrar Libros | CommunityBooks")

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

        # Establecer los layout para el contenido
        self.horizontal_layout = QHBoxLayout()
        self.form_layout = QFormLayout()
        
        # Logo
        self.icon = QPixmap("icon.svg").scaledToHeight(72)
        self.icon_label = QLabel()
        self.icon_label.setPixmap(self.icon)
        self.icon_label.setAlignment(Qt.AlignCenter)

        # Título
        self.books_text = QLabel()
        self.books_text.setText("Libros")
        self.books_text.setFont(QFont("...", 14))
        self.books_text.setAlignment(Qt.AlignCenter)

        self.blank_space = QLabel("\n") # Espacio en blanco

        # Definir los botones, inputs, etc.
        self.isbn_text = QLabel()
        self.isbn_text.setText("ISBN:")
        self.isbn_text.setFont(QFont("...", 10))
        self.isbn_input = QLineEdit()
        self.isbn_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; border-radius: 10px;")
        self.isbn_input.setFont(QFont("...", 10))
        self.isbn_input.setFixedWidth(200)

        self.name_text = QLabel()
        self.name_text.setText("Nombre:")
        self.name_text.setFont(QFont("...", 10))
        self.name_input = QLineEdit()
        self.name_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; border-radius: 10px;")
        self.name_input.setFont(QFont("...", 10))
        self.name_input.setFixedWidth(200)

        self.author_text = QLabel()
        self.author_text.setText("Autor:")
        self.author_text.setFont(QFont("...", 10))
        self.author_input = QLineEdit()
        self.author_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; border-radius: 10px;")
        self.author_input.setFont(QFont("...", 10))
        self.author_input.setFixedWidth(200)

        self.year_text = QLabel()
        self.year_text.setText("Año:")
        self.year_text.setFont(QFont("...", 10))
        self.year_input = QLineEdit()
        self.year_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; border-radius: 10px;")
        self.year_input.setFont(QFont("...", 10))
        self.year_input.setFixedWidth(200)

        self.genre_text = QLabel()
        self.genre_text.setText("Género:")
        self.genre_text.setFont(QFont("...", 10))
        self.genre_input = QLineEdit()
        self.genre_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; border-radius: 10px;")
        self.genre_input.setFont(QFont("...", 10))
        self.genre_input.setFixedWidth(200)

        self.back_button = QPushButton("Atrás")
        self.back_button.setFont(QFont("...", 10))
        self.back_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                       "QPushButton:pressed { background-color: #1c1f26; }")
        self.back_button.setFixedSize(100, 50)
        self.back_button.clicked.connect(self.activate_options_window)

        self.create_button = QPushButton("Registrar")
        self.create_button.setFont(QFont("...", 10))
        self.create_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #1c1f26; }")
        self.create_button.setFixedSize(100, 50)
        self.create_button.clicked.connect(self.create_book)

        self.sign_out_button = QPushButton("Cerrar Sesión")
        self.sign_out_button.setFont(QFont("...", 10))
        self.sign_out_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                           "QPushButton:pressed { background-color: #1c1f26; }")
        self.sign_out_button.setFixedSize(150, 50)
        self.sign_out_button.clicked.connect(self.sign_out)

        # Agrega el título y el resto del contenido al layout formulario
        self.form_layout.addRow(self.icon_label)
        self.form_layout.addRow(self.books_text)
        self.form_layout.addRow(self.blank_space)
        self.form_layout.addRow(self.isbn_text, self.isbn_input)
        self.form_layout.addRow(self.name_text, self.name_input)
        self.form_layout.addRow(self.author_text, self.author_input)
        self.form_layout.addRow(self.year_text, self.year_input)
        self.form_layout.addRow(self.genre_text, self.genre_input)

        # Agrega el botón de regresar y registrar estándo separado de los demás
        self.horizontal_layout.addWidget(self.back_button)
        self.horizontal_layout.addWidget(self.create_button)

        # Centrar los objetos
        # Se crea y define el layout con base a los botones que agregamos en el layout vertical
        self.widget1 = QWidget()
        self.widget1.setLayout(self.form_layout)
        self.button_widget = QWidget()
        self.button_widget.setLayout(self.horizontal_layout)

        # Se crea y define el layout principal, el cual permitirá centrar los layouts anteriores
        self.main_layout = QVBoxLayout()
        #self.main_layout.addWidget(self.sign_out_button, alignment=Qt.AlignRight)
        self.main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.main_layout.addWidget(self.widget1, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.button_widget, alignment=Qt.AlignCenter)
        self.main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Crea el widget principal y establece el layout principal como su layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)

        # Establece el widget principal como el widget central de la ventana
        self.setCentralWidget(self.central_widget)

    # Programar los botones
    def create_book(self):
        self.success_message = QMessageBox()
        self.success_message.setIcon(QMessageBox.Warning)
        self.success_message.setWindowTitle("Reserva Exitosa")
        self.success_message.setText("El libro se ha registrado con éxito.")
        self.success_message.setStandardButtons(QMessageBox.Ok)
        self.success_message.buttonClicked.connect(self.activate_success_message)
        
        # Verifica que exista el archivo de datos, si no, los crea
        if os.path.isfile("data/books.csv"):
            self.df = pd.read_csv("data/books.csv")
        else:
            self.df = pd.DataFrame(columns=["ISBN","Nombre","Autor","Año","Género"])

        # Se obtienen los datos ingresados
        self.data = {"ISBN": self.isbn_input.text(), "Nombre": self.name_input.text(), "Autor": self.author_input.text(),  "Año": self.year_input.text(), "Género": self.genre_input.text()}

        # Se actualiza los datos con la nueva información ingresada
        self.df = self.df._append(self.data, ignore_index=True)
        self.df.to_csv("data/books.csv", index=False, mode="w")
        
        # Se activa el mensaje de registro exitoso
        self.success_message.exec()

        # Se resetea los input
        self.isbn_input.setText("")
        self.name_input.setText("")
        self.author_input.setText("")
        self.year_input.setText("")
        self.genre_input.setText("")

    def activate_success_message(self):
        self.success_message.close()

    def activate_options_window(self):
        self.previous_window.show()
        self.close()

    def sign_out(self):
        pass
