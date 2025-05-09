from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QRadioButton, \
    QButtonGroup, QFrame
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from src.country import Country
from random import choice, sample
from src.map import MapWindow


class OutlineGameWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.setStyleSheet("""
            QLabel {
                font-family: Arial;
                font-size: 17px;
                font-weight: bold;
                color: #008cff;
            }

            QRadioButton {
                font-size: 15px;
                margin: 5px;
            }
        """)

        self.setWindowIcon(QIcon("assets/icons/pngtree-game-controller-flat-icon-png-image_9104382.png"))
        self.setWindowTitle("Guess Country Outline")

        self.outline_label = QLabel()

        self.hint1 = QLabel("Population (M): ")
        self.hint1.setFixedSize(300, 30)
        self.hint2 = QLabel("Capital: ")
        self.hint2.setFixedSize(300, 30)
        self.hint3 = QLabel("Name: ")
        self.hint3.setFixedSize(300, 30)

        self.radio1 = QRadioButton()
        self.radio2 = QRadioButton()
        self.radio3 = QRadioButton()
        self.radio4 = QRadioButton()

        self.points = 0
        self.points_label = QLabel("Points: {}".format(self.points))

        self.radio_buttons = [self.radio1, self.radio2, self.radio3, self.radio4]

        self.submit_button = QPushButton("Submit Guess")
        self.start_game_button = QPushButton("Start game")
        self.answered_countries = []
        self.available_countries = []
        self.radio_group = QButtonGroup()
        self.game_rounds = 0
        self.answer = None
        self.incorrect_answers = 0

        self.finland = Country("Finland", "assets/flags/Flag_of_Finland.png", "assets/outlines/fi-01.jpg", 5.58,
                               "Helsinki", "Euro", "Finnish",
                               338.462, self)
        self.france = Country("France", "assets/flags/Flag_of_France.png", "assets/outlines/fr-01.jpg", 68.29, "Paris",
                              "Euro", "French", 551.695,
                              self)
        self.germany = Country("Germany", "assets/flags/Flag_of_Germany.png", "assets/outlines/de-01.jpg", 83.28,
                               "Berlin", "Euro", "German",
                               357.592, self)
        self.spain = Country("Spain", "assets/flags/Flag_of_Spain.png", "assets/outlines/es-01.jpg", 48.35, "Madrid",
                             "Euro", "Spanish", 506.030,
                             self)
        self.sweden = Country("Sweden", "assets/flags/Flag_of_Sweden.png", "assets/outlines/se-01.jpg", 10.54,
                              "Stockholm", "Swedish krona",
                              "Swedish", 450.295, self)
        self.poland = Country("Poland", "assets/flags/Flag_of_Poland.png", "assets/outlines/pl-01.jpg", 36.69, "Warsaw",
                              "Złoty", "Polish", 322.575,
                              self)
        self.italy = Country("Italy", "assets/flags/Flag_of_Italy.png", "assets/outlines/it-01.jpg", 58.99, "Rome",
                             "Euro", "Italian", 302.073, self)
        self.czechia = Country("Czech Republic", "assets/flags/Flag_of_the_Czech_Republic.png",
                               "assets/outlines/cz-01.jpg", 10.90, "Prague",
                               "Czech koruna", "Czech", 78.871, self)
        self.austria = Country("Austria", "assets/flags/Flag_of_Austria.png", "assets/outlines/at-01.jpg", 9.13,
                               "Vienna", "Euro", "German", 83.871,
                               self)
        self.belgium = Country("Belgium", "assets/flags/Flag_of_Belgium.png", "assets/outlines/be-01.jpg", 11.79,
                               "Brussels", "Euro",
                               "Dutch, German, French", 30.689, self)
        self.croatia = Country("Croatia", "assets/flags/Flag_of_Croatia.png", "assets/outlines/hr-01.jpg", 3.86,
                               "Zagreb", "Euro", "Croatian",
                               56.561, self)
        self.netherlands = Country("Netherlands", "assets/flags/Flag_of_the_Netherlands.png",
                                   "assets/outlines/nl-01.jpg", 17.88, "Amsterdam",
                                   "Euro", "Dutch", 41.865, self)
        self.portugal = Country("Portugal", "assets/flags/Flag_of_Portugal.png", "assets/outlines/pt-01.jpg", 10.58,
                                "Lisbon", "Euro", "Portuguese",
                                92.230, self)
        self.slovakia = Country("Slovakia", "assets/flags/Flag_of_Slovakia.png", "assets/outlines/sk-01.jpg", 5.43,
                                "Bratislava", "Euro", "Slovak",
                                49.035, self)
        self.slovenia = Country("Slovenia", "assets/flags/Flag_of_Slovenia.png", "assets/outlines/si-01.jpg", 2.12,
                                "Ljubljana", "Euro", "Slovenian",
                                20.271, self)
        self.romania = Country("Romania", "assets/flags/Flag_of_Romania.png", "assets/outlines/ro-01.jpg", 19.06,
                               "Bucharest", "Romanian leu ",
                               "Romanian", 238.397, self)
        self.bulgaria = Country("Bulgaria", "assets/flags/Flag_of_Bulgaria.png", "assets/outlines/bg-01.jpg", 6.447,
                                "Sofia", "Lev", "Bulgarian",
                                110.993, self)
        self.hungary = Country("Hungary", "assets/flags/Flag_of_Hungary.png", "assets/outlines/hu-01.jpg", 9.58,
                               "Budapest", "Forint", "Hungarian",
                               93.030, self)
        self.ireland = Country("Republic of Ireland", "assets/flags/Flag_of_Ireland.png", "assets/outlines/ie-01.jpg",
                               5.38, "Dublin", "Euro",
                               "Irish, English", 70.27, self)
        self.latvia = Country("Latvia", "assets/flags/Flag_of_Latvia.png", "assets/outlines/lv-01.jpg", 1.84, "Riga",
                              "Euro", "Latvian", 64.589,
                              self)

        self.countries = [self.finland, self.france, self.germany, self.spain, self.sweden, self.poland, self.italy,
                          self.czechia, self.austria, self.belgium, self.croatia, self.netherlands,
                          self.portugal, self.slovakia, self.slovenia, self.romania, self.bulgaria, self.hungary,
                          self.ireland, self.latvia]

        self.start_game_button.clicked.connect(self.game_loop)
        self.submit_button.clicked.connect(self.check_answer)

        self.initUI()
        self.borderUI()
        self.hintUI()

    def initUI(self):
        game_layout_widget = QWidget()
        game_layout = QVBoxLayout()
        game_layout_widget.setLayout(game_layout)
        self.main_layout.addWidget(game_layout_widget)

        self.outline_label.setFixedSize(500, 400)
        self.outline_label.setScaledContents(True)

        game_layout.addWidget(self.outline_label)
        self.radio_group = QButtonGroup()

        for i in self.radio_buttons:
            self.radio_group.addButton(i)
            game_layout.addWidget(i)

        self.submit_button.setDisabled(True)
        game_layout.addWidget(self.points_label)
        game_layout.addWidget(self.submit_button)
        game_layout.addWidget(self.start_game_button)

    def hintUI(self):
        hint_layout_widget = QWidget()
        hint_layout = QVBoxLayout()
        hint_layout.setSpacing(0)
        hint_layout.setContentsMargins(0, 0, 0, 0)
        hint_layout_widget.setLayout(hint_layout)
        self.main_layout.addWidget(hint_layout_widget)

        hint_name = QLabel("HINTS")
        hint_name.setFixedSize(300, 100)
        hint_name.setStyleSheet(
            "font-family: Arial; font-size: 30px; font-weight: bold; background-color: #ffffff; color: #2155ff;")

        hint_layout.addWidget(hint_name)
        hint_layout.addWidget(self.hint1)
        hint_layout.addWidget(self.hint2)
        hint_layout.addWidget(self.hint3)

        hint_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.hint1.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        # self.hint2.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        # self.hint3.setAlignment(Qt.AlignmentFlag.AlignVCenter)

    def borderUI(self):
        line = QFrame()
        line.setFrameShape(QFrame.Shape.VLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        self.main_layout.addWidget(line)

    def game_loop(self):
        self.submit_button.setEnabled(True)
        self.start_game_button.setDisabled(True)
        self.incorrect_answers = 0
        self.game_rounds += 1
        self.hint1.setText("Population (M):")
        self.hint2.setText("Capital:")
        self.hint3.setText("Name:")
        self.points_label.setText("Points: {}".format(self.points))
        self.radio_group.setExclusive(False)
        for i in self.radio_buttons:
            i.setChecked(False)
        self.radio_group.setExclusive(True)

        self.available_countries = [c for c in self.countries if c not in self.answered_countries]
        options = sample(self.available_countries, 4)
        self.answer = choice(options)
        self.answered_countries.append(self.answer)

        outline = QPixmap(self.answer.get_outline())
        self.outline_label.setPixmap(outline)
        self.radio1.setText(options[0].get_name())
        self.radio2.setText(options[1].get_name())
        self.radio3.setText(options[2].get_name())
        self.radio4.setText(options[3].get_name())

    def check_answer(self):
        chosen_option = self.radio_group.checkedButton()

        if not chosen_option:
            QMessageBox.warning(self, "No Selection", "Please select an option before submitting.")
            return

        guess = chosen_option.text()
        if guess == self.answer.get_name():
            match self.incorrect_answers:
                case 0:
                    self.points += 1
                case 1:
                    self.points += 0.75
                case 2:
                    self.points += 0.5
            if self.game_rounds < 5:
                self.game_loop()
            else:
                QMessageBox.information(self, "Correct!", "Well done! Check countries on the map")
                map_window = MapWindow()
                map_window.disable_buttons(self.answered_countries)
                print(self.answered_countries)
                map_window.show()
                self.start_game_button.setDisabled(False)
                self.submit_button.setEnabled(False)
                self.game_rounds = 0
                self.points = 0
                self.available_countries = []
                self.answered_countries = []

        else:
            self.incorrect_answers += 1
            match self.incorrect_answers:
                case 1:
                    self.hint1.setText("Population (M): {}".format(self.answer.hint(self.incorrect_answers)))
                case 2:
                    self.hint2.setText("Capital: {}".format(self.answer.hint(self.incorrect_answers)))
                case 3:
                    self.hint3.setText("Name: {}".format(self.answer.hint(self.incorrect_answers)))
            QMessageBox.warning(self, "Incorrect", "Wrong answer -> check hints")