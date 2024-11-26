from PySide6.QtWidgets import QWidget
from ui.ui_rankings_main_menu import Ui_rankings_main_menu
from rankings_contest_main_menu import rankings_contest_main_menu
from functools import partial
from utils import load_widget
import resources_rc

class rankings_main_menu(QWidget,Ui_rankings_main_menu):
    def __init__(self,main_menu_widget):
        super().__init__()
        self.setupUi(self)

        self.esc_rankings_button.clicked.connect(partial(load_widget, self, rankings_contest_main_menu("ESC",self)))
        self.back_button.clicked.connect(partial(load_widget, self, main_menu_widget))