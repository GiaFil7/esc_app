# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quizzes_widget.ui'
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
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_quizzes_widget(object):
    def setupUi(self, quizzes_widget):
        if not quizzes_widget.objectName():
            quizzes_widget.setObjectName(u"quizzes_widget")
        quizzes_widget.resize(600, 400)
        self.layout = QVBoxLayout(quizzes_widget)
        self.layout.setSpacing(0)
        self.layout.setObjectName(u"layout")
        self.title_layout = QHBoxLayout()
        self.title_layout.setObjectName(u"title_layout")
        self.logo_label = QLabel(quizzes_widget)
        self.logo_label.setObjectName(u"logo_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy)
        self.logo_label.setMaximumSize(QSize(95, 30))
        self.logo_label.setPixmap(QPixmap(u":/images/heart_logos/empty_heart.svg"))
        self.logo_label.setScaledContents(True)

        self.title_layout.addWidget(self.logo_label)

        self.name_label = QLabel(quizzes_widget)
        self.name_label.setObjectName(u"name_label")

        self.title_layout.addWidget(self.name_label)

        self.spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.title_layout.addItem(self.spacer)

        self.score_label = QLabel(quizzes_widget)
        self.score_label.setObjectName(u"score_label")

        self.title_layout.addWidget(self.score_label)

        self.timer_label = QLabel(quizzes_widget)
        self.timer_label.setObjectName(u"timer_label")

        self.title_layout.addWidget(self.timer_label)

        self.play_pause_button = QPushButton(quizzes_widget)
        self.play_pause_button.setObjectName(u"play_pause_button")
        sizePolicy.setHeightForWidth(self.play_pause_button.sizePolicy().hasHeightForWidth())
        self.play_pause_button.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/icons/play_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_pause_button.setIcon(icon)

        self.title_layout.addWidget(self.play_pause_button)

        self.back_button = QPushButton(quizzes_widget)
        self.back_button.setObjectName(u"back_button")
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/back_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_button.setIcon(icon1)

        self.title_layout.addWidget(self.back_button)


        self.layout.addLayout(self.title_layout)

        self.desc_layout = QHBoxLayout()
        self.desc_layout.setSpacing(0)
        self.desc_layout.setObjectName(u"desc_layout")
        self.desc_label = QLabel(quizzes_widget)
        self.desc_label.setObjectName(u"desc_label")

        self.desc_layout.addWidget(self.desc_label)

        self.answer_line_edit = QLineEdit(quizzes_widget)
        self.answer_line_edit.setObjectName(u"answer_line_edit")

        self.desc_layout.addWidget(self.answer_line_edit)

        self.spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.desc_layout.addItem(self.spacer_2)

        self.give_up_button = QPushButton(quizzes_widget)
        self.give_up_button.setObjectName(u"give_up_button")
        sizePolicy.setHeightForWidth(self.give_up_button.sizePolicy().hasHeightForWidth())
        self.give_up_button.setSizePolicy(sizePolicy)

        self.desc_layout.addWidget(self.give_up_button)


        self.layout.addLayout(self.desc_layout)

        self.scroll_area = QScrollArea(quizzes_widget)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 582, 324))
        self.scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.layout.addWidget(self.scroll_area)


        self.retranslateUi(quizzes_widget)

        QMetaObject.connectSlotsByName(quizzes_widget)
    # setupUi

    def retranslateUi(self, quizzes_widget):
        quizzes_widget.setWindowTitle(QCoreApplication.translate("quizzes_widget", u"Form", None))
        self.logo_label.setText("")
        self.name_label.setText(QCoreApplication.translate("quizzes_widget", u"Title", None))
        self.score_label.setText(QCoreApplication.translate("quizzes_widget", u"Score: ##/##", None))
        self.timer_label.setText(QCoreApplication.translate("quizzes_widget", u"00:00", None))
        self.play_pause_button.setText("")
        self.back_button.setText("")
        self.desc_label.setText(QCoreApplication.translate("quizzes_widget", u"Description", None))
        self.give_up_button.setText(QCoreApplication.translate("quizzes_widget", u"Give up", None))
    # retranslateUi

