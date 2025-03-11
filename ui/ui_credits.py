# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'credits.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_credits(object):
    def setupUi(self, credits):
        if not credits.objectName():
            credits.setObjectName(u"credits")
        credits.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(credits.sizePolicy().hasHeightForWidth())
        credits.setSizePolicy(sizePolicy)
        credits.setStyleSheet(u"")
        self.vertical_layout = QVBoxLayout(credits)
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.vertical_layout.setContentsMargins(9, 0, 9, 0)
        self.top_layout = QHBoxLayout()
        self.top_layout.setSpacing(0)
        self.top_layout.setObjectName(u"top_layout")
        self.title_label = QLabel(credits)
        self.title_label.setObjectName(u"title_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy1)

        self.top_layout.addWidget(self.title_label)

        self.spacer_left = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.top_layout.addItem(self.spacer_left)

        self.close_button = QPushButton(credits)
        self.close_button.setObjectName(u"close_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy2)
        icon = QIcon()
        icon.addFile(u":/images/icons/close_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_button.setIcon(icon)

        self.top_layout.addWidget(self.close_button)


        self.vertical_layout.addLayout(self.top_layout)

        self.scroll_area = QScrollArea(credits)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setLineWidth(0)
        self.scroll_area.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 582, 368))
        self.text_label = QLabel(self.scrollAreaWidgetContents_2)
        self.text_label.setObjectName(u"text_label")
        self.text_label.setGeometry(QRect(0, 0, 581, 331))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.text_label.sizePolicy().hasHeightForWidth())
        self.text_label.setSizePolicy(sizePolicy3)
        self.text_label.setMargin(10)
        self.text_label.setOpenExternalLinks(True)
        self.scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.vertical_layout.addWidget(self.scroll_area)


        self.retranslateUi(credits)

        QMetaObject.connectSlotsByName(credits)
    # setupUi

    def retranslateUi(self, credits):
        credits.setWindowTitle(QCoreApplication.translate("credits", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("credits", u"Credits", None))
        self.close_button.setText("")
        self.text_label.setText("")
    # retranslateUi

