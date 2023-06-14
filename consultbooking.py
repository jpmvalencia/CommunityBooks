from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QDesktopWidget, QMessageBox, QVBoxLayout, QWidget
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtCore import Qt
import csv


class Consult_Booking(QMainWindow):
    def __init__(self, previous):
        super().__init__()
        
        # Icono de la ventana
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        # Guardar en una variable la ventana anterior
        self.previous_window = previous

        # Titulo de la ventana
        self.setWindowTitle("Consultar Préstamos | CommunityBooks")

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

        table.setMinimumSize(600, 500)
        table.setStyleSheet("QTableView {border: 1px solid #E4E7EB;}"
                            "QTableWidget {border-radius: 10px;}")

        # Creamos un objeto QWidget que contenga la tabla
        table_widget = QWidget()
        table_widget.setLayout(QVBoxLayout())
        table_widget.layout().addWidget(table, alignment=Qt.AlignCenter)

        # Establecer self.table_widget como el widget central de la ventana
        self.setCentralWidget(table_widget)

        # Leer los datos del archivo de texto
        file_path = "data/booking_data.txt"  # Ruta del archivo de texto
        booking_data = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split("\t")
                booking_data.append(data)

        # Ordenar los datos por fecha de entrega (columna 3)
        booking_data = sorted(booking_data, key=lambda x: x[3])

        # Verificar si hay datos en booking_data
        if booking_data:
            # Limpiar la tabla antes de agregar los datos ordenados
            self.table.clear()

            # Establecemos el número de filas y columnas en la tabla
            self.table.setRowCount(len(booking_data))
            self.table.setColumnCount(len(booking_data[0]))

            # Agregar los datos a la tabla
            for row in range(len(booking_data)):
                for col in range(len(booking_data[row])):
                    item = QTableWidgetItem(booking_data[row][col])
                    self.table.setItem(row, col, item)

        # Ocultamos las cabeceras de la tabla
        table.horizontalHeader().setVisible(True)
        
        # Ajustar el tamaño de las columnas y filas al contenido
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        # Establecer un ancho mínimo para cada columna
        for i in range(table.columnCount()):
            width = table.columnWidth(i)
            table.setColumnWidth(i, width + 30) # 30 es el espacio extra que queremos añadir
        
        table.cellDoubleClicked.connect(self.editCell)

        # Cambiar el texto de las cabeceras de la tabla
        headers = ['Documento', 'ID', 'Fecha de Reserva', 'Fecha de Entrega', 'Estado']
        table.setHorizontalHeaderLabels(headers)

        # Agregar un QPushButton para eliminar fila
        self.delete_button = QtWidgets.QPushButton("Eliminar fila", self)
        self.delete_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.delete_button.setFixedSize(150, 50)
        self.delete_button.clicked.connect(self.delete_row)

        # Agregar un QLineEdit y un QPushButton para buscar
        self.search_line_edit = QtWidgets.QLineEdit(self)
        self.search_line_edit.setFixedSize(700, 50)
        self.search_line_edit.setPlaceholderText("Buscar")
        self.search_line_edit.setStyleSheet("padding: 7px; border: none; background-color: #E4E7EB; "
                                            "border-radius: 10px;")
        self.search_line_edit.returnPressed.connect(self.search)
        self.search_button = QtWidgets.QPushButton("Buscar", self)
        self.search_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                         "QPushButton:pressed { background-color: #E4E7EB; }")
        self.search_button.setFixedSize(150, 50)
        self.search_button.clicked.connect(self.search)


        self.previous_button = QtWidgets.QPushButton("Atrás", self)
        self.previous_button.setStyleSheet("QPushButton { background-color: #F0F2F5; border-radius: 10px; }"
                                       "QPushButton:pressed { background-color: #E4E7EB; }")
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
        selected_row = self.table.currentRow()

        # Verificar si hay una fila seleccionada
        if selected_row >= 0:
            # Mostrar un cuadro de diálogo de confirmación
            confirm_dialog = QMessageBox.question(
                self, "Confirmar Eliminación",
                "¿Estás seguro de que deseas eliminar la fila seleccionada?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if confirm_dialog == QMessageBox.Yes:
                # Guardar el ID de la reserva a eliminar
                booking_id = self.table.item(selected_row, 1).text()

                # Eliminar la fila de la tabla
                self.table.removeRow(selected_row)

                # Guardar los datos actualizados en el archivo de texto
                file_path = "data/booking_data.txt"  # Ruta del archivo de texto
                lines = []  # Lista para almacenar las líneas excluyendo la de la reserva a eliminar
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
                    QMessageBox.information(self, "Eliminación Exitosa", "La fila ha sido eliminada exitosamente.")
                else:
                    # Mostrar un mensaje de error si no se encontró la reserva
                    QMessageBox.warning(self, "Error", "No se encontró la reserva en el archivo de datos.")
            else:
                # Mostrar un mensaje de cancelación
                QMessageBox.information(self, "Cancelado", "La eliminación de la fila ha sido cancelada.")
        else:
            # Mostrar un mensaje de error si no hay una fila seleccionada
            QMessageBox.warning(self, "Error", "No se ha seleccionado ninguna fila.")


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
        # Obtener el item de la celda seleccionada
        item = self.table.item(row, col)

        # Verificar si hay un item válido
        if item is not None:
            # Mostrar el cuadro de diálogo de edición
            text, ok = QtWidgets.QInputDialog.getText(
                self, "Editar Celda",
                "Ingrese el nuevo valor:",
                QtWidgets.QLineEdit.Normal,
                item.text()
            )

            # Verificar si se presionó el botón "Aceptar" en el cuadro de diálogo de edición
            if ok and text:
                # Validar que el nuevo valor tenga el formato correcto
                if col == 0 and not text.isnumeric():
                    QMessageBox.warning(self, "Error", "El número de documento debe ser numérico.")
                    return
                elif col == 1 and not text.isnumeric():
                    QMessageBox.warning(self, "Error", "El ID debe ser numérico.")
                    return

                # Mostrar un cuadro de diálogo de confirmación
                confirm_dialog = QMessageBox.question(
                    self, "Confirmar Cambio",
                    "¿Estás seguro de que deseas aplicar los cambios?",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
                )

                if confirm_dialog == QMessageBox.Yes:
                    # Actualizar los datos en la tabla
                    item.setText(text)

                    # Guardar los datos actualizados en el archivo de texto
                    file_path = "data/booking_data.txt"  # Ruta del archivo de texto
                    with open(file_path, "r", encoding="utf-8") as file:
                        lines = file.readlines()
                        lines[row] = lines[row].rstrip("\n")
                        columns = lines[row].split("\t")
                        if len(columns) > col:
                            columns[col] = text
                        lines[row] = "\t".join(columns) + "\n"

                    with open(file_path, "w", encoding="utf-8") as file:
                        file.writelines(lines)

                    # Mostrar un mensaje de éxito
                    QMessageBox.information(self, "Edición Exitosa", "El cambio ha sido aplicado exitosamente.")
                else:
                    # Mostrar un mensaje de cancelación
                    QMessageBox.information(self, "Cancelado", "La edición ha sido cancelada.")
