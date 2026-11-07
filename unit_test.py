import unittest
import operations as calc

class TestCalculatorOperations(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calc.multiply(4, 3), 12)
        self.assertEqual(calc.multiply(-2, 5), -10)
        self.assertEqual(calc.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertEqual(calc.divide(10, 0), "Ошибка: деление на 0")

    def test_modulo(self):
        self.assertEqual(calc.modulo(10, 3), 1)
        self.assertEqual(calc.modulo(10, 0), "Ошибка: деление на 0")

    def test_degree(self):
        self.assertEqual(calc.degree(2, 3), 8)
        self.assertEqual(calc.degree(5, 0), 1)
        self.assertEqual(calc.degree(5, -1), 0.2)

    def test_sqrt(self):
        self.assertEqual(calc.Sqrt(16), 4)
        self.assertEqual(calc.Sqrt(0), 0)
        self.assertEqual(calc.Sqrt(-4), "Ошибка: корень из отрицательного")

    def test_floor(self):
        self.assertEqual(calc.Floor(4.9), 4)
        self.assertEqual(calc.Floor(4.1), 4)
        self.assertEqual(calc.Floor(-4.1), -5)

    def test_ceil(self):
        self.assertEqual(calc.Ceil(4.1), 5)
        self.assertEqual(calc.Ceil(4.9), 5)
        self.assertEqual(calc.Ceil(-4.1), -4)

    def test_trigonometry(self):
        self.assertAlmostEqual(calc.Sin(30), 0.5, places=5)
        self.assertAlmostEqual(calc.Sin(0), 0.0, places=5)
        self.assertAlmostEqual(calc.Cos(60), 0.5, places=5)
        self.assertAlmostEqual(calc.Cos(0), 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
