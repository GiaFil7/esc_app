from PySide6.QtWidgets import QWidget
from ui.ui_rankings_contest_main_menu import Ui_rankings_contest_main_menu
from rankings_by_year import rankings_by_year
from statistics_menu import statistics_menu
from functools import partial
from utils import load_widget
import resources_rc

class rankings_contest_main_menu(QWidget,Ui_rankings_contest_main_menu):
    def __init__(self, contest_code, rankings_menu_widget):
        super().__init__()
        self.setupUi(self)
        
        self.rankings_button.clicked.connect(partial(load_widget, self, rankings_by_year(contest_code,self)))
        self.statistics_button.clicked.connect(partial(load_widget, self, statistics_menu(contest_code,self)))
        self.back_button.clicked.connect(partial(load_widget, self, rankings_menu_widget))