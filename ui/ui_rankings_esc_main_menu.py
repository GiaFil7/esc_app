# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rankings_esc_main_menu.ui'
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

class Ui_rankings_esc_main_menu(object):
    def setupUi(self, rankings_esc_main_menu):
        if not rankings_esc_main_menu.objectName():
            rankings_esc_main_menu.setObjectName(u"rankings_esc_main_menu")
        rankings_esc_main_menu.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(rankings_esc_main_menu.sizePolicy().hasHeightForWidth())
        rankings_esc_main_menu.setSizePolicy(sizePolicy)
        rankings_esc_main_menu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout = QHBoxLayout(rankings_esc_main_menu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_spacer = QSpacerItem(300, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.left_spacer)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.top_spacer = QSpacerItem(20, 68, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.top_spacer)

        self.rankings_button = QPushButton(rankings_esc_main_menu)
        self.rankings_button.setObjectName(u"rankings_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rankings_button.sizePolicy().hasHeightForWidth())
        self.rankings_button.setSizePolicy(sizePolicy1)
        self.rankings_button.setMinimumSize(QSize(300, 50))

        self.vertical_layout.addWidget(self.rankings_button)

        self.middle_spacer_1 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vertical_layout.addItem(self.middle_spacer_1)

        self.statistics_button = QPushButton(rankings_esc_main_menu)
        self.statistics_button.setObjectName(u"statistics_button")
        sizePolicy1.setHeightForWidth(self.statistics_button.sizePolicy().hasHeightForWidth())
        self.statistics_button.setSizePolicy(sizePolicy1)
        self.statistics_button.setMinimumSize(QSize(300, 50))

        self.vertical_layout.addWidget(self.statistics_button)

        self.middle_spacer_2 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vertical_layout.addItem(self.middle_spacer_2)

        self.back_button = QPushButton(rankings_esc_main_menu)
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


        self.retranslateUi(rankings_esc_main_menu)

        QMetaObject.connectSlotsByName(rankings_esc_main_menu)
    # setupUi

    def retranslateUi(self, rankings_esc_main_menu):
        rankings_esc_main_menu.setWindowTitle(QCoreApplication.translate("rankings_esc_main_menu", u"Form", None))
        self.rankings_button.setText(QCoreApplication.translate("rankings_esc_main_menu", u"Eurovision Song Contest - Rankings by Year", None))
        self.statistics_button.setText(QCoreApplication.translate("rankings_esc_main_menu", u"Statistics", None))
        self.back_button.setText(QCoreApplication.translate("rankings_esc_main_menu", u"Back to Rankings Main Menu", None))
    # retranslateUi

