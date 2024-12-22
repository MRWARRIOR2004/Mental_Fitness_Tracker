import unittest
from PyQt5.QtWidgets import QApplication
from app.main import MentalFitnessTracker

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.window = MentalFitnessTracker()

    def test_initial_state(self):
        self.assertEqual(self.window.result_label.text(), "")

    def test_prediction(self):
        # Set the age input
        self.window.age_input.setText("25")
        self.window.predict()
        # Check if result_label is updated (you might need to adjust the expected value)
        self.assertNotEqual(self.window.result_label.text(), "")

if __name__ == '__main__':
    unittest.main()