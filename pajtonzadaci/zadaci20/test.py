from addition import AdditionFunction

if __name__ == "__main__":
    import unittest

    class TestAddition(unittest.TestCase):
        def test_single_digit(self):
            self.assertEqual(AdditionFunction(2, 4), 6)
        def test_double_digits(self):
            self.assertEqual(AdditionFunction(23, 18), 41)
        def test_negative_num(self):
            self.assertEqual(AdditionFunction(-1, -5), -6)
        def test_negative_n_positive_num(self):
            self.assertEqual(AdditionFunction(-6, 3), -3)
        def test_zero(self):
            self.assertEqual(AdditionFunction(0, 0), 0)
            self.assertEqual(AdditionFunction(1, 0), 1)
            self.assertEqual(AdditionFunction(-1, 0), -1)

            
    unittest.main()
