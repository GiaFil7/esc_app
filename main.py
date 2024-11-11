# To compile ui: pyside6-uic tutorial.ui > ui_tutorial.py
#                          [source file] > [destination file]
# pyside6-uic ranking_widget.ui > ui_ranking_widget.py
# pyside6-uic ranking_item.ui > ui_ranking_item.py
# pyside6-uic ranking_import_export.ui > ui_ranking_import_export.py
# To compile resources: pyside6-rcc resources.qrc > resources_rc.py
#                                  [source file] > [destination file]
# Don't forget to change the encoding of the resulting file to UTF-8

from PySide6.QtWidgets import QApplication, QWidget
import sys

from ranking_widget import ranking_widget

def main():
    # print("Hello World!")
    app = QApplication(sys.argv)

    # window = QWidget()
    window = ranking_widget("Eurovision Song Contest",2024)
    window.show()

    app.exec()
    

if __name__ == "__main__":
    main()