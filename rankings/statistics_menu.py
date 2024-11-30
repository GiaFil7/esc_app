from PySide6.QtWidgets import QWidget
from ui.ui_statistics_menu import Ui_statistics_menu
from rankings.statistics_table import statistics_table
from rankings.statistics_per_country import statistics_per_country
from functools import partial
from utils import load_widget
import resources_rc

class statistics_menu(QWidget, Ui_statistics_menu):
    """
    The main statistics menu for a contest. It allows the user to navigate to
    tables that display their winners, 2nd places, 3rd places, last places and
    last places. Furthermore, it links to a menu that leads to statistics per country
    and finally back to the main contest menu.

    :param contest_code: The contest code of the contest
    :type contest_code: str
    :param contest_menu: The main contest menu (previous menu of this widget)
    :type contest_menu: object
    """

    def __init__(self, contest_code: str, contest_menu: object):
        super().__init__()
        self.setupUi(self)

        # Setup the properties
        self.contest_code = contest_code
        self.contest_name = contest_menu.contest_name

        # Setup the slots
        self.winners_button.clicked.connect(partial(self.load_table, "Winners"))
        self.second_places_button.clicked.connect(partial(self.load_table, "2nd Places"))
        self.third_places_button.clicked.connect(partial(self.load_table, "3rd Places"))
        self.last_places_button.clicked.connect(partial(self.load_table, "Last Places"))
        self.medal_table_button.clicked.connect(partial(self.load_table, "Medal table"))
        self.per_country_button.clicked.connect(self.load_per_country)
        self.back_button.clicked.connect(partial(load_widget, self, contest_menu))

    def load_table(self, table_type: str):
        """
        Loads the table widget specified by table_type.

        :param table_type: The type of table to be loaded
        :type table_type: str
        """

        load_widget(self, statistics_table(self.contest_code, table_type, self))

    def load_per_country(self):
        """
        Loads the "Per Country" menu.
        """

        load_widget(self, statistics_per_country(self.contest_code, self))