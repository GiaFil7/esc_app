from PySide6.QtWidgets import QMainWindow,QStackedWidget,QVBoxLayout
from ui.ui_main_window import Ui_main_window
from main_menu import main_menu
from rankings_main_menu import rankings_main_menu
from rankings_esc_main_menu import rankings_esc_main_menu

import resources_rc

class main_window(QMainWindow,Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stacked_widget = QStackedWidget()
        self.main_menu = main_menu()
        self.rankings_main_menu = rankings_main_menu()
        self.rankings_esc_main_menu = rankings_esc_main_menu()

        self.stacked_widget.addWidget(self.main_menu)
        self.stacked_widget.addWidget(self.rankings_main_menu)
        self.stacked_widget.addWidget(self.rankings_esc_main_menu)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stacked_widget)
        self.stacked_widget.setCurrentWidget(self.main_menu)
        self.setLayout(self.layout)
        self.setCentralWidget(self.stacked_widget)

        self.main_menu.rankings_button.clicked.connect(self.load_rankings_main_menu)
        self.main_menu.quizzes_button.clicked.connect(self.load_quizzes_main_menu)
        self.rankings_main_menu.back_button.clicked.connect(self.load_main_menu)
        self.rankings_main_menu.esc_rankings_button.clicked.connect(self.load_rankings_esc_main_menu)
        self.rankings_esc_main_menu.back_button.clicked.connect(self.load_rankings_main_menu)
        self.rankings_esc_main_menu.statistics_button.clicked.connect(self.load_rankings_statistics)
        self.rankings_esc_main_menu.rankings_button.clicked.connect(self.load_rankings_by_year)


    def load_main_menu(self):
        self.stacked_widget.setCurrentWidget(self.main_menu)

    def load_rankings_main_menu(self):
        self.stacked_widget.setCurrentWidget(self.rankings_main_menu)

    def load_quizzes_main_menu(self):
        print("Load Quizzes")

    def load_rankings_esc_main_menu(self):
        self.stacked_widget.setCurrentWidget(self.rankings_esc_main_menu)

    def load_rankings_by_year(self):
        print("Load rankings by year")

    def load_rankings_statistics(self):
        print("Load statistics")