import unittest
from utils.math_ops import basic_operations, solve_equation

class TestMathOps(unittest.TestCase):

    def test_basic_op(self):
        self.assertEqual(basic_operations(5, 3, '+'), 8.0)
        self.assertEqual(basic_operations(5, 3, '-'), 2.0)
        self.assertEqual(basic_operations(5, 3, '*'), 15.0)
        self.assertEqual(basic_operations(6, 2, '/'), 3.0)
        self.assertEqual(basic_operations(6, 0, '/'), "Ділення на нуль")
        self.assertEqual(basic_operations(6, 2, '^'), "Невідома операція")

    def test_solve_lin_eq(self):
        self.assertEqual(solve_equation("лінійне", [2, -4]), "x = 2.0")
        self.assertEqual(solve_equation("лінійне", [0, 0]), "Безліч розв'язків")
        self.assertEqual(solve_equation("лінійне", [0, 3]), "Немає розв'язку")
        with self.assertRaises(ValueError):
            solve_equation("лінійне", [1])

    def test_solve_quadratic_eq(self):
        self.assertEqual(solve_equation("quadratic", [1, -3, 2]), "x₁ = 2.0, x₂ = 1.0")
        self.assertEqual(solve_equation("quadratic", [1, 2, 1]), "x = -1.0")
        self.assertEqual(solve_equation("quadratic", [1, 0, 1]), "Немає дійсних коренів")
        with self.assertRaises(ValueError):
            solve_equation("quadratic", [1, 2])

    def test_unknown_eq_type(self):
        with self.assertRaises(ValueError):
            solve_equation("log", [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
