from PySide6.QtWidgets import QWidget
from ui.ui_quizzes_main_menu import Ui_quizzes_main_menu
from quizzes.quizzes_contest_main_menu import quizzes_contest_main_menu
from utils import load_widget
from functools import partial
import resources_rc

class quizzes_main_menu(QWidget, Ui_quizzes_main_menu):
    """
    The main menu for the quizzes. It allows the user to navigate to the main
    menu for every supported contest and back to the main menu of the app.

    :param main_menu: The main menu of the app (previous menu of this widget)
    :type main_menu: object
    """

    def __init__(self, main_menu: object):
        super().__init__()
        self.setupUi(self)

        # Setup the slots
        self.esc_quizzes_button.clicked.connect(partial(load_widget, self, quizzes_contest_main_menu("ESC", self)))
        self.back_button.clicked.connect(partial(load_widget, self, main_menu))

        self.title_label.setObjectName("menu_title")