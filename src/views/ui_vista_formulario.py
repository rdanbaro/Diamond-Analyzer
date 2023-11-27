# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista_formulario.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(441, 416)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_nombre_sprint = QLabel(Form)
        self.label_nombre_sprint.setObjectName(u"label_nombre_sprint")

        self.horizontalLayout_2.addWidget(self.label_nombre_sprint)

        self.entry_nombre_sprint = QLineEdit(Form)
        self.entry_nombre_sprint.setObjectName(u"entry_nombre_sprint")

        self.horizontalLayout_2.addWidget(self.entry_nombre_sprint)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_seleccione = QLabel(Form)
        self.label_seleccione.setObjectName(u"label_seleccione")

        self.verticalLayout_4.addWidget(self.label_seleccione)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_intenso = QRadioButton(Form)
        self.radioButton_intenso.setObjectName(u"radioButton_intenso")

        self.horizontalLayout.addWidget(self.radioButton_intenso)

        self.radioButton_standard = QRadioButton(Form)
        self.radioButton_standard.setObjectName(u"radioButton_standard")

        self.horizontalLayout.addWidget(self.radioButton_standard)

        self.radioButton_largo = QRadioButton(Form)
        self.radioButton_largo.setObjectName(u"radioButton_largo")

        self.horizontalLayout.addWidget(self.radioButton_largo)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_ingrese_ruta = QLabel(Form)
        self.label_ingrese_ruta.setObjectName(u"label_ingrese_ruta")

        self.verticalLayout_3.addWidget(self.label_ingrese_ruta)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_2.addWidget(self.lineEdit_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.boton_cancelar = QPushButton(Form)
        self.boton_cancelar.setObjectName(u"boton_cancelar")

        self.horizontalLayout_4.addWidget(self.boton_cancelar)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_nombre_sprint.setText(QCoreApplication.translate("Form", u"Nombre del Sprint", None))
        self.label_seleccione.setText(QCoreApplication.translate("Form", u"Seleccione el tipo de Sprint:", None))
        self.radioButton_intenso.setText(QCoreApplication.translate("Form", u"Intenso", None))
        self.radioButton_standard.setText(QCoreApplication.translate("Form", u"Standard", None))
        self.radioButton_largo.setText(QCoreApplication.translate("Form", u"Largo", None))
        self.label_ingrese_ruta.setText(QCoreApplication.translate("Form", u"Ingrese la ruta de los datasets:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Metas & objetivos", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"H\u00e1bitos", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Diamantes", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Entrenamiento", None))
        self.boton_cancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Aceptar", None))
    # retranslateUi

