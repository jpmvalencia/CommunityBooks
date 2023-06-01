from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QDesktopWidget, QMessageBox, QVBoxLayout, QWidget
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtCore import Qt
import csv


class Consult_Booking(QMainWindow):
    def __init__(self, previous):
        super().__init__()
        
        # Icono de la ventana
        self.setWindowIcon(QtGui.QIcon("icon.svg"))

        # Guardar en una variable la ventana anterior
        self.previous_window = previous

        # Titulo de la ventana
        self.setWindowTitle("Consultar Reservas | CommunityBooks")

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
        table = QTableWidget()
        self.setCentralWidget(table)

        self.table = table
        self.table.setStyleSheet("""
            QScrollBar:vertical {
                border: none;
                background: rgba(0, 0, 0, 0);
                width: 10px;
                margin: 0px 0px 0px 0px;
                border-radius: 5px;
            }

            QScrollBar::handle:vertical {
                background: #dbdbdb;
                min-height: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical {
                border: none;
                background: none;
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }

            QScrollBar::sub-line:vertical {
                border: none;
                background: none;
                height: 0px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }

            QScrollBar:horizontal {
                border: none;
                background: rgba(0, 0, 0, 0);
                height: 10px;
                margin: 0px 0px 0px 0px;
                border-radius: 5px;
            }

            QScrollBar::handle:horizontal {
                background: #dbdbdb;
                min-width: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:horizontal {
                border: none;
                background: none;
                width: 0px;
                subcontrol-position: rigth;
                subcontrol-origin: margin;
            }

            QScrollBar::sub-line:horizontal {
                border: none;
                background: none;
                width: 0px;
                subcontrol-position: left;
                subcontrol-origin: margin;
            }

            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                background: none;
            }
        """)

        table.setMinimumSize(700, 500)
        table.setStyleSheet("QTableView {border: 1px solid #1c1f26;}"
                            "QTableWidget {border-radius: 10px;}")

        # Creamos un objeto QWidget que contenga la tabla
        table_widget = QWidget()
        table_widget.setLayout(QVBoxLayout())
        table_widget.layout().addWidget(table, alignment=Qt.AlignCenter)

        # Establecer self.table_widget como el widget central de la ventana
        self.setCentralWidget(table_widget)

        # Cargamos los datos del archivo CSV
        with open('data/reserved_books.csv', newline='', encoding='utf-8') as csvfile:
            data = list(csv.reader(csvfile))

        # Establecemos el número de filas y columnas en la tabla
        table.setRowCount(len(data))
        table.setColumnCount(len(data[0]))

        # Ocultamos las cabeceras de la tabla
        table.horizontalHeader().setVisible(True)

        # Rellenamos la tabla con los datos del archivo CSV
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(item))
        
        # Ajustar el tamaño de las columnas y filas al contenido
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        # Establecer un ancho mínimo para cada columna
        for i in range(table.columnCount()):
            width = table.columnWidth(i)
            table.setColumnWidth(i, width + 30) # 30 es el espacio extra que queremos añadir
        
        table.cellDoubleClicked.connect(self.editCell)

        # Cambiar el texto de las cabeceras de la tabla
        headers = ['Número de Documento', 'ISBN', 'Fecha de Reserva', 'Fecha de Entrega', 'Estado']
        table.setHorizontalHeaderLabels(headers)

        # Agregar un QPushButton para eliminar fila
        self.delete_button = QtWidgets.QPushButton("Eliminar fila", self)
        self.delete_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #1c1f26; }")
        self.delete_button.setFixedSize(150, 50)
        self.delete_button.clicked.connect(self.delete_row)

        # Agregar un QLineEdit y un QPushButton para buscar
        self.search_line_edit = QtWidgets.QLineEdit(self)
        self.search_line_edit.setFixedSize(700, 50)
        self.search_line_edit.setPlaceholderText("Buscar")
        self.search_line_edit.setStyleSheet("padding: 7px; border: none; background-color: #1c1f26; "
                                            "border-radius: 10px;")
        self.search_line_edit.returnPressed.connect(self.search)
        self.search_button = QtWidgets.QPushButton("Buscar", self)
        self.search_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #1c1f26; }")
        self.search_button.setFixedSize(150, 50)
        self.search_button.clicked.connect(self.search)


        self.previous_button = QtWidgets.QPushButton("Atrás", self)
        self.previous_button.setStyleSheet("QPushButton { background-color: #232632; border-radius: 10px; }"
                                       "QPushButton:pressed { background-color: #1c1f26; }")
        self.previous_button.setFixedSize(150, 50)
        self.previous_button.clicked.connect(self.activate_previous_window)

        spacer = QtWidgets.QWidget(self)
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Agregar los widgets a la barra de herramientas
        self.toolbar = QtWidgets.QToolBar(self)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.toolbar.addWidget(self.delete_button)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.search_line_edit)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.search_button)
        self.toolbar.addWidget(spacer)
        self.toolbar.addWidget(self.previous_button)

    # Programar los botones
    def delete_row(self):
        # Obtener la fila seleccionada
        row = self.table.currentRow()

        # Eliminar la fila seleccionada
        self.table.removeRow(row)

        # Guardar los datos actualizados en el archivo CSV
        self.save_data_to_csv()

    def activate_previous_window(self):
        self.previous_window.show()
        self.close()

    def search(self):
        # Obtener el texto a buscar
        text_to_search = self.search_line_edit.text().lower()

        # Recorrer las filas de la tabla
        for row in range(self.table.rowCount()):
            # Recorrer las celdas de la fila actual
            for column in range(self.table.columnCount()):
                cell = self.table.item(row, column)
                if cell is not None:
                    cell_text = cell.text().lower()
                    if text_to_search in cell_text:
                        # Seleccionar la fila que contiene el texto buscado
                        self.table.selectRow(row)
                        # Centrar la vista en la fila seleccionada
                        self.table.scrollToItem(cell, QtWidgets.QAbstractItemView.PositionAtCenter)
                        return
        # Si no se encuentra el texto buscado, mostrar un mensaje
        QMessageBox.information(self, "Buscar", f"No se encontró '{text_to_search}'.")

    def editCell(self, row, col):
        # Obtener el valor actual de la celda
        current_value = self.table.item(row, col).text()

        # Crear un cuadro de diálogo para editar el valor de la celda
        new_value, ok = QtWidgets.QInputDialog.getText(self, "Editar valor", "Ingrese el nuevo valor:", text=current_value)

        # Actualizar el valor de la celda si se hace clic en "Aceptar" en el cuadro de diálogo
        if ok:
            self.table.setItem(row, col, QTableWidgetItem(new_value))
            self.save_data_to_csv()

    def save_data_to_csv(self):
        # Obtener los datos de la tabla
        data = []
        for i in range(self.table.rowCount()):
            row_data = []
            for j in range(self.table.columnCount()):
                item = self.table.item(i, j)
                row_data.append(item.text())
            data.append(row_data)

        # Guardar los datos en el archivo CSV
        with open('data/reserved_books.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

