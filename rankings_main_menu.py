from PySide6.QtWidgets import QWidget
from ui.ui_rankings_main_menu import Ui_rankings_main_menu
from rankings_esc_main_menu import rankings_esc_main_menu
from functools import partial

import resources_rc

class rankings_main_menu(QWidget,Ui_rankings_main_menu):
    def __init__(self,main_menu_widget):
        super().__init__()
        self.setupUi(self)
        self.main_menu_widget = main_menu_widget

        self.esc_rankings_button.clicked.connect(partial(self.load_contest_menu,"ESC"))
        self.back_button.clicked.connect(self.go_back)

    def load_contest_menu(self,contest_code):
        self.stacked_widget = self.parent()
        contest_menu = rankings_esc_main_menu(contest_code,self)
        self.stacked_widget.addWidget(contest_menu)
        self.stacked_widget.setCurrentWidget(contest_menu)
    
    def go_back(self):
        self.stacked_widget = self.parent()
        self.stacked_widget.addWidget(self.main_menu_widget)
        self.stacked_widget.setCurrentWidget(self.main_menu_widget)