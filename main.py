import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(
    os.path.abspath(__file__)
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(
        0,
        PROJECT_ROOT
    )

from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow


def main():

    app = QApplication(
        sys.argv
    )

    app.setApplicationName(
        "CYBERFORGE"
    )

    app.setStyle(
        "Fusion"
    )

    window = MainWindow()

    window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()