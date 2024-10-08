import unittest
from main import root, entry1, entry2, button_add, button_subtract, button_multiply, button_divide, result_label


class TestCalculatorInterface(unittest.TestCase):

    def setUp(self):
        """Підготовка інтерфейсу перед кожним тестом"""
        root.update()  # Оновлення інтерфейсу перед тестом

    def test_addition(self):
        """Тест додавання через інтерфейс"""
        entry1.delete(0, "end")
        entry2.delete(0, "end")
        entry1.insert(0, "5")
        entry2.insert(0, "3")

        button_add.invoke()  # Імітуємо натискання кнопки додавання
        self.assertEqual(result_label.cget("text"), "Результат: 8.0")

    def test_subtraction(self):
        """Тест віднімання через інтерфейс"""
        entry1.delete(0, "end")
        entry2.delete(0, "end")
        entry1.insert(0, "10")
        entry2.insert(0, "3")

        button_subtract.invoke()  # Імітуємо натискання кнопки віднімання
        self.assertEqual(result_label.cget("text"), "Результат: 7.0")

    def test_multiplication(self):
        """Тест множення через інтерфейс"""
        entry1.delete(0, "end")
        entry2.delete(0, "end")
        entry1.insert(0, "4")
        entry2.insert(0, "2")

        button_multiply.invoke()  # Імітуємо натискання кнопки множення
        self.assertEqual(result_label.cget("text"), "Результат: 8.0")

    def test_division(self):
        """Тест ділення через інтерфейс"""
        entry1.delete(0, "end")
        entry2.delete(0, "end")
        entry1.insert(0, "10")
        entry2.insert(0, "2")

        button_divide.invoke()  # Імітуємо натискання кнопки ділення
        self.assertEqual(result_label.cget("text"), "Результат: 5.0")

    def tearDown(self):
        """Закриття інтерфейсу після кожного тесту"""
        root.update()


if __name__ == '__main__':
    unittest.main()
