# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ranking_item.ui'
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
    QWidget)
import resources_rc
import resources_rc

class Ui_ranking_item(object):
    def setupUi(self, ranking_item):
        if not ranking_item.objectName():
            ranking_item.setObjectName(u"ranking_item")
        ranking_item.resize(708, 43)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ranking_item.sizePolicy().hasHeightForWidth())
        ranking_item.setSizePolicy(sizePolicy)
        self.h_layout = QHBoxLayout(ranking_item)
        self.h_layout.setSpacing(0)
        self.h_layout.setObjectName(u"h_layout")
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout = QHBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(-1, 2, -1, 2)
        self.number_label = QLabel(ranking_item)
        self.number_label.setObjectName(u"number_label")
        sizePolicy.setHeightForWidth(self.number_label.sizePolicy().hasHeightForWidth())
        self.number_label.setSizePolicy(sizePolicy)
        self.number_label.setMinimumSize(QSize(0, 0))
        self.number_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.main_layout.addWidget(self.number_label)

        self.heart_label = QLabel(ranking_item)
        self.heart_label.setObjectName(u"heart_label")
        self.heart_label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.heart_label.sizePolicy().hasHeightForWidth())
        self.heart_label.setSizePolicy(sizePolicy)
        self.heart_label.setMaximumSize(QSize(25, 25))
        self.heart_label.setPixmap(QPixmap(u":/images/heart_logos/empty_heart.svg"))
        self.heart_label.setScaledContents(True)

        self.main_layout.addWidget(self.heart_label)

        self.song_label = QLabel(ranking_item)
        self.song_label.setObjectName(u"song_label")
        sizePolicy.setHeightForWidth(self.song_label.sizePolicy().hasHeightForWidth())
        self.song_label.setSizePolicy(sizePolicy)

        self.main_layout.addWidget(self.song_label)


        self.h_layout.addLayout(self.main_layout)


        self.retranslateUi(ranking_item)

        QMetaObject.connectSlotsByName(ranking_item)
    # setupUi

    def retranslateUi(self, ranking_item):
        ranking_item.setWindowTitle(QCoreApplication.translate("ranking_item", u"Form", None))
        self.number_label.setText(QCoreApplication.translate("ranking_item", u"##", None))
        self.heart_label.setText("")
        self.song_label.setText(QCoreApplication.translate("ranking_item", u"Song Name - Artist", None))
    # retranslateUi

