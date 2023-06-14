from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QComboBox, QLineEdit, QWidget, QDesktopWidget, QFormLayout, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout, QMessageBox

from consultusers import Consult_Users


class Users(QMainWindow):
    def __init__(self, previous):
        super().__init__()
        
        # Icono de la ventana
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        # Guardar en una variable la ventana anterior
        self.previous_window = previous

        # Titulo de la ventana
        self.setWindowTitle("Registrar Usuarios | CommunityBooks")

        # Color de fondo y color de letras
        self.setStyleSheet("background-color: #F6F7F9; color: #646B7A;")

        # Establecer propiedades de ancho y alto
        self.width = 1280
        self.height = 800

        # Establecer el tamaño de la ventana
        self.resize(self.width, self.height)

        self.setFixedSize(self.width, self.height)

        # Centrar la ventana
        self.screen = self.frameGeometry()
        self.center = QDesktopWidget().availableGeometry().center()
        self.screen.moveCenter(self.center)
        self.move(self.screen.topLeft())

        # Establecer el layout que contendrán los objetos
        self.horizontal_layout = QHBoxLayout()
        self.form_layout = QFormLayout()
        self.horizontal2_layout = QHBoxLayout()

        # Definir los textos, inputs y botones
        # Logo
        self.icon = QPixmap("icon.png").scaledToHeight(72)
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
        self.user_type_options.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
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
        self.firstname_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.firstname_input.setFont(QFont("...", 10))
        self.firstname_input.setFixedWidth(200)

        # Texto e input para el apellido
        self.lastname_text = QLabel()
        self.lastname_text.setText("Apellido:")
        self.lastname_text.setFont(QFont("...", 10))
        self.lastname_input = QLineEdit()
        self.lastname_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.lastname_input.setFont(QFont("...", 10))
        self.lastname_input.setFixedWidth(200)

        # Texto y opciones para el sexo
        self.user_sex_text = QLabel()
        self.user_sex_text.setText("Sexo:")
        self.user_sex_text.setFont(QFont("...", 10))
        self.user_sex_options = QComboBox()
        self.user_sex_options.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
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
        self.doc_type_options.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
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
        self.doc_number_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.doc_number_input.setFont(QFont("...", 10))
        self.doc_number_input.setFixedWidth(200)

        # Texto e input para el correo electrónico
        self.email_text = QLabel()
        self.email_text.setText("Correo Electrónico:")
        self.email_text.setFont(QFont("...", 10))
        self.email_input = QLineEdit()
        self.email_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.email_input.setFont(QFont("...", 10))
        self.email_input.setFixedWidth(200)

        # Texto e input para el número de celular
        self.phone_number_text = QLabel()
        self.phone_number_text.setText("Número de Celular:")
        self.phone_number_text.setFont(QFont("...", 10))
        self.phone_number_input = QLineEdit()
        self.phone_number_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.phone_number_input.setFont(QFont("...", 10))
        self.phone_number_input.setFixedWidth(200)

        # Botón para regresar a la ventana anterior
        self.back_button = QPushButton("Atrás")
        self.back_button.setFont(QFont("...", 10))
        self.back_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                       "QPushButton:pressed { background-color: #E4E7EB; }")
        self.back_button.setFixedSize(100, 50)
        self.back_button.clicked.connect(self.activate_options_window)

        # Botón para registrar al usuario
        self.create_button = QPushButton("Registrar")
        self.create_button.setFont(QFont("...", 10))
        self.create_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.create_button.setFixedSize(100, 50)
        self.create_button.clicked.connect(self.register_user)

        # Botón para buscar
        self.search_button = QPushButton("Buscar")
        self.search_button.setFont(QFont("...", 10))
        self.search_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.search_button.setFixedSize(100, 50)
        self.search_button.clicked.connect(self.search_user)
        
        # Botón para actualizar
        self.update_button = QPushButton("Actualizar")
        self.update_button.setFont(QFont("...", 10))
        self.update_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.update_button.setFixedSize(100, 50)
        self.update_button.clicked.connect(self.update_user)

        # Botón para eliminar
        self.delete_button = QPushButton("Eliminar")
        self.delete_button.setFont(QFont("...", 10))
        self.delete_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.delete_button.setFixedSize(100, 50)
        self.delete_button.clicked.connect(self.delete_user)
        
        # Botón para forma tabular
        self.tabular_button = QPushButton("Forma Tabular")
        self.tabular_button.setFont(QFont("...", 10))
        self.tabular_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.tabular_button.setFixedSize(170, 50)
        self.tabular_button.clicked.connect(self.tabular_view)

         # Botón para limpiar
        self.clear_button = QPushButton("Limpiar")
        self.clear_button.setFont(QFont("...", 10))
        self.clear_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.clear_button.setFixedSize(170, 50)
        self.clear_button.clicked.connect(self.clear)

        # Agrega los objetos al layout tipo formulario
        self.form_layout.addRow(self.icon_label)
        self.form_layout.addRow(self.register_title)
        self.form_layout.addRow(self.blank_space)
        self.form_layout.addRow(self.doc_number_text, self.doc_number_input)
        #self.form_layout.addRow(self.user_type_text, self.user_type_options)
        self.form_layout.addRow(self.firstname_text, self.firstname_input)
        self.form_layout.addRow(self.lastname_text, self.lastname_input)
        self.form_layout.addRow(self.user_sex_text, self.user_sex_options)
        self.form_layout.addRow(self.doc_type_text, self.doc_type_options)
        self.form_layout.addRow(self.email_text, self.email_input)
        self.form_layout.addRow(self.phone_number_text, self.phone_number_input)

        # Agrega los botones CRUD estándo separado de los demás
        self.horizontal_layout.addWidget(self.create_button)
        self.horizontal_layout.addWidget(self.search_button)
        self.horizontal_layout.addWidget(self.update_button)
        self.horizontal_layout.addWidget(self.delete_button)

        # Agrega los botones tabular y limpiar
        self.horizontal2_layout.addWidget(self.tabular_button)
        self.horizontal2_layout.addWidget(self.clear_button)

        # Centrar los objetos
        # Se crea y define el layout con base a los objetos que agregamos en los layout anteriores
        self.widget1 = QWidget()
        self.widget1.setLayout(self.form_layout)

        self.button_widget = QWidget()
        self.button_widget.setLayout(self.horizontal_layout)

        self.tab_clear_widget = QWidget()
        self.tab_clear_widget.setLayout(self.horizontal2_layout)

        # Se crea y define el layout principal, el cual permitirá centrar los layouts anteriores.
        self.main_layout = QVBoxLayout()
        self.main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.main_layout.addWidget(self.widget1, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.button_widget, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.tab_clear_widget, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.back_button, alignment=Qt.AlignCenter)
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
    def clear(self):
        # Se resetea los input
        self.firstname_input.setText("")
        self.lastname_input.setText("")
        self.doc_number_input.setText("")
        self.email_input.setText("")
        self.phone_number_input.setText("")

    def register_user(self):
        # Obtener los valores de los campos de entrada
        user_type = self.user_type_options.currentText()
        firstname = self.firstname_input.text()
        lastname = self.lastname_input.text()
        user_sex = self.user_sex_options.currentText()
        doc_type = self.doc_type_options.currentText()
        doc_number = self.doc_number_input.text()
        email = self.email_input.text()
        phone_number = self.phone_number_input.text()

        # Verificar que no se hayan dejado campos en blanco
        if (
            user_type.strip() == ""
            or firstname.strip() == ""
            or lastname.strip() == ""
            or user_sex.strip() == ""
            or doc_type.strip() == ""
            or doc_number.strip() == ""
            or email.strip() == ""
            or phone_number.strip() == ""
        ):
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        # Validar que el nombre y apellido contengan solo letras
        if firstname.isnumeric():
            QMessageBox.warning(self, "Error", "El nombre solo debe contener letras.")
            return
        if lastname.isnumeric():
            QMessageBox.warning(self, "Error", "El apellido solo debe contener letras.")
            return

        # Validar que el número de documento y número de teléfono sean numéricos
        if not doc_number.isnumeric():
            QMessageBox.warning(self, "Error", "El número de documento debe ser numérico.")
            return
        if not phone_number.isnumeric():
            QMessageBox.warning(self, "Error", "El número de teléfono debe ser numérico.")
            return

        # Verificar usuarios repetidos basados en el nombre, apellido y número de documento
        file_path = "data/user_data.txt"  # Ruta del archivo de texto
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split("\t")
                if (
                    data[1].lower() == firstname.lower()
                    and data[2].lower() == lastname.lower()
                ):
                    QMessageBox.warning(
                        self, "Error", "Ya existe un usuario con el mismo nombre y apellido."
                    )
                    return
                if data[5] == doc_number:
                    QMessageBox.warning(self, "Error", "El número de documento ya está en uso.")
                    return

        # Crear una cadena con los datos del usuario en forma de columna
        user_data = f"{user_type}\t{firstname}\t{lastname}\t{user_sex}\t{doc_type}\t{doc_number}\t{email}\t{phone_number}\n"

        # Guardar los datos en el archivo de texto
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(user_data)

        # Mostrar un mensaje de éxito
        QMessageBox.information(self, "Registro Exitoso", "El usuario ha sido registrado exitosamente.")

    def activate_options_window(self):
        self.previous_window.show()
        self.close()
    
    def search_user(self):
        # Obtener el número de documento a buscar
        doc_number = self.doc_number_input.text()

        # Leer el archivo de texto línea por línea
        file_path = "data/user_data.txt"  # Ruta del archivo de texto
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Dividir la línea en columnas
                columns = line.strip().split("\t")

                # Verificar si el número de documento coincide
                if columns[5] == doc_number:
                    # Mostrar los datos del usuario encontrado
                    user_type = columns[0]
                    firstname = columns[1]
                    lastname = columns[2]
                    user_sex = columns[3]
                    doc_type = columns[4]
                    email = columns[6]
                    phone_number = columns[7]

                    # Actualizar los campos de entrada con los datos encontrados
                    self.user_type_options.setCurrentText(user_type)
                    self.firstname_input.setText(firstname)
                    self.lastname_input.setText(lastname)
                    self.user_sex_options.setCurrentText(user_sex)
                    self.doc_type_options.setCurrentText(doc_type)
                    self.email_input.setText(email)
                    self.phone_number_input.setText(phone_number)

                    return

        # Si no se encuentra el usuario, mostrar un mensaje de error
        QMessageBox.warning(self, "Error", "No se encontró ningun usuario con este documento.")

    def update_user(self):
        # Obtener el número de documento del usuario a actualizar
        doc_number = self.doc_number_input.text()

        # Verificar que no haya campos vacíos
        if (
            self.user_type_options.currentText().strip() == ""
            or self.firstname_input.text().strip() == ""
            or self.lastname_input.text().strip() == ""
            or self.user_sex_options.currentText().strip() == ""
            or self.doc_type_options.currentText().strip() == ""
            or self.doc_number_input.text().strip() == ""
            or self.email_input.text().strip() == ""
            or self.phone_number_input.text().strip() == ""
        ):
            # Mostrar un mensaje de error si hay campos vacíos
            QMessageBox.warning(self, "Error", "Completar todos los campos.")
            return

        # Validar que el nombre y apellido contengan solo letras
        if self.firstname_input.text().isnumeric():
            QMessageBox.warning(self, "Error", "El nombre solo debe contener letras.")
            return
        if self.lastname_input.text().isnumeric():
            QMessageBox.warning(self, "Error", "El apellido solo debe contener letras.")
            return

        # Validar que el número de documento y número de teléfono sean numéricos
        if not self.doc_number_input.text().isnumeric():
            QMessageBox.warning(self, "Error", "El número de documento debe ser numérico.")
            return
        if not self.phone_number_input.text().isnumeric():
            QMessageBox.warning(self, "Error", "El número de teléfono debe ser numérico.")
            return

        # Leer el archivo de texto línea por línea
        file_path = "data/user_data.txt"  # Ruta del archivo de texto
        lines = []  # Lista para almacenar las líneas actualizadas
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Dividir la línea en columnas
                columns = line.rstrip("\n").split("\t")

                # Verificar si el número de documento coincide
                if columns[5] == doc_number:
                    # Actualizar los datos del usuario
                    columns[0] = self.user_type_options.currentText()
                    columns[1] = self.firstname_input.text()
                    columns[2] = self.lastname_input.text()
                    columns[3] = self.user_sex_options.currentText()
                    columns[4] = self.doc_type_options.currentText()
                    columns[6] = self.email_input.text()
                    columns[7] = self.phone_number_input.text()

                # Reconstruir la línea con las columnas actualizadas
                updated_line = "\t".join(columns) + "\n"
                lines.append(updated_line)

        # Escribir las líneas actualizadas en el archivo de texto
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(lines)

        # Mostrar un mensaje de éxito
        QMessageBox.information(self, "Actualización Exitosa", "Datos de usuario actualizados.")

    def delete_user(self):
        # Obtener el número de documento del usuario a eliminar
        doc_number = self.doc_number_input.text()

        # Leer el archivo de texto línea por línea y excluir la línea del usuario a eliminar
        file_path = "data/user_data.txt"  # Ruta del archivo de texto
        lines = []  # Lista para almacenar las líneas excluyendo la del usuario a eliminar
        user_found = False  # Variable para indicar si se encontró el usuario
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Dividir la línea en columnas
                columns = line.rstrip("\n").split("\t")

                # Verificar si el número de documento coincide
                if columns[5] == doc_number:
                    user_found = True  # Se encontró el usuario
                else:
                    lines.append(line)  # Agregar la línea a la lista de líneas

        # Escribir las líneas actualizadas en el archivo de texto
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(lines)

        if user_found:
            # Mostrar un mensaje de éxito si se encontró y eliminó el usuario
            QMessageBox.information(self, "Eliminación Exitosa", "Usuario eliminado.")
        else:
            # Mostrar un mensaje de error si no se encontró el usuario
            QMessageBox.warning(self, "Error", "El usuario no existe.")

    def activate_options_window(self):
        self.previous_window.show()
        self.close()

    def tabular_view(self):
        self.consult_users = Consult_Users(self)
        self.consult_users.show()
        self.hide()
