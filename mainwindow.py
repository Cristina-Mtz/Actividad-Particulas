from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
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

   