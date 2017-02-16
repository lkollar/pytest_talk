import unittest

def func(x):
    return x + 1

class TestClass(unittest.TestCase):
    def test_func(self):
        self.assertEqual(5, func(3))

if __name__ == '__main__':
    unittest.main()
