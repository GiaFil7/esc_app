import subprocess

with open("ui_main_menu.py", "w") as output:
    subprocess.run(["pyside6-uic", "main_menu.ui"], stdout=output)