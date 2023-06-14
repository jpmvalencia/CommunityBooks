from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QFormLayout, QLabel, QLineEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QComboBox, QMessageBox, QDateEdit

from consultbooking import Consult_Booking


class Booking(QMainWindow):
    def __init__(self, previous):
        super().__init__()
        
        # Icono de la ventana
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        # Guardar en una variable la ventana anterior
        self.previous_window = previous

        # Titulo de la ventana
        self.setWindowTitle("Registrar Préstamos | CommunityBooks")

        # Color de fondo y color de letras
        self.setStyleSheet("background-color: #F6F7F9; color: #646B7A;")

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
        self.horizontal2_layout = QHBoxLayout()
        
        # Logo
        self.icon = QPixmap("icon.png").scaledToHeight(72)
        self.icon_label = QLabel()
        self.icon_label.setPixmap(self.icon)
        self.icon_label.setAlignment(Qt.AlignCenter)

        # Título
        self.booking_title = QLabel()
        self.booking_title.setText("Préstamo")
        self.booking_title.setFont(QFont("...", 14))
        self.booking_title.setAlignment(Qt.AlignCenter)

        self.blank_space = QLabel("\n") # Espacio en blanco

        # Definir los botones, inputs, etc.
        self.doc_number = QLabel()
        self.doc_number.setText("Número de Documento:")
        self.doc_number.setFont(QFont("...", 10))
        self.doc_input = QLineEdit()
        self.doc_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.doc_input.setFont(QFont("...", 10))
        self.doc_input.setFixedWidth(200)

        self.id_text = QLabel()
        self.id_text.setText("ID:")
        self.id_text.setFont(QFont("...", 10))
        self.id_input = QLineEdit()
        self.id_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.id_input.setFont(QFont("...", 10))
        self.id_input.setFixedWidth(200)

        self.quantity_text = QLabel()
        self.quantity_text.setText("Cantidad:")
        self.quantity_text.setFont(QFont("...", 10))
        self.quantity_input = QLineEdit()
        self.quantity_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.quantity_input.setFont(QFont("...", 10))
        self.quantity_input.setFixedWidth(200)

        self.booking_text = QLabel()
        self.booking_text.setText("Fecha de Reserva:")
        self.booking_text.setFont(QFont("...", 10))
        self.booking_input = QDateEdit()
        self.booking_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.booking_input.setFont(QFont("...", 10))
        self.booking_input.setFixedWidth(200)

        self.delivery_text = QLabel()
        self.delivery_text.setText("Fecha de Entrega:")
        self.delivery_text.setFont(QFont("...", 10))
        self.delivery_input = QDateEdit()
        self.delivery_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.delivery_input.setFont(QFont("...", 10))
        self.delivery_input.setFixedWidth(200)

        self.status_text = QLabel()
        self.status_text.setText("Estado:")
        self.status_text.setFont(QFont("...", 10))
        self.status_options = QComboBox()
        self.status_options.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.status_options.setFont(QFont("...", 10))
        self.status_options.setFixedWidth(200)

        self.status_options.addItem("Activo")
        self.status_options.addItem("Inactivo")

        self.back_button = QPushButton("Atrás")
        self.back_button.setFont(QFont("...", 10))
        self.back_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                       "QPushButton:pressed { background-color: #E4E7EB; }")
        self.back_button.setFixedSize(100, 50)
        self.back_button.clicked.connect(self.activate_options_window)

        self.create_button = QPushButton("Prestar")
        self.create_button.setFont(QFont("...", 10))
        self.create_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                          "QPushButton:pressed { background-color: #E4E7EB; }")
        self.create_button.setFixedSize(100, 50)
        self.create_button.clicked.connect(self.register_booking)
        
        # Botón para buscar
        self.search_button = QPushButton("Buscar")
        self.search_button.setFont(QFont("...", 10))
        self.search_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.search_button.setFixedSize(100, 50)
        self.search_button.clicked.connect(self.search_booking)
        
        # Botón para actualizar
        self.update_button = QPushButton("Actualizar")
        self.update_button.setFont(QFont("...", 10))
        self.update_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.update_button.setFixedSize(100, 50)
        self.update_button.clicked.connect(self.update_booking)

        # Botón para eliminar
        self.delete_button = QPushButton("Eliminar")
        self.delete_button.setFont(QFont("...", 10))
        self.delete_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.delete_button.setFixedSize(100, 50)
        self.delete_button.clicked.connect(self.delete_booking)

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

        # Agrega el título y el resto del contenido al layout formulario
        self.form_layout.addRow(self.icon_label)
        self.form_layout.addRow(self.booking_title)
        self.form_layout.addRow(self.blank_space)
        self.form_layout.addRow(self.doc_number, self.doc_input)
        self.form_layout.addRow(self.id_text, self.id_input)
        self.form_layout.addRow(self.booking_text, self.booking_input)
        self.form_layout.addRow(self.delivery_text, self.delivery_input)
        self.form_layout.addRow(self.status_text, self.status_options)
        
        # Agrega los botones CRUD estándo separado de los demás
        self.horizontal_layout.addWidget(self.create_button)
        self.horizontal_layout.addWidget(self.search_button)
        self.horizontal_layout.addWidget(self.update_button)
        self.horizontal_layout.addWidget(self.delete_button)

        # Agrega los botones tabular y limpiar
        self.horizontal2_layout.addWidget(self.tabular_button)
        self.horizontal2_layout.addWidget(self.clear_button)

        # Centrar los objetos
        # Se crea y define el layout con base a los botones que agregamos en el layout vertical
        self.widget1 = QWidget()
        self.widget1.setLayout(self.form_layout)
        self.button_widget = QWidget()
        self.button_widget.setLayout(self.horizontal_layout)
        self.tab_clear_widget = QWidget()
        self.tab_clear_widget.setLayout(self.horizontal2_layout)

        # Se crea y define el layout principal, el cual permitirá centrar los layouts anteriores
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
    
    # Programar botones
    def clear(self):
        # Se resetea los input
        self.doc_input.setText("")
        self.id_input.setText("")

    def register_booking(self):
        # Obtener los valores de los campos de entrada
        doc = self.doc_input.text()
        id = self.id_input.text()
        booking = self.booking_input.text()
        delivery = self.delivery_input.text()
        status = self.status_options.currentText()

        # Verificar que no se hayan dejado campos en blanco
        if (
            doc.strip() == ""
            or id.strip() == ""
            or booking.strip() == ""
            or delivery.strip() == ""
            or status.strip() == ""
        ):
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        # Validar que el documento y el id tengan el formato correcto
        if not id.isnumeric():
            QMessageBox.warning(self, "Error", "El ID del libro debe ser numérico.")
            return
        if not doc.isnumeric():
            QMessageBox.warning(self, "Error", "El documento debe ser numérico.")
            return

        # Verificar si existe el ID en books_data.txt
        books_file_path = "data/books_data.txt"
        with open(books_file_path, "r", encoding="utf-8") as books_file:
            book_ids = [line.strip().split("\t")[0] for line in books_file]
            if id not in book_ids:
                QMessageBox.warning(self, "Error", "El ID del libro no existe.")
                return

        # Verificar si existe el documento en users_data.txt
        users_file_path = "data/user_data.txt"
        with open(users_file_path, "r", encoding="utf-8") as users_file:
            user_docs = [line.strip().split("\t")[5] for line in users_file]
            if doc not in user_docs:
                QMessageBox.warning(self, "Error", "El documento no existe.")
                return

        # Verificar el estado del libro en booking_data.txt
        booking_file_path = "data/booking_data.txt"
        rows_to_keep = []
        with open(booking_file_path, "r", encoding="utf-8") as booking_file:
            for line in booking_file:
                data = line.strip().split("\t")
                if data[1] == id and data[4].strip().lower() == "activo":
                    QMessageBox.warning(self, "Error", "El libro no está disponible.")
                    return
                if data[4].strip().lower() != "inactivo":
                    rows_to_keep.append(line)  # Guardar las filas activas

        # Agregar la nueva reserva a los datos a guardar
        booking_data = f"{doc}\t{id}\t{booking}\t{delivery}\t{status}\n"
        if status.strip().lower() != "inactivo":
            rows_to_keep.append(booking_data)  # Agregar la nueva reserva si no es "inactivo"

        # Guardar los datos en el archivo de texto
        file_path = "data/booking_data.txt"  # Ruta del archivo de texto
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(rows_to_keep)

        # Mostrar un mensaje de éxito
        QMessageBox.information(self, "Registro Exitoso", "La reserva ha sido registrada exitosamente.")

    def search_booking(self):
        # Obtener el número de documento o ID a buscar
        search_input = self.id_input.text()
        doc = self.doc_input.text()

        # Leer el archivo de texto línea por línea
        file_path = "data/booking_data.txt"  # Ruta del archivo de texto
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Dividir la línea en columnas
                columns = line.strip().split("\t")

                # Verificar si el número de documento o ID coincide
                if columns[0] == doc or columns[1] == search_input:
                    # Mostrar los datos de la reserva encontrada
                    doc = columns[0]
                    id = columns[1]
                    booking = columns[2]
                    delivery = columns[3]
                    status = columns[4]

                    # Actualizar los campos de entrada con los datos encontrados
                    self.doc_input.setText(doc)
                    self.id_input.setText(id)
                    self.booking_input.setDateTime(QDateTime.fromString(booking, "d/M/yyyy"))
                    self.delivery_input.setDateTime(QDateTime.fromString(delivery, "d/M/yyyy"))
                    self.status_options.setCurrentText(status)

                    return

        # Si no se encuentra la reserva, mostrar un mensaje de error
        QMessageBox.warning(self, "Error", "No se encontró ninguna reserva con este documento o ID.")

    def update_booking(self):
        # Obtener el número de documento de la reserva a actualizar
        doc_number = self.doc_input.text()
        id_number = self.id_input.text()

        # Verificar que no haya campos vacíos
        if (
            self.doc_input.text()
            and self.id_input.text()
            and self.booking_input.text()
            and self.delivery_input.text()
            and self.status_options.currentText()
        ):
            # Validar que el número de documento tenga el formato correcto
            if not doc_number.isnumeric():
                QMessageBox.warning(self, "Error", "El número de documento debe ser numérico.")
                return
            
            if not id_number.isnumeric():
                QMessageBox.warning(self, "Error", "El número de documento debe ser numérico.")
                return

            # Leer el archivo de texto línea por línea
            file_path = "data/booking_data.txt"  # Ruta del archivo de texto
            lines = []  # Lista para almacenar las líneas actualizadas
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    # Dividir la línea en columnas
                    columns = line.rstrip("\n").split("\t")

                    # Verificar si el ID coincide
                    if columns[1] == id_number:
                        # Verificar si el estado está inactivo
                        if columns[4].strip().lower() == "inactivo":
                            continue  # Saltar la línea inactiva

                        # Actualizar los datos de la reserva
                        columns[0] = self.doc_input.text()
                        columns[2] = self.booking_input.text()
                        columns[3] = self.delivery_input.text()
                        columns[4] = self.status_options.currentText()

                        # Verificar si se seleccionó "inactivo"
                        if columns[4].strip().lower() == "inactivo":
                            continue  # Saltar la línea inactiva

                    # Reconstruir la línea con las columnas actualizadas
                    updated_line = "\t".join(columns) + "\n"
                    lines.append(updated_line)

            # Escribir las líneas actualizadas en el archivo de texto
            with open(file_path, "w", encoding="utf-8") as file:
                file.writelines(lines)

            # Mostrar un mensaje de éxito
            QMessageBox.information(self, "Actualización Exitosa", "Datos de la reserva actualizados.")
        else:
            # Mostrar un mensaje de error si hay campos vacíos
            QMessageBox.warning(self, "Error", "Completar todos los campos.")

    def delete_booking(self):
        # Obtener el ID de la reserva a eliminar
        booking_id = self.id_input.text()

        # Leer el archivo de texto línea por línea y excluir la línea de la reserva a eliminar
        file_path = "data/booking_data.txt"  # Ruta del archivo de texto
        lines = []  # Lista para almacenar las líneas excluyendo la de las reserva a eliminar
        booking_found = False  # Variable para indicar si se encontró la reserva
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Dividir la línea en columnas
                columns = line.rstrip("\n").split("\t")

                # Verificar si el ID de la reserva coincide
                if columns[1] == booking_id:
                    booking_found = True  # Se encontró la reserva
                else:
                    lines.append(line)  # Agregar la línea a la lista de líneas

        # Escribir las líneas actualizadas en el archivo de texto
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(lines)

        if booking_found:
            # Mostrar un mensaje de éxito si se encontró y eliminó la reserva
            QMessageBox.information(self, "Eliminación Exitosa", "Reserva eliminada.")
        else:
            # Mostrar un mensaje de error si no se encontró la reserva
            QMessageBox.warning(self, "Error", "La reserva no existe.")

    def activate_options_window(self):
        self.previous_window.show()
        self.close()

    def tabular_view(self):
        self.consult_booking = Consult_Booking(self)
        self.consult_booking.show()
        self.hide()
