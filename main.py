# To compile ui: pyside6-uic tutorial.ui > ui_tutorial.py
#                          [source file] > [destination file]
# To compile resources: pyside6-rcc resources.qrc > resources_rc.py
#                                  [source file] > [destination file]
# Don't forget to change the encoding of the resulting file to UTF-8

from PySide6.QtWidgets import QApplication, QWidget
import sys

from ranking_widget import ranking_widget
from main_window import main_window
from main_menu import main_menu

def main():
    app = QApplication(sys.argv)

    #widget= ranking_widget("Eurovision Song Contest",2024)
    window = main_window()
    window.show()

    app.exec()
    

if __name__ == "__main__":
    main()