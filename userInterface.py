from scraper import generateRandomVinyl, getGenreSpecificVinyl
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt6.QtCore import Qt

class userInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 250)
        self.setWindowTitle("Randomize Vinyl")
        self.setStyleSheet(
        "background-color: #ffffff;"
        )
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.startPage()

    def startPage(self, error=''):
        """
        Generates page that allows the user to get a genre specific vinyl or a random one from their collection
        """
        button = QPushButton("Generate Random Vinyl")
        button.setStyleSheet(
        "background-color: #8b7ff5;"
        "font-family: times;"
        "font-size: 14px;"
        )
        button.clicked.connect(self.getAndDisplayVinyl)
        self.layout.addWidget(button)

        errorLabel = QLabel(error, self)
        errorLabel.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(errorLabel)

        genreBoxLabel = QLabel("Feeling a certain genre? Input it here! \n (This may take a moment...)", self)
        genreBoxLabel.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(genreBoxLabel)

        self.genreBox = QLineEdit()
        self.genreBox.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.genreBox)

        genreBoxButton = QPushButton("Get a vinyl in this genre")
        genreBoxButton.setStyleSheet(
        "background-color: #8b7ff5;"
        "font-family: times;"
        "font-size: 14px;"
        )
        genreBoxButton.clicked.connect(self.getGenreVinyl)
        self.layout.addWidget(genreBoxButton)

    def clearLayout(self):
        """
        Removes all widgets on window
        """
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().deleteLater()

    def getGenreVinyl(self):
        """
        Calls the function that returns a genre specific vinyl
        """
        vinylData = getGenreSpecificVinyl(self.genreBox.text())
        if len(vinylData) != 1:
            self.displayGenreVinyl(vinylData)
        else:
            self.startPage(error='Couldn\'t find a match for that genre.')

    def displayGenreVinyl(self, vinylData):
        """
        Displays a randomly generated vinyl that is genre specific
        """
        self.clearLayout()

        displayText = QLabel("Here is your vinyl:", self)
        font = displayText.font()
        font.setPointSize(20)
        displayText.setFont(font)
        displayText.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(displayText)

        displayVinyl = QLabel(vinylData[0] + " - " + vinylData[1], self)
        font = displayVinyl.font()
        font.setPointSize(20)
        displayVinyl.setFont(font)
        displayVinyl.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(displayVinyl)

        displayNewVinyl = QLabel("Not happy? Get another one!", self)
        displayNewVinyl.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(displayNewVinyl)

        button = QPushButton("Generate Random Vinyl")
        button.setStyleSheet(
        "background-color: #8b7ff5;"
        "font-family: times;"
        "font-size: 14px;"
        )
        button.clicked.connect(self.getAndDisplayVinyl)
        self.layout.addWidget(button)

    def getAndDisplayVinyl(self):
        """
        Displays a randomly generated vinyl
        """
        self.clearLayout()

        displayText = QLabel("Here is your vinyl:", self)
        font = displayText.font()
        font.setPointSize(20)
        displayText.setFont(font)
        displayText.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(displayText)

        vinylData = generateRandomVinyl()
        displayVinyl = QLabel(vinylData["artist"] + " - " + vinylData['title'], self)
        font = displayVinyl.font()
        font.setPointSize(20)
        displayVinyl.setFont(font)
        displayVinyl.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(displayVinyl)

        displayNewVinyl = QLabel("Not happy? Get another one!", self)
        displayNewVinyl.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(displayNewVinyl)

        button = QPushButton("Generate Random Vinyl")
        button.setStyleSheet(
        "background-color: #8b7ff5;"
        "font-family: times;"
        "font-size: 14px;"
        )
        button.clicked.connect(self.getAndDisplayVinyl)
        self.layout.addWidget(button)
        

