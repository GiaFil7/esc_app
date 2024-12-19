from PySide6.QtWidgets import QApplication
from main_window import main_window
import sys

def main():
    app = QApplication(sys.argv)

    window = main_window()
    window.show()

    with open("styles.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    app.exec()

if __name__ == "__main__":
    main()