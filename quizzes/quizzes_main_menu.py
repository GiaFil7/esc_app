from PySide6.QtWidgets import QWidget
from ui.ui_quizzes_main_menu import Ui_quizzes_main_menu
from quizzes.quizzes_contest_main_menu import quizzes_contest_main_menu
from utils import load_widget
from functools import partial

class quizzes_main_menu(QWidget, Ui_quizzes_main_menu):
    def __init__(self, main_menu: object):
        super().__init__()
        self.setupUi(self)

        # Setup the slots
        self.esc_quizzes_button.clicked.connect(partial(load_widget, self, quizzes_contest_main_menu("ESC", self)))
        self.back_button.clicked.connect(partial(load_widget, self, main_menu))