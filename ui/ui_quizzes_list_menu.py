# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quizzes_list_menu.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_quizzes_list_menu(object):
    def setupUi(self, quizzes_list_menu):
        if not quizzes_list_menu.objectName():
            quizzes_list_menu.setObjectName(u"quizzes_list_menu")
        quizzes_list_menu.resize(600, 400)
        self.verticalLayout = QVBoxLayout(quizzes_list_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_layout = QHBoxLayout()
        self.title_layout.setObjectName(u"title_layout")
        self.logo_label = QLabel(quizzes_list_menu)
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

        self.name_label = QLabel(quizzes_list_menu)
        self.name_label.setObjectName(u"name_label")

        self.title_layout.addWidget(self.name_label)

        self.horizontal_spacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.title_layout.addItem(self.horizontal_spacer_1)

        self.totals_label = QLabel(quizzes_list_menu)
        self.totals_label.setObjectName(u"totals_label")

        self.title_layout.addWidget(self.totals_label)

        self.horizontal_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.title_layout.addItem(self.horizontal_spacer_2)

        self.back_button = QPushButton(quizzes_list_menu)
        self.back_button.setObjectName(u"back_button")
        icon = QIcon()
        icon.addFile(u":/images/icons/back_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_button.setIcon(icon)

        self.title_layout.addWidget(self.back_button)


        self.verticalLayout.addLayout(self.title_layout)

        self.scroll_area = QScrollArea(quizzes_list_menu)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 582, 344))
        self.scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scroll_area)


        self.retranslateUi(quizzes_list_menu)

        QMetaObject.connectSlotsByName(quizzes_list_menu)
    # setupUi

    def retranslateUi(self, quizzes_list_menu):
        quizzes_list_menu.setWindowTitle(QCoreApplication.translate("quizzes_list_menu", u"Form", None))
        self.logo_label.setText("")
        self.name_label.setText(QCoreApplication.translate("quizzes_list_menu", u"Contest Name - Menu Type", None))
        self.totals_label.setText(QCoreApplication.translate("quizzes_list_menu", u"Total score: ####/1700 (XX%) | Total time: XX:XX:XX", None))
        self.back_button.setText("")
    # retranslateUi

