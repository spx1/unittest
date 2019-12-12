import unittest
from foo import a

class TestFoo(unittest.TestCase):
    def test_result(self):
        assert a(2, 3) == 6
        assert a(0, 3) == 0

if __name__ == "__main__":
    unittest.main()