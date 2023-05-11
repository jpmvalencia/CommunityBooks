from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QFormLayout, QLabel, QLineEdit, QWidget, \
    QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QSpacerItem, QSizePolicy


class MasterBooking(QMainWindow):
    def __init__(self, previous, parent=None):
        super(MasterBooking, self).__init__(parent)

        # Icono de la ventana
        self.setWindowIcon(QtGui.QIcon("icon.svg"))

        self.previous_window = previous
        self.setWindowTitle("Reservas")

        self.setStyleSheet("background-color: #2a2d37; color: #c0c5ce;")

        self.width = 1280
        self.height = 720

        self.resize(self.width, self.height)

        self.screen = self.frameGeometry()
        self.center = QDesktopWidget().availableGeometry().center()
        self.screen.moveCenter(self.center)
        self.move(self.screen.topLeft())

        self.vertical_layout = QVBoxLayout()
        self.horizontal_layout = QHBoxLayout()
        self.form_layout = QGridLayout()
        
        # Logo
        self.icon = QPixmap("icon.svg").scaledToHeight(72)
        self.icon_label = QLabel()
        self.icon_label.setPixmap(self.icon)
        self.icon_label.setAlignment(Qt.AlignCenter)

        self.library_title = QLabel()
        self.library_title.setText("Reservas")
        self.library_title.setFont(QFont("...", 14))
        self.library_title.setAlignment(Qt.AlignCenter)

        self.blank_space = QLabel("\n")

        self.doc_number_text = QLabel()
        self.doc_number_text.setText("Número de documento")
        self.doc_number_text.setFont(QFont("...", 10))

        self.isbn_text = QLabel()
        self.isbn_text.setText("ISBN")
        self.isbn_text.setFont(QFont("...", 10))

        self.reserve_text = QLabel()
        self.reserve_text.setText("Fecha de Reserva")
        self.reserve_text.setFont(QFont("...", 10))

        self.return_text = QLabel()
        self.return_text.setText("Fecha de Entrega")
        self.return_text.setFont(QFont("...", 10))
        
        self.status_text = QLabel()
        self.status_text.setText("Estado")
        self.status_text.setFont(QFont("...", 10))
        
        self.options_text = QLabel()
        self.options_text.setText("Opciones")
        self.options_text.setFont(QFont("...", 10))




        
        self.doc_number_input = QLineEdit()
        self.doc_number_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                       "border-radius: 10px;")
        self.doc_number_input.setFont(QFont("...", 10))
        self.doc_number_input.setFixedWidth(200)

        self.doc_number_input2 = QLineEdit()
        self.doc_number_input2.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                       "border-radius: 10px;")
        self.doc_number_input2.setFont(QFont("...", 10))
        self.doc_number_input2.setFixedWidth(200)

        
        self.isbn_input = QLineEdit()
        self.isbn_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.isbn_input.setFont(QFont("...", 10))
        self.isbn_input.setFixedWidth(200)

        self.isbn_input2 = QLineEdit()
        self.isbn_input2.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.isbn_input2.setFont(QFont("...", 10))
        self.isbn_input2.setFixedWidth(200)
        
        
        self.reserve_input = QLineEdit()
        self.reserve_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.reserve_input.setFont(QFont("...", 10))
        self.reserve_input.setFixedWidth(200)

        self.reserve_input2 = QLineEdit()
        self.reserve_input2.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.reserve_input2.setFont(QFont("...", 10))
        self.reserve_input2.setFixedWidth(200)

        
        self.return_input = QLineEdit()
        self.return_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.return_input.setFont(QFont("...", 10))
        self.return_input.setFixedWidth(200)

        self.return_input2 = QLineEdit()
        self.return_input2.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.return_input2.setFont(QFont("...", 10))
        self.return_input2.setFixedWidth(200)

        
        self.status_input = QLineEdit()
        self.status_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.status_input.setFont(QFont("...", 10))
        self.status_input.setFixedWidth(200)

        self.status_input2 = QLineEdit()
        self.status_input2.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.status_input2.setFont(QFont("...", 10))
        self.status_input2.setFixedWidth(200)


        self.update_button = QPushButton("♺")
        self.update_button.setFont(QFont("...", 10))
        self.update_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #1c1f26; }")
        self.update_button.setFixedSize(55, 34)
        self.delete_button = QPushButton("🗑️")
        self.delete_button.setFont(QFont("...", 10))
        self.delete_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #1c1f26; }")
        self.delete_button.setFixedSize(55, 34)
        
        self.update_button2 = QPushButton("♺")
        self.update_button2.setFont(QFont("...", 10))
        self.update_button2.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #1c1f26; }")
        self.update_button2.setFixedSize(55, 34)
        self.delete_button2 = QPushButton("🗑️")
        self.delete_button2.setFont(QFont("...", 10))
        self.delete_button2.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #1c1f26; }")
        self.delete_button2.setFixedSize(55, 34)






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

        self.vertical_layout.addWidget(self.icon_label)
        self.vertical_layout.addWidget(self.library_title)
        self.vertical_layout.addWidget(self.blank_space)

        self.form_layout.addWidget(self.doc_number_text, 0, 0)
        self.form_layout.addWidget(self.isbn_text, 0, 1)
        self.form_layout.addWidget(self.reserve_text, 0, 2)
        self.form_layout.addWidget(self.return_text, 0, 3)
        self.form_layout.addWidget(self.status_text, 0, 4)
        self.form_layout.addWidget(self.options_text, 0, 5)
        
        self.form_layout.addWidget(self.doc_number_input, 1, 0)
        self.form_layout.addWidget(self.isbn_input, 1, 1)
        self.form_layout.addWidget(self.reserve_input, 1, 2)
        self.form_layout.addWidget(self.return_input, 1, 3)
        self.form_layout.addWidget(self.status_input, 1, 4)
        self.form_layout.addWidget(self.update_button, 1, 5)
        self.form_layout.addWidget(self.delete_button, 1, 6)

        self.form_layout.addWidget(self.doc_number_input2, 2, 0)
        self.form_layout.addWidget(self.isbn_input2, 2, 1)
        self.form_layout.addWidget(self.reserve_input2, 2, 2)
        self.form_layout.addWidget(self.return_input2, 2, 3)
        self.form_layout.addWidget(self.status_input2, 2, 4)
        self.form_layout.addWidget(self.update_button2, 2, 5)
        self.form_layout.addWidget(self.delete_button2, 2, 6)
        
        self.horizontal_layout.addWidget(self.back_button)
        #self.horizontal_layout.addWidget(self.add_button)
        
        self.widget1 = QWidget()
        self.widget1.setLayout(self.vertical_layout)

        self.widget2 = QWidget()
        self.widget2.setLayout(self.form_layout)

        self.button_widget = QWidget()
        self.button_widget.setLayout(self.horizontal_layout)

        self.main_layout = QVBoxLayout()
        #self.main_layout.addWidget(self.sign_out_button, alignment=Qt.AlignRight)
        self.main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.main_layout.addWidget(self.widget1, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.widget2, alignment=Qt.AlignCenter)
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
