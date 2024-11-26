from PySide6.QtWidgets import QWidget
from ui.ui_statistics_menu import Ui_statistics_menu
from statistics_table import statistics_table
from statistics_per_country import statistics_per_country
from functools import partial
from utils import load_widget

import resources_rc

class statistics_menu(QWidget,Ui_statistics_menu):
    def __init__(self,contest_code,contest_menu):
        super().__init__()
        self.setupUi(self)
        self.contest_code = contest_code
        self.contest_name = contest_menu.contest_name

        self.winners_button.clicked.connect(partial(self.load_table,"Winners"))
        self.second_places_button.clicked.connect(partial(self.load_table,"2nd Places"))
        self.third_places_button.clicked.connect(partial(self.load_table,"3rd Places"))
        self.last_places_button.clicked.connect(partial(self.load_table,"Last Places"))
        self.medal_table_button.clicked.connect(partial(self.load_table,"Medal table"))
        self.per_country_button.clicked.connect(self.load_per_country)
        self.back_button.clicked.connect(partial(load_widget, self, contest_menu))

    def load_table(self,table_type):
        load_widget(self, statistics_table(self.contest_code,table_type,self))

    def load_per_country(self):
        load_widget(self, statistics_per_country(self.contest_code,self))