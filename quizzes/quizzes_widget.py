from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from ui.ui_quizzes_widget import Ui_quizzes_widget
from utils import load_widget, get_country_code
from functools import partial
import resources_rc

class quizzes_widget(QWidget, Ui_quizzes_widget):
    def __init__(self, quiz_name: str, quiz_type: str, parent_menu: object):
        super().__init__()
        self.setupUi(self)

        # Initialise properties
        self.quiz_name = quiz_name
        self.quiz_type = quiz_type
        self.contest_code = parent_menu.contest_code
        self.contest_name = parent_menu.contest_name
        self.is_paused = True

        # Setup slots
        self.back_button.clicked.connect(partial(load_widget, self, parent_menu))
        self.play_pause_button.clicked.connect(self.toggle_quiz_state)
        self.give_up_button.clicked.connect(self.end_quiz)

        # Set texts
        self.name_label.setText(quiz_name)
        self.desc_label.setText(f"Can you name all the entries of {quiz_name}?") # Make special cases for misc

        # Setup the logo
        match self.quiz_type:
            case "country":
                country_code = get_country_code(self.quiz_name)
                logo_path = f":/images/heart_logos/{country_code}.png"

            case "year":
                split_text = self.quiz_name.split(" ")
                year = split_text[-1]
                logo_path = f":/images/contest_logos/{self.contest_code}/{self.contest_code}_{year}.png"

            case _:
                logo_path = ":/images/heart_logos/empty_heart.svg"
        
        self.logo_label.setPixmap(QPixmap(logo_path))

        # Keep give up button hidden until the quiz starts
        self.give_up_button.hide()


    def toggle_quiz_state(self):
        self.is_paused = not(self.is_paused)

        if self.is_paused:
            self.play_pause_button.setIcon(QPixmap(":/images/icons/play_icon.png"))
        else:
            self.play_pause_button.setIcon(QPixmap(":/images/icons/pause_icon.png"))

    def end_quiz(self):
        print("Quiz ended")