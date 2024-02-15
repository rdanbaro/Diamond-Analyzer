# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista_habitos.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_VistaHabitos(object):
    def setupUi(self, VistaHabitos):
        if not VistaHabitos.objectName():
            VistaHabitos.setObjectName(u"VistaHabitos")
        VistaHabitos.resize(504, 300)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(168, 218, 220, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(211, 236, 237, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(84, 109, 110, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(112, 145, 147, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        VistaHabitos.setPalette(palette)
        VistaHabitos.setStyleSheet(u"background-color: rgb(168, 218, 220);")
        self.gridLayout = QGridLayout(VistaHabitos)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 6, 0, 0)
        self.Layout_stats = QVBoxLayout()
        self.Layout_stats.setObjectName(u"Layout_stats")
        self.label = QLabel(VistaHabitos)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(168, 218, 220);\n"
"gridline-color: rgb(168, 218, 220);\n"
"border-color: rgb(168, 218, 220);")

        self.Layout_stats.addWidget(self.label)


        self.gridLayout.addLayout(self.Layout_stats, 0, 0, 1, 1)

        self.Layout_graf1 = QVBoxLayout()
        self.Layout_graf1.setObjectName(u"Layout_graf1")

        self.gridLayout.addLayout(self.Layout_graf1, 2, 0, 1, 1)

        self.Layout_graf2 = QVBoxLayout()
        self.Layout_graf2.setObjectName(u"Layout_graf2")

        self.gridLayout.addLayout(self.Layout_graf2, 2, 1, 1, 1)

        self.horizontalLayout_graf3 = QHBoxLayout()
        self.horizontalLayout_graf3.setSpacing(0)
        self.horizontalLayout_graf3.setObjectName(u"horizontalLayout_graf3")
        self.Layout_graf3_1 = QVBoxLayout()
        self.Layout_graf3_1.setSpacing(0)
        self.Layout_graf3_1.setObjectName(u"Layout_graf3_1")

        self.horizontalLayout_graf3.addLayout(self.Layout_graf3_1)

        self.Layout_graf3_2 = QVBoxLayout()
        self.Layout_graf3_2.setSpacing(0)
        self.Layout_graf3_2.setObjectName(u"Layout_graf3_2")

        self.horizontalLayout_graf3.addLayout(self.Layout_graf3_2)


        self.gridLayout.addLayout(self.horizontalLayout_graf3, 0, 1, 1, 1)


        self.retranslateUi(VistaHabitos)

        QMetaObject.connectSlotsByName(VistaHabitos)
    # setupUi

    def retranslateUi(self, VistaHabitos):
        VistaHabitos.setWindowTitle(QCoreApplication.translate("VistaHabitos", u"Form", None))
        self.label.setText(QCoreApplication.translate("VistaHabitos", u"Estadisticas:", None))
    # retranslateUi

