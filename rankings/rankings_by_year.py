from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer
from ui.ui_rankings_by_year import Ui_rankings_by_year
from rankings.rankings_menu_item import rankings_menu_item
from rankings.ranking_widget import ranking_widget
from functools import partial
from utils import load_widget, get_contest_data, resize_scrollarea
import resources_rc

class rankings_by_year(QWidget, Ui_rankings_by_year):
    """
    Widget that displays a list of items that when clicked load the ranking
    for the year selected.

    :param contest_code: The contest code the rankings are for
    :type contest_code: str
    :param contest_menu: A rankings_contest_main_menu widget (previous menu of this widget)
    :type contest_menu: object
    """

    def __init__(self, contest_code: str, contest_menu: object):
        super().__init__()
        self.setupUi(self)

        # Setup the properties
        self.contest_code = contest_code
        self.contest_menu = contest_menu

        self.logo_label.setPixmap(QPixmap(f":/images/contest_logos/{self.contest_code}/{self.contest_code}.png"))
        self.name_label.setText(contest_menu.contest_name)
        self.name_label.setObjectName("widget_title")
        self.scroll_area.setObjectName("rankings_by_year_scrollarea")
        self.back_button.setObjectName("button_small")

        self.back_button.clicked.connect(partial(load_widget, self, contest_menu))

        self.setup_menu_items()

    def setup_menu_items(self):
        """
        Setups the menu items.
        """

        # Get needed properties from the contest menu
        self.contest_name = self.contest_menu.contest_name
        self.contest_data = self.contest_menu.contest_data

        self.name_label.setText(self.contest_name)

        # Add an item to the layout for every year the contest was held
        years = self.contest_data['year'].to_list()
        self.layout = QVBoxLayout()
        for year in years:
            ind = self.contest_data.index[self.contest_data['year'] == year].tolist()
            ind = ind[0]
            flag = self.contest_data.iloc[ind,2]

            text  = f"{self.contest_name} {str(year)}"
            logo_path = f":/images/contest_logos/{self.contest_code}/{self.contest_code}_{year}.png"
            item = rankings_menu_item(text, submitted=flag, logo=logo_path)
            item.clicked.connect(partial(self.load_ranking, year))
            item.setAttribute(Qt.WA_StyledBackground, True)
            item.setObjectName("by_year_item")

            self.layout.addWidget(item)
        self.layout.setSpacing(10)

        # Create a temporary widget to set the layout onto the scroll area
        self.scroll_widget = QWidget()
        self.scroll_widget.setObjectName("scroll_widget")
        self.scroll_widget.setLayout(self.layout)
        self.scroll_area.setWidget(self.scroll_widget)

        self.align_icons()
        QTimer.singleShot(20, partial(resize_scrollarea, self.scroll_area, self.layout, 10))
    
    def load_ranking(self, year: str):
        """
        Loads the ranking corresponding to the item clicked.

        :param year: The year of the contest clicked
        :type: str
        """

        load_widget(self, ranking_widget(int(year), self))

    def update_submitted_status(self, by_year_widget: object):
        """
        Updates the icons of the menu items to reflect whether a ranking
        has been submitted by the user for each year.

        :param by_year_widget: An instance of this widget
        :type by_year_widget: object
        """

        # Read the new data
        contest_data = get_contest_data(self.contest_code)

        # Update the icon for every menu item
        for i in range(by_year_widget.layout.count()):
            menu_item = self.layout.itemAt(i).widget()
            if isinstance(menu_item, rankings_menu_item):
                contest_and_year = menu_item.text.split()
                year = int(contest_and_year[-1])

                ind = contest_data.index[contest_data['year'] == year].tolist()
                ind = ind[0]

                menu_item.update_icon(contest_data.iloc[ind,2])

    def align_icons(self):
        """
        Aligns the submitted_label icons with each other.
        """

        # Find the maximum width of the menu items
        widths = []
        for i in range(self.layout.count()):
            item = self.layout.itemAt(i).widget()
            widths.append(item.sizeHint().width())

        max_width = max(widths)

        # Adjust the spacer width of the items
        for i in range(self.layout.count()):
            item = self.layout.itemAt(i).widget()
            spacer_width = item.name_submitted_spacer.sizeHint().width()
            spacer_height = item.name_submitted_spacer.sizeHint().height()
            item.name_submitted_spacer.changeSize(spacer_width + max_width - item.width(), spacer_height)

        self.layout.invalidate()