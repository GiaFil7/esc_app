from PySide6.QtWidgets import QDialog
from ui.ui_confirm_dialog import Ui_confirm_dialog

class confirm_dialog(QDialog, Ui_confirm_dialog):
    """
    A dialog box asking the user to confirm if they want to go back.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)