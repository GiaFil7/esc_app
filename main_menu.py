from PySide6.QtWidgets import QWidget
from ui.ui_main_menu import Ui_main_menu

import resources_rc

class main_menu(QWidget,Ui_main_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)