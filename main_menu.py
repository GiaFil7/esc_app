from PySide6.QtWidgets import QWidget
from ui.ui_main_menu import Ui_main_menu
from rankings_main_menu import rankings_main_menu
from utils import load_widget
from functools import partial
import resources_rc

class main_menu(QWidget,Ui_main_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.rankings_button.clicked.connect(partial(load_widget, self, rankings_main_menu(self)))
        self.quizzes_button.clicked.connect(self.load_quizzes_main_menu)

    def load_quizzes_main_menu(self):
        print("Load quizzes")