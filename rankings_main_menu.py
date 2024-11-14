from PySide6.QtWidgets import QWidget
from ui_rankings_main_menu import Ui_rankings_main_menu
from main_menu import main_menu
from rankings_esc_main_menu import rankings_esc_main_menu

import resources_rc

class rankings_main_menu(QWidget,Ui_rankings_main_menu):
    def __init__(self,main_menu):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_menu.parent()

        self.back_button.clicked.connect(self.load_main_menu)
        self.esc_rankings_button.clicked.connect(self.load_esc_rankings)

    def load_esc_rankings(self):
        esc_rankings = rankings_esc_main_menu(self.main_window)
        self.main_window.setCentralWidget(esc_rankings)
    
    def load_main_menu(self):
        main_menu_widget = main_menu(self.main_window)
        self.main_window.setCentralWidget(main_menu_widget)