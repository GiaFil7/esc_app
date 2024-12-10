from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import Qt
from ui.ui_quizzes_list_menu import Ui_quizzes_list_menu
from rankings.rankings_menu_item import rankings_menu_item
from quizzes.quizzes_widget import quizzes_widget
from quizzes.quizzes_data_display import quizzes_data_display
from utils import load_widget, get_countries, get_entry_data, get_country_code, get_contest_data, get_quiz_data
from functools import partial
import datetime
import resources_rc

class quizzes_list_menu(QWidget, Ui_quizzes_list_menu):
    def __init__(self, menu_type: str, contest_main_menu: object):
        super().__init__()
        self.setupUi(self)

        # Initialise properties
        self.menu_type = menu_type
        self.contest_code = contest_main_menu.contest_code
        self.contest_name = contest_main_menu.contest_name
        self.entry_data = get_entry_data(self.contest_code)
        self.contest_data = get_contest_data(self.contest_code)

        self.back_button.clicked.connect(partial(load_widget, self, contest_main_menu))

        # Set text
        match self.menu_type:
            case "by_country":
                text = f"{self.contest_name} - Quizzes by country"

            case "by_year":
                text = f"{self.contest_name} - Quizzes by year"

            case "misc":
                text = f"{self.contest_name} - Miscellaneous Quizzes"

        self.name_label.setText(text)

        self.setup_layout()
    
    def load_quiz(self, quiz_name: str, quiz_type: str):
        load_widget(self, quizzes_widget(quiz_name, quiz_type, self))

    def add_item(self, text: str, logo_path: str, quiz_name: str, quiz_type: str,
                 best_score_text: str, best_time_text: str):
        item = rankings_menu_item(text, logo = logo_path)
        item.submitted_label.hide()
        item.setFixedWidth(300)
        item.clicked.connect(partial(self.load_quiz, quiz_name, quiz_type))

        score_and_time_widget = quizzes_data_display(best_score_text, best_time_text)

        item_layout = QHBoxLayout()
        item_layout.addWidget(item)
        item_layout.addWidget(score_and_time_widget)

        widget = QWidget()
        widget.setLayout(item_layout)
        widget.setFixedWidth(600)
        self.layout.addWidget(widget)

    def get_score_and_time(self, quiz_code: str):
        quiz_row = self.quiz_data[self.quiz_data['quiz'] == quiz_code]
        best_score = int(quiz_row['best_score'].iloc[0])
        max_score = int(quiz_row['max_score'].iloc[0])
        best_time = int(quiz_row['best_time'].iloc[0])

        self.total_max_score += max_score
        self.total_best_score += best_score
        if best_score > 0:
            self.total_best_time += best_time

        time_value = str(datetime.timedelta(seconds = best_time))
        if best_time < 3600:
            time_value = time_value[-5:]
        
        percentage = round((best_score / max_score) * 100)

        if best_score > 0:
            best_score_text = f"Best score: {best_score}/{max_score} ({percentage}%)"
            best_time_text = f"Best time: {time_value}"
        else:
            best_score_text = "No score set."
            best_time_text = "No time set."

        return best_score_text, best_time_text
    
    def setup_layout(self):
        self.quiz_data = get_quiz_data(self.contest_code)
        self.total_max_score = 0
        self.total_best_score = 0
        self.total_best_time = 0

        # Setup menu items
        self.layout = QVBoxLayout()
        match self.menu_type:
            case "by_country":
                countries = get_countries(self.entry_data)

                for country in countries:
                    country_code = get_country_code(country)
                    logo_path = f":/images/heart_logos/{country_code}.png"

                    best_score_text, best_time_text = self.get_score_and_time(country_code)

                    self.add_item(country, logo_path, country, "country", best_score_text, best_time_text)

            case "by_year":
                years = list(self.contest_data['year'])

                for year in years:
                    logo_path = f":/images/contest_logos/{self.contest_code}/{self.contest_code}_{year}.png"

                    best_score_text, best_time_text = self.get_score_and_time(year)

                    self.add_item(f"{self.contest_name} {year}", logo_path, f"{self.contest_name} {year}", "year", best_score_text, best_time_text)

            case "misc":
                quizzes = ["All entries", "Winners"]

                for quiz in quizzes:
                    self.add_item(quiz, ":/images/heart_logos/empty_heart.svg", quiz, "misc", " ", " ")
        
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignTop)

        # Create a temporary widget to set the layout onto the scroll area
        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.layout)
        self.scroll_area.setWidget(self.scroll_widget)

        if self.menu_type != "misc":
            total_time_value = str(datetime.timedelta(seconds = self.total_best_time))
            if self.total_best_time < 3600:
                total_time_value = total_time_value[-5:]
        
            percentage = round((self.total_best_score / self.total_max_score) * 100)

            text = f"Total score: {self.total_best_score}/{self.total_max_score} ({percentage}%) | Total time: {total_time_value}"
        else:
            text = ""
        
        self.totals_label.setText(text)