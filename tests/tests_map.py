import unittest
import sys
from PyQt6.QtWidgets import QApplication
from src.map import MapWindow
from src.country import Country

app = QApplication(sys.argv)


class TestMapWindow(unittest.TestCase):
    def setUp(self):
        self.window = MapWindow()

    def test_window_instantiation(self):
        self.assertIsInstance(self.window, MapWindow)

    def test_country_in_map_list(self):
        self.assertIn(self.window.latvia_button, self.window.country_buttons)
        self.assertIn(self.window.ireland_button, self.window.country_buttons)
        self.assertIn(self.window.finland_button, self.window.country_buttons)

    def test_button_is_enabled(self):
        countries = [
            Country("Finland", "assets/flags/Flag_of_Finland.png", "assets/outlines/fi-01.jpg", 5.58, "Helsinki",
                    "Euro", "Finnish",
                    338.462, self),
            Country("France", "assets/flags/Flag_of_France.png", "assets/outlines/fr-01.jpg", 68.29, "Paris", "Euro",
                    "French", 551.695,
                    self),
            Country("Germany", "assets/flags/Flag_of_Germany.png", "assets/outlines/de-01.jpg", 83.28, "Berlin", "Euro",
                    "German",
                    357.592, self)]

        self.window.disable_buttons(countries)
        for country in countries:
            button = self.window.buttons[country.get_name()]
            self.assertTrue(button.isEnabled())
        for country in self.window.buttons:
            if self.window.buttons[country] not in [self.window.buttons[c.get_name()] for c in countries]:
                self.assertFalse(self.window.buttons[country].isEnabled())