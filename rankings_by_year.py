from PySide6.QtWidgets import QWidget,QVBoxLayout
from PySide6.QtGui import QPixmap
from ui.ui_rankings_by_year import Ui_rankings_by_year
from rankings_menu_item import rankings_menu_item
from ranking_widget import ranking_widget
from functools import partial
import pandas as pd # type: ignore

import resources_rc

class rankings_by_year(QWidget,Ui_rankings_by_year):
    def __init__(self,contest_name="Eurovision Song Contest",logo=":/images/Eurovision_generic_black.png"): # Change
        super().__init__()
        self.setupUi(self)

        self.contest_name = contest_name
        self.contest_code = "ESC" # Change
        self.logo = logo

        self.name_label.setText(self.contest_name)
        self.logo_label.setPixmap(QPixmap(self.logo))

        self.setup_menu_items(self.contest_name)

    def setup_menu_items(self,contest):
        contest_data = pd.read_excel('contest_data.xlsx')
        contest_data = contest_data[contest_data['contest_code'] == self.contest_code]

        years = self.get_years(contest)
        self.layout = QVBoxLayout()
        for year in years:
            ind = contest_data.index[contest_data['year'] == year].tolist()
            ind = ind[0]
            flag = contest_data.iloc[ind,2]

            text  = f"{contest} {str(year)}"
            item = rankings_menu_item(text, submitted=flag)
            item.clicked.connect(partial(self.load_ranking, item))
            self.layout.addWidget(item)
        self.layout.setSpacing(0)

        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.layout)
        self.scroll_area.setWidget(self.scroll_widget)

    def get_years(self,contest):
        if contest == "Eurovision Song Contest": #Change
            return range(1956,2024+1) # Change
        else:
            print("Invalid contest")
            return []
        
    def load_ranking(self,item):
        stacked_widget = self.parent()
        year = item.text.split(" ")[-1]
        ranking = ranking_widget(self.contest_name,int(year))
        ranking.back_button.clicked.connect(partial(self.go_back, ranking))

        stacked_widget.addWidget(ranking)
        stacked_widget.setCurrentWidget(ranking)

    def go_back(self,ranking):
        stacked_widget = self.parent()
        main_window = stacked_widget.parent()
        main_window.load_rankings_by_year()
        self.update_submitted_status(self)
        stacked_widget.removeWidget(ranking)

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
                #menu_item.update()