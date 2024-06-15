import unittest
from sea_level_predictor import draw_plot

class TestSeaLevelPredictor(unittest.TestCase):
    def test_draw_plot(self):
        ax = draw_plot()
        self.assertIsNotNone(ax)
        self.assertEqual(ax.get_title(), 'Rise in Sea Level')
        self.assertEqual(ax.get_xlabel(), 'Year')
        self.assertEqual(ax.get_ylabel(), 'Sea Level (inches)')

if __name__ == "__main__":
    unittest.main()
