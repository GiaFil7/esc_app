from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QLabel
from PySide6.QtGui import QPixmap, Qt, QColor
from PySide6.QtCore import QTimer
from ui.ui_quizzes_widget import Ui_quizzes_widget
from utils import load_widget, get_country_code, get_quiz_data, update_quiz_data
from utils import get_misc_quiz_entries, get_misc_quiz_data, get_years, resize_table
import re, datetime
from functools import partial
import resources_rc

class quizzes_widget(QWidget, Ui_quizzes_widget):
    """
    The main quiz widget. It displays the needed entries in a table and allows
    the user to play the quiz.

    :param quiz_name: The name of the quiz
    :type quiz_name: str
    :param quiz_type: The type of the quiz (e.g. year, country, misc)
    :type quiz_type: str
    :param parent_menu: The parent menu of the widget
    :type parent_menu: object
    """

    def __init__(self, quiz_name: str, quiz_type: str, parent_menu: object):
        super().__init__()
        self.setupUi(self)

        # Initialise properties
        self.quiz_name = quiz_name
        self.quiz_type = quiz_type
        self.parent_menu = parent_menu
        self.contest_code = self.parent_menu.contest_code
        self.contest_name = self.parent_menu.contest_name
        self.is_paused = True
        self.time = 0

        # Setup slots
        self.back_button.clicked.connect(self.go_back)
        self.play_pause_button.clicked.connect(self.toggle_quiz_state)
        self.give_up_button.clicked.connect(self.end_quiz)
        self.answer_line_edit.textChanged.connect(self.check_answer)
        self.replay_button.clicked.connect(self.replay_quiz)

        # Setup the logo and texts
        self.name_label.setText(quiz_name)

        match self.quiz_type:
            case "country":
                self.country_code = get_country_code(self.quiz_name)
                self.quiz_code = self.country_code
                logo_path = f":/images/heart_logos/{self.country_code}.png"
                desc = f"Can you name all the entries of {quiz_name}?"

            case "year":
                split_text = self.quiz_name.split(" ")
                self.year = split_text[-1]
                self.quiz_code = self.year
                logo_path = f":/images/contest_logos/{self.contest_code}/{self.contest_code}_{self.year}.png"
                desc = f"Can you name all the entries of {quiz_name}?"

            case "misc":
                self.misc_quiz_data = get_misc_quiz_data(self.contest_code)
                misc_data = self.misc_quiz_data[self.misc_quiz_data['quiz_name'] == self.quiz_name]
                self.quiz_code = misc_data['quiz_code'].to_string(header = False, index = False)
                desc = misc_data['desc'].to_string(header = False, index = False)
                logo_path = ":/images/heart_logos/empty_heart.svg"
        
        logo_pixmap = QPixmap(logo_path)
        logo_pixmap = logo_pixmap.scaled(self.logo_label.size(), aspectMode = Qt.KeepAspectRatio, mode = Qt.SmoothTransformation)
        self.logo_label.setPixmap(logo_pixmap)
        self.desc_label.setText(desc)

        # Set a name for objects for styling purposes
        self.name_label.setObjectName("quiz_title")
        self.score_label.setObjectName("quiz_score")
        self.timer_label.setObjectName("quiz_timer")
        self.desc_label.setObjectName("quiz_desc")
        self.answer_line_edit.setObjectName("quiz_field")

        # Keep unnecessary components hidden until needed
        self.give_up_button.hide()
        self.answer_line_edit.hide()
        self.replay_button.hide()

        self.setup_table()

    def go_back(self):
        """
        Loads the parent menu of the widget while updating its data.
        """

        load_widget(self, self.parent_menu)
        self.parent_menu.setup_layout()

    def toggle_quiz_state(self):
        """
        Handles what happens when the play/pause button is clicked.
        """

        # Toggle the is_paused property
        self.is_paused = not(self.is_paused)

        if self.is_paused:
            self.play_pause_button.setIcon(QPixmap(":/images/icons/play_icon.png"))
            self.give_up_button.hide()
            self.answer_line_edit.hide()
            self.table.hide()

            self.timer.stop()
            
            # Display the pause screen
            self.pause_label = QLabel("Paused", parent = self)
            self.pause_label.setObjectName("quiz_pause_text")
            self.pause_label.setAlignment(Qt.AlignCenter)
            self.pause_label.adjustSize()
            self.pause_label.raise_()
            self.pause_label.show()
            self.center_pause_label()
        else:
            self.play_pause_button.setIcon(QPixmap(":/images/icons/pause_icon.png"))
            self.desc_label.hide()
            self.give_up_button.show()
            self.answer_line_edit.show()
            self.table.show()

            if self.time > 0:
                self.pause_label.hide()

            # Setup the timer
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_time)
            self.timer.start(1000)

    def center_pause_label(self):
        """
        Centers the label in the pause menu within the window.
        """

        window_width = self.width()
        window_height = self.height()
        label_width = self.pause_label.width()
        label_height = self.pause_label.height()

        # Calculate the center position
        x = (window_width - label_width) // 2
        y = (window_height - label_height) // 2
        self.pause_label.move(x, y)
        
        self.pause_label.adjustSize()

    def resizeEvent(self, event):
        """
        Handles resizing of the widget.
        """

        if self.is_paused and self.time > 0 and hasattr(self, 'pause_label'):
            self.center_pause_label()
            super().resizeEvent(event)

    def setup_table(self):
        """
        Sets up the table contained in the widget.
        """

        cols, table_data, accepted_answers = self.get_table_data()

        # Initialisations
        self.num_of_entries = len(table_data[0])
        self.score = 0
        self.score_label.setText(f"{self.score}/{self.num_of_entries}")
        self.table = QTableWidget()
        self.table.verticalHeader().setVisible(False)

        # Get the number of groups to split the entries into
        if self.num_of_entries > 10:
            self.col_group_num = 2
            if self.quiz_code == "all":
                self.col_group_num = 4
        else:
            self.col_group_num = 1

        # Get and set the column and row labels and counts
        col_count = len(cols) * self.col_group_num
        col_labels = []
        for _ in range(self.col_group_num):
            col_labels += cols

        row_count = self.num_of_entries // self.col_group_num 
        if self.num_of_entries % row_count != 0:
            row_count = row_count + 1

        self.table.setColumnCount(col_count)
        self.table.setHorizontalHeaderLabels(col_labels)
        self.table.setRowCount(row_count)

        # Store the data required for answer checking and display all data
        # in the table
        self.ans_data = []
        for entry_i in range(self.num_of_entries):
            for entry_j in range(len(cols)):
                table_i = entry_i % row_count
                table_j = (entry_i // row_count) * len(cols) + entry_j
                
                table_inds = [table_i, table_j]
                text = table_data[entry_j][entry_i]

                if table_j % len(cols) == 1:
                    self.ans_data.append([table_i, table_j, text, accepted_answers[entry_i]])
                    text = ""
                
                self.set_table_item(table_inds, text)

        self.scroll_area.setWidget(self.table)

        # Resize the columns to fit the contents
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        # For the "all entries" quiz, merge the first column by year
        if self.quiz_code == "all":
            for j in range(self.table.columnCount()):
                if j % (self.table.columnCount() / self.col_group_num) == 0:
                    year_count = 0
                    curr_text = self.table.item(0, j).text()
                    for i in range(self.table.rowCount()):
                        if self.table.item(i, j) != None:
                            if self.table.item(i, j).text() == curr_text:
                                year_count += 1
                                if i == self.table.rowCount() - 1:
                                    if year_count != 1:
                                        self.table.setSpan(i - year_count + 1, j, year_count, 1)
                                        year_count = 1
                            else:
                                curr_text = self.table.item(i, j).text()
                                if year_count != 1:
                                    self.table.setSpan(i - year_count, j, year_count, 1)
                                    year_count = 1
                        else:
                            if year_count != 1:
                                self.table.setSpan(i - year_count, j, year_count, 1)
                                year_count = 1

        QTimer.singleShot(100, partial(resize_table, self.table))
        self.handle_accepted_answers()
    
    def get_table_data(self) -> tuple[list, list, list]:
        """
        Returns all data needed for setting up the table and for answer
        checking.

        :returns: The column labels, the table data and the accepted answers
        :rtype: tuple[list, list, list]
        """

        entry_data = self.parent_menu.entry_data

        match self.quiz_type:
            case "country":
                cols = ["Year", "Song", "Placing"]
                entries = entry_data[entry_data['country'] == self.quiz_name]

                years = get_years(entries)
                songs = list(entries['song'])
                placings = entries['placing'].astype(str).values.tolist()

                table_data = [years, songs, placings]
                
            case "year":
                contest = f"{self.contest_code} {self.year}"
                cols = ["Country", "Song", "Placing"]

                entries = entry_data[entry_data['contest'] == contest].sort_values(by=['country'])

                countries = list(entries['country'])
                songs = list(entries['song'])
                placings = entries['placing'].astype(str).values.tolist()

                table_data = [countries, songs, placings]

            case "misc":
                cols = ["Year", "Song", "Country"]
                entries = get_misc_quiz_entries(self.contest_code, self.quiz_code)

                years = get_years(entries)
                songs = list(entries['song'])
                countries = list(entries['country'])

                table_data = [years, songs, countries]

        accepted_answers = list(entries['accepted_answers'])

        return cols, table_data, accepted_answers

    def handle_accepted_answers(self):
        """
        Prepares the data needed for answer checking and displaying
        missed answers.
        """

        self.ans_filtered_text = []
        self.ans_table_inds = []
        self.ans_original_text = []
        for entry in self.ans_data:
            entry_answers = entry[-1].split("|")
            for answer in entry_answers:
                self.ans_filtered_text.append(answer)
                self.ans_table_inds.append([entry[0], entry[1]])
                self.ans_original_text.append(entry[2])

    def set_table_item(self, inds: list, text: str):
        """
        Initialises and sets a table item.

        :param inds: The indices of the item
        :type inds: list
        :param text: The text of the item
        :type text: str
        """

        widget_item = QTableWidgetItem(text)
        widget_item.setTextAlignment(Qt.AlignCenter)
        widget_item.setFlags(Qt.ItemIsEnabled)
        self.table.setItem(inds[0], inds[1], widget_item)

    def check_answer(self, answer: str):
        """
        Checks if the text in the line edit is a valid answer. If all answers
        have been guessed, it ends the quiz.

        :param answer: The text of the line edit
        :type answer: str
        """

        modified_answer = self.clean_answer(answer)
        if modified_answer in self.ans_filtered_text:
            inds = [i for i, x in enumerate(self.ans_filtered_text) if x == modified_answer]

            for ind in inds:
                table_ind = self.ans_table_inds[ind]
                item = self.table.item(table_ind[0], table_ind[1])

                if item.text() == "": # If not guessed before
                    item.setText(self.ans_original_text[ind])
                    self.score += 1
                    self.score_label.setText(f"{self.score}/{self.num_of_entries}")

                    # Clear the line edit
                    self.answer_line_edit.setText("")

                    # Resize table
                    resize_table(self.table)

                    # All answers are guessed, end the quiz
                    if self.score == len(self.ans_data):
                        self.end_quiz()

    def clean_answer(self, answer: str) -> str:
        """
        Removes or substitutes special characters from the answer.

        :param answer: The user's answer
        :type answer: str
        """

        modified_answer = answer.lower()
        modified_answer = modified_answer.replace(" ", "")
        modified_answer = re.sub("([àäåáãâăā])", "a", modified_answer)
        modified_answer = modified_answer.replace("æ", "ae")
        modified_answer = re.sub("([çčć])", "c", modified_answer)
        modified_answer = re.sub("([ðđ])", "d", modified_answer)
        modified_answer = re.sub("([éèêėęëə])", "e", modified_answer)
        modified_answer = re.sub("([îìíı])", "i", modified_answer)
        modified_answer = modified_answer.replace("ħ", "h")
        modified_answer = modified_answer.replace("ł", "l")
        modified_answer = re.sub("([ñň])", "n", modified_answer)
        modified_answer = re.sub("([øöóò])", "o", modified_answer)
        modified_answer = modified_answer.replace("œ", "oe")
        modified_answer = re.sub("([şšș])", "s", modified_answer)
        modified_answer = modified_answer.replace("ß", "ss")
        modified_answer = re.sub("([ťț])", "t", modified_answer)
        modified_answer = modified_answer.replace("þ", "th")
        modified_answer = re.sub("([üùú])", "u", modified_answer)
        modified_answer = modified_answer.replace("ý", "y")
        modified_answer = re.sub("([žż])", "z", modified_answer)
        chars_to_remove = ["(", ")", ",", "?", "'", '"', ".", "-", "–", ":", "!", "¿"]
        rx = '[' + re.escape(''.join(chars_to_remove)) + ']'
        modified_answer = re.sub(rx, "", modified_answer)

        return modified_answer

    def update_time(self):
        """
        Increments the quiz timer.
        """

        self.time += 1

        time_value = str(datetime.timedelta(seconds = self.time))
        if self.time < 3600:
            time_value = time_value[-5:]

        self.timer_label.setText(str(time_value))

    def replay_quiz(self):
        """
        Resets the widget to its original state.
        """

        self.setup_table()
        self.replay_button.hide()
        self.play_pause_button.show()
        self.desc_label.show()
        self.time = -1
        self.update_time()
        self.play_pause_button.setIcon(QPixmap(":/images/icons/play_icon.png"))

    def end_quiz(self):
        """
        Handles what happens when the quiz ends.
        """

        # Hide, show or toggle needed components/properties
        self.give_up_button.hide()
        self.play_pause_button.hide()
        self.answer_line_edit.hide()
        self.timer.stop()
        self.replay_button.show()
        self.is_paused = True

        self.quiz_data = get_quiz_data(self.contest_code)

        # Update the user's best score and/or best time if needed
        ind = self.quiz_data.index[self.quiz_data['quiz'] == self.quiz_code].tolist()
        ind = ind[0]
        if self.score > 0: 
            if self.score > self.quiz_data.iloc[ind, 1]:
                self.quiz_data.iloc[ind, 1] = self.score
                self.quiz_data.iloc[ind, 3] = self.time
            elif self.score == self.quiz_data.iloc[ind, 1]:
                if self.time < self.quiz_data.iloc[ind, 3]:
                    self.quiz_data.iloc[ind, 3] = self.time

        update_quiz_data(self.quiz_data, self.contest_code)

        # Reveal any missed answers
        max_score = self.quiz_data.iloc[ind, 2]
        if self.score < max_score:
            for i in range(self.table.rowCount()):
                for j in range(self.table.columnCount()):
                    if j % (self.table.columnCount() / self.col_group_num) == 1:
                        item = self.table.item(i, j)

                        if item != None:
                            if item.text() == "":
                                ind = self.ans_table_inds.index([i, j])
                                item.setText(str(self.ans_original_text[ind]))
                                item.setForeground(QColor(255, 0, 0))
        
        QTimer.singleShot(100, partial(resize_table, self.table))