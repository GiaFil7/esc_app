from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, Qt
from ui.ui_ranking_widget import Ui_ranking_widget
from rankings.ranking_item import ranking_item, drag_target_indicator
from rankings.ranking_import_export import ranking_import_export
from rankings.rankings_image import rankings_image
from rankings.confirm_dialog import confirm_dialog
from functools import partial
from typing import List
from utils import load_widget, read_html_file, save_widget_to_file
from utils import get_contest_data, update_contest_data
from utils import get_entry_data, update_entry_data
import pandas as pd
import resources_rc

class ranking_widget(QWidget, Ui_ranking_widget):
    """
    Widget that displays the user's ranking for a particular year. It allows for
    reordering of the entries, import and exporting the ranking, as well as save
    it on the app. It also allows the user to see their ranking for each show in
    the year (Semi-Finals and Grand Final).

    :param year: The year of the ranking
    :type year: int
    :param by_year_widget: A rankings_by_year widget (previous menu of this widget)
    :type by_year_widget: object
    """

    orderChanged = Signal(list)

    def __init__(self, year: int, by_year_widget: object):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)

        # Setup the properties
        self.year = year
        self.is_info_visible = False
        self.allow_dragging = True
        self.previous_combo_box_text = self.show_combo_box.currentText()
        self.contest_code = by_year_widget.contest_code
        self.by_year_widget = by_year_widget
        self.contest_name = by_year_widget.contest_name

        # Setup the slots
        self.info_button.clicked.connect(self.toggle_info)
        self.import_export_button.clicked.connect(self.open_import_export_dialog)
        self.save_button.clicked.connect(self.save_ranking_to_file)
        self.show_combo_box.currentTextChanged.connect(self.text_changed)
        self.save_img_button.clicked.connect(self.save_img)
        self.back_button.clicked.connect(partial(self.go_back, self.by_year_widget))

        self.logo_path = f":/images/contest_logos/{self.contest_code}/{self.contest_code}_{self.year}.png"

        logo_pixmap = QPixmap(self.logo_path)
        logo_pixmap = logo_pixmap.scaled(self.logo_label.size(), aspectMode = Qt.KeepAspectRatio, mode = Qt.SmoothTransformation)
        self.logo_label.setPixmap(logo_pixmap)
        self.year_label.setText(f"{self.contest_name} {str(self.year)}")

        self.get_ranking_data()

        self.setup_ranking_items(self.ranking, self.songs, self.artists)

        # Add the appropriate combo box items according to the year. If none, hide it.
        if self.contest_code == "ESC":
            if year <= 2003:
                self.show_combo_box.hide()
            elif year <= 2008:
                self.show_combo_box.addItems(["Full Ranking", "Semi-Final", "Grand Final"])
            else:
                self.show_combo_box.addItems(["Full Ranking", "Semi-Final 1", "Semi-Final 2", "Grand Final"])

    def get_ranking_data(self):
        """
        Gets songs, artists and the user's ranking for the ranking widget's contest and year.
        """

        data = get_entry_data(self.contest_code)
        self.contest_and_year = f"{self.contest_code} {str(self.year)}"
        self.entries = data[data['contest'] == self.contest_and_year]

        self.songs = list(self.entries['song'])
        self.artists = list(self.entries['artist'])
        self.ranking = list(self.entries['country_code'])

    def toggle_info(self):
        """
        Toggles a QLabel widget used to display information about the ranking
        to the user.
        """

        if not self.is_info_visible:
            # Get the help file and read it   
            if self.contest_and_year != "ESC 1956":
                help_file = f"files\\help_ranking_{self.contest_code}.html"
            else:
                help_file = "files\\help_ranking_ESC_1956.html"

            html_as_string = read_html_file(help_file)

            # Create a QLabel widget and display the info to the user
            self.info_label = QLabel()
            self.info_label.setText(html_as_string)
            self.info_label.setAlignment(Qt.AlignTop)
            self.main_layout.addWidget(self.info_label)

            # Hide all unneeded widgets
            self.entry_scroll_area.hide()
            self.import_export_button.hide()
            self.save_button.hide()
            self.back_button.hide()
            self.show_combo_box.hide()
            self.vertical_line.hide()

            # Repurpose the info button as a close button for the info
            self.info_button.setIcon(QPixmap(":/images/icons/close_icon.png"))

            self.is_info_visible = True
        else:
            # Show hidden widgets and hide the info label
            self.entry_scroll_area.show()
            self.import_export_button.show()
            self.save_button.show()
            self.back_button.show()

            if not (self.contest_code == "ESC" and self.year <= 2003):
                self.show_combo_box.show()
            
            self.vertical_line.show()
            self.info_label.hide()

            self.info_button.setIcon(QPixmap(":/images/icons/help_icon.png"))
            self.is_info_visible = False

    def open_import_export_dialog(self):
        """
        Records the ranking the user set by dragging the ranking items and
        displays the import/export widget.
        """

        self.update_ranking()
        self.dialog = ranking_import_export(self.ranking, self.entries)
        self.dialog.setParent(self, Qt.Dialog)
        self.dialog.show()

    def update_ranking(self):
        """
        Updates the entries, songs and artists properties of the widget
        according to the order set by the user by dragging the ranking
        items.
        """

        # Get the new order
        new_ranking = []
        c = 0
        for n in range(self.layout.count()):
            c = c + 1
            w = self.layout.itemAt(n).widget()
            if hasattr(w,'number_label'):
                new_ranking.append(w.country_code)
            else:
                # Ignore the drag_target_indicator widget
                c = c - 1
        
        self.ranking = new_ranking

        # Reorder the entries property DataFrame
        old_index = self.entries.index
        new_order = self.entries.set_index(self.entries['country_code'])
        self.entries = new_order.reindex(self.ranking)
        self.entries = self.entries.set_index(old_index)

        self.songs = list(self.entries['song'])
        self.artists = list(self.entries['artist'])

    def save_ranking_to_file(self):
        """
        Saves the user's ranking to file.
        """

        self.update_ranking()
        update_entry_data(self.entries, self.contest_code)

        # Get the index of the year in contest_data
        contest_data = get_contest_data(self.contest_code)
        ind = contest_data.index[contest_data['year'] == self.year].tolist()
        ind = ind[0]

        # If the user hadn't submitted a ranking for the ranking widget's year,
        # update the contest_data
        if contest_data.iloc[ind, 2] == False:
            contest_data.iloc[ind, 2] = True
            update_contest_data(contest_data)

            print(f"New year submitted: {self.year}")

        print("Saved")

    def text_changed(self, text: str):
        """
        Handler for when the combo box text changes. It displays the
        appropriate items depeding on the option selected by the user.

        :param text: The combo box text of the selected option
        :type text: str
        """

        # If the user selects the same option as already selected, do nothing
        if self.previous_combo_box_text == text:
            return

        # Update the widgets properties with the new ranking
        if self.previous_combo_box_text == "Full Ranking":
            self.update_ranking()

        # Only allow dragging of items when viewing the full ranking
        if text == "Full Ranking":
            self.allow_dragging = True
        else:
            self.allow_dragging = False

        # Handle the options per Eurovision year
        if self.contest_code == "ESC":
            # Get the semi-finalists
            if self.year <= 2007:
                semi_finalists = self.entries[self.entries['show'] == "SF"]
            else:
                semi_finalists_1 = self.entries[self.entries['show'] == "SF1"]
                semi_finalists_2 = self.entries[self.entries['show'] == "SF2"]
            
            # Keep the original order of the entries in a temporary column
            self.entries['original_order'] = range(len(self.entries))

            # Get the entries that need to be displayed
            if text == "Semi-Final":
                entries_to_show = semi_finalists
            elif text == "Semi-Final 1":
                entries_to_show = semi_finalists_1
            elif text == "Semi-Final 2":
                entries_to_show = semi_finalists_2
            elif text == "Grand Final":
                automatic = self.entries[self.entries['show'] == "GF"]

                # Find the qualifiers from each show
                if self.year <= 2007:
                    qualifiers = semi_finalists.iloc[:10]
                else:
                    qualifiers_1 = semi_finalists_1.iloc[:10]
                    qualifiers_2 = semi_finalists_2.iloc[:10]
                    qualifiers = pd.concat([qualifiers_1, qualifiers_2])
                
                entries_to_show = pd.concat([qualifiers, automatic]).sort_values(by='original_order')
            else:
                entries_to_show = self.entries

        # Remove the temporary column
        entries_to_show = entries_to_show.drop(columns='original_order').reset_index(drop=True)

        # Display the items
        self.setup_ranking_items(list(entries_to_show['country_code']), list(entries_to_show['song']), list(entries_to_show['artist']))
        
        self.previous_combo_box_text = text

    def save_img(self):
        """
        Saves the ranking as an image, at the location and with the name
        specified by the user.
        """

        # Initialise the rankings_image widget
        image_widget = rankings_image(f"{self.contest_name} {self.year}")
        image_widget.left_layout.setAlignment(Qt.AlignTop)
        image_widget.right_layout.setAlignment(Qt.AlignTop)

        c = 0
        for n in range(self.layout.count()):
            c += 1

            # Get the ranking item at each index
            w = self.layout.itemAt(n).widget()

            if hasattr(w,'number_label'):
                # Reinitialise the ranking item
                song_and_artist = w.song_label.text().split(" - ")
                song = song_and_artist[0]
                pos = int(w.number_label.text())
                item = ranking_item(pos, w.country_code, song, " ")
                item.song_label.setText(song)

                # Determine which layout should the item be placed in
                if c / self.layout.count() <= 0.5:
                    image_widget.left_layout.addWidget(item)
                else:
                    image_widget.right_layout.addWidget(item)

                image_widget.adjustSize()
            else:
                # Ignore drag_target_indicator widget
                c -= 1

        save_widget_to_file(self, image_widget, 0.75)

    def go_back(self, by_year_widget: object):
        """
        Displays a dialog confirming if the user is sure about going back. If
        the user selects "OK", then it loads the ranking_by_year widget and
        updates the Pixmaps of its menu items according to if the user has
        submitted a ranking.

        :param by_year_widget: A rankings_by_year widget (previous menu of this widget)
        :type by_year_widget: object
        """

        # Initialise the dialog box
        dlg = confirm_dialog()
        chosen_button = dlg.exec()

        # Check if user selected "OK"
        if chosen_button == 1:
            load_widget(self, by_year_widget)

            by_year_widget.update_submitted_status(by_year_widget)
            self.stacked_widget.removeWidget(self)

    def setup_ranking_items(self, ranking: List[str], songs: List[str], artists: List[str]):
        """
        Creates a layout that contains ranking items based on the order in the
        user's ranking.

        :param ranking: A list of country codes reflecting the user's ranking of the songs
        :type ranking: List[str]
        :param songs: A list of the song titles in the order of the ranking
        :type songs: List[str]
        :param artists: A list of the artists in the order of the ranking
        :type artists: List[str]
        """

        # Setup the layout
        self.layout = QVBoxLayout()
        for i in range(len(ranking)):
            country = str(ranking[i])
            song = str(songs[i])
            artist = str(artists[i])

            entry = ranking_item(i+1, country, song, artist)
            entry.set_data(i)
            self.layout.addWidget(entry)

        self.item_height = self.layout.itemAt(0).widget().heart_label.height()

        self.layout.setSpacing(0)
        self.scroll_bar = self.entry_scroll_area.verticalScrollBar()
        self.scroll_bar.setSingleStep(self.item_height)

        self.title_layout.setSpacing(0)
        
        # Setup the temporary dragging widget
        self.drag_target_indicator = drag_target_indicator()
        self.layout.addWidget(self.drag_target_indicator)
        self.drag_target_indicator.hide()

        # Create a temporary widget to set the layout onto the scroll area
        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.layout)
        self.scroll_widget.setContentsMargins(0, 0, 0, 0)

        self.entry_scroll_area.setWidget(self.scroll_widget)
        self.entry_scroll_area.setContentsMargins(0, 0, 0, 0)

    def dragEnterEvent(self, e):
        """
        Accepts the drag event.

        :param e: The event object
        """

        e.accept()

    def dragLeaveEvent(self, e):
        """
        Handles dragging outside the widget's area.

        :param e: The event object
        """
        
        self.drag_target_indicator.hide()
        e.accept()

    def dropEvent(self, e):
        """
        When the user lets go of left click, it drops the dragged item on the
        location of the drag_target_indicator widget.

        :param e: The event object
        """

        widget = e.source()

        # Use drop target location for destination, then remove it.
        self.drag_target_indicator.hide()
        index = self.layout.indexOf(self.drag_target_indicator)
        if index is not None:
            self.layout.insertWidget(index, widget)
            self.orderChanged.emit(self.get_item_data())
            widget.show()
            self.layout.activate()
        e.accept()

        # Update entry numbering
        c = 0
        for n in range(self.layout.count()):
            # Get the widget at each index
            c = c + 1
            w = self.layout.itemAt(n).widget()
            if hasattr(w,'number_label'):
                if c <=9:
                    w.number_label.setText(f" {str(c)}")
                else:
                    w.number_label.setText(str(c))
            else:
                # Ignore the drag_target_indicator widget
                c = c - 1
    
    def dragMoveEvent(self, e):
        """
        Handles what happens during dragging of an item.

        :param e: The event object
        """

        # Scroll up or down if dragging to top or bottom of the scroll area
        pos = e.position()
        if pos.y() <= self.logo_label.height() and self.scroll_bar.value() > self.scroll_bar.minimum():
            self.scroll_bar.setValue( self.scroll_bar.value() - 5)
        elif pos.y() >= self.entry_scroll_area.height() and self.scroll_bar.value() < self.scroll_bar.maximum():
            self.scroll_bar.setValue( self.scroll_bar.value() + 5)


        # Find the correct location of the drop target
        index = self.find_drop_location(e)
        if index is not None:
            # Inserting moves the item if its alreaady in the layout
            self.layout.insertWidget(index, self.drag_target_indicator)

            # Hide the item being dragged
            e.source().hide()
            
            # Show the target
            self.drag_target_indicator.show()
        e.accept()

    def find_drop_location(self, e) -> int:
        """
        Calculates the drop location of the dragged item and returns its index.

        :param e: The event object
        :returns: The index of the drop location
        :rtype: int
        """

        pos = e.position()
        spacing = 2

        count_visible = 0
        for n in range(self.layout.count()):
            # Get the widget at each index
            w = self.layout.itemAt(n).widget()

            # Get only the visible items and account for the top one being
            # only partially visible
            extra = 0
            if w.visibleRegion().isEmpty():
                continue
            elif hasattr(w,"heart_label"):
                rect = w.visibleRegion().boundingRect()

                if rect.height() != w.heart_label.height():
                    extra = w.heart_label.height() - rect.height()
                else:
                    extra = 0

                count_visible = count_visible + 1

            # Calculate the drop location
            loc = count_visible * (self.item_height + 6) + self.logo_label.height() + extra

            # Check if the drop location is valid
            drop_here = (
                pos.y() >= loc - spacing
                and pos.y() <= loc + w.size().height() + spacing
            )

            if drop_here:
                # Drop over this target.
                break
        
        return n
    
    def get_item_data(self) -> list:
        """
        Gets the data of the items in the layout.

        :returns: The data of the items in the layout
        :rtype: list
        """

        data = []
        for n in range(self.layout.count()):
            # Get the widget at each index
            w = self.layout.itemAt(n).widget()
            if w != self.drag_target_indicator:
                # The target indicator has no data
                data.append(w.data)
        return data