from PySide6.QtWidgets import QWidget
from ui.ui_rankings_main_menu import Ui_rankings_main_menu
from rankings.rankings_contest_main_menu import rankings_contest_main_menu
from functools import partial
from utils import load_widget
import resources_rc

class rankings_main_menu(QWidget, Ui_rankings_main_menu):
    """
    The main menu for the rankings. It allows the user to navigate to the main
    menu for every supported contest and back to the main menu of the app.

    :param main_menu_widget: The main menu of the app (previous menu of this widget)
    :type main_menu_widget: object
    """

    def __init__(self, main_menu_widget: object):
        super().__init__()
        self.setupUi(self)

        # Setup the slots
        self.esc_rankings_button.clicked.connect(partial(load_widget, self, rankings_contest_main_menu("ESC", self)))
        self.back_button.clicked.connect(partial(load_widget, self, main_menu_widget))