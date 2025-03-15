from PySide6.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout
from ui.ui_main_window import Ui_main_window
from main_menu import main_menu
import resources_rc

class main_window(QMainWindow, Ui_main_window):
    """
    Contains a QStackedWidget that is used to display one menu or widget at a time as needed.
    """
    def __init__(self):
        # Initial setup
        super().__init__()
        self.setupUi(self)
        
        # Setup stacked_widget and add the main_menu widget to it
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setObjectName("stacked_widget")
        self.main_menu = main_menu()
        self.stacked_widget.addWidget(self.main_menu)

        # Setup the layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stacked_widget)
        self.stacked_widget.setCurrentWidget(self.main_menu)
        self.setLayout(self.layout)
        self.setCentralWidget(self.stacked_widget)