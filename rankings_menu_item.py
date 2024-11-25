from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal
from ui.ui_ranking_menu_item import Ui_ranking_menu_item

import resources_rc

class rankings_menu_item(QWidget,Ui_ranking_menu_item):
    clicked = Signal()

    def __init__(self,text,submitted=True,logo=":/images/heart_logos/empty_heart.svg"):
        super().__init__()
        self.setupUi(self)

        self.logo = logo
        self.text = text
        self.submitted = submitted

        self.contest_name_label.setText(self.text)
        self.logo_label.setPixmap(QPixmap(self.logo))

        self.update_icon(self.submitted)

    def mousePressEvent(self, e):
        self.clicked.emit()

    def update_icon(self,flag):
        if flag:
            self.submitted_label.setPixmap(QPixmap(":/images/icons/tick_icon.png"))
        else:
            self.submitted_label.setPixmap(QPixmap(":/images/icons/close_icon.png"))
