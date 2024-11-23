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
            case "Medal table":
                self.icon_label.setPixmap(QPixmap(":/images/heart_logos/empty_heart.svg")) # Change
            case _:
                country_codes = pd.read_excel('country_codes.xlsx')
                country_code_row = country_codes[country_codes['country'] == self.table_type]
                country_code = country_code_row['code'].to_string(index=False)

                self.icon_label.setPixmap(QPixmap(f":/images/heart_logos/{country_code}.png"))
        
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
                #self.table.setSortingEnabled(True)
                self.table.horizontalHeader().sectionClicked.connect(self.handle_sort)
            elif self.table_type in self.countries:
                self.years_participated = data[data['country'] == self.table_type]
                self.years_participated = self.years_participated['contest'].to_string(index=False)
                self.years_participated = self.years_participated.split("\n")
                self.years_participated = [item.split(" ") for item in self.years_participated]
                self.years_participated = [int(item[1]) for item in self.years_participated]

                years_participated_and_submitted = set(self.years_participated) & set(self.submitted_years)
                if len(years_participated_and_submitted) != 0:
                    cols = ["Song","Artist","Place"]
                    self.table.setColumnCount(len(cols))
                    self.table.setHorizontalHeaderLabels(cols)
                    self.table.setRowCount(len(years_participated_and_submitted))
                    years_participated_and_submitted = list(years_participated_and_submitted)
                    years_participated_and_submitted = [str(x) for x in years_participated_and_submitted]
                    self.table.setVerticalHeaderLabels(years_participated_and_submitted)
                else:
                    print("No submitted years") # Change Create func
            else:
                cols = ["Country","Song","Artist"]
                self.table.setColumnCount(len(cols))
                self.table.setHorizontalHeaderLabels(cols)
                labels = [str(x) for x in self.submitted_years]
                self.table.setRowCount(len(self.submitted_years))
                self.table.setVerticalHeaderLabels(labels)
        
            for year in self.submitted_years:
                entries = data[data['contest'] == f"{self.contest} {year}"]

                match self.table_type:
                    case "Winners":
                        entry = entries.iloc[0]
                        items = [entry['country'], entry['song'], entry['artist']]
                        self.setRowItems(items,year)
                    case "2nd Places":
                        entry = entries.iloc[1]
                        items = [entry['country'], entry['song'], entry['artist']]
                        self.setRowItems(items,year)
                    case "3rd Places":
                        entry = entries.iloc[2]
                        items = [entry['country'], entry['song'], entry['artist']]
                        self.setRowItems(items,year)
                    case "Last Places":
                        entry = entries.iloc[-1]
                        items = [entry['country'], entry['song'], entry['artist']]
                        self.setRowItems(items,year)
                    case "Medal table":
                        places = [0,1,2,3,4,len(entries)-1]
                        for i in places:
                            entry = entries.iloc[i]
                            placing_data.loc[entry['country'],cols[places.index(i)]] += 1
                    case _:
                        entry = entries[entries['country'] == self.table_type]
                        if self.table_type in list(entries['country']):
                            place_text = self.get_placing_text(entries)
                            items = [entry['song'].to_string(index=False), entry['artist'].to_string(index=False), place_text]
                            self.setRowItems(items,year)
            
            if self.table_type == "Medal table":
                for country in self.countries:
                    items = [str(placing_data.loc[country,col]) for col in cols]
                    self.setRowItems(items,country)

            header = self.table.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeToContents)
        else:
            print("No submitted years") # Change Create func


    def setRowItems(self,items,ind):
        for i in range(len(items)):
            item = items[i]
            widget_item = QTableWidgetItem(item)
            widget_item.setTextAlignment(Qt.AlignCenter)
            widget_item.setFlags(Qt.ItemIsEnabled)
            if self.table_type == "Medal table":
                self.table.setItem(self.countries.index(ind),i,widget_item)
            elif self.table_type in self.countries:
                self.table.setItem(self.years_participated.index(ind),i,widget_item)
            else:
                self.table.setItem(self.submitted_years.index(ind),i,widget_item)

    def get_placing_text(self,entries):
        countries = list(entries['country'])
        place = countries.index(self.table_type) + 1
        if (place >= 11 and place <=19) or place % 10 == 0 or (place % 10 >=4 and place % 10 <=9):
            text = f"{place}th/{len(countries)}"
        elif place % 10 == 1:
            text = f"{place}st/{len(countries)}"
        elif place % 10 == 2:
            text = f"{place}nd/{len(countries)}"
        elif place % 10 == 3:
            text = f"{place}rd/{len(countries)}"
        return text
    
    def handle_sort(self,logical_ind):
        # Extract the column headers
        column_headers = [self.table.horizontalHeaderItem(col).text() for col in range(self.table.columnCount())]

        # Extract the row headers
        row_headers = [self.table.verticalHeaderItem(row).text() for row in range(self.table.rowCount())]

        # Extract the table data
        data = []
        for row in range(self.table.rowCount()):
            row_data = []
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                row_data.append(item.text() if item else "")
            data.append(row_data)

        # Create the DataFrame
        df = pd.DataFrame(data, columns=column_headers, index=row_headers)

        # Print the DataFrame
        print(df)
