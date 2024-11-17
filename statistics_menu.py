from PySide6.QtWidgets import QWidget
from ui.ui_statistics_menu import Ui_statistics_menu

import resources_rc

class statistics_menu(QWidget,Ui_statistics_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        