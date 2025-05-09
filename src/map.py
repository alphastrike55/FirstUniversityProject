from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from src.country import Country


class MapWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1500, 950)
        self.setWindowTitle("Map")
        self.setWindowIcon(QIcon("assets/icons/235861.png"))

        self.setStyleSheet("""
        QPushButton {
            background-color: lightblue;
        }

        QPushButton:disabled {
            background-color: rgba(173, 216, 230, 25);  /* LightBlue with low opacity */
        }
        QLabel {
                font-family: Arial;
                font-size: 20px;
                font-weight: bold;
                color: #008cff;
        }
        """)


        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.country_flag = QLabel()
        self.country_name = QLabel()
        self.country_capital = QLabel()
        self.country_population = QLabel()
        self.country_currency = QLabel()
        self.country_area = QLabel()

        self.finland = Country("Finland", "assets/flags/Flag_of_Finland.png", "assets/outlines/fi-01.jpg", 5.58, "Helsinki", "Euro", "Finnish",
                               338.462, self)
        self.france = Country("France", "assets/flags/Flag_of_France.png", "assets/outlines/fr-01.jpg", 68.29, "Paris", "Euro", "French", 551.695,
                              self)
        self.germany = Country("Germany", "assets/flags/Flag_of_Germany.png", "assets/outlines/de-01.jpg", 83.28, "Berlin", "Euro", "German",
                               357.592, self)
        self.spain = Country("Spain", "assets/flags/Flag_of_Spain.png", "assets/outlines/es-01.jpg", 48.35, "Madrid", "Euro", "Spanish", 506.030,
                             self)
        self.sweden = Country("Sweden", "assets/flags/Flag_of_Sweden.png", "assets/outlines/se-01.jpg", 10.54, "Stockholm", "Swedish krona",
                              "Swedish", 450.295, self)
        self.poland = Country("Poland", "assets/flags/Flag_of_Poland.png", "assets/outlines/pl-01.jpg", 36.69, "Warsaw", "Złoty", "Polish", 322.575,
                              self)
        self.italy = Country("Italy", "assets/flags/Flag_of_Italy.png", "assets/outlines/-01.jpg", 58.99, "Rome", "Euro", "Italian", 302.073, self)
        self.czechia = Country("Czech Republic", "assets/flags/Flag_of_the_Czech_Republic.png", "assets/outlines/cz-01.jpg", 10.90, "Prague",
                               "Czech koruna", "Czech", 78.871, self)
        self.austria = Country("Austria", "assets/flags/Flag_of_Austria.png", "assets/outlines/at-01.jpg", 9.13, "Vienna", "Euro", "German", 83.871,
                               self)
        self.belgium = Country("Belgium", "assets/flags/Flag_of_Belgium.png", "assets/outlines/be-01.jpg", 11.79, "Brussels", "Euro",
                               "Dutch, German, French", 30.689, self)
        self.croatia = Country("Croatia", "assets/flags/Flag_of_Croatia.png", "assets/outlines/hr-01.jpg", 3.86, "Zagreb", "Euro", "Croatian",
                               56.561, self)
        self.netherlands = Country("Netherlands", "assets/flags/Flag_of_the_Netherlands.png", "assets/outlines/nl-01.jpg", 17.88, "Amsterdam",
                                   "Euro", "Dutch", 41.865, self)
        self.portugal = Country("Portugal", "assets/flags/Flag_of_Portugal.png", "assets/outlines/pt-01.jpg", 10.58, "Lisbon", "Euro", "Portuguese",
                                92.230, self)
        self.slovakia = Country("Slovakia", "assets/flags/Flag_of_Slovakia.png", "assets/outlines/sk-01.jpg", 5.43, "Bratislava", "Euro", "Slovak",
                                49.035, self)
        self.slovenia = Country("Slovenia", "assets/flags/Flag_of_Slovenia.png", "assets/outlines/si-01.jpg", 2.12, "Ljubljana", "Euro", "Slovenian",
                                20.271, self)
        self.romania = Country("Romania", "assets/flags/Flag_of_Romania.png", "assets/outlines/ro-01.jpg", 19.06, "Bucharest", "Romanian leu ",
                               "Romanian", 238.397, self)
        self.bulgaria = Country("Bulgaria", "assets/flags/Flag_of_Bulgaria.png", "assets/outlines/bg-01.jpg", 6.447, "Sofia", "Lev", "Bulgarian",
                                110.993, self)
        self.hungary = Country("Hungary", "assets/flags/Flag_of_Hungary.png", "assets/outlines/hu-01.jpg", 9.58, "Budapest", "Forint", "Hungarian",
                               93.030, self)
        self.ireland = Country("Republic of Ireland", "assets/flags/Flag_of_Ireland.png", "assets/outlines/ie-01.jpg", 5.38, "Dublin", "Euro",
                               "Irish, English", 70.27, self)
        self.latvia = Country("Latvia", "assets/flags/Flag_of_Latvia.png", "assets/outlines/lv-01.jpg", 1.84, "Riga", "Euro", "Latvian", 64.589,
                              self)

        self.finland_button = QPushButton("", self)
        self.france_button = QPushButton("", self)
        self.germany_button = QPushButton("", self)
        self.spain_button = QPushButton("", self)
        self.sweden_button = QPushButton("", self)
        self.poland_button = QPushButton("", self)
        self.italy_button = QPushButton("", self)
        self.czechia_button = QPushButton("", self)
        self.austria_button = QPushButton("", self)
        self.belgium_button = QPushButton("", self)
        self.croatia_button = QPushButton("", self)
        self.netherlands_button = QPushButton("", self)
        self.portugal_button = QPushButton("", self)
        self.slovakia_button = QPushButton("", self)
        self.slovenia_button = QPushButton("", self)
        self.romania_button = QPushButton("", self)
        self.bulgaria_button = QPushButton("", self)
        self.hungary_button = QPushButton("", self)
        self.ireland_button = QPushButton("", self)
        self.latvia_button = QPushButton("", self)

        self.country_buttons = None
        self.buttons = None

        self.mapUI()
        self.infoUI()
        self.buttons_UI()

    def mapUI(self):
        map_label = QLabel()
        map_label.setFixedSize(950, 950)
        map_picture = QPixmap("assets/util/Europe_map.png")
        map_label.setPixmap(map_picture)
        map_label.setScaledContents(True)
        self.main_layout.addWidget(map_label)

    def infoUI(self):
        info_widget = QWidget()
        info_layout = QVBoxLayout()
        info_widget.setLayout(info_layout)
        info_widget.setFixedSize(550, 950)
        self.main_layout.addWidget(info_widget)

        self.country_flag = QLabel()
        self.country_flag.setFixedSize(550, 336)
        country_flag_picture = QPixmap(
            "assets/util/sieninis-medinis-pasaulio-zemelapis-su-saliu-valstybiu-pavadinimais-kelioniu-zemelapis-azuolas-map-it-studio.jpg")
        self.country_flag.setPixmap(country_flag_picture)
        self.country_flag.setScaledContents(True)
        self.country_name = QLabel("Name:")
        self.country_capital = QLabel("Capital:")
        self.country_population = QLabel("Population (M):")
        self.country_currency = QLabel("Currency:")
        self.country_area = QLabel("Area (km²): ")

        info_layout.addWidget(self.country_flag)
        info_layout.addWidget(self.country_name)
        info_layout.addWidget(self.country_capital)
        info_layout.addWidget(self.country_population)
        info_layout.addWidget(self.country_currency)
        info_layout.addWidget(self.country_area)

    def buttons_UI(self):
        self.finland_button = QPushButton("", self)
        self.france_button = QPushButton("", self)
        self.germany_button = QPushButton("", self)
        self.spain_button = QPushButton("", self)
        self.sweden_button = QPushButton("", self)
        self.poland_button = QPushButton("", self)
        self.italy_button = QPushButton("", self)
        self.czechia_button = QPushButton("", self)
        self.austria_button = QPushButton("", self)
        self.belgium_button = QPushButton("", self)
        self.croatia_button = QPushButton("", self)
        self.netherlands_button = QPushButton("", self)
        self.portugal_button = QPushButton("", self)
        self.slovakia_button = QPushButton("", self)
        self.slovenia_button = QPushButton("", self)
        self.romania_button = QPushButton("", self)
        self.bulgaria_button = QPushButton("", self)
        self.hungary_button = QPushButton("", self)
        self.ireland_button = QPushButton("", self)
        self.latvia_button = QPushButton("", self)

        self.country_buttons = [
            self.finland_button,
            self.france_button,
            self.germany_button,
            self.spain_button,
            self.sweden_button,
            self.poland_button,
            self.italy_button,
            self.czechia_button,
            self.austria_button,
            self.belgium_button,
            self.croatia_button,
            self.netherlands_button,
            self.portugal_button,
            self.slovakia_button,
            self.slovenia_button,
            self.romania_button,
            self.bulgaria_button,
            self.hungary_button,
            self.ireland_button,
            self.latvia_button
        ]

        self.buttons = {"Finland": self.finland_button, "France": self.france_button, "Germany": self.germany_button,
                        "Spain": self.spain_button, "Sweden": self.sweden_button, "Poland": self.poland_button,
                        "Italy": self.italy_button,
                        "Czech Republic": self.czechia_button, "Austria": self.austria_button,
                        "Belgium": self.belgium_button,
                        "Croatia": self.croatia_button, "Netherlands": self.netherlands_button,
                        "Portugal": self.portugal_button,
                        "Slovakia": self.slovakia_button, "Slovenia": self.slovenia_button,
                        "Romania": self.romania_button,
                        "Bulgaria": self.bulgaria_button, "Hungary": self.hungary_button,
                        "Republic of Ireland": self.ireland_button,
                        "Latvia": self.latvia_button}

        self.finland_button.setGeometry(600, 200, 75, 75)
        self.finland_button.clicked.connect(self.finland.set_info)

        self.france_button.setGeometry(275, 625, 75, 75)
        self.france_button.clicked.connect(self.france.set_info)

        self.germany_button.setGeometry(400, 520, 75, 75)
        self.germany_button.clicked.connect(self.germany.set_info)

        self.spain_button.setGeometry(130, 775, 75, 75)
        self.spain_button.clicked.connect(self.spain.set_info)

        self.sweden_button.setGeometry(475, 340, 50, 50)
        self.sweden_button.clicked.connect(self.sweden.set_info)

        self.poland_button.setGeometry(550, 475, 75, 75)
        self.poland_button.clicked.connect(self.poland.set_info)

        self.italy_button.setGeometry(440, 700, 30, 30)
        self.italy_button.clicked.connect(self.italy.set_info)

        self.czechia_button.setGeometry(515, 570, 30, 30)
        self.czechia_button.clicked.connect(self.czechia.set_info)

        self.austria_button.setGeometry(510, 625, 30, 30)
        self.austria_button.clicked.connect(self.austria.set_info)

        self.belgium_button.setGeometry(340, 550, 30, 30)
        self.belgium_button.clicked.connect(self.belgium.set_info)

        self.croatia_button.setGeometry(523, 700, 30, 30)
        self.croatia_button.clicked.connect(self.croatia.set_info)

        self.netherlands_button.setGeometry(360, 515, 30, 30)
        self.netherlands_button.clicked.connect(self.netherlands.set_info)

        self.portugal_button.setGeometry(63, 810, 30, 30)
        self.portugal_button.clicked.connect(self.portugal.set_info)

        self.slovakia_button.setGeometry(585, 600, 20,20)
        self.slovakia_button.clicked.connect(self.slovakia.set_info)

        self.slovenia_button.setGeometry(520, 675, 20, 20)
        self.slovenia_button.clicked.connect(self.slovenia.set_info)

        self.romania_button.setGeometry(670, 623, 75, 75)
        self.romania_button.clicked.connect(self.romania.set_info)

        self.bulgaria_button.setGeometry(710, 730, 30, 30)
        self.bulgaria_button.clicked.connect(self.bulgaria.set_info)

        self.hungary_button.setGeometry(590, 635, 30, 30)
        self.hungary_button.clicked.connect(self.hungary.set_info)

        self.ireland_button.setGeometry(157, 460, 30, 30)
        self.ireland_button.clicked.connect(self.ireland.set_info)

        self.latvia_button.setGeometry(650, 370, 30, 30)
        self.latvia_button.clicked.connect(self.latvia.set_info)

    def disable_buttons(self, country_list):
        for i in self.country_buttons:
            i.setDisabled(True)
        for j in country_list:
            self.buttons[j.get_name()].setEnabled(True)