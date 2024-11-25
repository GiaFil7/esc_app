from ui.ui_rankings_by_year import Ui_rankings_by_year
from PySide6.QtWidgets import QWidget,QVBoxLayout
from PySide6.QtGui import QPixmap
from rankings_menu_item import rankings_menu_item
from statistics_table import statistics_table
from functools import partial

import pandas as pd # type: ignore
import resources_rc

class statistics_per_country(QWidget,Ui_rankings_by_year):
    def __init__(self,contest_code,statistics_menu):
        super().__init__()
        self.setupUi(self)

        self.contest_code = contest_code
        self.statistics_menu = statistics_menu

        self.get_contest_name()
        self.name_label.setText(self.contest_name)

        logo_path = f":/images/contest_logos/{self.contest_code}/{self.contest_code}.png"
        self.logo_label.setPixmap(QPixmap(logo_path))

        self.back_button.clicked.connect(self.go_back)

        self.setup_menu_items()

    def setup_menu_items(self):
        countries = self.get_countries(self.contest_code)

        country_codes = pd.read_excel('country_codes.xlsx')
        self.layout = QVBoxLayout()
        for country in countries:
            country_code_row = country_codes[country_codes['country'] == country]
            country_code = country_code_row['code'].to_string(index=False)
            item = rankings_menu_item(country, logo=f":/images/heart_logos/{country_code}.png")
            item.submitted_label.hide()
            item.clicked.connect(partial(self.load_country_stats,country))
            self.layout.addWidget(item)
        self.layout.setSpacing(0)

        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.layout)
        self.scroll_area.setWidget(self.scroll_widget)

    def get_countries(self,contest_code):
        filename = f"{contest_code}_data.xlsx"
        data = pd.read_excel(filename)
        countries = data['country'].unique()
        countries = list(countries)
        countries.sort()

        return countries
    
    def get_contest_name(self):
        contest_data = pd.read_excel('contest_data.xlsx')
        contest_data = contest_data[contest_data['contest_code'] == self.contest_code]

        name_column = contest_data['contest_name']
        self.contest_name = name_column[0]

    def load_country_stats(self,country):
        self.stacked_widget = self.parent()
        country_stats_widget = statistics_table(self.contest_code,country,self)

        self.stacked_widget.addWidget(country_stats_widget)
        self.stacked_widget.setCurrentWidget(country_stats_widget)

    def go_back(self):
        self.stacked_widget = self.parent()
        self.stacked_widget.addWidget(self.statistics_menu)
        self.stacked_widget.setCurrentWidget(self.statistics_menu)