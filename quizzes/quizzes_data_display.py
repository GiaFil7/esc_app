from PySide6.QtWidgets import QWidget
from ui.ui_quizzes_data_display import Ui_quizzes_data_display

class quizzes_data_display(QWidget, Ui_quizzes_data_display):
    """
    A widget with two labels in a horizontal layout used to display data.

    :param left_text: The text to display on the left label
    :type left_text: str
    :param right_text: The text to display on the right label
    :type right_text: str
    """

    def __init__(self, left_text: str, right_text: str):
        super().__init__()
        self.setupUi(self)

        self.left_label.setText(left_text)
        self.right_label.setText(right_text)