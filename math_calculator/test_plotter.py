import unittest
import os
import shutil
from utils.plotter import plot_function

class TestPlotFunction(unittest.TestCase):

    def setUp(self):
        self.test_dir = "test_output"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_valid_expression(self):
        expr = "np.sin(x)"
        x_range = (-3.14, 3.14)
        path = plot_function(expr, x_range, self.test_dir)
        self.assertTrue(os.path.exists(path))
        self.assertTrue(path.endswith("plot.png"))

    def test_invalid_expression(self):
        expr = "np.unknown_func(x)"
        x_range = (0, 1)
        with self.assertRaises(ValueError) as context:
            plot_function(expr, x_range, self.test_dir)
        self.assertIn("Помилка у виразі", str(context.exception))

    def test_math_expression(self):
        expr = "x**2 + 3*x - 5"
        x_range = (-10, 10)
        path = plot_function(expr, x_range, self.test_dir)
        self.assertTrue(os.path.isfile(path))

if __name__ == "__main__":
    unittest.main()
