from PySide6.QtWidgets import QWidget
from ui.ui_main_menu import Ui_main_menu
from rankings.rankings_main_menu import rankings_main_menu
from quizzes.quizzes_main_menu import quizzes_main_menu
from credits import credits
from utils import load_widget
from functools import partial
import resources_rc

class main_menu(QWidget, Ui_main_menu):
    """
    The main menu of the app. It allows the user to navigate to the rankings
    main menu, the quizzes main menu and the credits.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Setup button slots
        self.rankings_button.clicked.connect(partial(load_widget, self, rankings_main_menu(self)))
        self.quizzes_button.clicked.connect(partial(load_widget, self, quizzes_main_menu(self)))
        self.credits_button.clicked.connect(partial(load_widget, self, credits(self)))