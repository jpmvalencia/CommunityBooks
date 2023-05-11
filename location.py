from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QFormLayout, QLineEdit, QLabel, QPushButton, \
    QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy


class Location(QMainWindow):
    def __init__(self, previous, parent=None):
        super(Location, self).__init__(parent)

        self.previous_window = previous
        self.setWindowTitle("Ubicación")

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

        self.location_text = QLabel()
        self.location_text.setText("Ubicación")
        self.location_text.setFont(QFont("...", 14))
        self.location_text.setAlignment(Qt.AlignCenter)

        self.blank_space = QLabel("\n")

        self.bookcase_text = QLabel()
        self.bookcase_text.setText("Estantería:")
        self.bookcase_text.setFont(QFont("...", 10))
        self.bookcase_input = QLineEdit()
        self.bookcase_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.bookcase_input.setFont(QFont("...", 10))
        self.bookcase_input.setFixedWidth(200)

        self.column_text = QLabel()
        self.column_text.setText("Columna:")
        self.column_text.setFont(QFont("...", 10))
        self.column_input = QLineEdit()
        self.column_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.column_input.setFont(QFont("...", 10))
        self.column_input.setFixedWidth(200)

        self.row_text = QLabel()
        self.row_text.setText("Fila:")
        self.row_text.setFont(QFont("...", 10))
        self.row_input = QLineEdit()
        self.row_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.row_input.setFont(QFont("...", 10))
        self.row_input.setFixedWidth(200)

        self.isbn_text = QLabel()
        self.isbn_text.setText("ISBN:")
        self.isbn_text.setFont(QFont("...", 10))
        self.isbn_input = QLineEdit()
        self.isbn_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.isbn_input.setFont(QFont("...", 10))
        self.isbn_input.setFixedWidth(200)

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
        self.form_layout.addRow(self.location_text)
        self.form_layout.addRow(self.blank_space)
        self.form_layout.addRow(self.bookcase_text, self.bookcase_input)
        self.form_layout.addRow(self.column_text, self.column_input)
        self.form_layout.addRow(self.row_text, self.row_input)
        self.form_layout.addRow(self.isbn_text, self.isbn_input)
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
