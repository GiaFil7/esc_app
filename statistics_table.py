from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PySide6.QtGui import QPixmap,Qt
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

        # Get only the years with submitted rankings
        self.submitted_years = [year for year in self.years if self.submitted[self.years.index(year)]]

        # Read the data
        data = pd.read_excel(self.filename)

        # Get all participating countries
        self.countries = data['country'].unique()
        self.countries = list(self.countries)
        self.countries.sort()


        if self.submitted_years != []:
            if self.table_type == "Medal table":
                cols = ['1st','2nd','3rd','4th','5th','Last']
                placing_data = [[0, 0, 0, 0, 0, 0] for _ in range(len(self.countries))]
                placing_data = pd.DataFrame(placing_data, columns=cols, index=self.countries)
                self.table.setRowCount(len(self.countries))
                self.table.setColumnCount(len(cols))
                self.table.setHorizontalHeaderLabels(cols)
                self.table.setVerticalHeaderLabels(self.countries)
            elif self.table_type in self.countries:
                print("Fix")
            else:
                self.table.setRowCount(len(self.submitted_years))
        
            for year in self.submitted_years:
                entries = data[data['contest'] == f"{self.contest} {year}"]

                match self.table_type:
                    case "Winners":
                        entry = entries.iloc[0]
                        items = [str(year), entry['country'], entry['song'], entry['artist']]
                        self.setRowItems(items,year)
                    case "2nd Places":
                        entry = entries.iloc[1]
                        items = [str(year), entry['country'], entry['song'], entry['artist']]
                        self.setRowItems(items,year)
                    case "3rd Places":
                        entry = entries.iloc[2]
                        items = [str(year), entry['country'], entry['song'], entry['artist']]
                        self.setRowItems(items,year)
                    case "Last Places":
                        entry = entries.iloc[-1]
                        items = [str(year), entry['country'], entry['song'], entry['artist']]
                        self.setRowItems(items,year)
                    case "Medal table":
                        places = [0,1,2,3,4,len(entries)-1]
                        for i in places:
                            entry = entries.iloc[i]
                            placing_data.loc[entry['country'],cols[places.index(i)]] += 1
            
            if self.table_type == "Medal table":
                for country in self.countries:
                    items = [str(placing_data.loc[country,col]) for col in cols]
                    self.setRowItems(items,country)

            header = self.table.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeToContents)
        else:
            print("No submitted years") # Change


    def setRowItems(self,items,ind):
        for i in range(len(items)):
            item = items[i]
            widget_item = QTableWidgetItem(item)
            widget_item.setTextAlignment(Qt.AlignCenter)
            if self.table_type == "Medal table":
                self.table.setItem(self.countries.index(ind),i,widget_item)
            elif self.table_type in self.countries:
                print("Fix")
            else:
                self.table.setItem(self.submitted_years.index(ind),i,widget_item)

        

