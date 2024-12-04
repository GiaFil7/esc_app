from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import Qt
from ui.ui_quizzes_list_menu import Ui_quizzes_list_menu
from rankings.rankings_menu_item import rankings_menu_item
from utils import load_widget, get_countries, get_entry_data, get_country_codes, get_contest_data
from functools import partial
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

        # Setup menu items
        self.layout = QVBoxLayout()
        match self.menu_type:
            case "by_country":
                countries = get_countries(self.entry_data)
                country_codes = get_country_codes()

                for country in countries:
                    country_code = country_codes[country_codes['country'] == country]
                    country_code = country_code['code'].to_string(index = False, header = False)
                    logo_path = f":/images/heart_logos/{country_code}.png"
                    self.add_item(country, logo_path, country)

            case "by_year":
                years = list(self.contest_data['year'])

                for year in years:
                    logo_path = f":/images/contest_logos/{self.contest_code}/{self.contest_code}_{year}.png"
                    self.add_item(f"{self.contest_name} {year}", logo_path, year)

            case "misc":
                quizzes = ["All entries", "Winners"]

                for quiz in quizzes:
                    self.add_item(quiz, ":/images/heart_logos/empty_heart.svg", quiz)
        
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignTop)

        # Create a temporary widget to set the layout onto the scroll area
        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.layout)
        self.scroll_area.setWidget(self.scroll_widget)
    
    def load_quiz(self, var):
        print(var)
        load_widget(self, QWidget()) # Change

    def add_item(self, text: str, logo_path: str, var):
        item = rankings_menu_item(text, logo = logo_path)
        item.submitted_label.hide()
        item.clicked.connect(partial(self.load_quiz, var))
        self.layout.addWidget(item)