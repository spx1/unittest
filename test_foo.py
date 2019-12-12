import unittest
from foo import a

class TestFoo(unittest.TestCase):
    def test_result(self):
        self.assertEqual(a(2, 3), 6)
        self.assertEqual(a(0, 3), 0)

if __name__ == "__main__":
    unittest.main()