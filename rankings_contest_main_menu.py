from PySide6.QtWidgets import QWidget
from ui.ui_rankings_contest_main_menu import Ui_rankings_contest_main_menu
from rankings_by_year import rankings_by_year
from statistics_menu import statistics_menu

import resources_rc

class rankings_contest_main_menu(QWidget,Ui_rankings_contest_main_menu):
    def __init__(self, contest_code, rankings_menu_widget):
        super().__init__()
        self.setupUi(self)
        self.contest_code = contest_code
        self.rankings_menu_widget = rankings_menu_widget
        
        self.rankings_button.clicked.connect(self.load_rankings)
        self.statistics_button.clicked.connect(self.load_statistics)
        self.back_button.clicked.connect(self.go_back)

    def load_rankings(self):
        self.stacked_widget = self.parent()
        rankings_widget = rankings_by_year(self.contest_code)
        rankings_widget.back_button.clicked.connect(self.load_contest_menu) # Remove
        self.stacked_widget.addWidget(rankings_widget)
        self.stacked_widget.setCurrentWidget(rankings_widget)

    def load_statistics(self):
        self.stacked_widget = self.parent()
        statistics_menu_widget = statistics_menu(self.contest_code)
        statistics_menu_widget.back_button.clicked.connect(self.load_contest_menu)
        self.stacked_widget.addWidget(statistics_menu_widget)
        self.stacked_widget.setCurrentWidget(statistics_menu_widget)

    def load_contest_menu(self):
        self.stacked_widget = self.parent()
        self.stacked_widget.setCurrentWidget(self)

    def go_back(self):
        self.stacked_widget = self.parent()
        self.stacked_widget.addWidget(self.rankings_menu_widget)
        self.stacked_widget.setCurrentWidget(self.rankings_menu_widget)