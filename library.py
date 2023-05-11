from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QFormLayout, QLabel, QLineEdit, QWidget, \
    QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy


class Library(QMainWindow):
    def __init__(self, previous, parent=None):
        super(Library, self).__init__(parent)

        # Icono de la ventana
        self.setWindowIcon(QtGui.QIcon("icon.svg"))

        self.previous_window = previous
        self.setWindowTitle("Librería")

        self.setStyleSheet("background-color: #2a2d37; color: #c0c5ce;")

        self.width = 1280
        self.height = 720

        self.resize(self.width, self.height)

        self.screen = self.frameGeometry()
        self.center = QDesktopWidget().availableGeometry().center()
        self.screen.moveCenter(self.center)
        self.move(self.screen.topLeft())

        self.horizontal_layout = QHBoxLayout()
        self.form_layout = QFormLayout()
        
        # Logo
        self.icon = QPixmap("icon.svg").scaledToHeight(72)
        self.icon_label = QLabel()
        self.icon_label.setPixmap(self.icon)
        self.icon_label.setAlignment(Qt.AlignCenter)

        self.library_title = QLabel()
        self.library_title.setText("Librería")
        self.library_title.setFont(QFont("...", 14))
        self.library_title.setAlignment(Qt.AlignCenter)

        self.blank_space = QLabel("\n")

        self.genre_text = QLabel()
        self.genre_text.setText("Género:")
        self.genre_text.setFont(QFont("...", 10))
        self.genre_input = QLineEdit()
        self.genre_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                       "border-radius: 10px;")
        self.genre_input.setFont(QFont("...", 10))
        self.genre_input.setFixedWidth(200)

        self.isbn_text = QLabel()
        self.isbn_text.setText("Código:")
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

        self.back_button = QPushButton("Atrás")
        self.back_button.setFont(QFont("...", 10))
        self.back_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                      "QPushButton:pressed { background-color: #1c1f26; }")
        self.back_button.setFixedSize(100, 50)
        self.back_button.clicked.connect(self.activate_options_window)

        self.add_button = QPushButton("Agregar")
        self.add_button.setFont(QFont("...", 10))
        self.add_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                      "QPushButton:pressed { background-color: #1c1f26; }")
        self.add_button.setFixedSize(100, 50)

        # Botón para cerrar sesión
        self.sign_out_button = QPushButton("Cerrar Sesión")
        self.sign_out_button.setFont(QFont("...", 10))
        self.sign_out_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                           "QPushButton:pressed { background-color: #1c1f26; }")
        self.sign_out_button.setFixedSize(150, 50)
        self.sign_out_button.clicked.connect(self.sign_out)

        self.form_layout.addRow(self.icon_label)
        self.form_layout.addRow(self.library_title)
        self.form_layout.addRow(self.blank_space)
        self.form_layout.addRow(self.genre_text, self.genre_input)
        self.form_layout.addRow(self.isbn_text, self.isbn_input)
        self.form_layout.addRow(self.name_text, self.name_input)
        self.horizontal_layout.addWidget(self.back_button)
        self.horizontal_layout.addWidget(self.add_button)

        self.widget1 = QWidget()
        self.widget1.setLayout(self.form_layout)

        self.button_widget = QWidget()
        self.button_widget.setLayout(self.horizontal_layout)

        self.main_layout = QVBoxLayout()
        #self.main_layout.addWidget(self.sign_out_button, alignment=Qt.AlignRight)
        self.main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.main_layout.addWidget(self.widget1, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.button_widget, alignment=Qt.AlignCenter)
        self.main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

    def activate_options_window(self):
        self.previous_window.show()
        self.close()

    def sign_out(self):
        pass
