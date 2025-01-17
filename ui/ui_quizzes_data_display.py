# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quizzes_data_display.ui'
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
    QSizePolicy, QWidget)

class Ui_quizzes_data_display(object):
    def setupUi(self, quizzes_data_display):
        if not quizzes_data_display.objectName():
            quizzes_data_display.setObjectName(u"quizzes_data_display")
        quizzes_data_display.resize(400, 41)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(quizzes_data_display.sizePolicy().hasHeightForWidth())
        quizzes_data_display.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(quizzes_data_display)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_label = QLabel(quizzes_data_display)
        self.left_label.setObjectName(u"left_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_label.sizePolicy().hasHeightForWidth())
        self.left_label.setSizePolicy(sizePolicy1)
        self.left_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.left_label)

        self.line = QFrame(quizzes_data_display)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.right_label = QLabel(quizzes_data_display)
        self.right_label.setObjectName(u"right_label")
        sizePolicy1.setHeightForWidth(self.right_label.sizePolicy().hasHeightForWidth())
        self.right_label.setSizePolicy(sizePolicy1)
        self.right_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.right_label)


        self.retranslateUi(quizzes_data_display)

        QMetaObject.connectSlotsByName(quizzes_data_display)
    # setupUi

    def retranslateUi(self, quizzes_data_display):
        quizzes_data_display.setWindowTitle(QCoreApplication.translate("quizzes_data_display", u"Form", None))
        self.left_label.setText(QCoreApplication.translate("quizzes_data_display", u"TextLabel", None))
        self.right_label.setText(QCoreApplication.translate("quizzes_data_display", u"TextLabel", None))
    # retranslateUi

