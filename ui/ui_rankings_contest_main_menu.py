# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rankings_contest_main_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_rankings_contest_main_menu(object):
    def setupUi(self, rankings_contest_main_menu):
        if not rankings_contest_main_menu.objectName():
            rankings_contest_main_menu.setObjectName(u"rankings_contest_main_menu")
        rankings_contest_main_menu.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(rankings_contest_main_menu.sizePolicy().hasHeightForWidth())
        rankings_contest_main_menu.setSizePolicy(sizePolicy)
        rankings_contest_main_menu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.layout = QHBoxLayout(rankings_contest_main_menu)
        self.layout.setObjectName(u"layout")
        self.left_spacer = QSpacerItem(100, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.layout.addItem(self.left_spacer)

        self.main_vertical_layout = QVBoxLayout()
        self.main_vertical_layout.setObjectName(u"main_vertical_layout")
        self.top_spacer = QSpacerItem(20, 68, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.main_vertical_layout.addItem(self.top_spacer)

        self.menu_title_label = QLabel(rankings_contest_main_menu)
        self.menu_title_label.setObjectName(u"menu_title_label")
        sizePolicy.setHeightForWidth(self.menu_title_label.sizePolicy().hasHeightForWidth())
        self.menu_title_label.setSizePolicy(sizePolicy)
        self.menu_title_label.setMinimumSize(QSize(300, 50))
        self.menu_title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.main_vertical_layout.addWidget(self.menu_title_label)

        self.middle_spacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.main_vertical_layout.addItem(self.middle_spacer_3)

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setObjectName(u"horizontal_layout")
        self.center_left_spacer = QSpacerItem(33, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout.addItem(self.center_left_spacer)

        self.center_vertical_layout = QVBoxLayout()
        self.center_vertical_layout.setObjectName(u"center_vertical_layout")
        self.rankings_button = QPushButton(rankings_contest_main_menu)
        self.rankings_button.setObjectName(u"rankings_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rankings_button.sizePolicy().hasHeightForWidth())
        self.rankings_button.setSizePolicy(sizePolicy1)
        self.rankings_button.setMinimumSize(QSize(300, 50))

        self.center_vertical_layout.addWidget(self.rankings_button)

        self.middle_spacer_2 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.center_vertical_layout.addItem(self.middle_spacer_2)

        self.statistics_button = QPushButton(rankings_contest_main_menu)
        self.statistics_button.setObjectName(u"statistics_button")
        sizePolicy1.setHeightForWidth(self.statistics_button.sizePolicy().hasHeightForWidth())
        self.statistics_button.setSizePolicy(sizePolicy1)
        self.statistics_button.setMinimumSize(QSize(300, 50))

        self.center_vertical_layout.addWidget(self.statistics_button)

        self.middle_spacer_1 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.center_vertical_layout.addItem(self.middle_spacer_1)

        self.back_button = QPushButton(rankings_contest_main_menu)
        self.back_button.setObjectName(u"back_button")
        sizePolicy1.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy1)
        self.back_button.setMinimumSize(QSize(300, 50))

        self.center_vertical_layout.addWidget(self.back_button)


        self.horizontal_layout.addLayout(self.center_vertical_layout)

        self.center_right_spacer = QSpacerItem(33, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout.addItem(self.center_right_spacer)


        self.main_vertical_layout.addLayout(self.horizontal_layout)

        self.bottom_spacer = QSpacerItem(17, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.main_vertical_layout.addItem(self.bottom_spacer)


        self.layout.addLayout(self.main_vertical_layout)

        self.right_spacer = QSpacerItem(100, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.layout.addItem(self.right_spacer)


        self.retranslateUi(rankings_contest_main_menu)

        QMetaObject.connectSlotsByName(rankings_contest_main_menu)
    # setupUi

    def retranslateUi(self, rankings_contest_main_menu):
        rankings_contest_main_menu.setWindowTitle(QCoreApplication.translate("rankings_contest_main_menu", u"Form", None))
        self.menu_title_label.setText(QCoreApplication.translate("rankings_contest_main_menu", u"Contest - Rankings", None))
        self.rankings_button.setText(QCoreApplication.translate("rankings_contest_main_menu", u"Rankings by Year", None))
        self.statistics_button.setText(QCoreApplication.translate("rankings_contest_main_menu", u"Statistics", None))
        self.back_button.setText(QCoreApplication.translate("rankings_contest_main_menu", u"Back to Rankings Main Menu", None))
    # retranslateUi

