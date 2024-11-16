import subprocess
from contextlib import chdir


# Compile resources
with open("resources_rc.py", "w") as output:
    subprocess.run(["pyside6-rcc", "resources.qrc"], stdout=output)


files = ["main_menu",
         "main_window",
         "ranking_import_export",
         "ranking_item",
         "ranking_menu_item",
         "ranking_widget",
         "rankings_esc_main_menu",
         "rankings_main_menu"]

# Compile UI files
for file in files:
    input_file = f"{file}.ui"
    output_file = f"ui_{file}.py"
    with chdir(".\\ui"):
        with open(output_file, "w") as output:
            subprocess.run(["pyside6-uic", input_file], stdout=output)

print("Done compiling!")
