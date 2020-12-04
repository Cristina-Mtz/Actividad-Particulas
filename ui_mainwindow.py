# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(535, 619)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardad = QAction(MainWindow)
        self.actionGuardad.setObjectName(u"actionGuardad")
        self.actionGrafo = QAction(MainWindow)
        self.actionGrafo.setObjectName(u"actionGrafo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.id_lineEdit = QLineEdit(self.groupBox_2)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout.addWidget(self.id_lineEdit, 0, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_7 = QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 0, 2, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox_4)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout_7.addWidget(self.red_spinBox, 0, 1, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox_4)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout_7.addWidget(self.green_spinBox, 0, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 0, 4, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox_4)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout_7.addWidget(self.blue_spinBox, 0, 5, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 4, 0, 1, 3)

        self.velocidad_lineEdit = QLineEdit(self.groupBox_2)
        self.velocidad_lineEdit.setObjectName(u"velocidad_lineEdit")

        self.gridLayout.addWidget(self.velocidad_lineEdit, 5, 2, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 2)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_8 = QGridLayout(self.groupBox_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.velocidad_pushButton_3 = QPushButton(self.groupBox_5)
        self.velocidad_pushButton_3.setObjectName(u"velocidad_pushButton_3")

        self.gridLayout_8.addWidget(self.velocidad_pushButton_3, 4, 0, 1, 1)

        self.id_pushButton = QPushButton(self.groupBox_5)
        self.id_pushButton.setObjectName(u"id_pushButton")

        self.gridLayout_8.addWidget(self.id_pushButton, 5, 0, 1, 1)

        self.agregarinicio_pushButton = QPushButton(self.groupBox_5)
        self.agregarinicio_pushButton.setObjectName(u"agregarinicio_pushButton")

        self.gridLayout_8.addWidget(self.agregarinicio_pushButton, 2, 0, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox_5)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout_8.addWidget(self.mostrar_pushButton, 1, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.groupBox_5)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_8.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.agregarfinal_pushButton = QPushButton(self.groupBox_5)
        self.agregarfinal_pushButton.setObjectName(u"agregarfinal_pushButton")

        self.gridLayout_8.addWidget(self.agregarfinal_pushButton, 3, 0, 1, 1)

        self.distancia_pushButton_2 = QPushButton(self.groupBox_5)
        self.distancia_pushButton_2.setObjectName(u"distancia_pushButton_2")

        self.gridLayout_8.addWidget(self.distancia_pushButton_2, 6, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_5, 6, 0, 1, 3)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.origenx_spinBox = QSpinBox(self.groupBox_3)
        self.origenx_spinBox.setObjectName(u"origenx_spinBox")
        self.origenx_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.origenx_spinBox, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)

        self.origeny_spinBox = QSpinBox(self.groupBox_3)
        self.origeny_spinBox.setObjectName(u"origeny_spinBox")
        self.origeny_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.origeny_spinBox, 0, 3, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 3)

        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.destinox_spinBox = QSpinBox(self.groupBox_6)
        self.destinox_spinBox.setObjectName(u"destinox_spinBox")
        self.destinox_spinBox.setMaximum(500)

        self.gridLayout_6.addWidget(self.destinox_spinBox, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 0, 2, 1, 1)

        self.destinoy_spinBox = QSpinBox(self.groupBox_6)
        self.destinoy_spinBox.setObjectName(u"destinoy_spinBox")
        self.destinoy_spinBox.setMaximum(500)

        self.gridLayout_6.addWidget(self.destinoy_spinBox, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.groupBox_6, 3, 0, 1, 3)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_9 = QGridLayout(self.tab_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.graphicsView = QGraphicsView(self.tab_4)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_9.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.limpiar_pushButton_2 = QPushButton(self.tab_4)
        self.limpiar_pushButton_2.setObjectName(u"limpiar_pushButton_2")

        self.gridLayout_9.addWidget(self.limpiar_pushButton_2, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_4 = QGridLayout(self.tab_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.table = QTableWidget(self.tab_5)
        self.table.setObjectName(u"table")

        self.gridLayout_4.addWidget(self.table, 0, 0, 1, 3)

        self.search_lineEdit = QLineEdit(self.tab_5)
        self.search_lineEdit.setObjectName(u"search_lineEdit")

        self.gridLayout_4.addWidget(self.search_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_5)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton_2 = QPushButton(self.tab_5)
        self.mostrar_tabla_pushButton_2.setObjectName(u"mostrar_tabla_pushButton_2")

        self.gridLayout_4.addWidget(self.mostrar_tabla_pushButton_2, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 535, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardad)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardad.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardad.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionGrafo.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Captura de part\u00edculas", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Colores", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"G:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"B:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Salida", None))
        self.velocidad_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Ordenar VELOCIDAD (m a M)", None))
        self.id_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar ID(m a M)", None))
        self.agregarinicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.agregarfinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.distancia_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ordenar DISTANCIA (M a m)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.limpiar_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Visualizador", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID de part\u00edcula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuVer.setTitle("")
    # retranslateUi

