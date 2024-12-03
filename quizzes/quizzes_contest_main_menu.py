from PySide6.QtWidgets import QWidget
from ui.ui_quizzes_contest_main_menu import Ui_quizzes_contest_main_menu
from utils import get_contest_name, get_contest_data, load_widget
from functools import partial

class quizzes_contest_main_menu(QWidget, Ui_quizzes_contest_main_menu):
    def __init__(self, contest_code: str, quizzes_main_menu: object):
        super().__init__()
        self.setupUi(self)

        # Initialise the properties
        self.contest_code = contest_code
        self.contest_data = get_contest_data(self.contest_code)
        self.contest_name = get_contest_name(self.contest_data)

        # Setup the slots
        # self.by_country_button.clicked.connect(partial(load_widget, self, quizzes_list_menu("by_country", self)))
        # self.by_year_button.clicked.connect(partial(load_widget, self, quizzes_list_menu("by_year", self)))
        # self.misc_button.clicked.connect(partial(load_widget, self, quizzes_list_menu("misc", self)))
        # self.statistics_button.clicked.connect(partial(load_widget, self, quizzes_statistics(self)))
        self.back_button.clicked.connect(partial(load_widget, self, quizzes_main_menu))

        # Set button texts
        self.by_country_button.setText(f"{self.contest_name} - Quizzes by Country")
        self.by_year_button.setText(f"{self.contest_name} - Quizzes by Year")
        self.misc_button.setText(f"{self.contest_name} - Miscellaneous")