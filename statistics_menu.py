from PySide6.QtWidgets import QWidget
from ui.ui_statistics_menu import Ui_statistics_menu
from statistics_table import statistics_table
from functools import partial

import resources_rc

class statistics_menu(QWidget,Ui_statistics_menu):
    def __init__(self,contest):
        super().__init__()
        self.setupUi(self)

        self.contest = contest

        #self.back_button.clicked.connect(self.stacked_widget.load_rankings_esc_main_menu)
        self.winners_button.clicked.connect(partial(self.load_table,"Winners"))
        self.second_places_button.clicked.connect(partial(self.load_table,"2nd Places"))
        self.third_places_button.clicked.connect(partial(self.load_table,"3rd Places"))
        self.last_places_button.clicked.connect(partial(self.load_table,"Last Places"))

    # Access and manipulate stacked_widget from here for the different tables (winners, 2nd, etc.)

    def load_table(self,table_type):
        self.stacked_widget = self.parent()
        table_to_load = statistics_table("ESC",table_type)
        #table_to_load.back_button.connect(partial(self.go_back, table_to_load))
        table_to_load.back_button.connect(lambda table_to_load: self.go_back(table_to_load))
        self.stacked_widget.addWidget(table_to_load)
        self.stacked_widget.setCurrentWidget(table_to_load)

    def go_back(self,table):
        self.stacked_widget.setCurrentWidget(self)
        self.stacked_widget.removeWidget(table)
