# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ranking_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_ranking_widget(object):
    def setupUi(self, ranking_widget):
        if not ranking_widget.objectName():
            ranking_widget.setObjectName(u"ranking_widget")
        ranking_widget.resize(755, 584)
        self.verticalLayout = QVBoxLayout(ranking_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_layout = QVBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.title_layout = QHBoxLayout()
        self.title_layout.setObjectName(u"title_layout")
        self.title_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.logo_label = QLabel(ranking_widget)
        self.logo_label.setObjectName(u"logo_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy)
        self.logo_label.setMinimumSize(QSize(0, 80))
        self.logo_label.setMaximumSize(QSize(16777215, 80))
        self.logo_label.setPixmap(QPixmap(u":/images/contest_logos/ESC/ESC.png"))
        self.logo_label.setScaledContents(False)

        self.title_layout.addWidget(self.logo_label)

        self.year_label = QLabel(ranking_widget)
        self.year_label.setObjectName(u"year_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.year_label.sizePolicy().hasHeightForWidth())
        self.year_label.setSizePolicy(sizePolicy1)

        self.title_layout.addWidget(self.year_label)

        self.vertical_line = QFrame(ranking_widget)
        self.vertical_line.setObjectName(u"vertical_line")
        self.vertical_line.setFrameShape(QFrame.Shape.VLine)
        self.vertical_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.title_layout.addWidget(self.vertical_line)

        self.show_combo_box = QComboBox(ranking_widget)
        self.show_combo_box.setObjectName(u"show_combo_box")
        sizePolicy.setHeightForWidth(self.show_combo_box.sizePolicy().hasHeightForWidth())
        self.show_combo_box.setSizePolicy(sizePolicy)

        self.title_layout.addWidget(self.show_combo_box)

        self.import_export_button = QPushButton(ranking_widget)
        self.import_export_button.setObjectName(u"import_export_button")
        sizePolicy.setHeightForWidth(self.import_export_button.sizePolicy().hasHeightForWidth())
        self.import_export_button.setSizePolicy(sizePolicy)

        self.title_layout.addWidget(self.import_export_button)

        self.save_img_button = QPushButton(ranking_widget)
        self.save_img_button.setObjectName(u"save_img_button")
        sizePolicy.setHeightForWidth(self.save_img_button.sizePolicy().hasHeightForWidth())
        self.save_img_button.setSizePolicy(sizePolicy)

        self.title_layout.addWidget(self.save_img_button)

        self.save_button = QPushButton(ranking_widget)
        self.save_button.setObjectName(u"save_button")
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/icons/save_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_button.setIcon(icon)

        self.title_layout.addWidget(self.save_button)

        self.info_button = QPushButton(ranking_widget)
        self.info_button.setObjectName(u"info_button")
        sizePolicy.setHeightForWidth(self.info_button.sizePolicy().hasHeightForWidth())
        self.info_button.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/help_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.info_button.setIcon(icon1)

        self.title_layout.addWidget(self.info_button)

        self.back_button = QPushButton(ranking_widget)
        self.back_button.setObjectName(u"back_button")
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/back_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_button.setIcon(icon2)

        self.title_layout.addWidget(self.back_button)


        self.main_layout.addLayout(self.title_layout)

        self.entry_scroll_area = QScrollArea(ranking_widget)
        self.entry_scroll_area.setObjectName(u"entry_scroll_area")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.entry_scroll_area.sizePolicy().hasHeightForWidth())
        self.entry_scroll_area.setSizePolicy(sizePolicy2)
        self.entry_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 733, 474))
        self.entry_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.main_layout.addWidget(self.entry_scroll_area)


        self.verticalLayout.addLayout(self.main_layout)


        self.retranslateUi(ranking_widget)

        QMetaObject.connectSlotsByName(ranking_widget)
    # setupUi

    def retranslateUi(self, ranking_widget):
        ranking_widget.setWindowTitle(QCoreApplication.translate("ranking_widget", u"Form", None))
        self.logo_label.setText("")
        self.year_label.setText(QCoreApplication.translate("ranking_widget", u"Eurovision Song Contest ####", None))
        self.import_export_button.setText(QCoreApplication.translate("ranking_widget", u"Import/Export", None))
        self.save_img_button.setText(QCoreApplication.translate("ranking_widget", u"Save as image", None))
        self.save_button.setText("")
        self.info_button.setText("")
        self.back_button.setText("")
    # retranslateUi

