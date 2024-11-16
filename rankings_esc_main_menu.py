from PySide6.QtWidgets import QWidget
from ui_rankings_esc_main_menu import Ui_rankings_esc_main_menu
#from rankings_main_menu import rankings_main_menu

import resources_rc

class rankings_esc_main_menu(QWidget,Ui_rankings_esc_main_menu):
    def __init__(self,main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window

        self.back_button.clicked.connect(self.load_main_ranking_menu)
        self.rankings_button.clicked.connect(self.load_rankings_by_year)
        self.statistics_button.clicked.connect(self.load_statistics)

    def load_rankings_by_year(self):
        print("Load rankings by year")
        #rankings_by_year_widget = QWidget() # Change
        #self.main_window.setCentralWidget(rankings_by_year_widget)

    def load_statistics(self):
        print("Load statistics")
        #statistics_widget = QWidget() # Change
        #self.main_window.setCentralWidget(statistics_widget)

    def load_main_ranking_menu(self):
        #main_ranking_menu_widget = rankings_main_menu()
        self.main_window.setCurentWidget(self.main_window.rankings_main_menu)