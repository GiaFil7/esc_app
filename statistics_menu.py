from PySide6.QtWidgets import QWidget
from ui.ui_statistics_menu import Ui_statistics_menu
from statistics_table import statistics_table
from statistics_per_country import statistics_per_country
from functools import partial

import resources_rc

class statistics_menu(QWidget,Ui_statistics_menu):
    def __init__(self,contest_code,contest_menu):
        super().__init__()
        self.setupUi(self)

        self.contest_code = contest_code
        self.contest_menu = contest_menu

        self.winners_button.clicked.connect(partial(self.load_table,"Winners"))
        self.second_places_button.clicked.connect(partial(self.load_table,"2nd Places"))
        self.third_places_button.clicked.connect(partial(self.load_table,"3rd Places"))
        self.last_places_button.clicked.connect(partial(self.load_table,"Last Places"))
        self.medal_table_button.clicked.connect(partial(self.load_table,"Medal table"))
        self.per_country_button.clicked.connect(partial(self.load_per_country,self.contest_code))
        self.back_button.clicked.connect(self.go_back)

    def load_table(self,table_type):
        self.stacked_widget = self.parent()
        table_to_load = statistics_table(self.contest_code,table_type,self)
        self.stacked_widget.addWidget(table_to_load)
        self.stacked_widget.setCurrentWidget(table_to_load)

    def load_per_country(self,contest_code):
        self.stacked_widget = self.parent()
        widget = statistics_per_country(contest_code,self)
        self.stacked_widget.addWidget(widget)
        self.stacked_widget.setCurrentWidget(widget)

    def go_back(self):
        self.stacked_widget = self.parent()
        self.stacked_widget.addWidget(self.contest_menu)
        self.stacked_widget.setCurrentWidget(self.contest_menu)