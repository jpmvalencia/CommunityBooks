import os
import pandas as pd

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QComboBox, QLineEdit, QWidget, QDesktopWidget, \
    QFormLayout, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout, QMessageBox


class Users(QMainWindow):
    def __init__(self, previous):
        super().__init__()
        
        # Icono de la ventana
        self.setWindowIcon(QtGui.QIcon("icon.svg"))

        # Guardar en una variable la ventana anterior
        self.previous_window = previous

        # Titulo de la ventana
        self.setWindowTitle("Registro")

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

        # Establecer el layout que contendrán los objetos
        self.horizontal_layout = QHBoxLayout()
        self.form_layout = QFormLayout()

        # Definir los textos, inputs y botones
        # Logo
        self.icon = QPixmap("icon.svg").scaledToHeight(72)
        self.icon_label = QLabel()
        self.icon_label.setPixmap(self.icon)
        self.icon_label.setAlignment(Qt.AlignCenter)

        # Título
        self.register_title = QLabel()
        self.register_title.setText("Registro de Usuario")
        self.register_title.setFont(QFont("...", 14))
        self.register_title.setAlignment(Qt.AlignCenter)

        self.blank_space = QLabel("\n") # Espacio en blanco

        # Texto y opciones para el tipo de usuario
        self.user_type_text = QLabel()
        self.user_type_text.setText("Tipo de Usuario:")
        self.user_type_text.setFont(QFont("...", 10))
        self.user_type_options = QComboBox()
        self.user_type_options.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; border-radius: 10px;")
        self.user_type_options.setFont(QFont("...", 10))
        self.user_type_options.setFixedWidth(200)

        # Definir los tipos de usuario
        self.user_type_options.addItem("Administrador")
        self.user_type_options.addItem("Empleado")
        self.user_type_options.addItem("Estudiante")

        # Texto e input para el nombre
        self.firstname_text = QLabel()
        self.firstname_text.setText("Nombre:")
        self.firstname_text.setFont(QFont("...", 10))
        self.firstname_input = QLineEdit()
        self.firstname_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; border-radius: 10px;")
        self.firstname_input.setFont(QFont("...", 10))
        self.firstname_input.setFixedWidth(200)

        # Texto e input para el apellido
        self.lastname_text = QLabel()
        self.lastname_text.setText("Apellido:")
        self.lastname_text.setFont(QFont("...", 10))
        self.lastname_input = QLineEdit()
        self.lastname_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; border-radius: 10px;")
        self.lastname_input.setFont(QFont("...", 10))
        self.lastname_input.setFixedWidth(200)

        # Texto y opciones para el sexo
        self.user_sex_text = QLabel()
        self.user_sex_text.setText("Sexo:")
        self.user_sex_text.setFont(QFont("...", 10))
        self.user_sex_options = QComboBox()
        self.user_sex_options.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; border-radius: 10px;")
        self.user_sex_options.setFont(QFont("...", 10))
        self.user_sex_options.setFixedWidth(200)

        # Definir el sexo
        self.user_sex_options.addItem("Masculino")
        self.user_sex_options.addItem("Femenino")

        # Texto y opciones para el tipo de documento
        self.doc_type_text = QLabel()
        self.doc_type_text.setText("Tipo de Documento:")
        self.doc_type_text.setFont(QFont("...", 10))
        self.doc_type_options = QComboBox()
        self.doc_type_options.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; border-radius: 10px;")
        self.doc_type_options.setFont(QFont("...", 10))
        self.doc_type_options.setFixedWidth(200)

        # Definir los tipos de documento
        self.doc_type_options.addItem("Cédula de Ciudadanía")
        self.doc_type_options.addItem("Tarjeta de Identidad")

        # Texto e input para el el número de documento
        self.doc_number_text = QLabel()
        self.doc_number_text.setText("Número de Documento:")
        self.doc_number_text.setFont(QFont("...", 10))
        self.doc_number_input = QLineEdit()
        self.doc_number_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; border-radius: 10px;")
        self.doc_number_input.setFont(QFont("...", 10))
        self.doc_number_input.setFixedWidth(200)

        # Texto e input para el correo electrónico
        self.email_text = QLabel()
        self.email_text.setText("Correo Electrónico:")
        self.email_text.setFont(QFont("...", 10))
        self.email_input = QLineEdit()
        self.email_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; border-radius: 10px;")
        self.email_input.setFont(QFont("...", 10))
        self.email_input.setFixedWidth(200)

        # Texto e input para el número de celular
        self.phone_number_text = QLabel()
        self.phone_number_text.setText("Número de Celular:")
        self.phone_number_text.setFont(QFont("...", 10))
        self.phone_number_input = QLineEdit()
        self.phone_number_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; border-radius: 10px;")
        self.phone_number_input.setFont(QFont("...", 10))
        self.phone_number_input.setFixedWidth(200)

        # Botón para regresar a la ventana anterior
        self.back_button = QPushButton("Atrás")
        self.back_button.setFont(QFont("...", 10))
        self.back_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                       "QPushButton:pressed { background-color: #1c1f26; }")
        self.back_button.setFixedSize(100, 50)
        self.back_button.clicked.connect(self.activate_options_window)

        # Botón para registrar al usuario
        self.create_button = QPushButton("Registrar")
        self.create_button.setFont(QFont("...", 10))
        self.create_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                           "QPushButton:pressed { background-color: #1c1f26; }")
        self.create_button.setFixedSize(100, 50)
        self.create_button.clicked.connect(self.register_user)

        # Botón para cerrar sesión
        self.sign_out_button = QPushButton("Cerrar Sesión")
        self.sign_out_button.setFont(QFont("...", 10))
        self.sign_out_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                           "QPushButton:pressed { background-color: #1c1f26; }")
        self.sign_out_button.setFixedSize(150, 50)
        self.sign_out_button.clicked.connect(self.sign_out)

        # Agrega los objetos al layout tipo formulario
        self.form_layout.addRow(self.icon_label)
        self.form_layout.addRow(self.register_title)
        self.form_layout.addRow(self.blank_space)
        self.form_layout.addRow(self.user_type_text, self.user_type_options)
        self.form_layout.addRow(self.firstname_text, self.firstname_input)
        self.form_layout.addRow(self.lastname_text, self.lastname_input)
        self.form_layout.addRow(self.user_sex_text, self.user_sex_options)
        self.form_layout.addRow(self.doc_type_text, self.doc_type_options)
        self.form_layout.addRow(self.doc_number_text, self.doc_number_input)
        self.form_layout.addRow(self.email_text, self.email_input)
        self.form_layout.addRow(self.phone_number_text, self.phone_number_input)

        # Agrega los botones al layout horizontal
        self.horizontal_layout.addWidget(self.back_button)
        self.horizontal_layout.addWidget(self.create_button)

        # Centrar los objetos
        # Se crea y define el layout con base a los objetos que agregamos en los layout anteriores
        self.widget1 = QWidget()
        self.widget1.setLayout(self.form_layout)

        self.button_widget = QWidget()
        self.button_widget.setLayout(self.horizontal_layout)

        # Se crea y define el layout principal, el cual permitirá centrar los layouts anteriores.
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

        self.user_type_content = self.user_type_options.currentText()
        self.user_sex_content = self.user_sex_options.currentText()
        self.doc_type_content = self.doc_type_options.currentText()
    
    # Programar botones
    def register_user(self):
        self.success_message = QMessageBox()
        self.success_message.setIcon(QMessageBox.Warning)
        self.success_message.setWindowTitle("Registro Exitoso")
        self.success_message.setText("Los datos han sido ingresados correctamente.")
        self.success_message.setStandardButtons(QMessageBox.Ok)
        self.success_message.buttonClicked.connect(self.activate_success_message)

        # Verifica que exista el archivo de datos, si no, los crea
        if os.path.isfile("data/users.csv"):
            self.df = pd.read_csv("data/users.csv")
        else:
            self.df = pd.DataFrame(columns=["Tipo de Usuario","Nombre","Apellido","Sexo","Tipo de Documento","Número de Documento","Correo Electrónico","Número de Celular"])

        # Se obtienen los datos ingresados
        self.data = {"Tipo de Usuario": self.user_type_content, "Nombre": self.firstname_input.text(), "Apellido": self.lastname_input.text(),  "Sexo": self.user_sex_content, "Tipo de Documento": self.doc_type_content, "Número de Documento": self.doc_number_input.text(), "Correo Electrónico": self.email_input.text(), "Número de Celular": self.phone_number_input.text()}

        # Se actualiza los datos con la nueva información ingresada
        self.df = self.df._append(self.data, ignore_index=True)
        self.df.to_csv("data/users.csv", index=False, mode="w")

        # Se activa el mensaje de registro exitoso
        self.success_message.exec()

        # Se resetea los input
        self.firstname_input.setText("")
        self.lastname_input.setText("")
        self.doc_number_input.setText("")
        self.email_input.setText("")
        self.phone_number_input.setText("")

    def activate_success_message(self):
        self.success_message.close()

    def activate_options_window(self):
        self.previous_window.show()
        self.close()

    def sign_out(self):
        pass
