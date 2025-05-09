from PyQt6.QtWidgets import QMainWindow, QLabel,QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from src.map import MapWindow
from src.gamemode_outline import OutlineGameWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Map Guessing game (by Gleb Tretiakov)")
        self.setWindowIcon(QIcon("assets/icons/spec-fury-icon.webp"))
        self.setStyleSheet("""
            QLabel {
                font-family: Arial;
                font-size: 30px;
                font-weight: bold;
                color: #008cff;
            
        }
        QPushButton#exitButton {
        background-color: red;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
    }
    QPushButton#exitButton:hover {
        background-color: darkred;
        }
        """)

        layout_widget = QWidget()
        layout = QVBoxLayout()
        layout_widget.setLayout(layout)
        self.setCentralWidget(layout_widget)

        title1 = QLabel()
        title2 = QLabel()

        title1.setText("Map Guessing Game")
        title2.setText("by Gleb Tretiakov")

        map_button = QPushButton("Open Map")
        map_button.clicked.connect(self.open_map_button)

        outline_button = QPushButton("Play")
        outline_button.clicked.connect(self.open_gamemode_outline)

        exit_button = QPushButton("Exit")
        exit_button.setObjectName("exitButton")
        exit_button.clicked.connect(self.exit_program)

        title1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title2.setAlignment(Qt.AlignmentFlag.AlignCenter)


        layout.addWidget(title1, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(map_button, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(outline_button, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(exit_button, Qt.AlignmentFlag.AlignCenter)

    def open_map_button(self):
        map_window = MapWindow()
        map_window.show()

    def open_gamemode_outline(self):
        gamemode_outline = OutlineGameWindow()
        gamemode_outline.show()

    def exit_program(self):
        self.close()
