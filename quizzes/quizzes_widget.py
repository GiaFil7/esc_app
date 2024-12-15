from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QLabel
from PySide6.QtGui import QPixmap, Qt, QColor
from PySide6.QtCore import QTimer
from ui.ui_quizzes_widget import Ui_quizzes_widget
from utils import load_widget, get_country_code, get_quiz_data, update_quiz_data
from utils import get_misc_quiz_entries, get_misc_quiz_data
import re, datetime
import resources_rc

class quizzes_widget(QWidget, Ui_quizzes_widget):
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

        # Keep unnecessary components hidden until needed
        self.give_up_button.hide()
        self.answer_line_edit.hide()
        self.replay_button.hide()

        self.setup_table()

    def go_back(self):
        load_widget(self, self.parent_menu)
        self.parent_menu.setup_layout()

    def toggle_quiz_state(self):
        self.is_paused = not(self.is_paused)

        if self.is_paused:
            self.play_pause_button.setIcon(QPixmap(":/images/icons/play_icon.png"))
            self.give_up_button.hide()
            self.answer_line_edit.hide()
            self.table.hide()

            self.timer.stop()

            self.pause_label = QLabel("Paused", parent = self)
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

            self.timer = QTimer()
            self.timer.timeout.connect(self.update_time)
            self.timer.start(1000)

    def center_pause_label(self):
        window_width = self.width()
        window_height = self.height()
        label_width = self.pause_label.width()
        label_height = self.pause_label.height()

        # Calculate the center position
        x = (window_width - label_width) // 2
        y = (window_height - label_height) // 2
        self.pause_label.move(x, y)

        # Ensure the label's sizeHint is considered
        self.pause_label.adjustSize()

    def resizeEvent(self, event):
        if self.is_paused and self.time > 0:
            self.center_pause_label()
            super().resizeEvent(event)

    def end_quiz(self):
        self.give_up_button.hide()
        self.play_pause_button.hide()
        self.answer_line_edit.hide()
        self.replay_button.show()
        self.timer.stop()
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
                item = self.table.item(i, 1)
                if item != None:
                    if item.text() == "":
                        ind = self.ans_inds.index([i, 1])
                        item.setText(self.songs[ind])
                        item.setForeground(QColor(255, 0, 0))
                
                if self.num_of_entries > 10:
                    item = self.table.item(i, 4)
                    if item != None:
                        if item.text() == "":
                            ind = self.ans_inds.index([i, 4])
                            item.setText(str(self.songs[ind]))
                            item.setForeground(QColor(255, 0, 0))

    def setup_table(self):
        cols, table_data, accepted_answers = self.get_table_data()

        self.num_of_entries = len(table_data[0])
        self.score = 0
        self.score_label.setText(f"{self.score}/{self.num_of_entries}")
        self.table = QTableWidget()
        self.table.verticalHeader().setVisible(False)

        self.ans_data = []
        if self.num_of_entries > 10:
            self.table.setColumnCount(len(cols) * 2)
            self.table.setHorizontalHeaderLabels(cols + cols)
            if len(table_data[0]) % 2 == 0:
                self.table.setRowCount(self.num_of_entries / 2)
            else:
                self.table.setRowCount(0.5 + self.num_of_entries / 2)

            row_count = self.table.rowCount()
            for i in range(self.num_of_entries):
                for j in range(len(cols)):
                    row_ind = i % row_count
                    if i <= ((self.num_of_entries - 1) / 2):
                        col_ind = j
                    else:
                        col_ind = j + len(cols)

                    inds = [row_ind, col_ind]
                    text = table_data[j][i]

                    if j == 1:
                        self.ans_data.append([row_ind, col_ind, text, accepted_answers[i]])
                        text = ""

                    self.set_table_item(inds, text)
        else:
            self.table.setColumnCount(len(cols))
            self.table.setHorizontalHeaderLabels(cols)
            self.table.setRowCount(self.num_of_entries)

            row_count = self.table.rowCount()
            for i in range(self.num_of_entries):
                for j in range(len(cols)):
                    inds = [i, j]
                    text = table_data[j][i]

                    if j == 1:
                        self.ans_data.append([i, j, text, accepted_answers[i]])
                        text = ""

                    self.set_table_item(inds, text)

        self.scroll_area.setWidget(self.table)

        # Resize the columns to fit the contents
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        # For the "all entries" quiz, merge the first column by year
        if self.quiz_code == "all":
            row_count = self.table.rowCount()
            m_cols = [0, 3]
            
            for col in m_cols:
                total_count = 0
                year_count = 0
                
                while total_count < row_count:
                    curr_text = self.table.item(total_count, col).text()
                    while self.table.item(total_count + year_count, col).text() == curr_text:
                        year_count += 1

                        if self.table.item(total_count + year_count, col) == None:
                            break
                    
                    self.table.setSpan(total_count, col, year_count, 1)
                    total_count += year_count
                    year_count = 0

        self.handle_accepted_answers()
    
    def get_table_data(self):
        entry_data = self.parent_menu.entry_data

        match self.quiz_type:
            case "country":
                cols = ["Year", "Song", "Placing"]
                entries = entry_data[entry_data['country'] == self.quiz_name]
                
                years = entries['contest'].to_string(index = False)
                years = years.split("\n")
                years = [item.split(" ") for item in years]
                years = [item[1] for item in years]

                songs = list(entries['song'])
                placings = entries['placing'].astype(str).values.tolist()

                table_data = [years, songs, placings]
                
            case "year":
                cols = ["Country", "Song", "Placing"]
                contest = f"{self.contest_code} {self.year}"
                entries = entry_data[entry_data['contest'] == contest].sort_values(by=['country'])

                countries = list(entries['country'])
                songs = list(entries['song'])
                placings = entries['placing'].astype(str).values.tolist()

                table_data = [countries, songs, placings]

            case "misc":
                entries = get_misc_quiz_entries(self.contest_code, self.quiz_code)
                years = entries['contest'].to_string(index = False)
                years = years.split("\n")
                years = [item.split(" ") for item in years]
                years = [item[1] for item in years]
                songs = list(entries['song'])
                countries = list(entries['country'])

                cols = ["Year", "Song", "Country"]
                table_data = [years, songs, countries]

        accepted_answers = list(entries['accepted_answers'])

        return cols, table_data, accepted_answers

    def handle_accepted_answers(self):
        self.ans_text = []
        self.ans_inds = []
        self.songs = []
        for entry in self.ans_data:
            entry_answers = entry[-1].split("|")
            for answer in entry_answers:
                self.ans_text.append(answer)
                self.ans_inds.append([entry[0], entry[1]])
                self.songs.append(entry[2])

    def set_table_item(self, inds: list, text: str):
        widget_item = QTableWidgetItem(text)
        widget_item.setTextAlignment(Qt.AlignCenter)
        widget_item.setFlags(Qt.ItemIsEnabled)
        self.table.setItem(inds[0], inds[1], widget_item)

    def check_answer(self, answer: str):
        modified_answer = self.clean_answer(answer)
        if modified_answer in self.ans_text:
            inds = [i for i,x in enumerate(self.ans_text) if x == modified_answer]

            for ind in inds:
                table_ind = self.ans_inds[ind]
                item = self.table.item(table_ind[0], table_ind[1])

                if item.text() == "": # If not guessed before
                    item.setText(self.songs[ind])
                    self.score += 1
                    self.score_label.setText(f"{self.score}/{self.num_of_entries}")

                    # Clear the line edit
                    self.answer_line_edit.setText("")

                    # All answers are guessed, end the quiz
                    if self.score == len(self.ans_data):
                        self.end_quiz()

    def clean_answer(self, answer: str) -> str:
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
        self.time += 1

        time_value = str(datetime.timedelta(seconds = self.time))
        if self.time < 3600:
            time_value = time_value[-5:]

        self.timer_label.setText(str(time_value))

    def replay_quiz(self):
        self.setup_table()
        self.replay_button.hide()
        self.play_pause_button.show()
        self.desc_label.show()
        self.time = -1
        self.update_time()
        self.play_pause_button.setIcon(QPixmap(":/images/icons/play_icon.png"))