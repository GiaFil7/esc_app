# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rankings_main_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_rankings_main_menu(object):
    def setupUi(self, rankings_main_menu):
        if not rankings_main_menu.objectName():
            rankings_main_menu.setObjectName(u"rankings_main_menu")
        rankings_main_menu.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(rankings_main_menu.sizePolicy().hasHeightForWidth())
        rankings_main_menu.setSizePolicy(sizePolicy)
        rankings_main_menu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout = QHBoxLayout(rankings_main_menu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_spacer = QSpacerItem(300, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.left_spacer)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.top_spacer = QSpacerItem(20, 68, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.top_spacer)

        self.esc_rankings_button = QPushButton(rankings_main_menu)
        self.esc_rankings_button.setObjectName(u"esc_rankings_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.esc_rankings_button.sizePolicy().hasHeightForWidth())
        self.esc_rankings_button.setSizePolicy(sizePolicy1)
        self.esc_rankings_button.setMinimumSize(QSize(300, 50))

        self.vertical_layout.addWidget(self.esc_rankings_button)

        self.middle_spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vertical_layout.addItem(self.middle_spacer)

        self.back_button = QPushButton(rankings_main_menu)
        self.back_button.setObjectName(u"back_button")
        sizePolicy1.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy1)
        self.back_button.setMinimumSize(QSize(300, 50))

        self.vertical_layout.addWidget(self.back_button)

        self.bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.bottom_spacer)


        self.horizontalLayout.addLayout(self.vertical_layout)

        self.right_spacer = QSpacerItem(300, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.right_spacer)


        self.retranslateUi(rankings_main_menu)

        QMetaObject.connectSlotsByName(rankings_main_menu)
    # setupUi

    def retranslateUi(self, rankings_main_menu):
        rankings_main_menu.setWindowTitle(QCoreApplication.translate("rankings_main_menu", u"Form", None))
        self.esc_rankings_button.setText(QCoreApplication.translate("rankings_main_menu", u"Eurovision Song Contest Rankings", None))
        self.back_button.setText(QCoreApplication.translate("rankings_main_menu", u"Back to Main Menu", None))
    # retranslateUi

