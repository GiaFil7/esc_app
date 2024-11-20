from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtGui import QPixmap
from ui.ui_statistics_table import Ui_statistics_table

import pandas as pd # type: ignore
import resources_rc

class statistics_table(QWidget,Ui_statistics_table):
    def __init__(self,contest,table_type):
        super().__init__()
        self.setupUi(self)

        self.contest = contest
        self.table_type = table_type

        self.title_label.setText(self.table_type)
        match self.table_type:
            case "Winners":
                self.icon_label.setPixmap(QPixmap(":/images/heart_logos/empty_heart.svg")) # Change
            case "2nd Places":
                self.icon_label.setPixmap(QPixmap(":/images/heart_logos/empty_heart.svg")) # Change
            case "3rd Places":
                self.icon_label.setPixmap(QPixmap(":/images/heart_logos/empty_heart.svg")) # Change
            case "Last Places":
                self.icon_label.setPixmap(QPixmap(":/images/heart_logos/empty_heart.svg")) # Change
        
        # Get the years the contest was held and if the user has submitted a ranking for each one
        all_contest_data = pd.read_excel('contest_data.xlsx')
        contest_data = all_contest_data[all_contest_data['contest_code'] ==  self.contest]
        self.filename = f"{self.contest}_data.xlsx"
        self.years = list(contest_data['year'])
        self.submitted = list(contest_data['submitted'])

        row_count = sum(1 for x in self.submitted if x)
        self.table.setRowCount(row_count)

        # Get only the years with submitted rankings
        self.submitted_years = [year for year in self.years if self.submitted[self.years.index(year)]]

        if self.submitted_years != []:
            data = pd.read_excel(self.filename)

            countries = data['country'].unique()
            countries = list(countries)
            countries.sort()

            for year in self.submitted_years:
                entries = data[data['contest'] == f"{self.contest} {year}"]

                match self.table_type:
                    case "Winners":
                        entry = entries.iloc[0]
                    case "2nd Places":
                        entry = entries.iloc[1]
                    case "3rd Places":
                        entry = entries.iloc[2]
                    case "Last Places":
                        entry = entries.iloc[-1]
                    case "Medal table":
                        placing_data = [[0, 0, 0, 0, 0, 0] for _ in range(len(countries))]
                        for country in countries:
                            places = [0,1,2,3,4,len(entries)]
                            if country in entries['country']:
                                print("do something")


                year_item = QTableWidgetItem(str(year))
                country_item = QTableWidgetItem(entry['country'])
                song_item = QTableWidgetItem(entry['song'])
                artist_item = QTableWidgetItem(entry['artist'])

                self.table.setItem(self.submitted_years.index(year),0,year_item)
                self.table.setItem(self.submitted_years.index(year),1,country_item)
                self.table.setItem(self.submitted_years.index(year),2,song_item)
                self.table.setItem(self.submitted_years.index(year),3,artist_item)  
        else:
            print("No submitted years") # Change




        

