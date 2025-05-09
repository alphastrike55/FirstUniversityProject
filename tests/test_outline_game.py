import unittest
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap
from src.gamemode_outline import OutlineGameWindow

app = QApplication(sys.argv)

def point_add(var):
    points = 0
    match var:
        case 0:
            points += 1
            return points
        case 1:
            points += 0.75
            return points
        case 2:
            points += 0.5
            return points

class TestOutlineGameWindow(unittest.TestCase):
    def setUp(self):
        self.main_window = OutlineGameWindow()

    def test_point_add(self):
        self.assertEqual(point_add(0), 1)
        self.assertEqual(point_add(1), 0.75)
        self.assertEqual(point_add(2), 0.5)

    def test_initial_answer_is_None(self):
        self.assertIsNone(self.main_window.answer)

    def test_country_in_map_list(self):
        self.assertIn(self.main_window.latvia, self.main_window.countries)
        self.assertIn(self.main_window.finland, self.main_window.countries)
        self.assertIn(self.main_window.ireland, self.main_window.countries)

if __name__ == "__main__":
    unittest.main()