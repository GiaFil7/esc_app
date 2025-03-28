from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtCore import Signal
from ui.ui_ranking_menu_item import Ui_ranking_menu_item

import resources_rc

class rankings_menu_item(QWidget, Ui_ranking_menu_item):
    """
    A clickable menu item that displays text, a logo and whether the ranking
    it represents has been sumbitted by the user.

    :param text: The text to be displayed on the item
    :type text: str
    :param submitted: A boolean describing whether the ranking has been submitted or not (default: True)
    :type submitted: bool
    :param logo: The path to the logo to be displayed (default: ":/images/heart_logos/empty_heart.png")
    :type logo: str
    """

    # Make the item clickable
    clicked = Signal()

    def __init__(self, text:str , submitted: bool = True, logo: str = ":/images/heart_logos/empty_heart.png"):
        super().__init__()
        self.setupUi(self)

        # Setup the properties
        self.logo = logo
        self.text = text
        self.submitted = submitted
        
        self.contest_name_label.setText(self.text)
        self.contest_name_label.setObjectName("menu_item")

        logo_pixmap = QPixmap(self.logo)
        logo_pixmap = logo_pixmap.scaled(self.logo_label.size(), aspectMode = Qt.KeepAspectRatio, mode = Qt.SmoothTransformation)
        self.logo_label.setPixmap(logo_pixmap)

        self.update_icon(self.submitted)

    def mousePressEvent(self, e):
        """
        Handles the event when the item is clicked.

        :param e: The event object
        """

        self.clicked.emit()

    def update_icon(self, flag: bool):
        """
        Updates the icon of the item based on the flag parameter.

        :param flag: If True, the icon is a checkmark, else it's an X.
        :type flag: bool
        """

        if flag:
            self.submitted_label.setPixmap(QPixmap(":/images/icons/tick_icon.png"))
        else:
            self.submitted_label.setPixmap(QPixmap(":/images/icons/close_icon.png"))
