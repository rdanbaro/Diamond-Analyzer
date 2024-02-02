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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QProgressBar, QSizePolicy, QSpacerItem, QWidget)

class Ui_Sprint_Review(object):
    def setupUi(self, Sprint_Review):
        if not Sprint_Review.objectName():
            Sprint_Review.setObjectName(u"Sprint_Review")
        Sprint_Review.resize(551, 472)
        self.label = QLabel(Sprint_Review)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 211, 51))
        self.label_2 = QLabel(Sprint_Review)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 70, 121, 17))
        self.label_3 = QLabel(Sprint_Review)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 60, 81, 31))
        self.label_4 = QLabel(Sprint_Review)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 120, 161, 17))
        self.label_5 = QLabel(Sprint_Review)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 120, 91, 17))
        self.label_8 = QLabel(Sprint_Review)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(230, 250, 67, 17))
        self.label_9 = QLabel(Sprint_Review)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(130, 290, 67, 17))
        self.progressBar_2 = QProgressBar(Sprint_Review)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(210, 290, 118, 23))
        self.progressBar_2.setValue(24)
        self.label_10 = QLabel(Sprint_Review)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(210, 380, 81, 17))
        self.widget = QWidget(Sprint_Review)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 160, 501, 27))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout.addWidget(self.progressBar)

        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)


        self.retranslateUi(Sprint_Review)

        QMetaObject.connectSlotsByName(Sprint_Review)
    # setupUi

    def retranslateUi(self, Sprint_Review):
        Sprint_Review.setWindowTitle(QCoreApplication.translate("Sprint_Review", u"Form", None))
        self.label.setText(QCoreApplication.translate("Sprint_Review", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Sprint Review</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Sprint_Review", u"Sprint Standard 1", None))
        self.label_3.setText(QCoreApplication.translate("Sprint_Review", u"Tipo:", None))
        self.label_4.setText(QCoreApplication.translate("Sprint_Review", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Metas &amp; Objetivos:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Sprint_Review", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Requisito</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Sprint_Review", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Sprint_Review", u"cumplido", None))
        self.label_10.setText(QCoreApplication.translate("Sprint_Review", u"Felicidades", None))
        self.label_6.setText(QCoreApplication.translate("Sprint_Review", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Sprint_Review", u"7", None))
        self.checkBox.setText("")
    # retranslateUi

