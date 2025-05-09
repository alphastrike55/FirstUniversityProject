from PyQt6.QtGui import QPixmap

class Country:
    def __init__(self, name, flag, outline, population, capital, currency, language, area, window):
        self.name = name
        self.flag = flag
        self.outline = outline
        self.population = population
        self.capital = capital
        self.currency = currency
        self.language = language
        self.area = area
        self.window = window

    def hint(self, level):
        match level:
            case 1:
                return self.get_population()
            case 2:
                return self.get_capital()
            case 3:
                return self.get_name()

    def set_info(self):
        self.window.country_flag.setPixmap(QPixmap(self.flag))
        self.window.country_flag.setScaledContents(True)
        self.window.country_name.setText(f"Name: {self.name}")
        self.window.country_capital.setText(f"Capital: {self.capital}")
        self.window.country_population.setText(f"Population (M): {self.population}")
        self.window.country_currency.setText(f"Currency: {self.currency}")
        self.window.country_area.setText(f"Area (km²): {self.area}")

    def get_name(self):
        return self.name

    def get_flag(self):
        return self.flag

    def get_outline(self):
        return self.outline

    def get_population(self):
        return self.population

    def get_capital(self):
        return self.capital

    def get_currency(self):
        return self.currency

    def get_language(self):
        return self.language

    def get_area(self):
        return self.area