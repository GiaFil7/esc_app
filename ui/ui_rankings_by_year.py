# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rankings_by_year.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from rounded_scrollarea import rounded_scrollarea
import resources_rc

class Ui_rankings_by_year(object):
    def setupUi(self, rankings_by_year):
        if not rankings_by_year.objectName():
            rankings_by_year.setObjectName(u"rankings_by_year")
        rankings_by_year.resize(600, 400)
        self.verticalLayout = QVBoxLayout(rankings_by_year)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_layout = QHBoxLayout()
        self.title_layout.setObjectName(u"title_layout")
        self.logo_label = QLabel(rankings_by_year)
        self.logo_label.setObjectName(u"logo_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy)
        self.logo_label.setMaximumSize(QSize(95, 30))
        self.logo_label.setPixmap(QPixmap(u":/images/contest_logos/ESC/ESC.png"))
        self.logo_label.setScaledContents(True)

        self.title_layout.addWidget(self.logo_label)

        self.name_label = QLabel(rankings_by_year)
        self.name_label.setObjectName(u"name_label")

        self.title_layout.addWidget(self.name_label)

        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.title_layout.addItem(self.horizontal_spacer)

        self.back_button = QPushButton(rankings_by_year)
        self.back_button.setObjectName(u"back_button")
        icon = QIcon()
        icon.addFile(u":/images/icons/back_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_button.setIcon(icon)

        self.title_layout.addWidget(self.back_button)


        self.verticalLayout.addLayout(self.title_layout)

        self.scroll_area = rounded_scrollarea(rankings_by_year)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 582, 344))
        self.scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scroll_area)


        self.retranslateUi(rankings_by_year)

        QMetaObject.connectSlotsByName(rankings_by_year)
    # setupUi

    def retranslateUi(self, rankings_by_year):
        rankings_by_year.setWindowTitle(QCoreApplication.translate("rankings_by_year", u"Form", None))
        self.logo_label.setText("")
        self.name_label.setText(QCoreApplication.translate("rankings_by_year", u"Eurovision Song Contest", None))
        self.back_button.setText("")
    # retranslateUi

