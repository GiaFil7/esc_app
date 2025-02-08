from PySide6.QtWidgets import QWidget
from ui.ui_rankings_image import Ui_rankings_image

class rankings_image(QWidget, Ui_rankings_image):
    """
    A helper widget to save a ranking as an image. It contains two
    columns with the entries in the order of the ranking.

    :param contest_name: the full name and year of the contest
    :type contest_name: str
    """

    def __init__(self, contest_name: str):
        super().__init__()
        self.setupUi(self)

        self.title_label.setText(contest_name)
        self.title_label.setObjectName("img_title")