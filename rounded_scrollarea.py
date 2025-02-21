from PySide6.QtWidgets import QScrollArea
from PySide6.QtGui import QRegion, QPainterPath
from PySide6.QtCore import QRect

class rounded_scrollarea(QScrollArea):
    """
    Custom scrollarea with rounded corners.
    """

    def resizeEvent(self, event):
        """
        Handles the cropping of the scrollarea.
        """

        super().resizeEvent(event)
        path = QPainterPath()
        path.addRoundedRect(QRect(0, 0, self.width(), self.height()), 16, 16)
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)
