# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ranking_menu_item.ui'
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
    QSizePolicy, QSpacerItem, QWidget)
import resources_rc

class Ui_ranking_menu_item(object):
    def setupUi(self, ranking_menu_item):
        if not ranking_menu_item.objectName():
            ranking_menu_item.setObjectName(u"ranking_menu_item")
        ranking_menu_item.resize(579, 58)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ranking_menu_item.sizePolicy().hasHeightForWidth())
        ranking_menu_item.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(ranking_menu_item)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.main_layout = QHBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.logo_label = QLabel(ranking_menu_item)
        self.logo_label.setObjectName(u"logo_label")
        sizePolicy.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy)
        self.logo_label.setMinimumSize(QSize(0, 0))
        self.logo_label.setMaximumSize(QSize(40, 40))
        self.logo_label.setBaseSize(QSize(40, 40))
        self.logo_label.setStyleSheet(u"border: 1px solid black")
        self.logo_label.setFrameShadow(QFrame.Shadow.Plain)
        self.logo_label.setPixmap(QPixmap(u":/images/heart_logos/empty_heart.svg"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.main_layout.addWidget(self.logo_label)

        self.contest_name_label = QLabel(ranking_menu_item)
        self.contest_name_label.setObjectName(u"contest_name_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.contest_name_label.sizePolicy().hasHeightForWidth())
        self.contest_name_label.setSizePolicy(sizePolicy1)
        self.contest_name_label.setMinimumSize(QSize(0, 0))
        self.contest_name_label.setMaximumSize(QSize(400, 16777215))
        self.contest_name_label.setStyleSheet(u"border: 1px solid black")

        self.main_layout.addWidget(self.contest_name_label)

        self.name_submitted_spacer = QSpacerItem(75, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.main_layout.addItem(self.name_submitted_spacer)

        self.submitted_label = QLabel(ranking_menu_item)
        self.submitted_label.setObjectName(u"submitted_label")
        sizePolicy.setHeightForWidth(self.submitted_label.sizePolicy().hasHeightForWidth())
        self.submitted_label.setSizePolicy(sizePolicy)
        self.submitted_label.setMaximumSize(QSize(20, 20))
        self.submitted_label.setStyleSheet(u"border: 1px solid black")
        self.submitted_label.setPixmap(QPixmap(u":/images/close_icon.png"))
        self.submitted_label.setScaledContents(True)

        self.main_layout.addWidget(self.submitted_label)


        self.horizontalLayout_2.addLayout(self.main_layout)

        self.right_spacer = QSpacerItem(300, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.right_spacer)


        self.retranslateUi(ranking_menu_item)

        QMetaObject.connectSlotsByName(ranking_menu_item)
    # setupUi

    def retranslateUi(self, ranking_menu_item):
        ranking_menu_item.setWindowTitle(QCoreApplication.translate("ranking_menu_item", u"Form", None))
        self.logo_label.setText("")
        self.contest_name_label.setText(QCoreApplication.translate("ranking_menu_item", u"text text text text text", None))
        self.submitted_label.setText("")
    # retranslateUi

