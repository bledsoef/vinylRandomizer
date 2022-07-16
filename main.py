from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
import webbrowser
import sys
from scraper import setupAPI
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("priceComparison")
        self.url = setupAPI()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        showUrl = QLabel(self.url, self)
        self.layout.addWidget(showUrl, alignment= Qt.AlignmentFlag.AlignCenter)
     
        button = QPushButton("Go to URL")
        button.clicked.connect(self.redirectToAuthorizer)
        self.layout.addWidget(button)
 
    def redirectToAuthorizer(self):
        webbrowser.open_new(self.url)
        self.askForVerifier()

    def askForVerifier(self):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().deleteLater()

        askVerifier = QLabel("Please input the ", self)
        self.layout.addWidget(askVerifier)
        verifier = QLineEdit()
        self.layout.addWidget(verifier)

    def displayAuthorizeURL(self):

        self.close()

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())