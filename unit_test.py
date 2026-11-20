import unittest
import operations as calc
import main 

class TestCalculatorOperations(unittest.TestCase):

    def setUp(self):
        main.btn_clear()
        main.memory_clear()

    def test_divide_by_zero(self):
        self.assertEqual(calc.divide(10, 0), "Ошибка: деление на 0")
        self.assertEqual(calc.modulo(10, 0), "Ошибка: деление на 0")

    def test_sqrt(self):
        self.assertEqual(calc.Sqrt(16), 4)
        self.assertEqual(calc.Sqrt(-4), "Ошибка: корень из отрицательного")

    def test_floor_and_ceil(self):
        self.assertEqual(calc.Floor(4.9), 4)
        self.assertEqual(calc.Ceil(4.1), 5)

    def test_trigonometry(self):
        self.assertAlmostEqual(calc.Sin(30), 0.5, places=5)
        self.assertAlmostEqual(calc.Cos(60), 0.5, places=5)

#тесты на память
    
    def test_memory_operations(self):
        main.input_text.set("10.5")
        main.memory_add()
        
        main.input_text.set("0")
        main.memory_recall()
        self.assertEqual(main.input_text.get(), "10.5")

        main.input_text.set("5.5")
        main.memory_subtract()
        main.memory_recall()
        self.assertEqual(main.input_text.get(), "5")

    def test_long_expression(self):
        main.input_text.set("Sin(30) + Sqrt(16) * 2")
        main.equal()
        self.assertEqual(main.input_text.get(), "8.5")

    def test_security_eval(self):
        main.input_text.set("__import__('os').system('clear')")
        main.equal()
        self.assertEqual(main.input_text.get(), "Ошибка")

if __name__ == '__main__':
    unittest.main()
