from PySide6.QtWidgets import QMainWindow
from ui_main_window import Ui_main_window

import resources_rc

class main_window(QMainWindow,Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)