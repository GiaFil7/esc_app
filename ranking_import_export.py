from ui.ui_ranking_import_export import Ui_import_export_dialog
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QGuiApplication

import pandas as pd # type: ignore
import resources_rc

class ranking_import_export(QWidget, Ui_import_export_dialog):
    def __init__(self,ranking,entries):
        super().__init__()
        self.setupUi(self)
        self.ranking = ranking
        self.entries = entries
        self.country_codes = list(entries['country_code'])

        # Clean up the ranking string
        self.ranking = self.clean_string_from_list(self.ranking)

        self.export_field.setText(self.ranking)

        self.import_button.pressed.connect(self.import_ranking)
        self.export_button.pressed.connect(self.copy_to_clipboard)

    def import_ranking(self):
        raw_text = self.import_field.text()
        contest = list(self.entries['contest'])
        contest = contest[0]

        if contest == "ESC 1956":
            valid_country_codes = ["nl1","ch1","be1","de1","fr1","lu1","it1",
                                   "nl2","ch2","be2","de2","fr2","lu2","it2"]
            acceptable_characters = set("abcdefghijklmnopqrstuvxyz,12")
        else:
            valid_country_codes = ["ad","al","am","at","au","az","ba","be","bg","by","ch","cs","cy",
                                   "cz","de","dk","ee","es","fi","fr","gb","ge","gr","hr","hu","ie",
                                   "il","is","it","lt","lu","lv","ma","mc","md","me","mk","mt","nl",
                                   "no","pl","pt","ro","rs","ru","se","si","sk","sm","tr","ua","yu"]
            acceptable_characters = set("abcdefghijklmnopqrstuvxyz,")

        # Check if the field is empty
        if raw_text == "":
            self.error_label.setText("Please input a list of comma-separated country codes")
            return ""
        else:
            self.error_label.setText("")
        
        raw_text = raw_text.replace(" ","")

        # Check for invalid characters
        if not(all((c in acceptable_characters) for c in raw_text)):
            self.error_label.setText("Invalid character(s) or capital letter(s) in input")
            return ""
        else:
            self.error_label.setText("")

        # Check for invalid country codes
        input_codes = raw_text.split(",")
        for code in input_codes:
            if code not in valid_country_codes:
                if code != "":
                    self.error_label.setText(f"Invalid country code: {code}")
                    return ""
                else:
                    self.error_label.setText("Missing code or extra comma found")
                    return ""
        self.error_label.setText("")

        # Find and show duplicate entries 
        seen = set()
        duplicate_codes = [x for x in input_codes if x in seen or seen.add(x)]
        if duplicate_codes != []:
            duplicate_codes = self.clean_string_from_list(str(duplicate_codes))
            self.error_label.setText(f"Duplicate entries found: {duplicate_codes}")
            return ""

        # Find and show missing entries
        missing_codes = list(set(self.country_codes).difference(input_codes))
        if missing_codes != []:
            missing_codes = self.clean_string_from_list(str(missing_codes))
            self.error_label.setText(f"Missing entries found: {missing_codes}")
            return ""

        # Find and show extra entries
        extra_codes = list(set(input_codes).difference(self.country_codes))
        if extra_codes != []:
            extra_codes = self.clean_string_from_list(str(extra_codes))
            self.error_label.setText(f"Extra entries found: {extra_codes}")
            return ""

        self.error_label.setText("") # Clear any error messages

        # Reorder the entries
        new_order = self.entries.set_index(self.entries['country_code'])
        new_order = new_order.reindex(input_codes)

        # Change the order of the ranking items in the ranking widget
        ranking_widget = self.parent()
        ranking_widget.setup_ranking_items(list(new_order['country_code']),list(new_order['song']),list(new_order['artist']))

        self.close()
        

    def copy_to_clipboard(self):
        clipboard = QGuiApplication.clipboard()
        newText = self.export_field.text()
        clipboard.setText(newText)

    def clean_string_from_list(self,input_list):
        output_list = input_list.replace("[","")
        output_list = output_list.replace("]","")
        output_list = output_list.replace("'","")
        return output_list