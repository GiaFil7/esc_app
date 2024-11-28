from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QLabel
from PySide6.QtGui import QPixmap,Qt
from ui.ui_statistics_table import Ui_statistics_table
from functools import partial
from utils import load_widget,get_contest_data,get_entry_data,get_countries,get_country_codes
import pandas as pd # type: ignore
import resources_rc

class statistics_table(QWidget,Ui_statistics_table):
    def __init__(self, contest_code, table_type, parent_menu):
        super().__init__()
        self.setupUi(self)

        self.contest_code = contest_code
        self.table_type = table_type
        self.parent_menu = parent_menu

        self.title_label.setText(self.table_type)

        self.back_button.clicked.connect(partial(load_widget, self, parent_menu))

        match self.table_type:
            case "Winners":
                self.icon_label.setPixmap(QPixmap(":/images/icons/1st_place_icon.png"))
            case "2nd Places":
                self.icon_label.setPixmap(QPixmap(":/images/icons/2nd_place_icon.png"))
            case "3rd Places":
                self.icon_label.setPixmap(QPixmap(":/images/icons/3rd_place_icon.png"))
            case "Last Places":
                self.icon_label.setPixmap(QPixmap(":/images/icons/thumbs_down_icon.png"))
            case "Medal table":
                self.icon_label.setPixmap(QPixmap(":/images/icons/podium_icon.png"))
            case _:
                country_codes = get_country_codes()
                country_code_row = country_codes[country_codes['country'] == self.table_type]
                country_code = country_code_row['code'].to_string(index=False)

                self.icon_label.setPixmap(QPixmap(f":/images/heart_logos/{country_code}.png"))
        
        # Get the years the contest was held and if the user has submitted a ranking for each one
        contest_data = get_contest_data(self.contest_code)

        self.years = list(contest_data['year'])
        self.submitted = list(contest_data['submitted'])

        # Get only the years with submitted rankings
        self.submitted_years = [year for year in self.years if self.submitted[self.years.index(year)]]

        # Read the data
        data = get_entry_data(self.contest_code)

        # Get all participating countries
        self.countries = get_countries(data)

        if self.submitted_years != []:
            if self.table_type == "Medal table":
                cols = ['1st','2nd','3rd','4th','5th','Last']
                placing_data = [[0, 0, 0, 0, 0, 0] for _ in range(len(self.countries))]
                placing_data = pd.DataFrame(placing_data, columns=cols, index=self.countries)
                self.table.setRowCount(len(self.countries))
                self.table.setColumnCount(len(cols))
                self.table.setHorizontalHeaderLabels(cols)
                self.table.setVerticalHeaderLabels(self.countries)
                self.table.horizontalHeader().sectionClicked.connect(self.handle_sort)
            elif self.table_type in self.countries:
                self.years_participated = data[data['country'] == self.table_type]
                self.years_participated = self.years_participated['contest'].to_string(index=False)
                self.years_participated = self.years_participated.split("\n")
                self.years_participated = [item.split(" ") for item in self.years_participated]
                self.years_participated = [int(item[1]) for item in self.years_participated]

                self.years_participated_and_submitted = set(self.years_participated) & set(self.submitted_years)
                if len(self.years_participated_and_submitted) != 0:
                    cols = ["Song","Artist","Place"]
                    self.table.setColumnCount(len(cols))
                    self.table.setHorizontalHeaderLabels(cols)
                    self.table.setRowCount(len(self.years_participated_and_submitted))
                    self.years_participated_and_submitted = list(self.years_participated_and_submitted)
                    self.years_participated_and_submitted.sort()
                    self.years_participated_and_submitted = [str(x) for x in self.years_participated_and_submitted]
                    self.table.setVerticalHeaderLabels(self.years_participated_and_submitted)
                else:
                    self.show_none_label(f"No submitted years for {self.table_type}.")
            else:
                cols = ["Country","Song","Artist"]
                self.table.setColumnCount(len(cols))
                self.table.setHorizontalHeaderLabels(cols)
                labels = [str(x) for x in self.submitted_years]
                self.table.setRowCount(len(self.submitted_years))
                self.table.setVerticalHeaderLabels(labels)
        
            for year in self.submitted_years:
                entries = data[data['contest'] == f"{self.contest_code} {year}"]

                match self.table_type:
                    case "Winners":
                        entry = entries.iloc[0]
                        items = [entry['country'], entry['song'], entry['artist']]
                        self.set_row_items(items,year)
                    case "2nd Places":
                        entry = entries.iloc[1]
                        items = [entry['country'], entry['song'], entry['artist']]
                        self.set_row_items(items,year)
                    case "3rd Places":
                        entry = entries.iloc[2]
                        items = [entry['country'], entry['song'], entry['artist']]
                        self.set_row_items(items,year)
                    case "Last Places":
                        entry = entries.iloc[-1]
                        items = [entry['country'], entry['song'], entry['artist']]
                        self.set_row_items(items,year)
                    case "Medal table":
                        places = [0,1,2,3,4,len(entries)-1]
                        for i in places:
                            entry = entries.iloc[i]
                            placing_data.loc[entry['country'],cols[places.index(i)]] += 1
                    case _:
                        if year in self.years_participated:
                            entry = entries[entries['country'] == self.table_type]
                            if self.table_type in list(entries['country']):
                                place_text = self.get_placing_text(entries)
                                items = [entry['song'].to_string(index=False), entry['artist'].to_string(index=False), place_text]
                                self.set_row_items(items,year)
                
            if self.table_type == "Medal table":
                for country in self.countries:
                    items = [str(placing_data.loc[country,col]) for col in cols]
                    self.set_row_items(items,country)

            header = self.table.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeToContents)
        else:
            self.show_none_label("No submitted years.")


    def set_row_items(self,items,ind):
        for i in range(len(items)):
            item = items[i]
            widget_item = QTableWidgetItem(item)
            widget_item.setTextAlignment(Qt.AlignCenter)
            widget_item.setFlags(Qt.ItemIsEnabled)
            if self.table_type == "Medal table":
                self.table.setItem(self.countries.index(ind),i,widget_item)
            elif self.table_type in self.countries:
                self.table.setItem(self.years_participated_and_submitted.index(str(ind)),i,widget_item)
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
        table_data = pd.DataFrame(data, columns=column_headers, index=row_headers)

        cols = ['1st','2nd','3rd','4th','5th','Last']
        cols.insert(0, cols.pop(cols.index(cols[logical_ind])))
        flags = [False, False, False, False, False, False]
        table_data = table_data.sort_values(cols, ascending=flags)

        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                item.setText(table_data.iloc[[row],[col]].to_string(index=False,header=False))
        
        self.table.setVerticalHeaderLabels(table_data.index.to_list())

    def show_none_label(self,text):
        self.table.hide()
        label_widget = QLabel(text)
        label_widget.setStyleSheet("color: red")
        label_widget.setAlignment(Qt.AlignTop)
        self.layout.addWidget(label_widget)