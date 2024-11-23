from PySide6.QtWidgets import QWidget
from ui.ui_main_menu import Ui_main_menu
from rankings_main_menu import rankings_main_menu

import resources_rc

class main_menu(QWidget,Ui_main_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.rankings_button.clicked.connect(self.load_rankings_main_menu)
        self.quizzes_button.clicked.connect(self.load_quizzes_main_menu)

    def load_rankings_main_menu(self):
        self.stacked_widget = self.parent()
        rankings_menu = rankings_main_menu(self)
        self.stacked_widget.addWidget(rankings_menu)
        self.stacked_widget.setCurrentWidget(rankings_menu)

    def load_quizzes_main_menu(self):
        print("Load quizzes")