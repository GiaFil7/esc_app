from ui.ui_ranking_import_export import Ui_import_export_dialog
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QGuiApplication
from utils import get_country_codes
import pandas as pd # type: ignore
from typing import List
import resources_rc

class ranking_import_export(QWidget, Ui_import_export_dialog):
    """
    A widget that allows the user to import and export rankings using country codes.

    :param ranking: A list of country codes representing the order of the ranking items.
    :type ranking: List[str]
    :param entries: Dataframe containing all data about entries in a specific year.
    :type entries: DataFrame
    """
    def __init__(self, ranking: List[str], entries: pd.DataFrame):
        super().__init__()
        self.setupUi(self)
        self.ranking = ranking
        self.entries = entries
        self.country_codes = list(entries['country_code'])

        # Clean up the ranking string
        self.ranking = ", ".join(str(code) for code in self.ranking)

        self.export_field.setText(self.ranking)
        
        # Connect all slots
        self.import_button.pressed.connect(self.import_ranking)
        self.export_button.pressed.connect(self.copy_to_clipboard)

    def import_ranking(self):
        """
        Takes the text typed by the user in the import field, validates
        it, displays any errors to the user and rearranges the ranking
        items.
        """

        raw_text = self.import_field.text()

        # Get the name of the contest
        contest = list(self.entries['contest'])
        contest = contest[0]

        # Initializes the valid country codes and all acceptable characters
        if contest == "ESC 1956": # Since there are 2 entries per country in 1956, it needs a special case
            valid_country_codes = get_country_codes(contest)
            valid_country_codes = list(valid_country_codes['code'])
            acceptable_characters = set("abcdefghijklmnopqrstuvxyz,12")
        else:
            valid_country_codes = get_country_codes()
            valid_country_codes = list(valid_country_codes['code'])
            acceptable_characters = set("abcdefghijklmnopqrstuvxyz,")

        # Check if the field is empty
        if raw_text == "":
            self.error_label.setText("Please input a list of comma-separated country codes")
            return

        # Remove extra spaces
        raw_text = raw_text.replace(" ","")

        # Check for invalid characters
        if not(all((c in acceptable_characters) for c in raw_text)):
            self.error_label.setText("Invalid character(s) or capital letter(s) in input")
            return

        # Check for invalid country codes
        input_codes = raw_text.split(",")
        for code in input_codes:
            if code not in valid_country_codes:
                if code != "":
                    self.error_label.setText(f"Invalid country code: {code}")
                    return
                else:
                    self.error_label.setText("Missing code or extra comma found")
                    return

        # Find and show duplicate entries 
        seen = set()
        duplicate_codes = [x for x in input_codes if x in seen or seen.add(x)]
        if duplicate_codes != []:
            duplicate_codes = ", ".join(str(code) for code in duplicate_codes)
            self.error_label.setText(f"Duplicate entries found: {duplicate_codes}")
            return

        # Find and show missing entries
        missing_codes = list(set(self.country_codes).difference(input_codes))
        if missing_codes != []:
            missing_codes = ", ".join(str(code) for code in missing_codes)
            self.error_label.setText(f"Missing entries found: {missing_codes}")
            return

        # Find and show extra entries
        extra_codes = list(set(input_codes).difference(self.country_codes))
        if extra_codes != []:
            extra_codes = ", ".join(str(code) for code in extra_codes)
            self.error_label.setText(f"Extra entries found: {extra_codes}")
            return

        # Clear any error messages
        self.error_label.setText("")

        # Reorder the entries
        new_order = self.entries.set_index(self.entries['country_code'])
        new_order = new_order.reindex(input_codes)

        # Change the order of the ranking items in the ranking widget
        ranking_widget = self.parent()
        ranking_widget.setup_ranking_items(list(new_order['country_code']), list(new_order['song']), list(new_order['artist']))

        self.close()
        

    def copy_to_clipboard(self):
        """
        Copies the text of the export field to the clipboard.
        """

        clipboard = QGuiApplication.clipboard()
        newText = self.export_field.text()
        clipboard.setText(newText)