# To compile ui: pyside6-uic tutorial.ui > ui_tutorial.py
#                          [source file] > [destination file]
# pyside6-uic ranking_widget.ui > ui_ranking_widget.py
# pyside6-uic ranking_item.ui > ui_ranking_item.py
# pyside6-uic ranking_import_export.ui > ui_ranking_import_export.py
# pyside6-uic main_window.ui > ui_main_window.py
# pyside6-uic main_menu.ui > ui_main_menu.py
# pyside6-uic ranking_menu_item.ui > ui_ranking_menu_item.py
# pyside6-uic rankings_esc_main_menu.ui > ui_rankings_esc_main_menu.py
# pyside6-uic rankings_main_menu.ui > ui_rankings_main_menu.py
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