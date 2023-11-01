import unittest

def add(x, y):
    return x + y

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_mixed_numbers(self):
        result = add(2, -3)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
