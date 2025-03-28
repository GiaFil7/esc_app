from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import Qt, QPixmap
from PySide6.QtCore import QTimer
from ui.ui_quizzes_list_menu import Ui_quizzes_list_menu
from rankings.rankings_menu_item import rankings_menu_item
from quizzes.quizzes_widget import quizzes_widget
from quizzes.quizzes_data_display import quizzes_data_display
from utils import load_widget, get_countries, get_entry_data, get_country_code
from utils import get_contest_data, get_quiz_data, get_misc_quiz_data
from utils import resize_scrollarea
from functools import partial
import datetime
import resources_rc

class quizzes_list_menu(QWidget, Ui_quizzes_list_menu):
    """
    A menu that allows the user to navigate to all quizzes of a specific
    category and back to the main contest menu.

    :param menu_type: The type of menu
    :type menu_type: str
    :param contest_main_menu: The main contest menu (previous menu)
    :type contest_main_menu: object
    """

    def __init__(self, menu_type: str, contest_main_menu: object):
        super().__init__()
        self.setupUi(self)

        # Initialise properties
        self.menu_type = menu_type
        self.contest_code = contest_main_menu.contest_code
        self.contest_name = contest_main_menu.contest_name
        self.entry_data = get_entry_data(self.contest_code)
        self.contest_data = get_contest_data(self.contest_code)
        
        self.back_button.setObjectName("button_small")
        self.back_button.clicked.connect(partial(load_widget, self, contest_main_menu))

        # Set text
        match self.menu_type:
            case "by_country":
                text = "Quizzes by Country"

            case "by_year":
                text = "Quizzes by Year"

            case "misc":
                text = "Miscellaneous Quizzes"

        self.name_label.setText(text)
        self.name_label.setObjectName("widget_title")
        self.logo_label.setPixmap(QPixmap(f":/images/contest_logos/{self.contest_code}/{self.contest_code}.png"))
        self.scroll_area.setObjectName("quizzes_list_menu_scrollarea")

        self.setup_layout()
    
    def load_quiz(self, quiz_name: str, quiz_type: str):
        """
        Loads the specified quiz.

        :param quiz_name: The name of the quiz
        :type quiz_name: str
        :param quiz_type: The type of the quiz (country, year or misc)
        :type quiz_type: str
        """

        load_widget(self, quizzes_widget(quiz_name, quiz_type, self))

    def add_item(self, logo_path: str, quiz_name: str, quiz_type: str,
                 best_score: str, best_time: str, quiz_code: str):
        """
        Add a new item to the menu that when clicked loads the proper quiz.

        :param logo_path: The logo path
        :type logo_path: str
        :param quiz_name: The name of the quiz
        :type quiz_name: str
        :param quiz_type: The type of the quiz
        :type quiz_type: str
        :param best_score: The user's best score for the quiz
        :type best_score: str
        :param best_time: The user's best time for the quiz
        :type best_time: str
        :param quiz_code: The quiz code
        :type quiz_code: str
        """
        
        # Initialise the item
        item = rankings_menu_item(quiz_name, logo = logo_path)
        item.main_layout.removeWidget(item.submitted_label)
        item.submitted_label.deleteLater()
        item.submitted_label = None
        item.setFixedWidth(300)
        item.clicked.connect(partial(self.load_quiz, quiz_name, quiz_type))

        # Setup a horizontal layout with the item and an data display widget
        item_layout = QHBoxLayout()
        item_layout.addWidget(item)
        item_layout.addStretch(1)

        score_and_time_widget = quizzes_data_display(best_score, best_time)
        score_and_time_widget.setObjectName(str(quiz_code))
        item_layout.addWidget(score_and_time_widget)
        item_layout.setContentsMargins(0, 0, 0, 0)

        # Create a widget for the created layout and add to the menu layout
        widget = QWidget(parent = self)
        widget.setLayout(item_layout)
        widget.setFixedWidth(650)
        widget.setAttribute(Qt.WA_StyledBackground, True)
        widget.setObjectName("quizzes_list_menu_item")
        self.layout.addWidget(widget)

    def get_score_and_time(self, quiz_code: str) -> tuple[str, str]:
        """
        Gets the user's best score and time for a quiz with the proper format.
        It also adds these values to the menu's total.

        :param quiz_code: The quiz code
        :type quiz_code: str
        :returns: The user's best score and time
        :rtype: tuple[str, str]
        """

        # Get data
        quiz_row = self.quiz_data[self.quiz_data['quiz'] == quiz_code]
        best_score = int(quiz_row['best_score'].iloc[0])
        max_score = int(quiz_row['max_score'].iloc[0])
        best_time = int(quiz_row['best_time'].iloc[0])

        # Add score and time to the totals
        self.total_max_score += max_score
        self.total_best_score += best_score
        if best_score > 0:
            self.total_best_time += best_time

        # Convert seconds to timedelta
        time_value = str(datetime.timedelta(seconds = best_time))
        if best_time < 36000:
            time_value = time_value[-5:]
        
        percentage = round((best_score / max_score) * 100)

        # Set the texts for the best score and time
        if best_score > 0:
            best_score_text = f"Best score: {best_score}/{max_score} ({percentage}%)"
            best_time_text = f"Best time: {time_value}"
        else:
            best_score_text = "No score set."
            best_time_text = "No time set."

        return best_score_text, best_time_text
    
    def setup_layout(self):
        """
        Sets up the layout of the menu and displays the user's total score and
        time for the menu's quiz type.
        """

        # Get quiz data and initialise values
        self.quiz_data = get_quiz_data(self.contest_code)
        self.total_max_score = 0
        self.total_best_score = 0
        self.total_best_time = 0

        # Setup menu items
        self.layout = QVBoxLayout()
        match self.menu_type:
            case "by_country":
                countries = get_countries(self.entry_data)

                self.quiz_codes = []
                for country in countries:
                    country_code = get_country_code(country)
                    self.quiz_codes.append(country_code)

                    logo_path = f":/images/heart_logos/{country_code}.png"

                    best_score_text, best_time_text = self.get_score_and_time(country_code)

                    self.add_item(logo_path, country, "country", best_score_text, best_time_text, country_code)

            case "by_year":
                years = list(self.contest_data['year'])
                self.quiz_codes = years

                for year in years:
                    logo_path = f":/images/contest_logos/{self.contest_code}/{self.contest_code}_{year}.png"

                    best_score_text, best_time_text = self.get_score_and_time(year)

                    self.add_item(logo_path, f"{self.contest_name} {year}", "year", best_score_text, best_time_text, year)

            case "misc":
                self.misc_quiz_data = get_misc_quiz_data(self.contest_code)
                quiz_names = list(self.misc_quiz_data['quiz_name'])
                self.quiz_codes = list(self.misc_quiz_data['quiz_code'])
                logo_path = ":/images/heart_logos/empty_heart.png"
                
                for i, quiz_title in enumerate(quiz_names):
                    best_score_text, best_time_text = self.get_score_and_time(self.quiz_codes[i])
                    self.add_item(logo_path, quiz_title, "misc", best_score_text, best_time_text, self.quiz_codes[i])

                # Add a dummy item and hide it to account for the removal of 
                # the drag indicator when the resize_scrollarea is used for
                # rankings.
                self.add_item(logo_path, "", "misc", "", "", "")
                dummy_item = self.layout.itemAt(self.layout.count() - 1).widget()
                dummy_item.hide()
        
        self.layout.setSpacing(10)
        self.layout.setAlignment(Qt.AlignTop)

        # Create a temporary widget to set the layout onto the scroll area
        self.scroll_widget = QWidget(parent = self)
        self.scroll_widget.setObjectName("scroll_widget")
        self.scroll_widget.setLayout(self.layout)
        self.scroll_area.setWidget(self.scroll_widget)

        self.align_labels()
        QTimer.singleShot(20, partial(resize_scrollarea, self.scroll_area, self.layout, 10))
        self.verticalLayout.setAlignment(Qt.AlignTop)

        self.display_totals()

    def align_labels(self):
        """
        Aligns the labels for best score and time.
        """

        # Get the biggest width for the left and right labels
        left_labels = []
        right_labels = []
        max_left = 0
        max_right = 0
        for i in range(self.layout.count()):
            item = self.layout.itemAt(i).widget()

            left_label = item.findChild(QLabel, "left_label")
            left_label.adjustSize()
            left_labels.append(left_label)

            right_label = item.findChild(QLabel, "right_label")
            right_label.adjustSize()
            right_labels.append(right_label)

            if left_label.width() > max_left:
                max_left = left_label.width()

            if right_label.width() > max_right:
                max_right = right_label.width()
        
        # Apply uniform width to the labels
        for i in range(self.layout.count()):
            left_labels[i].setFixedWidth(max_left)
            left_labels[i].adjustSize()

            right_labels[i].setFixedWidth(max_right)
            right_labels[i].adjustSize()

            item = self.layout.itemAt(i).widget()
            item.setContentsMargins(0, 0, 5, 0)
    
    def display_totals(self):
        """
        Displays the total score and time.
        """

        if self.menu_type != "misc":
            total_time_value = str(datetime.timedelta(seconds = self.total_best_time))
            if self.total_best_time < 3600:
                total_time_value = total_time_value[-5:]
        
            percentage = round((self.total_best_score / self.total_max_score) * 100)

            text = f"Total score: {self.total_best_score}/{self.total_max_score} ({percentage}%) | Total time: {total_time_value}"
        else:
            text = ""
        
        self.totals_label.setText(text)

    def update_data(self):
        """
        Updates the data shown on quizzes_data_display widgets and the total
        score and time.
        """

        # Get quiz data and initialise values
        self.quiz_data = get_quiz_data(self.contest_code)
        self.total_max_score = 0
        self.total_best_score = 0
        self.total_best_time = 0

        # Update labels based on the new data
        for quiz_code in self.quiz_codes:
            best_score, best_time = self.get_score_and_time(quiz_code)
            data_display = self.findChild(quizzes_data_display, str(quiz_code))

            data_display.left_label.setText(best_score)
            data_display.right_label.setText(best_time)

            data_display.left_label.adjustSize()
            data_display.right_label.adjustSize()
                    
        self.display_totals()