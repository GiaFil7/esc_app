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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ranking_item.sizePolicy().hasHeightForWidth())
        ranking_item.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(ranking_item)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.number_label = QLabel(ranking_item)
        self.number_label.setObjectName(u"number_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.number_label.sizePolicy().hasHeightForWidth())
        self.number_label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.number_label)

        self.heart_label = QLabel(ranking_item)
        self.heart_label.setObjectName(u"heart_label")
        self.heart_label.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.heart_label.sizePolicy().hasHeightForWidth())
        self.heart_label.setSizePolicy(sizePolicy1)
        self.heart_label.setMaximumSize(QSize(25, 25))
        self.heart_label.setPixmap(QPixmap(u":/images/heart_logos/empty_heart.svg"))
        self.heart_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.heart_label)

        self.song_label = QLabel(ranking_item)
        self.song_label.setObjectName(u"song_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.song_label.sizePolicy().hasHeightForWidth())
        self.song_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.song_label)


        self.retranslateUi(ranking_item)

        QMetaObject.connectSlotsByName(ranking_item)
    # setupUi

    def retranslateUi(self, ranking_item):
        ranking_item.setWindowTitle(QCoreApplication.translate("ranking_item", u"Form", None))
        self.number_label.setText(QCoreApplication.translate("ranking_item", u"#", None))
        self.heart_label.setText("")
        self.song_label.setText(QCoreApplication.translate("ranking_item", u"Song Name - Artist", None))
    # retranslateUi

