from ui.ui_rankings_by_year import Ui_rankings_by_year
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer
from rankings.rankings_menu_item import rankings_menu_item
from rankings.statistics_table import statistics_table
from functools import partial
from utils import load_widget, get_entry_data, get_countries, get_country_codes
from utils import resize_scrollarea
import resources_rc

class statistics_per_country(QWidget, Ui_rankings_by_year):
    """
    A menu with a clickable item for every participating country in the contest.
    After clicking, the proper table is loaded.

    :param contest_code: The contest code of the contest
    :type: str
    :param statistics_menu: The main statistics menu (previous menu of this widget)
    :type object
    """

    def __init__(self, contest_code: str, statistics_menu: object):
        super().__init__()
        self.setupUi(self)

        # Setup the properties
        self.contest_code = contest_code
        self.statistics_menu = statistics_menu
        self.contest_name = statistics_menu.contest_name

        self.name_label.setText(self.contest_name)
        self.name_label.setObjectName("widget_title")
        self.scroll_area.setObjectName("per_country_scrollarea")
        self.back_button.setObjectName("button_small")
        
        logo_path = f":/images/contest_logos/{self.contest_code}/{self.contest_code}.png"
        self.logo_label.setPixmap(QPixmap(logo_path))

        self.back_button.clicked.connect(partial(load_widget, self, statistics_menu))

        self.setup_menu_items()
        self.title_layout.setAlignment(Qt.AlignLeft)

    def setup_menu_items(self):
        """
        Adds a menu item to the layout for every participating country in the contest.
        """

        # Get all the participating countries and country codes
        data = get_entry_data(self.contest_code)
        countries = get_countries(data)
        country_codes = get_country_codes()
        
        # Setup the layout
        self.layout = QVBoxLayout()
        for country in countries:
            country_code_row = country_codes[country_codes['country'] == country]
            country_code = country_code_row['code'].to_string(index = False)
            item = rankings_menu_item(country, logo = f":/images/heart_logos/{country_code}.png")
            item.submitted_label.hide()
            item.clicked.connect(partial(self.load_country_stats, country))
            item.setAttribute(Qt.WA_StyledBackground, True)
            item.setObjectName("stats_per_country_item")
            item.setFixedWidth(225)

            self.layout.addWidget(item)
        self.layout.setSpacing(10)

        # Initialise a temporary widget and set it to the scroll area
        self.scroll_widget = QWidget()
        self.scroll_widget.setObjectName("scroll_widget")
        self.scroll_widget.setLayout(self.layout)
        self.scroll_area.setWidget(self.scroll_widget)

        QTimer.singleShot(20, partial(resize_scrollarea, self.scroll_area, self.layout, 10))

    def load_country_stats(self, country: str):
        """
        Loads the statistics table of the specified country.

        :param country: The name of the country
        :type country: str
        """

        load_widget(self, statistics_table(self.contest_code, country, self))