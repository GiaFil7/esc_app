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
        if self.table_type == "Winners":
            self.icon_label.setPixmap(QPixmap(":/images/heart_logos/empty_heart.svg")) # Change
        elif self.table_type == "2nd Places":
            self.icon_label.setPixmap(QPixmap(":/images/heart_logos/empty_heart.svg")) # Change
        elif self.table_type == "3rd Places":
            self.icon_label.setPixmap(QPixmap(":/images/heart_logos/empty_heart.svg")) # Change
        elif self.table_type == "Last Places":
            self.icon_label.setPixmap(QPixmap(":/images/heart_logos/empty_heart.svg")) # Change

        if self.contest == "ESC":
            self.filename = "esc_data.xlsx"
            self.years = range(1956,2024+1) # Change
            self.submitted = len(self.years) * [True] # Change

        row_count = sum(1 for x in self.submitted if x)
        self.table.setRowCount(row_count)

        # Get only the years with submitted rankings
        self.submitted_years = [year for year in self.years if self.submitted[self.years.index(year)]]

        if self.submitted_years != []:
            data = pd.read_excel(self.filename)
            for year in self.submitted_years:
                entries = data[data['contest'] == f"{self.contest} {year}"]
                if self.table_type == "Winners":
                    entry = entries.iloc[0]
                elif self.table_type == "2nd Places":
                    entry = entries.iloc[1]
                elif self.table_type == "3rd Places":
                    entry = entries.iloc[2]
                elif self.table_type == "Last Places":
                    entry = entries.iloc[-1]

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




        

