import sys
from PyQt6.QtWidgets import QApplication
from userInterface import userInterface

def main():
    # initializes application
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = userInterface()
    window.show()

    sys.exit(app.exec())

main()