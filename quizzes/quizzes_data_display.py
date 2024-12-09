from PySide6.QtWidgets import QWidget
from ui.ui_quizzes_data_display import Ui_quizzes_data_display

class quizzes_data_display(QWidget, Ui_quizzes_data_display):
    def __init__(self, left_text: str, right_text: str):
        super().__init__()
        self.setupUi(self)

        self.left_label.setText(left_text)
        self.right_label.setText(right_text)