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
        MainWindow.resize(671, 536)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardad = QAction(MainWindow)
        self.actionGuardad.setObjectName(u"actionGuardad")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.dibujo_tabWidget = QTabWidget(self.centralwidget)
        self.dibujo_tabWidget.setObjectName(u"dibujo_tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.id_lineEdit = QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout.addWidget(self.id_lineEdit, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.origenx_spinBox = QSpinBox(self.groupBox)
        self.origenx_spinBox.setObjectName(u"origenx_spinBox")
        self.origenx_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenx_spinBox, 1, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)

        self.origeny_spinBox = QSpinBox(self.groupBox)
        self.origeny_spinBox.setObjectName(u"origeny_spinBox")
        self.origeny_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origeny_spinBox, 2, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)

        self.destinox_spinBox = QSpinBox(self.groupBox)
        self.destinox_spinBox.setObjectName(u"destinox_spinBox")
        self.destinox_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinox_spinBox, 3, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 2)

        self.destinoy_spinBox = QSpinBox(self.groupBox)
        self.destinoy_spinBox.setObjectName(u"destinoy_spinBox")
        self.destinoy_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoy_spinBox, 4, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 2)

        self.velocidad_lineEdit = QLineEdit(self.groupBox)
        self.velocidad_lineEdit.setObjectName(u"velocidad_lineEdit")

        self.gridLayout.addWidget(self.velocidad_lineEdit, 5, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 2)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 1, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.red_spinBox, 7, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 8, 1, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.green_spinBox, 8, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 1, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.blue_spinBox, 9, 2, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 10, 0, 1, 3)

        self.agregarinicio_pushButton = QPushButton(self.groupBox)
        self.agregarinicio_pushButton.setObjectName(u"agregarinicio_pushButton")

        self.gridLayout.addWidget(self.agregarinicio_pushButton, 11, 0, 1, 3)

        self.agregarfinal_pushButton = QPushButton(self.groupBox)
        self.agregarfinal_pushButton.setObjectName(u"agregarfinal_pushButton")

        self.gridLayout.addWidget(self.agregarfinal_pushButton, 12, 0, 1, 3)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.dibujo_tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.search_lineEdit = QLineEdit(self.tab_2)
        self.search_lineEdit.setObjectName(u"search_lineEdit")

        self.gridLayout_3.addWidget(self.search_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_3.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton_2 = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton_2.setObjectName(u"mostrar_tabla_pushButton_2")

        self.gridLayout_3.addWidget(self.mostrar_tabla_pushButton_2, 1, 2, 1, 1)

        self.table = QTableWidget(self.tab_2)
        self.table.setObjectName(u"table")

        self.gridLayout_3.addWidget(self.table, 0, 0, 1, 3)

        self.dibujo_tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar_pushButton = QPushButton(self.tab_3)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout_4.addWidget(self.dibujar_pushButton, 1, 0, 1, 1)

        self.limpiar_pushButton_2 = QPushButton(self.tab_3)
        self.limpiar_pushButton_2.setObjectName(u"limpiar_pushButton_2")

        self.gridLayout_4.addWidget(self.limpiar_pushButton_2, 1, 1, 1, 1)

        self.dibujo_tabWidget.addTab(self.tab_3, "")

        self.gridLayout_5.addWidget(self.dibujo_tabWidget, 0, 0, 1, 3)

        self.distancia_pushButton_2 = QPushButton(self.centralwidget)
        self.distancia_pushButton_2.setObjectName(u"distancia_pushButton_2")

        self.gridLayout_5.addWidget(self.distancia_pushButton_2, 1, 1, 1, 1)

        self.velocidad_pushButton_3 = QPushButton(self.centralwidget)
        self.velocidad_pushButton_3.setObjectName(u"velocidad_pushButton_3")

        self.gridLayout_5.addWidget(self.velocidad_pushButton_3, 1, 2, 1, 1)

        self.id_pushButton = QPushButton(self.centralwidget)
        self.id_pushButton.setObjectName(u"id_pushButton")

        self.gridLayout_5.addWidget(self.id_pushButton, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 671, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardad)

        self.retranslateUi(MainWindow)

        self.dibujo_tabWidget.setCurrentIndex(0)


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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Captura de part\u00edculas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen_X", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen_Y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino_X", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Destino_Y", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Colores", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.agregarinicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.agregarfinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.dibujo_tabWidget.setTabText(self.dibujo_tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID de part\u00edcula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.dibujo_tabWidget.setTabText(self.dibujo_tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujo_tabWidget.setTabText(self.dibujo_tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"P\u00e1gina", None))
        self.distancia_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ordenar DISTANCIA (M a m)", None))
        self.velocidad_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Ordenar VELOCIDAD (m a M)", None))
        self.id_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar ID(m a M)", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

