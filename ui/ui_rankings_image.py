# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rankings_image.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_rankings_image(object):
    def setupUi(self, rankings_image):
        if not rankings_image.objectName():
            rankings_image.setObjectName(u"rankings_image")
        rankings_image.resize(600, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(rankings_image.sizePolicy().hasHeightForWidth())
        rankings_image.setSizePolicy(sizePolicy)
        rankings_image.setMinimumSize(QSize(600, 600))
        self.layout = QVBoxLayout(rankings_image)
        self.layout.setObjectName(u"layout")
        self.top_layout = QHBoxLayout()
        self.top_layout.setSpacing(0)
        self.top_layout.setObjectName(u"top_layout")
        self.left_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.top_layout.addItem(self.left_spacer)

        self.title_label = QLabel(rankings_image)
        self.title_label.setObjectName(u"title_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy1)

        self.top_layout.addWidget(self.title_label)

        self.right_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.top_layout.addItem(self.right_spacer)


        self.layout.addLayout(self.top_layout)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.left_layout = QVBoxLayout()
        self.left_layout.setObjectName(u"left_layout")
        self.left_layout.setContentsMargins(-1, 0, -1, -1)

        self.bottom_layout.addLayout(self.left_layout)

        self.right_layout = QVBoxLayout()
        self.right_layout.setObjectName(u"right_layout")

        self.bottom_layout.addLayout(self.right_layout)


        self.layout.addLayout(self.bottom_layout)


        self.retranslateUi(rankings_image)

        QMetaObject.connectSlotsByName(rankings_image)
    # setupUi

    def retranslateUi(self, rankings_image):
        rankings_image.setWindowTitle(QCoreApplication.translate("rankings_image", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("rankings_image", u"Eurovision Song Contest ####", None))
    # retranslateUi

