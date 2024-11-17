# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statistics_menu.ui'
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

class Ui_statistics_menu(object):
    def setupUi(self, statistics_menu):
        if not statistics_menu.objectName():
            statistics_menu.setObjectName(u"statistics_menu")
        statistics_menu.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(statistics_menu.sizePolicy().hasHeightForWidth())
        statistics_menu.setSizePolicy(sizePolicy)
        statistics_menu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout = QHBoxLayout(statistics_menu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_spacer = QSpacerItem(300, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.left_spacer)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setSpacing(0)
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.top_spacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.top_spacer)

        self.per_country_button = QPushButton(statistics_menu)
        self.per_country_button.setObjectName(u"per_country_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.per_country_button.sizePolicy().hasHeightForWidth())
        self.per_country_button.setSizePolicy(sizePolicy1)
        self.per_country_button.setMinimumSize(QSize(300, 30))

        self.vertical_layout.addWidget(self.per_country_button)

        self.middle_spacer_1 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vertical_layout.addItem(self.middle_spacer_1)

        self.medal_table_button = QPushButton(statistics_menu)
        self.medal_table_button.setObjectName(u"medal_table_button")
        sizePolicy1.setHeightForWidth(self.medal_table_button.sizePolicy().hasHeightForWidth())
        self.medal_table_button.setSizePolicy(sizePolicy1)
        self.medal_table_button.setMinimumSize(QSize(300, 30))

        self.vertical_layout.addWidget(self.medal_table_button)

        self.middle_spacer_2 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vertical_layout.addItem(self.middle_spacer_2)

        self.winners_button = QPushButton(statistics_menu)
        self.winners_button.setObjectName(u"winners_button")
        sizePolicy1.setHeightForWidth(self.winners_button.sizePolicy().hasHeightForWidth())
        self.winners_button.setSizePolicy(sizePolicy1)
        self.winners_button.setMinimumSize(QSize(300, 30))

        self.vertical_layout.addWidget(self.winners_button)

        self.middle_spacer_3 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vertical_layout.addItem(self.middle_spacer_3)

        self.second_places_button = QPushButton(statistics_menu)
        self.second_places_button.setObjectName(u"second_places_button")
        sizePolicy1.setHeightForWidth(self.second_places_button.sizePolicy().hasHeightForWidth())
        self.second_places_button.setSizePolicy(sizePolicy1)
        self.second_places_button.setMinimumSize(QSize(300, 30))

        self.vertical_layout.addWidget(self.second_places_button)

        self.middle_spacer_4 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vertical_layout.addItem(self.middle_spacer_4)

        self.third_places_button = QPushButton(statistics_menu)
        self.third_places_button.setObjectName(u"third_places_button")
        sizePolicy1.setHeightForWidth(self.third_places_button.sizePolicy().hasHeightForWidth())
        self.third_places_button.setSizePolicy(sizePolicy1)
        self.third_places_button.setMinimumSize(QSize(300, 30))

        self.vertical_layout.addWidget(self.third_places_button)

        self.middle_spacer_5 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vertical_layout.addItem(self.middle_spacer_5)

        self.last_places_button = QPushButton(statistics_menu)
        self.last_places_button.setObjectName(u"last_places_button")
        sizePolicy1.setHeightForWidth(self.last_places_button.sizePolicy().hasHeightForWidth())
        self.last_places_button.setSizePolicy(sizePolicy1)
        self.last_places_button.setMinimumSize(QSize(300, 30))

        self.vertical_layout.addWidget(self.last_places_button)

        self.middle_spacer_6 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vertical_layout.addItem(self.middle_spacer_6)

        self.back_button = QPushButton(statistics_menu)
        self.back_button.setObjectName(u"back_button")
        sizePolicy1.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy1)
        self.back_button.setMinimumSize(QSize(300, 30))

        self.vertical_layout.addWidget(self.back_button)

        self.bottom_spacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.bottom_spacer)


        self.horizontalLayout.addLayout(self.vertical_layout)

        self.right_spacer = QSpacerItem(300, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.right_spacer)


        self.retranslateUi(statistics_menu)

        QMetaObject.connectSlotsByName(statistics_menu)
    # setupUi

    def retranslateUi(self, statistics_menu):
        statistics_menu.setWindowTitle(QCoreApplication.translate("statistics_menu", u"Form", None))
        self.per_country_button.setText(QCoreApplication.translate("statistics_menu", u"Per country", None))
        self.medal_table_button.setText(QCoreApplication.translate("statistics_menu", u"Medal table", None))
        self.winners_button.setText(QCoreApplication.translate("statistics_menu", u"Winners", None))
        self.second_places_button.setText(QCoreApplication.translate("statistics_menu", u"2nd Places", None))
        self.third_places_button.setText(QCoreApplication.translate("statistics_menu", u"3rd Places", None))
        self.last_places_button.setText(QCoreApplication.translate("statistics_menu", u"Last places", None))
        self.back_button.setText(QCoreApplication.translate("statistics_menu", u"Back to Main Menu", None))
    # retranslateUi

