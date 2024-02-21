# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista_review.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Sprint_Review(object):
    def setupUi(self, Sprint_Review):
        if not Sprint_Review.objectName():
            Sprint_Review.setObjectName(u"Sprint_Review")
        Sprint_Review.resize(404, 335)
        self.verticalLayout = QVBoxLayout(Sprint_Review)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Sprint_Review)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_nombre_sprint = QLabel(Sprint_Review)
        self.label_nombre_sprint.setObjectName(u"label_nombre_sprint")

        self.horizontalLayout_3.addWidget(self.label_nombre_sprint)

        self.horizontalSpacer_3 = QSpacerItem(150, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Sprint_Review)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_tipo_sprint = QLabel(Sprint_Review)
        self.label_tipo_sprint.setObjectName(u"label_tipo_sprint")

        self.horizontalLayout_2.addWidget(self.label_tipo_sprint)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 30)
        self.Layout_titulo_metas = QVBoxLayout()
        self.Layout_titulo_metas.setObjectName(u"Layout_titulo_metas")
        self.label_4 = QLabel(Sprint_Review)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.Layout_titulo_metas.addWidget(self.label_4)

        self.Layout_metas = QVBoxLayout()
        self.Layout_metas.setObjectName(u"Layout_metas")

        self.Layout_titulo_metas.addLayout(self.Layout_metas)


        self.horizontalLayout.addLayout(self.Layout_titulo_metas)

        self.Layout_titulo_requisitos = QVBoxLayout()
        self.Layout_titulo_requisitos.setObjectName(u"Layout_titulo_requisitos")
        self.Layout_titulo_requisitos.setContentsMargins(-1, 0, -1, -1)
        self.label_5 = QLabel(Sprint_Review)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.Layout_titulo_requisitos.addWidget(self.label_5)

        self.Layout_requisitos = QVBoxLayout()
        self.Layout_requisitos.setObjectName(u"Layout_requisitos")

        self.Layout_titulo_requisitos.addLayout(self.Layout_requisitos)


        self.horizontalLayout.addLayout(self.Layout_titulo_requisitos)

        self.Layout_titulo_cumplidos = QVBoxLayout()
        self.Layout_titulo_cumplidos.setObjectName(u"Layout_titulo_cumplidos")
        self.Layout_titulo_cumplidos.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Layout_titulo_cumplidos.setContentsMargins(0, -1, -1, -1)
        self.label_9 = QLabel(Sprint_Review)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)

        self.Layout_titulo_cumplidos.addWidget(self.label_9)

        self.Layout_cumplidos = QVBoxLayout()
        self.Layout_cumplidos.setObjectName(u"Layout_cumplidos")

        self.Layout_titulo_cumplidos.addLayout(self.Layout_cumplidos)


        self.horizontalLayout.addLayout(self.Layout_titulo_cumplidos)

        self.Layout_titulo_checks = QVBoxLayout()
        self.Layout_titulo_checks.setObjectName(u"Layout_titulo_checks")
        self.Layout_titulo_checks.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Layout_titulo_checks.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(Sprint_Review)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.Layout_titulo_checks.addWidget(self.label_2)

        self.Layout_checks = QVBoxLayout()
        self.Layout_checks.setSpacing(7)
        self.Layout_checks.setObjectName(u"Layout_checks")
        self.Layout_checks.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Layout_checks.setContentsMargins(-1, 0, -1, -1)

        self.Layout_titulo_checks.addLayout(self.Layout_checks)


        self.horizontalLayout.addLayout(self.Layout_titulo_checks)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.label_6 = QLabel(Sprint_Review)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.progreso_general = QProgressBar(Sprint_Review)
        self.progreso_general.setObjectName(u"progreso_general")
        self.progreso_general.setStyleSheet(u"selection-background-color: rgb(143, 240, 164);")
        self.progreso_general.setValue(24)

        self.horizontalLayout_4.addWidget(self.progreso_general)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_mensaje = QLabel(Sprint_Review)
        self.label_mensaje.setObjectName(u"label_mensaje")

        self.verticalLayout.addWidget(self.label_mensaje)

        self.Boton_Siguiente = QPushButton(Sprint_Review)
        self.Boton_Siguiente.setObjectName(u"Boton_Siguiente")

        self.verticalLayout.addWidget(self.Boton_Siguiente, 0, Qt.AlignRight)


        self.retranslateUi(Sprint_Review)

        QMetaObject.connectSlotsByName(Sprint_Review)
    # setupUi

    def retranslateUi(self, Sprint_Review):
        Sprint_Review.setWindowTitle(QCoreApplication.translate("Sprint_Review", u"Form", None))
        self.label.setText(QCoreApplication.translate("Sprint_Review", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Sprint Review</span></p></body></html>", None))
        self.label_nombre_sprint.setText(QCoreApplication.translate("Sprint_Review", u"Sprint Standard 1", None))
        self.label_3.setText(QCoreApplication.translate("Sprint_Review", u"Tipo:", None))
        self.label_tipo_sprint.setText(QCoreApplication.translate("Sprint_Review", u"t_valor", None))
        self.label_4.setText(QCoreApplication.translate("Sprint_Review", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Metas &amp; Objetivos:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Sprint_Review", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Requisito</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Sprint_Review", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Cumplido</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Sprint_Review", u"<html><head/><body><p><span style=\" font-size:12pt;\"/><br/></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Sprint_Review", u"General", None))
        self.label_mensaje.setText(QCoreApplication.translate("Sprint_Review", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#813d9c;\">hola</span></p></body></html>", None))
        self.Boton_Siguiente.setText(QCoreApplication.translate("Sprint_Review", u"Siguiente", None))
    # retranslateUi

