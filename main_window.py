from PySide6.QtWidgets import QMainWindow,QStackedWidget,QVBoxLayout
from ui_main_window import Ui_main_window
from main_menu import main_menu
from rankings_main_menu import rankings_main_menu
from rankings_esc_main_menu import rankings_esc_main_menu

import resources_rc

class main_window(QMainWindow,Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stacked_widget = QStackedWidget()
        self.main_menu = main_menu(self.stacked_widget)
        self.rankings_main_menu = rankings_main_menu(self.stacked_widget)
        self.rankings_esc_main_menu = rankings_esc_main_menu(self.stacked_widget)

        self.stacked_widget.addWidget(self.main_menu)
        self.stacked_widget.addWidget(self.rankings_main_menu)
        self.stacked_widget.addWidget(self.rankings_esc_main_menu)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stacked_widget)
        self.setLayout(self.layout)