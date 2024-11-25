from PySide6.QtWidgets import QWidget,QVBoxLayout
from PySide6.QtGui import QPixmap
from ui.ui_rankings_by_year import Ui_rankings_by_year
from rankings_menu_item import rankings_menu_item
from ranking_widget import ranking_widget
from functools import partial
import pandas as pd # type: ignore
import resources_rc

class rankings_by_year(QWidget,Ui_rankings_by_year):
    def __init__(self,contest_code,contest_menu):
        super().__init__()
        self.setupUi(self)

        self.contest_code = contest_code
        self.contest_menu = contest_menu
        self.logo_label.setPixmap(QPixmap(f":/images/contest_logos/{self.contest_code}/{self.contest_code}.png"))

        self.back_button.clicked.connect(self.go_back)

        self.setup_menu_items()

    def setup_menu_items(self):
        self.get_contest_name()
        self.name_label.setText(self.contest_name)

        years = self.contest_data['year'].to_list()
        self.layout = QVBoxLayout()
        for year in years:
            ind = self.contest_data.index[self.contest_data['year'] == year].tolist()
            ind = ind[0]
            flag = self.contest_data.iloc[ind,2]

            text  = f"{self.contest_name} {str(year)}"
            logo_path = f":/images/contest_logos/{self.contest_code}/{self.contest_code}_{year}.png"
            item = rankings_menu_item(text, submitted=flag, logo=logo_path)
            item.clicked.connect(partial(self.load_ranking, year))
            self.layout.addWidget(item)
        self.layout.setSpacing(0)

        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.layout)
        self.scroll_area.setWidget(self.scroll_widget)

    def get_contest_name(self):
        self.contest_data = pd.read_excel('contest_data.xlsx')
        self.contest_data = self.contest_data[self.contest_data['contest_code'] == self.contest_code]

        name_column = self.contest_data['contest_name']
        self.contest_name = name_column[0]
        
    def load_ranking(self,year):
        stacked_widget = self.parent()
        ranking = ranking_widget(self.contest_name,int(year),self)

        stacked_widget.addWidget(ranking)
        stacked_widget.setCurrentWidget(ranking)

    def update_submitted_status(self,by_year_widget):
        contest_data = pd.read_excel('contest_data.xlsx')
        contest_data = contest_data[contest_data['contest_code'] == self.contest_code]

        for i in range(by_year_widget.layout.count()):
            menu_item = self.layout.itemAt(i).widget()
            if isinstance(menu_item,rankings_menu_item):
                contest_and_year = menu_item.text.split()
                year = int(contest_and_year[-1])

                ind = contest_data.index[contest_data['year'] == year].tolist()
                ind = ind[0]

                menu_item.update_icon(contest_data.iloc[ind,2])
    
    def go_back(self):
        self.stacked_widget = self.parent()
        self.stacked_widget.addWidget(self.contest_menu)
        self.stacked_widget.setCurrentWidget(self.contest_menu)