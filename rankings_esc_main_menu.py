from PySide6.QtWidgets import QWidget
from ui.ui_rankings_esc_main_menu import Ui_rankings_esc_main_menu
from statistics_menu import statistics_menu

import resources_rc

class rankings_esc_main_menu(QWidget,Ui_rankings_esc_main_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.statistics_button.clicked.connect(self.load_statistics)

    def load_statistics(self):
        self.stacked_widget = self.parent()
        statistics_menu_widget = statistics_menu("ESC")
        statistics_menu_widget.back_button.clicked.connect(self.stacked_widget.parent().load_rankings_esc_main_menu)
        self.stacked_widget.addWidget(statistics_menu_widget)
        self.stacked_widget.setCurrentWidget(statistics_menu_widget)
