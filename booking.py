import os
import pandas as pd

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QFormLayout, QLabel, QLineEdit, QWidget, \
    QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QComboBox, QMessageBox, QDateEdit, QApplication


class Booking(QMainWindow):
    def __init__(self, previous):
        super().__init__()
        
        # Icono de la ventana
        self.setWindowIcon(QtGui.QIcon("icon.svg"))

        self.previous_window = previous
        self.setWindowTitle("Reserva")

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

        self.booking_title = QLabel()
        self.booking_title.setText("Reserva")
        self.booking_title.setFont(QFont("...", 14))
        self.booking_title.setAlignment(Qt.AlignCenter)

        self.blank_space = QLabel("\n")

        self.doc_number = QLabel()
        self.doc_number.setText("Número de Documento:")
        self.doc_number.setFont(QFont("...", 10))
        self.doc_input = QLineEdit()
        self.doc_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                       "border-radius: 10px;")
        self.doc_input.setFont(QFont("...", 10))
        self.doc_input.setFixedWidth(200)

        self.isbn_text = QLabel()
        self.isbn_text.setText("ISBN:")
        self.isbn_text.setFont(QFont("...", 10))
        self.isbn_input = QLineEdit()
        self.isbn_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.isbn_input.setFont(QFont("...", 10))
        self.isbn_input.setFixedWidth(200)

        self.quantity_text = QLabel()
        self.quantity_text.setText("Cantidad:")
        self.quantity_text.setFont(QFont("...", 10))
        self.quantity_input = QLineEdit()
        self.quantity_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.quantity_input.setFont(QFont("...", 10))
        self.quantity_input.setFixedWidth(200)

        self.booking_text = QLabel()
        self.booking_text.setText("Fecha de Reserva:")
        self.booking_text.setFont(QFont("...", 10))
        self.booking_input = QDateEdit()
        self.booking_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.booking_input.setFont(QFont("...", 10))
        self.booking_input.setFixedWidth(200)

        self.delivery_text = QLabel()
        self.delivery_text.setText("Fecha de Entrega:")
        self.delivery_text.setFont(QFont("...", 10))
        self.delivery_input = QDateEdit()
        self.delivery_input.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                      "border-radius: 10px;")
        self.delivery_input.setFont(QFont("...", 10))
        self.delivery_input.setFixedWidth(200)

        self.status_text = QLabel()
        self.status_text.setText("Estado:")
        self.status_text.setFont(QFont("...", 10))
        self.status_options = QComboBox()
        self.status_options.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                            "border-radius: 10px;")
        self.status_options.setFont(QFont("...", 10))
        self.status_options.setFixedWidth(200)

        self.status_options.addItem("Activo")
        self.status_options.addItem("Inactivo")

        self.back_button = QPushButton("Atrás")
        self.back_button.setFont(QFont("...", 10))
        self.back_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                      "QPushButton:pressed { background-color: #1c1f26; }")
        self.back_button.setFixedSize(100, 50)
        self.back_button.clicked.connect(self.activate_options_window)

        self.booking_button = QPushButton("Reservar")
        self.booking_button.setFont(QFont("...", 10))
        self.booking_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                      "QPushButton:pressed { background-color: #1c1f26; }")
        self.booking_button.setFixedSize(100, 50)
        self.booking_button.clicked.connect(self.reserve_book)

        # Botón para cerrar sesión
        self.sign_out_button = QPushButton("Cerrar Sesión")
        self.sign_out_button.setFont(QFont("...", 10))
        self.sign_out_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                           "QPushButton:pressed { background-color: #1c1f26; }")
        self.sign_out_button.setFixedSize(150, 50)
        self.sign_out_button.clicked.connect(self.sign_out)

        self.form_layout.addRow(self.icon_label)
        self.form_layout.addRow(self.booking_title)
        self.form_layout.addRow(self.blank_space)
        self.form_layout.addRow(self.doc_number, self.doc_input)
        self.form_layout.addRow(self.isbn_text, self.isbn_input)
        self.form_layout.addRow(self.booking_text, self.booking_input)
        self.form_layout.addRow(self.delivery_text, self.delivery_input)
        self.form_layout.addRow(self.status_text, self.status_options)
        self.horizontal_layout.addWidget(self.back_button)
        self.horizontal_layout.addWidget(self.booking_button)

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
    
    def reserve_book(self):
        self.success_message = QMessageBox()
        self.success_message.setIcon(QMessageBox.Warning)
        self.success_message.setWindowTitle("Reserva Exitosa")
        self.success_message.setText("El libro se ha reservado con éxito.")
        self.success_message.setStandardButtons(QMessageBox.Ok)
        self.success_message.buttonClicked.connect(self.activate_success_message)
        
        if os.path.isfile("reserved_books.csv"):
            self.df = pd.read_csv("reserved_books.csv")
        else:
            self.df = pd.DataFrame(columns=["Número de Documento","ISBN","Fecha de Reserva","Fecha de Entrega","Estado"])

        self.data = {"Número de Documento": self.doc_input.text(), "ISBN": self.isbn_input.text(), "Fecha de Reserva": self.booking_input.text(),  "Fecha de Entrega": self.delivery_input.text(), "Estado": self.status_options.currentText()}

        self.df = self.df._append(self.data, ignore_index=True)
        
        self.df.to_csv("reserved_books.csv", index=False, mode="w")
        
        self.success_message.exec()

        self.doc_input.setText("")
        self.isbn_input.setText("")

    def activate_success_message(self):
        self.success_message.close()

    def activate_options_window(self):
        self.previous_window.show()
        self.close()

    def sign_out(self):
        pass
