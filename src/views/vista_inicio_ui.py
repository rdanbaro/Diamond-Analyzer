# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vista_inicio.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_VistaInicio(object):
    def setupUi(self, VistaInicio):
        if not VistaInicio.objectName():
            VistaInicio.setObjectName(u"VistaInicio")
        VistaInicio.resize(829, 476)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(64, 155, 191, 122))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(100, 165, 249, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(83, 137, 207, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(33, 55, 83, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(45, 73, 110, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        brush7 = QBrush(QColor(67, 110, 166, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush8 = QBrush(QColor(161, 182, 210, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        brush9 = QBrush(QColor(255, 255, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 128))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
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
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
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
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        VistaInicio.setPalette(palette)
        VistaInicio.setAutoFillBackground(True)
        VistaInicio.setStyleSheet(u"")
        self.centralwidget = QWidget(VistaInicio)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-image: url(:/prefijoNuevo/src/Captura desde 2024-04-06 18-51-22.png);")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setAutoFillBackground(True)
        self.widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.welcome = QLabel(self.widget)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setAutoFillBackground(False)
        self.welcome.setStyleSheet(u"background-color: rgb(153, 193, 241);\n"
"alternate-background-color: rgb(153, 193, 241);\n"
"color: rgb(153, 193, 241);")
        self.welcome.setFrameShape(QFrame.NoFrame)
        self.welcome.setScaledContents(False)
        self.welcome.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.welcome.setMargin(13)

        self.verticalLayout.addWidget(self.welcome)

        self.sprintAnalysisButton = QPushButton(self.widget)
        self.sprintAnalysisButton.setObjectName(u"sprintAnalysisButton")
        palette1 = QPalette()
        brush11 = QBrush(QColor(192, 28, 40, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        self.sprintAnalysisButton.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        self.sprintAnalysisButton.setFont(font)
        self.sprintAnalysisButton.setFocusPolicy(Qt.NoFocus)
        self.sprintAnalysisButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.sprintAnalysisButton.setAcceptDrops(False)
        self.sprintAnalysisButton.setAutoFillBackground(False)
        self.sprintAnalysisButton.setStyleSheet(u"background-color: rgb(192, 28, 40);")
        self.sprintAnalysisButton.setInputMethodHints(Qt.ImhNone)
        self.sprintAnalysisButton.setCheckable(False)
        self.sprintAnalysisButton.setAutoDefault(False)
        self.sprintAnalysisButton.setFlat(False)

        self.verticalLayout.addWidget(self.sprintAnalysisButton)

        self.statsButton = QPushButton(self.widget)
        self.statsButton.setObjectName(u"statsButton")
        self.statsButton.setFocusPolicy(Qt.StrongFocus)
        self.statsButton.setAutoFillBackground(False)
        self.statsButton.setStyleSheet(u"background-color: rgb(153, 193, 241);")

        self.verticalLayout.addWidget(self.statsButton)

        self.exitButton = QPushButton(self.widget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setStyleSheet(u"background-color: rgb(153, 193, 241);")

        self.verticalLayout.addWidget(self.exitButton)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        VistaInicio.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VistaInicio)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 829, 22))
        VistaInicio.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(VistaInicio)
        self.statusbar.setObjectName(u"statusbar")
        VistaInicio.setStatusBar(self.statusbar)

        self.retranslateUi(VistaInicio)

        self.sprintAnalysisButton.setDefault(False)


        QMetaObject.connectSlotsByName(VistaInicio)
    # setupUi

    def retranslateUi(self, VistaInicio):
        VistaInicio.setWindowTitle(QCoreApplication.translate("VistaInicio", u"MainWindow", None))
        self.welcome.setText(QCoreApplication.translate("VistaInicio", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0354;\">WELCOME</span></p></body></html>", None))
        self.sprintAnalysisButton.setText(QCoreApplication.translate("VistaInicio", u"An\u00e1lisis Sprint", None))
#if QT_CONFIG(accessibility)
        self.statsButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.statsButton.setText(QCoreApplication.translate("VistaInicio", u"Estad\u00edsticas", None))
        self.exitButton.setText(QCoreApplication.translate("VistaInicio", u"Salir", None))
    # retranslateUi

