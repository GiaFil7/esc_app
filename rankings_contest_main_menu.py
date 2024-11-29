from PySide6.QtWidgets import QWidget
from ui.ui_rankings_contest_main_menu import Ui_rankings_contest_main_menu
from rankings_by_year import rankings_by_year
from statistics_menu import statistics_menu
from functools import partial
from utils import load_widget, get_contest_name, get_contest_data
import resources_rc

class rankings_contest_main_menu(QWidget, Ui_rankings_contest_main_menu):
    """
    A widget that allows the user to navigate to their rankings of the
    contest, statistics about those rankings and back to the main menu
    of the app.

    :param contest_code: The contest code of the contest
    :type contest_code: str
    :param rankings_menu_widget: The main menu of the app (previous menu of this widget)
    :type rankings_menu_widget: object
    """

    def __init__(self, contest_code: str, rankings_menu_widget: object):
        super().__init__()
        self.setupUi(self)

        # Setup the properties
        self.contest_code = contest_code
        self.contest_data = get_contest_data(self.contest_code)
        self.contest_name = get_contest_name(self.contest_data)
        
        # Setup the slots
        self.rankings_button.clicked.connect(partial(load_widget, self, rankings_by_year(self.contest_code, self)))
        self.statistics_button.clicked.connect(partial(load_widget, self, statistics_menu(self.contest_code, self)))
        self.back_button.clicked.connect(partial(load_widget, self, rankings_menu_widget))