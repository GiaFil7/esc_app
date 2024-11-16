# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ranking_import_export.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_import_export_dialog(object):
    def setupUi(self, import_export_dialog):
        if not import_export_dialog.objectName():
            import_export_dialog.setObjectName(u"import_export_dialog")
        import_export_dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        import_export_dialog.resize(517, 103)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(import_export_dialog.sizePolicy().hasHeightForWidth())
        import_export_dialog.setSizePolicy(sizePolicy)
        import_export_dialog.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        import_export_dialog.setAutoFillBackground(False)
        self.layoutWidget = QWidget(import_export_dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 501, 82))
        self.layout = QVBoxLayout(self.layoutWidget)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.import_layout = QHBoxLayout()
        self.import_layout.setObjectName(u"import_layout")
        self.import_label = QLabel(self.layoutWidget)
        self.import_label.setObjectName(u"import_label")
        sizePolicy.setHeightForWidth(self.import_label.sizePolicy().hasHeightForWidth())
        self.import_label.setSizePolicy(sizePolicy)
        self.import_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.import_layout.addWidget(self.import_label)

        self.import_field = QLineEdit(self.layoutWidget)
        self.import_field.setObjectName(u"import_field")

        self.import_layout.addWidget(self.import_field)

        self.import_button = QPushButton(self.layoutWidget)
        self.import_button.setObjectName(u"import_button")
        sizePolicy.setHeightForWidth(self.import_button.sizePolicy().hasHeightForWidth())
        self.import_button.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/tick_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.import_button.setIcon(icon)

        self.import_layout.addWidget(self.import_button)


        self.layout.addLayout(self.import_layout)

        self.export_layout = QHBoxLayout()
        self.export_layout.setObjectName(u"export_layout")
        self.export_label = QLabel(self.layoutWidget)
        self.export_label.setObjectName(u"export_label")
        sizePolicy.setHeightForWidth(self.export_label.sizePolicy().hasHeightForWidth())
        self.export_label.setSizePolicy(sizePolicy)
        self.export_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.export_layout.addWidget(self.export_label)

        self.export_field = QLineEdit(self.layoutWidget)
        self.export_field.setObjectName(u"export_field")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.export_field.sizePolicy().hasHeightForWidth())
        self.export_field.setSizePolicy(sizePolicy1)
        self.export_field.setReadOnly(False)

        self.export_layout.addWidget(self.export_field)

        self.export_button = QPushButton(self.layoutWidget)
        self.export_button.setObjectName(u"export_button")
        sizePolicy.setHeightForWidth(self.export_button.sizePolicy().hasHeightForWidth())
        self.export_button.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/images/copy_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.export_button.setIcon(icon1)

        self.export_layout.addWidget(self.export_button)


        self.layout.addLayout(self.export_layout)

        self.error_label = QLabel(self.layoutWidget)
        self.error_label.setObjectName(u"error_label")
        sizePolicy1.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy1)
        self.error_label.setStyleSheet(u"color:red")

        self.layout.addWidget(self.error_label)


        self.retranslateUi(import_export_dialog)

        QMetaObject.connectSlotsByName(import_export_dialog)
    # setupUi

    def retranslateUi(self, import_export_dialog):
        import_export_dialog.setWindowTitle(QCoreApplication.translate("import_export_dialog", u"Import/Export Ranking", None))
        self.import_label.setText(QCoreApplication.translate("import_export_dialog", u"Import", None))
        self.import_button.setText("")
        self.export_label.setText(QCoreApplication.translate("import_export_dialog", u"Export", None))
        self.export_button.setText("")
        self.error_label.setText("")
    # retranslateUi

