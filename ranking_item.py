from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap, QDrag
from PySide6.QtCore import QMimeData, Qt
from ui.ui_ranking_item import Ui_ranking_item

import resources_rc

class ranking_item(QWidget, Ui_ranking_item):
    def __init__(self,position,country,song,artist):
        super().__init__()
        self.setupUi(self)

        self.position = position
        self.country = country
        self.song = song
        self.artist = artist

        # Remove 1 and 2 from country code for 1956
        country_code_for_icon = self.country.replace("1","")
        country_code_for_icon = country_code_for_icon.replace("2","")

        self.number_label.setText(str(self.position))
        self.heart_label.setPixmap(QPixmap(f":/images/heart_logos/{country_code_for_icon}.png"))
        self.song_label.setText(f"{self.song} - {self.artist}")

        # If these values change, update find_drop_location in ranking_widget
        self.horizontalLayout.setContentsMargins(0,3,0,3)
        self.number_label.setContentsMargins(0,0,3,0)
        self.song_label.setContentsMargins(3,0,0,0)

    def mouseMoveEvent(self, e):
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
        self.data = data

class DragTargetIndicator(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContentsMargins(25, 5, 25, 5)
        self.setStyleSheet(
            "QLabel { background-color: #ccc; border: 1px solid black; }"
        )
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)