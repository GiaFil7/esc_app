from PySide6.QtWidgets import QWidget
from PySide6.QtGui import Qt
from ui.ui_rankings_contest_main_menu import Ui_rankings_contest_main_menu
from rankings.rankings_by_year import rankings_by_year
from rankings.statistics_menu import statistics_menu
from functools import partial
from utils import load_widget, get_contest_name, get_contest_data
import resources_rc

class rankings_contest_main_menu(QWidget, Ui_rankings_contest_main_menu):
    """
    The main contest menu. It allows the user to navigate to their rankings of
    the contest, statistics about those rankings and back to the main menu
    of the app.

    :param contest_code: The contest code of the contest
    :type contest_code: str
    :param rankings_menu_widget: The main rankings menu (previous menu of this widget)
    :type rankings_menu_widget: object
    """

    def __init__(self, contest_code: str, rankings_menu_widget: object):
        super().__init__()
        self.setupUi(self)

        # Setup the properties
        self.contest_code = contest_code
        self.contest_data = get_contest_data(self.contest_code)
        self.contest_name = get_contest_name(self.contest_data)

        self.rankings_button.setObjectName("button_large")
        self.statistics_button.setObjectName("button_large")
        self.back_button.setObjectName("button_large")
        
        # Setup the slots
        self.rankings_button.clicked.connect(self.load_rankings)
        self.statistics_button.clicked.connect(self.load_statistics)
        self.back_button.clicked.connect(partial(load_widget, self, rankings_menu_widget))

        # Set menu title properties
        self.menu_title_label.setText(f"{self.contest_name} - Rankings")
        self.menu_title_label.setObjectName("menu_title")

    def load_rankings(self):
        """
        Loads the rankings_by_year widget.
        """

        load_widget(self, rankings_by_year(self.contest_code, self))

    def load_statistics(self):
        """
        Loads the statistics_menu widget.
        """

        load_widget(self, statistics_menu(self.contest_code, self))