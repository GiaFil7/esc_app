from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from ui.ui_credits import Ui_credits
from utils import load_widget, read_html_file
from functools import partial
import resources_rc

class credits(QWidget, Ui_credits):
    """
    Displays the credits of the app.

    :param main_menu: The main menu of the app
    :type main_menu: object
    """

    def __init__(self, main_menu: object):
        super().__init__()
        self.setupUi(self)

        self.close_button.clicked.connect(partial(load_widget, self, main_menu))

        # Read and display the credits HTML file
        html_text = read_html_file("files\\credits.html")
        self.text_label.setText(html_text)
        self.text_label.setAlignment(Qt.AlignTop)
