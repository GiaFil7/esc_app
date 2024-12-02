# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_confirm_dialog(object):
    def setupUi(self, confirm_dialog):
        if not confirm_dialog.objectName():
            confirm_dialog.setObjectName(u"confirm_dialog")
        confirm_dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        confirm_dialog.resize(240, 80)
        self.layout = QVBoxLayout(confirm_dialog)
        self.layout.setObjectName(u"layout")
        self.msg_label = QLabel(confirm_dialog)
        self.msg_label.setObjectName(u"msg_label")
        self.msg_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.msg_label)

        self.button_box = QDialogButtonBox(confirm_dialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Orientation.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.button_box.setCenterButtons(True)

        self.layout.addWidget(self.button_box)


        self.retranslateUi(confirm_dialog)
        self.button_box.accepted.connect(confirm_dialog.accept)
        self.button_box.rejected.connect(confirm_dialog.reject)

        QMetaObject.connectSlotsByName(confirm_dialog)
    # setupUi

    def retranslateUi(self, confirm_dialog):
        confirm_dialog.setWindowTitle(QCoreApplication.translate("confirm_dialog", u"Are you sure?", None))
        self.msg_label.setText(QCoreApplication.translate("confirm_dialog", u"All unsaved changes will be lost. Go back?", None))
    # retranslateUi

