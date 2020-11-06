from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particula import Particula
from administracion import Administracion

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.administracion = Administracion()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregarfinal_pushButton.clicked.connect(self.click_agregarfinal)
        self.ui.agregarinicio_pushButton.clicked.connect(self.click_agregarinicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardad.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton_2.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar)
    
    @Slot()
    def mostrar_tabla(self):
        self.ui.table.setColumnCount(10)
        headers = ["Id", "Origen_x", "Origen_y", "Destino_x", "Destino_y", "Velocidad", "Distancia", "Red", "Green", "Blue"]
        self.ui.table.setHorizontalHeaderLabels(headers)
        self.ui.table.setRowCount(len(self.administracion))
        row = 0
        for particula in self.administracion:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            distancia_widget = QTableWidgetItem (str(particula.distancia))           
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))

            self.ui.table.setItem(row, 0, id_widget)
            self.ui.table.setItem(row, 1, origen_x_widget)
            self.ui.table.setItem(row, 2, origen_y_widget)
            self.ui.table.setItem(row, 3, destino_x_widget)
            self.ui.table.setItem(row, 4, destino_y_widget)
            self.ui.table.setItem(row, 5, velocidad_widget)
            self.ui.table.setItem(row, 6, distancia_widget)
            self.ui.table.setItem(row, 7, red_widget)
            self.ui.table.setItem(row, 8, green_widget)
            self.ui.table.setItem(row, 9, blue_widget) 
            row += 1


    @Slot()
    def buscar(self):
        id = self.ui.search_lineEdit.text()
        encontrado = False
        for particula in self.administracion:
            if id == particula.id:
                self.ui.table.clear()
                self.ui.table.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                distancia_widget = QTableWidgetItem (str(particula.distancia))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))

                self.ui.table.setItem(0, 0, id_widget)
                self.ui.table.setItem(0, 1, origen_x_widget)
                self.ui.table.setItem(0, 2, origen_y_widget)
                self.ui.table.setItem(0, 3, destino_x_widget)
                self.ui.table.setItem(0, 4, destino_y_widget)
                self.ui.table.setItem(0, 5, velocidad_widget)
                self.ui.table.setItem(0, 6, distancia_widget)
                self.ui.table.setItem(0, 7, red_widget)
                self.ui.table.setItem(0, 8, green_widget)
                self.ui.table.setItem(0, 9, blue_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'La partícula "{id}" no fue encontrada'
            )



    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            '.',
            'JSON (*.json)' 
        )[0]
        if self.administracion.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo" + ubicacion
            )


    @Slot()
    def action_guardar_archivo(self):
       ubicacion =  QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
       print(ubicacion)
       if self.administracion.guardar(ubicacion):
           QMessageBox.information(
               self,
               "Éxito",
               "Se creó exitosamente el archivo" + ubicacion
           )  
       else:
            QMessageBox.critical(
                self,
                "Error",
                "Falla al crear el archivo" + ubicacion
            )

    @Slot() 
    def click_mostrar(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.administracion))


    @Slot()
    def click_agregarfinal(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origenx_spinBox.value()
        origen_y = self.ui.origeny_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.administracion.agregar_final(particula)
 
      
    @Slot()
    def click_agregarinicio(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origenx_spinBox.value()
        origen_y = self.ui.origeny_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.administracion.agregar_inicio(particula)
        

   