from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QLabel, QLineEdit, QFormLayout, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem, QMessageBox

from consultbooks import Consult_Books

class Books(QMainWindow):
    def __init__(self, previous):
        super().__init__()

        # Icono de la ventana
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        # Guardar en una variable la ventana anterior
        self.previous_window = previous

        # Titulo de la ventana
        self.setWindowTitle("Registrar Libros | CommunityBooks")

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
        self.books_text = QLabel()
        self.books_text.setText("Libros")
        self.books_text.setFont(QFont("...", 14))
        self.books_text.setAlignment(Qt.AlignCenter)

        self.blank_space = QLabel("\n") # Espacio en blanco

        # Definir los botones, inputs, etc.
        self.id_text = QLabel()
        self.id_text.setText("ID:")
        self.id_text.setFont(QFont("...", 10))
        self.id_input = QLineEdit()
        self.id_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.id_input.setFont(QFont("...", 10))
        self.id_input.setFixedWidth(200)

        self.title_text = QLabel()
        self.title_text.setText("Título:")
        self.title_text.setFont(QFont("...", 10))
        self.title_input = QLineEdit()
        self.title_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.title_input.setFont(QFont("...", 10))
        self.title_input.setFixedWidth(200)

        self.author_text = QLabel()
        self.author_text.setText("Autor:")
        self.author_text.setFont(QFont("...", 10))
        self.author_input = QLineEdit()
        self.author_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.author_input.setFont(QFont("...", 10))
        self.author_input.setFixedWidth(200)

        self.year_text = QLabel()
        self.year_text.setText("Año:")
        self.year_text.setFont(QFont("...", 10))
        self.year_input = QLineEdit()
        self.year_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.year_input.setFont(QFont("...", 10))
        self.year_input.setFixedWidth(200)

        self.genre_text = QLabel()
        self.genre_text.setText("Género:")
        self.genre_text.setFont(QFont("...", 10))
        self.genre_input = QLineEdit()
        self.genre_input.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; border-radius: 10px;")
        self.genre_input.setFont(QFont("...", 10))
        self.genre_input.setFixedWidth(200)

        self.back_button = QPushButton("Atrás")
        self.back_button.setFont(QFont("...", 10))
        self.back_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                       "QPushButton:pressed { background-color: #E4E7EB; }")
        self.back_button.setFixedSize(100, 50)
        self.back_button.clicked.connect(self.activate_options_window)

        self.create_button = QPushButton("Registrar")
        self.create_button.setFont(QFont("...", 10))
        self.create_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.create_button.setFixedSize(100, 50)
        self.create_button.clicked.connect(self.register_book)

        # Botón para buscar
        self.search_button = QPushButton("Buscar")
        self.search_button.setFont(QFont("...", 10))
        self.search_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.search_button.setFixedSize(100, 50)
        self.search_button.clicked.connect(self.search_book)
        
        # Botón para actualizar
        self.update_button = QPushButton("Actualizar")
        self.update_button.setFont(QFont("...", 10))
        self.update_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.update_button.setFixedSize(100, 50)
        self.update_button.clicked.connect(self.update_book)

        # Botón para forma tabular
        self.tabular_button = QPushButton("Forma Tabular")
        self.tabular_button.setFont(QFont("...", 10))
        self.tabular_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.tabular_button.setFixedSize(170, 50)
        self.tabular_button.clicked.connect(self.tabular_view)

        # Botón para eliminar
        self.delete_button = QPushButton("Eliminar")
        self.delete_button.setFont(QFont("...", 10))
        self.delete_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.delete_button.setFixedSize(100, 50)
        self.delete_button.clicked.connect(self.delete_book)
        
        # Botón para limpiar
        self.clear_button = QPushButton("Limpiar")
        self.clear_button.setFont(QFont("...", 10))
        self.clear_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.clear_button.setFixedSize(170, 50)
        self.clear_button.clicked.connect(self.clear)

        # Agrega el título y el resto del contenido al layout formulario
        self.form_layout.addRow(self.icon_label)
        self.form_layout.addRow(self.books_text)
        self.form_layout.addRow(self.blank_space)
        self.form_layout.addRow(self.id_text, self.id_input)
        self.form_layout.addRow(self.title_text, self.title_input)
        self.form_layout.addRow(self.author_text, self.author_input)
        self.form_layout.addRow(self.year_text, self.year_input)
        self.form_layout.addRow(self.genre_text, self.genre_input)

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
        self.id_input.setText("")
        self.title_input.setText("")
        self.author_input.setText("")
        self.year_input.setText("")
        self.genre_input.setText("")

    def register_book(self):
        # Obtener los valores de los campos de entrada
        id = self.id_input.text()
        title = self.title_input.text()
        author = self.author_input.text()
        year = self.year_input.text()
        genre = self.genre_input.text()

        # Verificar que no se hayan dejado campos en blanco
        if (
            id.strip() == ""
            or title.strip() == ""
            or author.strip() == ""
            or year.strip() == ""
            or genre.strip() == ""
        ):
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        # Validar que el genero, autor, año e identificador tengan el formato que es
        if genre.isnumeric():
            QMessageBox.warning(self, "Error", "El género solo debe contener letras.")
            return
        if author.isnumeric():
            QMessageBox.warning(self, "Error", "El autor solo debe contener letras.")
            return
        if not year.isnumeric():
            QMessageBox.warning(self, "Error", "El año del libro debe ser numérico.")
            return
        if not id.isnumeric():
            QMessageBox.warning(self, "Error", "El ID del libro debe ser numérico.")
            return

        # Verificar libros repetidos basados en el identificador y titulo
        file_path = "data/books_data.txt"  # Ruta del archivo de texto
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split("\t")
                if (
                    data[1].lower() == title.lower()
                ):
                    QMessageBox.warning(
                        self, "Error", "Ya existe un libro con el mismo nombre."
                    )
                    return
                if data[0] == id:
                    QMessageBox.warning(self, "Error", "El identificador ya está en uso.")
                    return

        # Crear una cadena con los datos del libro en forma de columna
        book_data = f"{id}\t{title}\t{author}\t{year}\t{genre}\n"

        # Guardar los datos en el archivo de texto
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(book_data)

        # Mostrar un mensaje de éxito
        QMessageBox.information(self, "Registro Exitoso", "El libro ha sido registrado exitosamente.")

    def search_book(self):
        # Obtener el número de identificador a buscar
        id_number = self.id_input.text()

        # Leer el archivo de texto línea por línea
        file_path = "data/books_data.txt"  # Ruta del archivo de texto
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Dividir la línea en columnas
                columns = line.strip().split("\t")

                # Verificar si el número de ID coincide
                if columns[0] == id_number or columns[1] == self.title_input.text():
                    # Mostrar los datos del libro encontrado
                    id = columns[0]
                    title = columns[1]
                    author = columns[2]
                    year = columns[3]
                    genre = columns[4]

                    # Actualizar los campos de entrada con los datos encontrados
                    self.id_input.setText(id)
                    self.title_input.setText(title)
                    self.author_input.setText(author)
                    self.year_input.setText(year)
                    self.genre_input.setText(genre)

                    return

        # Si no se encuentra el libro, mostrar un mensaje de error
        QMessageBox.warning(self, "Error", "No se encontró ningun libro con este ID.")

    def update_book(self):
        # Obtener el número de identificador del libro a actualizar
        id_number = self.id_input.text()

        # Verificar que no haya campos vacíos
        if (
            self.id_input.text()
            and self.title_input.text()
            and self.author_input.text()
            and self.year_input.text()
            and self.genre_input.text()
        ):
            # Validar que el genero, autor, año e identificador tengan el formato correcto
            id = self.id_input.text()
            title = self.title_input.text()
            author = self.author_input.text()
            year = self.year_input.text()
            genre = self.genre_input.text()

            # Verificar que no se hayan dejado campos en blanco
            if (
                id.strip() == ""
                or title.strip() == ""
                or author.strip() == ""
                or year.strip() == ""
                or genre.strip() == ""
            ):
                QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
                return

            # Validar que el genero, autor, año tengan el formato correcto
            if genre.isnumeric():
                QMessageBox.warning(self, "Error", "El género solo debe contener letras.")
                return
            if author.isnumeric():
                QMessageBox.warning(self, "Error", "El autor solo debe contener letras.")
                return
            if not year.isnumeric():
                QMessageBox.warning(self, "Error", "El año del libro debe ser numérico.")
                return

            # Leer el archivo de texto línea por línea
            file_path = "data/books_data.txt"  # Ruta del archivo de texto
            lines = []  # Lista para almacenar las líneas actualizadas
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    # Dividir la línea en columnas
                    columns = line.rstrip("\n").split("\t")

                    # Verificar si el número de identificador coincide
                    if columns[0] == id_number:
                        # Mantener el ID original y actualizar los demás datos del libro
                        columns[1] = title
                        columns[2] = author
                        columns[3] = year
                        columns[4] = genre

                    # Reconstruir la línea con las columnas actualizadas
                    updated_line = "\t".join(columns) + "\n"
                    lines.append(updated_line)

            # Escribir las líneas actualizadas en el archivo de texto
            with open(file_path, "w", encoding="utf-8") as file:
                file.writelines(lines)

            # Mostrar un mensaje de éxito
            QMessageBox.information(self, "Actualización Exitosa", "Datos del libro actualizados.")
        else:
            # Mostrar un mensaje de error si hay campos vacíos
            QMessageBox.warning(self, "Error", "Completar todos los campos.")


    def delete_book(self):
        # Obtener el número de identificador del libro a eliminar
        id_number = self.id_input.text()

        # Leer el archivo de texto línea por línea y excluir la línea del libro a eliminar
        file_path = "data/books_data.txt"  # Ruta del archivo de texto
        lines = []  # Lista para almacenar las líneas excluyendo la del libro a eliminar
        book_found = False  # Variable para indicar si se encontró el libro
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Dividir la línea en columnas
                columns = line.rstrip("\n").split("\t")

                # Verificar si el número de identificador coincide
                if columns[0] == id_number:
                    book_found = True  # Se encontró el libro
                else:
                    lines.append(line)  # Agregar la línea a la lista de líneas

        # Escribir las líneas actualizadas en el archivo de texto
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(lines)

        if book_found:
            # Mostrar un mensaje de éxito si se encontró y eliminó el libro
            QMessageBox.information(self, "Eliminación Exitosa", "Libro eliminado.")
        else:
            # Mostrar un mensaje de error si no se encontró el libro
            QMessageBox.warning(self, "Error", "El libro no existe.")

        """# Se resetea los input
        self.id_input.setText("")
        self.title_input.setText("")
        self.author_input.setText("")
        self.year_input.setText("")
        self.genre_input.setText("")"""

    def activate_options_window(self):
        self.previous_window.show()
        self.close()

    def tabular_view(self):
        self.consult_books = Consult_Books(self)
        self.consult_books.show()
        self.hide()
