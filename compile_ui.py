"""
Helper script to compile all .ui files.

To manually compile use the following:
    * To compile ui: pyside6-uic tutorial.ui > ui_tutorial.py
                                [source file] > [destination file]
    * To compile resources: pyside6-rcc resources.qrc > resources_rc.py
                                        [source file] > [destination file]
Don't forget to change the encoding of the resulting file to UTF-8 when
compiling manually.
"""

import subprocess
from contextlib import chdir

# Compile resources
with open("resources_rc.py", "w") as output:
    subprocess.run(["pyside6-rcc", "resources.qrc"], stdout = output)

# UI files to compile
files = [
    "confirm_dialog",
    "credits",
    "main_menu",
    "main_window",
    "quizzes_contest_main_menu",
    "quizzes_list_menu",
    "quizzes_main_menu",
    "ranking_import_export",
    "ranking_item",
    "ranking_menu_item",
    "ranking_widget",
    "rankings_by_year",
    "rankings_contest_main_menu",
    "rankings_image",
    "rankings_main_menu",
    "statistics_menu",
    "statistics_table"
]

# Compile UI files
for file in files:
    input_file = f"{file}.ui"
    output_file = f"ui_{file}.py"
    with chdir(".\\ui"):
        with open(output_file, "w") as output:
            subprocess.run(["pyside6-uic", input_file], stdout = output)

print("Done compiling!")