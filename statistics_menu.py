from PySide6.QtWidgets import QWidget
from ui.ui_statistics_menu import Ui_statistics_menu
from statistics_table import statistics_table
from statistics_per_country import statistics_per_country
from functools import partial

import resources_rc

class statistics_menu(QWidget,Ui_statistics_menu):
    def __init__(self,contest,contest_menu):
        super().__init__()
        self.setupUi(self)

        self.contest = contest
        self.contest_menu = contest_menu

        self.winners_button.clicked.connect(partial(self.load_table,"Winners"))
        self.second_places_button.clicked.connect(partial(self.load_table,"2nd Places"))
        self.third_places_button.clicked.connect(partial(self.load_table,"3rd Places"))
        self.last_places_button.clicked.connect(partial(self.load_table,"Last Places"))
        self.medal_table_button.clicked.connect(partial(self.load_table,"Medal table"))
        self.per_country_button.clicked.connect(partial(self.load_per_country,self.contest))
        self.back_button.clicked.connect(self.go_back_to_contest)

    def load_table(self,table_type):
        self.stacked_widget = self.parent()
        table_to_load = statistics_table("ESC",table_type)
        table_to_load.back_button.clicked.connect(partial(self.go_back, table_to_load))
        self.stacked_widget.addWidget(table_to_load)
        self.stacked_widget.setCurrentWidget(table_to_load)

    def load_per_country(self,contest):
        self.stacked_widget = self.parent()
        widget = statistics_per_country(contest)
        widget.back_button.clicked.connect(partial(self.go_back, widget))
        self.stacked_widget.addWidget(widget)
        self.stacked_widget.setCurrentWidget(widget)

    def go_back(self,widget):
        if isinstance(widget, statistics_table):
            self.stacked_widget.setCurrentWidget(self)
            self.stacked_widget.removeWidget(widget)
        else:
            self.stacked_widget.setCurrentWidget(self)
            self.stacked_widget.removeWidget(widget)

    def go_to_per_country_menu(self,table):
        widget = statistics_per_country(self.contest)
        self.stacked_widget.setCurrentWidget(widget)
        self.stacked_widget.removeWidget(table)

    def go_back_to_contest(self):
        self.stacked_widget = self.parent()
        self.stacked_widget.addWidget(self.contest_menu)
        self.stacked_widget.setCurrentWidget(self.contest_menu)