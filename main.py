from PySide6.QtWidgets import QApplication
from main_window import main_window
import sys

def main():
    app = QApplication(sys.argv)

    window = main_window()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()