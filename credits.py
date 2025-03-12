from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt
from ui.ui_credits import Ui_credits
from utils import load_widget, read_html_file, round_corners
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

        self.title_label.setObjectName("menu_title")
        self.text_label.setObjectName("credits_label")
        self.setObjectName("credits")

        # Read and display the credits HTML file
        html_text = read_html_file("files\\credits.html")
        self.text_label.setText(html_text)

        # Adjust UI
        self.text_label.setAlignment(Qt.AlignTop)
        self.text_label.setWordWrap(True)
        self.text_label.adjustSize()
        self.title_label.adjustSize()

        margin = 10
        self.vertical_layout.setContentsMargins(margin, margin, margin, margin)
        self.scroll_area.setFixedSize(self.text_label.width(), self.text_label.height())

        total_width = self.text_label.width() + 2 * margin
        total_height = self.title_label.height() + self.vertical_layout.spacing() * 3 + self.text_label.height() + 2 * margin
        self.setFixedSize(total_width, total_height)

        self.vertical_layout.setAlignment(Qt.AlignCenter)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("#791BDE"))

    def resizeEvent(self, event):
        """
        Handles the cropping of the scrollarea.
        """

        super().resizeEvent(event)
        round_corners(self, 16)