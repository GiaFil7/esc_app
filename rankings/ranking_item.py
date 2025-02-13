from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap, QDrag
from PySide6.QtCore import QMimeData, Qt
from ui.ui_ranking_item import Ui_ranking_item
import resources_rc

class ranking_item(QWidget, Ui_ranking_item):
    """
    A draggable widget that displays the position, country, song and artist for an
    entry that is part of a ranking.

    :param position: A number indicating the position in the ranking of the entry
    :type position: int
    :param country_code: The country code of the country the entry is from
    :type country_code: str
    :param song: The song title of the entry
    :type song: str
    :param artist: The artist of the entry
    :type artist: str
    """

    def __init__(self, position: int, country_code: str, song: str, artist: str):
        super().__init__()
        self.setupUi(self)

        # Set the object properties
        self.position = position
        self.country_code = country_code
        self.song = song
        self.artist = artist

        # Remove 1 and 2 from country code for 1956
        country_code_for_icon = self.country_code.replace("1","")
        country_code_for_icon = country_code_for_icon.replace("2","")

        # Label text and Pixmap
        if self.position <= 9:
            self.number_label.setText(f" {str(self.position)}")
        else:
            self.number_label.setText(str(self.position))
        self.heart_label.setPixmap(QPixmap(f":/images/heart_logos/{country_code_for_icon}.png"))
        self.song_label.setText(f"{self.song} - {self.artist}")

        self.number_label.setFixedWidth(20)

        # If these values change, update find_drop_location in ranking_widget
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setSpacing(3)
        self.h_layout.setAlignment(Qt.AlignLeft)

    def mouseMoveEvent(self, e):
        """
        Handles the mouseMoveEvent when dragging the widget.
        
        :param e: The event object
        """

        ranking_widget = self.parent().parent().parent().parent()
        if e.buttons() == Qt.MouseButton.LeftButton and ranking_widget.allow_dragging:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)

            drag.exec(Qt.DropAction.MoveAction)
    
    def set_data(self, data):
        """
        Sets the data when the widget is dragged.

        :param data: The data to be set.
        """

        self.data = data

class drag_target_indicator(QLabel):
    """
    Dummy widget used as a preview of the location the ranking widget would
    be dropped if the user stopped dragging.
    """

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setContentsMargins(0, 7, 0, 7)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)