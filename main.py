from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase
from main_window import main_window
import sys

def main():
    app = QApplication(sys.argv)

    window = main_window()
    window.show()

    QFontDatabase.addApplicationFont('styles\\Roboto.ttf')
    QFontDatabase.addApplicationFont('styles\\AlfaSlabOne.ttf')
    QFontDatabase.addApplicationFont('styles\\Lexend.ttf')
    QFontDatabase.addApplicationFont('styles\\Shrikhand.ttf')
    QFontDatabase.addApplicationFont('styles\\Teko.ttf')
    QFontDatabase.addApplicationFont('styles\\TitanOne.ttf')
    QFontDatabase.addApplicationFont('styles\\Ultra.ttf')

    with open("styles\\styles.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    app.exec()

if __name__ == "__main__":
    main()