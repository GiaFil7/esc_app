from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHeaderView
from PySide6.QtGui import QPixmap, Qt
from ui.ui_quizzes_widget import Ui_quizzes_widget
from utils import load_widget, get_country_code
from functools import partial
import resources_rc

class quizzes_widget(QWidget, Ui_quizzes_widget):
    def __init__(self, quiz_name: str, quiz_type: str, parent_menu: object):
        super().__init__()
        self.setupUi(self)

        # Initialise properties
        self.quiz_name = quiz_name
        self.quiz_type = quiz_type
        self.parent_menu = parent_menu
        self.contest_code = self.parent_menu.contest_code
        self.contest_name = self.parent_menu.contest_name
        self.is_paused = True

        # Setup slots
        self.back_button.clicked.connect(partial(load_widget, self, self.parent_menu))
        self.play_pause_button.clicked.connect(self.toggle_quiz_state)
        self.give_up_button.clicked.connect(self.end_quiz)

        # Set texts
        self.name_label.setText(quiz_name)
        self.desc_label.setText(f"Can you name all the entries of {quiz_name}?") # Make special cases for misc

        # Setup the logo
        match self.quiz_type:
            case "country":
                country_code = get_country_code(self.quiz_name)
                logo_path = f":/images/heart_logos/{country_code}.png"

            case "year":
                split_text = self.quiz_name.split(" ")
                self.year = split_text[-1]
                logo_path = f":/images/contest_logos/{self.contest_code}/{self.contest_code}_{self.year}.png"

            case _:
                logo_path = ":/images/heart_logos/empty_heart.svg"
        
        self.logo_label.setPixmap(QPixmap(logo_path))

        # Keep give up button hidden until the quiz starts
        self.give_up_button.hide()

        self.setup_table()


    def toggle_quiz_state(self):
        self.is_paused = not(self.is_paused)

        if self.is_paused:
            self.play_pause_button.setIcon(QPixmap(":/images/icons/play_icon.png"))
        else:
            self.play_pause_button.setIcon(QPixmap(":/images/icons/pause_icon.png"))

    def end_quiz(self):
        print("Quiz ended")

    def setup_table(self):
        cols, table_data, accepted_answers = self.get_table_data()

        self.handle_accepted_answers(accepted_answers)

        self.table = QTableWidget()
        self.table.setColumnCount(len(cols) * 2)
        self.table.setHorizontalHeaderLabels(cols + cols)
        if len(table_data[0]) % 2 == 0:
            self.table.setRowCount(len(table_data[0]) / 2)
        else:
            self.table.setRowCount(0.5 + len(table_data[0]) / 2)
        self.table.verticalHeader().setVisible(False)

        row_count = self.table.rowCount()
        for i in range(len(table_data[0])):
            for j in range(len(cols)):
                row_ind = i % row_count
                if i <= ((len(table_data[0]) - 1) / 2):
                    col_ind = j
                else:
                    col_ind = j + len(cols)

                inds = [row_ind, col_ind]
                text = table_data[j][i]

                self.set_table_item(inds, text)

        self.scroll_area.setWidget(self.table)

        # Resize the columns to fit the contents
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
    
    def get_table_data(self):
        entry_data = self.parent_menu.entry_data

        match self.quiz_type:
            case "country":
                cols = ["Year", "Song", "Placing"]
                entries = entry_data[entry_data['country'] == self.quiz_name]
                
                years = entries['contest'].to_string(index = False)
                years = years.split("\n")
                years = [item.split(" ") for item in years]
                years = [item[1] for item in years]

                songs = list(entries['song'])
                placings = entries['placing'].astype(str).values.tolist()

                table_data = [years, songs, placings]
                
            case "year":
                cols = ["Country", "Song", "Placing"]
                contest = f"{self.contest_code} {self.year}"
                entries = entry_data[entry_data['contest'] == contest]

                countries = list(entries['country'])
                songs = list(entries['song'])
                placings = entries['placing'].astype(str).values.tolist()

                table_data = [countries, songs, placings]

            case _:
                cols = ["Thing", "Song", "Hint"] # Temporary

        accepted_answers = list(entries['accepted_answers'])

        return cols, table_data, accepted_answers

    def handle_accepted_answers(self, accepted_answers: list):
        #print(accepted_answers)
        x = []

    def set_table_item(self, inds: list, text: str):
        widget_item = QTableWidgetItem(text)
        widget_item.setTextAlignment(Qt.AlignCenter)
        widget_item.setFlags(Qt.ItemIsEnabled)
        self.table.setItem(inds[0], inds[1], widget_item)