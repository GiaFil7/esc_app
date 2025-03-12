from PySide6.QtWidgets import QScrollArea
from utils import round_corners

class rounded_scrollarea(QScrollArea):
    """
    Custom scrollarea with rounded corners.
    """

    def resizeEvent(self, event):
        """
        Handles the cropping of the scrollarea.
        """

        super().resizeEvent(event)
        round_corners(self, 16)