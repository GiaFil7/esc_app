from PySide6.QtWidgets import QWidget
from ui_rankings_esc_main_menu import Ui_rankings_esc_main_menu

import resources_rc

class rankings_esc_main_menu(QWidget,Ui_rankings_esc_main_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)