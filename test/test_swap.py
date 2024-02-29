import unittest
from src.swap import swap

class TestSwapFunction(unittest.TestCase):

    def test_swap_integers(self):
        # Test swapping two integers
        a, b = 10, 20
        swapped_a, swapped_b = swap(a, b)
        self.assertEqual(swapped_a, 20)
        self.assertEqual(swapped_b, 10)

    def test_swap_strings(self):
        # Test swapping two strings
        x, y = "hello", "world"
        swapped_x, swapped_y = swap(x, y)
        self.assertEqual(swapped_x, "world")
        self.assertEqual(swapped_y, "hello")

    def test_swap_mixed_types(self):
        # Test swapping variables of different types
        a, b = 123, "abc"
        swapped_a, swapped_b = swap(a, b)
        self.assertEqual(swapped_a, "abc")
        self.assertEqual(swapped_b, 123)

if __name__ == '__main__':
    unittest.main()
  
