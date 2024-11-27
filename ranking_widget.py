from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap,Qt
from ui.ui_ranking_widget import Ui_ranking_widget
from ranking_item import ranking_item,DragTargetIndicator
from ranking_import_export import ranking_import_export
from functools import partial
from utils import load_widget,get_contest_data,update_contest_data
import pandas as pd # type: ignore
import resources_rc

class ranking_widget(QWidget, Ui_ranking_widget):
    orderChanged = Signal(list)

    def __init__(self,year,by_year_widget):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
 
        self.year = year
        self.is_info_visible = False
        self.allow_dragging = True
        self.previous_combo_box_text = self.show_combo_box.currentText()
        self.contest_code = by_year_widget.contest_code
        self.by_year_widget = by_year_widget
        self.contest_name = by_year_widget.contest_name

        self.info_button.pressed.connect(self.toggle_info)
        self.import_export_button.pressed.connect(self.open_import_export_dialog)
        self.save_button.pressed.connect(self.save_ranking_to_file)
        self.show_combo_box.currentTextChanged.connect(self.text_changed)
        self.back_button.pressed.connect(partial(self.go_back,self.by_year_widget))

        self.logo_path = f":/images/contest_logos/{self.contest_code}/{self.contest_code}_{self.year}.png"
        self.logo_label.setPixmap(QPixmap(self.logo_path))
        self.year_label.setText(f"{self.contest_name} {str(self.year)}")

        self.get_contest_data()

        self.setup_ranking_items(self.ranking,self.songs,self.artists)

        if self.contest_code == "ESC":
            if year <= 2003:
                self.show_combo_box.hide()
            elif year <= 2008:
                self.show_combo_box.addItems(["Full Ranking","Semi-Final","Grand Final"])
            else:
                self.show_combo_box.addItems(["Full Ranking","Semi-Final 1","Semi-Final 2","Grand Final"])

    def get_contest_data(self):
        self.filename = f'{self.contest_code}_data.xlsx'
        data = pd.read_excel(self.filename)

        self.contest_and_year = f"{self.contest_code} {str(self.year)}"
        self.entries = data[data['contest'] == self.contest_and_year]

        self.songs = list(self.entries['song'])
        self.artists = list(self.entries['artist'])
        self.ranking = list(self.entries['country_code'])

    def toggle_info(self):
        if not self.is_info_visible:    
            if self.contest_and_year != "ESC 1956":
                help_file = f"help_ranking_{self.contest_code}.html"
            else:
                help_file = "help_ranking_ESC_1956.html"
            
            with open(help_file, 'r') as file:
                html_as_string = file.read()

            self.info_label = QLabel()
            self.info_label.setText(html_as_string)
            self.info_label.setAlignment(Qt.AlignTop)
            self.main_layout.addWidget(self.info_label)
        
            self.entry_scroll_area.hide()
            self.import_export_button.hide()
            self.save_button.hide()
            self.back_button.hide()
            self.show_combo_box.hide()
            self.vertical_line.hide()

            self.info_button.setIcon(QPixmap(":/images/icons/close_icon.png"))

            self.is_info_visible = True
        else:
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
        self.update_ranking()
        self.dialog = ranking_import_export(str(self.ranking),self.entries)
        self.dialog.setParent(self,Qt.Dialog)
        self.dialog.show()

    def update_ranking(self):
        new_ranking = []
        c = 0
        for n in range(self.layout.count()):
            c = c + 1
            w = self.layout.itemAt(n).widget()
            if hasattr(w,'number_label'):
                new_ranking.append(w.country)
            else:
                c = c - 1
        
        self.ranking = new_ranking

        old_index = self.entries.index
        new_order = self.entries.set_index(self.entries['country_code'])
        self.entries = new_order.reindex(self.ranking)
        self.entries = self.entries.set_index(old_index)

        self.songs = list(self.entries['song'])
        self.artists = list(self.entries['artist'])

    def save_ranking_to_file(self):
        self.update_ranking()

        with pd.ExcelWriter(self.filename, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
            self.entries.to_excel(writer, sheet_name=self.contest_code, header=False, index=False, startrow=self.entries.index[0]+1)

        contest_data = get_contest_data(self.contest_code)
        ind = contest_data.index[contest_data['year'] == self.year].tolist()
        ind = ind[0]

        if contest_data.iloc[ind,2] == False:
            contest_data.iloc[ind,2] = True
            update_contest_data(contest_data)

            print(f"New year submitted: {self.year}")

        print("Saved")

    def text_changed(self,text):
        if self.previous_combo_box_text == text:
            return None

        if self.previous_combo_box_text == "Full Ranking":
            self.update_ranking()
            self.temp_layout = self.layout

        # Only allow dragging of items when viewing the full ranking
        if text == "Full Ranking":
            self.allow_dragging = True
        else:
            self.allow_dragging = False

        if self.contest_code == "ESC":
            if self.year <= 2007:
                semi_finalists = self.entries[self.entries['show'] == "SF"]
            else:
                semi_finalists_1 = self.entries[self.entries['show'] == "SF1"]
                semi_finalists_2 = self.entries[self.entries['show'] == "SF2"]
            
            self.entries['original_order'] = range(len(self.entries))
            if text == "Semi-Final":
                entries_to_show = semi_finalists
            elif text == "Semi-Final 1":
                entries_to_show = semi_finalists_1
            elif text == "Semi-Final 2":
                entries_to_show = semi_finalists_2
            elif text == "Grand Final":
                automatic = self.entries[self.entries['show'] == "GF"]

                if self.year <= 2007:
                    qualifiers = semi_finalists.iloc[:10]
                else:
                    qualifiers_1 = semi_finalists_1.iloc[:10]
                    qualifiers_2 = semi_finalists_2.iloc[:10]
                    qualifiers = pd.concat([qualifiers_1, qualifiers_2])
                
                entries_to_show = pd.concat([qualifiers, automatic]).sort_values(by='original_order')
            else:
                entries_to_show = self.entries

        entries_to_show = entries_to_show.drop(columns='original_order').reset_index(drop=True)
        self.setup_ranking_items(list(entries_to_show['country_code']),list(entries_to_show['song']),list(entries_to_show['artist']))
        
        self.previous_combo_box_text = text

    def go_back(self,by_year_widget):
        load_widget(self, by_year_widget)

        by_year_widget.update_submitted_status(by_year_widget)
        self.stacked_widget.removeWidget(self)

    def setup_ranking_items(self,ranking,songs,artists):
        self.layout = QVBoxLayout()
        for i in range(len(ranking)):
            country = str(ranking[i])
            song = str(songs[i])
            artist = str(artists[i])

            entry = ranking_item(i+1,country,song,artist)
            entry.set_data(i)
            self.layout.addWidget(entry)

        self.item_height = self.layout.itemAt(0).widget().heart_label.height()

        self.layout.setSpacing(0)
        self.scroll_bar = self.entry_scroll_area.verticalScrollBar()
        self.scroll_bar.setSingleStep(self.item_height)

        self.title_layout.setSpacing(0)
        
        self.drag_target_indicator = DragTargetIndicator()
        self.layout.addWidget(self.drag_target_indicator)
        self.drag_target_indicator.hide()
        
        self.setup_temp_widget(self.layout)

    def setup_temp_widget(self,layout):
        self.temp_widget = QWidget()
        self.temp_widget.setLayout(layout)
        self.temp_widget.setContentsMargins(0,0,0,0)

        self.entry_scroll_area.setWidget(self.temp_widget)
        self.entry_scroll_area.setContentsMargins(0,0,0,0)

    def dragEnterEvent(self, e):
        e.accept()

    def dragLeaveEvent(self, e):
        self.drag_target_indicator.hide()
        e.accept()

    def dropEvent(self, e):
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
            # Get the widget at each index in turn.
            c = c + 1
            w = self.layout.itemAt(n).widget()
            if hasattr(w,'number_label'):
                w.number_label.setText(str(c))
            else:
                c = c - 1
    
    def dragMoveEvent(self, e):
        # Scroll up or down if draggin to top or bottom of the scroll area
        pos = e.position()
        if pos.y() <= self.logo_label.height() and self.scroll_bar.value() > self.scroll_bar.minimum():
            self.scroll_bar.setValue( self.scroll_bar.value() - 5)
        elif pos.y() >= self.entry_scroll_area.height() and self.scroll_bar.value() < self.scroll_bar.maximum():
            self.scroll_bar.setValue( self.scroll_bar.value() + 5)


        # Find the correct location of the drop target, so we can move it there.
        index = self.find_drop_location(e)
        if index is not None:
            # Inserting moves the item if its alreaady in the layout.
            self.layout.insertWidget(index, self.drag_target_indicator)
            # Hide the item being dragged.
            e.source().hide()
            # Show the target.
            self.drag_target_indicator.show()
        e.accept()

    def find_drop_location(self, e):
        pos = e.position()
        spacing = 2

        count_visible = 0
        for n in range(self.layout.count()):
            # Get the widget at each index in turn.
            w = self.layout.itemAt(n).widget()

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

            loc = count_visible * (self.item_height + 6) + self.logo_label.height() + extra

            drop_here = (
                pos.y() >= loc - spacing
                and pos.y() <= loc + w.size().height() + spacing
            )

            if drop_here:
                # Drop over this target.
                break
        
        return n
    
    def add_item(self, item):
        self.layout.addWidget(item)
    
    def get_item_data(self):
        data = []
        for n in range(self.layout.count()):
            # Get the widget at each index in turn.
            w = self.layout.itemAt(n).widget()
            if w != self.drag_target_indicator:
                # The target indicator has no data.
                data.append(w.data)
        return data