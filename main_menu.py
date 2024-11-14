from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from ui_main_menu import Ui_main_menu
from rankings_main_menu import rankings_main_menu

import resources_rc

class main_menu(QWidget,Ui_main_menu):
    def __init__(self,main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window

        self.rankings_button.clicked.connect(self.load_rankings_menu)
        self.quizzes_button.clicked.connect(self.load_quizzes_menu)

    def load_rankings_menu(self):
        rankings_widget = rankings_main_menu(self)
        self.main_window.setCentralWidget(rankings_widget)

    def load_quizzes_menu(self):
        quizzes_widget = QWidget() # Change
        self.main_window.setCentralWidget(quizzes_widget)