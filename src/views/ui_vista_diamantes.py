# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista_diamantes.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_VistaDiamantes(object):
    def setupUi(self, VistaDiamantes):
        if not VistaDiamantes.objectName():
            VistaDiamantes.setObjectName(u"VistaDiamantes")
        VistaDiamantes.resize(512, 300)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(141, 153, 174, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(213, 228, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(177, 190, 214, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(71, 77, 87, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(94, 102, 116, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(198, 204, 214, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        VistaDiamantes.setPalette(palette)
        VistaDiamantes.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(VistaDiamantes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Layout_stats = QVBoxLayout()
        self.Layout_stats.setObjectName(u"Layout_stats")
        self.label = QLabel(VistaDiamantes)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(141, 153, 174);\n"
"border-color: rgb(141, 153, 174);\n"
"gridline-color: rgb(141, 153, 174);")

        self.Layout_stats.addWidget(self.label)


        self.gridLayout.addLayout(self.Layout_stats, 0, 0, 1, 1)

        self.Layout_graf1_Act = QVBoxLayout()
        self.Layout_graf1_Act.setObjectName(u"Layout_graf1_Act")

        self.gridLayout.addLayout(self.Layout_graf1_Act, 0, 1, 1, 2)

        self.Layout_graf2_CatBar = QVBoxLayout()
        self.Layout_graf2_CatBar.setObjectName(u"Layout_graf2_CatBar")

        self.gridLayout.addLayout(self.Layout_graf2_CatBar, 1, 0, 1, 1)

        self.Layout_graf3_CatPie = QVBoxLayout()
        self.Layout_graf3_CatPie.setObjectName(u"Layout_graf3_CatPie")

        self.gridLayout.addLayout(self.Layout_graf3_CatPie, 1, 1, 1, 1)

        self.Layout_graf4_CatPlot = QVBoxLayout()
        self.Layout_graf4_CatPlot.setObjectName(u"Layout_graf4_CatPlot")

        self.gridLayout.addLayout(self.Layout_graf4_CatPlot, 1, 2, 1, 1)


        self.retranslateUi(VistaDiamantes)

        QMetaObject.connectSlotsByName(VistaDiamantes)
    # setupUi

    def retranslateUi(self, VistaDiamantes):
        VistaDiamantes.setWindowTitle(QCoreApplication.translate("VistaDiamantes", u"Form", None))
        self.label.setText(QCoreApplication.translate("VistaDiamantes", u"Estadisticas:", None))
    # retranslateUi

