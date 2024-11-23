from ui.ui_rankings_by_year import Ui_rankings_by_year
from PySide6.QtWidgets import QWidget,QVBoxLayout
from PySide6.QtGui import QPixmap
from rankings_menu_item import rankings_menu_item
from statistics_table import statistics_table
from functools import partial

import pandas as pd # type: ignore
import resources_rc

class statistics_per_country(QWidget,Ui_rankings_by_year):
    def __init__(self,contest_name):
        super().__init__()
        self.setupUi(self)

        self.contest_name = contest_name

        self.name_label.setText(self.contest_name)
        self.logo_label.setPixmap(QPixmap(":/images/Eurovision_generic_black.png")) # Change

        self.setup_menu_items()

    def setup_menu_items(self):
        countries = self.get_countries(self.contest_name)

        country_codes = pd.read_excel('country_codes.xlsx')
        self.layout = QVBoxLayout()
        for country in countries:
            country_code_row = country_codes[country_codes['country'] == country]
            country_code = country_code_row['code'].to_string(index=False)
            item = rankings_menu_item(country, logo=f":/images/heart_logos/{country_code}.png")
            item.submitted_label.hide()
            item.clicked.connect(partial(self.load_country_stats,self.contest_name,country))
            self.layout.addWidget(item)
        self.layout.setSpacing(0)

        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.layout)
        self.scroll_area.setWidget(self.scroll_widget)

    def get_countries(self,contest):
        filename = f"{contest}_data.xlsx"
        data = pd.read_excel(filename)
        countries = data['country'].unique()
        countries = list(countries)
        countries.sort()

        return countries

    def load_country_stats(self,contest,country):
        stacked_widget = self.parent()
        country_stats_widget = statistics_table(contest,country)
        country_stats_widget.back_button.clicked.connect(partial(self.go_back, country_stats_widget))

        stacked_widget.addWidget(country_stats_widget)
        stacked_widget.setCurrentWidget(country_stats_widget)
    
    def go_back(self,widget):
        stacked_widget = self.parent()
        stacked_widget.setCurrentWidget(self)
        stacked_widget.removeWidget(widget)