# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu.ui'
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

class Ui_main_menu(object):
    def setupUi(self, main_menu):
        if not main_menu.objectName():
            main_menu.setObjectName(u"main_menu")
        main_menu.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_menu.sizePolicy().hasHeightForWidth())
        main_menu.setSizePolicy(sizePolicy)
        main_menu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout = QHBoxLayout(main_menu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_spacer = QSpacerItem(300, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.left_spacer)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.top_spacer = QSpacerItem(20, 68, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.top_spacer)

        self.rankings_button = QPushButton(main_menu)
        self.rankings_button.setObjectName(u"rankings_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rankings_button.sizePolicy().hasHeightForWidth())
        self.rankings_button.setSizePolicy(sizePolicy1)
        self.rankings_button.setMinimumSize(QSize(300, 50))

        self.vertical_layout.addWidget(self.rankings_button)

        self.middle_spacer = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vertical_layout.addItem(self.middle_spacer)

        self.quizzes_button = QPushButton(main_menu)
        self.quizzes_button.setObjectName(u"quizzes_button")
        sizePolicy1.setHeightForWidth(self.quizzes_button.sizePolicy().hasHeightForWidth())
        self.quizzes_button.setSizePolicy(sizePolicy1)
        self.quizzes_button.setMinimumSize(QSize(300, 50))

        self.vertical_layout.addWidget(self.quizzes_button)

        self.bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.bottom_spacer)

        self.info_label = QLabel(main_menu)
        self.info_label.setObjectName(u"info_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy2)
        self.info_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vertical_layout.addWidget(self.info_label)


        self.horizontalLayout.addLayout(self.vertical_layout)

        self.right_spacer = QSpacerItem(300, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.right_spacer)


        self.retranslateUi(main_menu)

        QMetaObject.connectSlotsByName(main_menu)
    # setupUi

    def retranslateUi(self, main_menu):
        main_menu.setWindowTitle(QCoreApplication.translate("main_menu", u"Form", None))
        self.rankings_button.setText(QCoreApplication.translate("main_menu", u"Rankings", None))
        self.quizzes_button.setText(QCoreApplication.translate("main_menu", u"Quizzes", None))
        self.info_label.setText(QCoreApplication.translate("main_menu", u"Created by GiaFil using Qt for Python (PySide6)", None))
    # retranslateUi

