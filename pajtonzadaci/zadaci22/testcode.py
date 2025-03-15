from main import FindSurface

if __name__ == "__main__":
    import unittest

    class TestSurface(unittest.TestCase):
        def test_triangle(self):
            self.assertEqual(FindSurface(figure="triangle", a =5, b = 4), 10)
        def test_triangle_decimal(self):
            self.assertEqual(FindSurface(figure = "triangle", a = 5, b = 4.5), 11.25)
            self.assertEqual(FindSurface(figure = "triangle", a = 5.5, b = 4.5), 12.375)
            self.assertEqual(FindSurface(figure = "triangle", a = 5.5, b = 4), 11)
        def test_triangle_errors_decimal_negatives(self):
            self.assertEqual(FindSurface(figure = "triangle", a = 5, b = -4.5), "Error")
            self.assertEqual(FindSurface(figure = "triangle", a = -5, b = 4.5), "Error")
            self.assertEqual(FindSurface(figure = "triangle", a = 5.5, b = -4), "Error")
            self.assertEqual(FindSurface(figure = "triangle", a = -5.5, b = 4), "Error")
            self.assertEqual(FindSurface(figure = "triangle", a = 5.5, b = -4.5), "Error")
            self.assertEqual(FindSurface(figure = "triangle", a = -5.5, b = 4.5), "Error")
            self.assertEqual(FindSurface(figure = "triangle", a = -5.5, b = -4.5), "Error")
        def test_triangle_errors_decimal_zero(self):
            self.assertEqual(FindSurface(figure = "triangle", a = 0, b = 4.5), "Error")
            self.assertEqual(FindSurface(figure = "triangle", a = 5.5, b = 0), "Error")
        def test_triangle_errors_decimal_negatives_zero(self):
            self.assertEqual(FindSurface(figure = "triangle", a = -5.5, b = 0), "Error")
            self.assertEqual(FindSurface(figure = "triangle", a = 0, b = -4.5), "Error")
        def test_triangle_errors_negatives(self):
            self.assertEqual(FindSurface(figure = "triangle", a = -5, b = 4), "Error")
            self.assertEqual(FindSurface(figure = "triangle", a = 5, b = -4), "Error")
        def test_triangle_errors_negatives_zero(self):
            self.assertEqual(FindSurface(figure = "triangle", a = 0, b = -4), "Error")
            self.assertEqual(FindSurface(figure = "triangle", a = -5, b = 0), "Error")
        def test_triangle_errors_zero(self):
            self.assertEqual(FindSurface(figure = "triangle", a = 0, b = 4), "Error")
            self.assertEqual(FindSurface(figure = "triangle", a = 5, b = 0), "Error")
            self.assertEqual(FindSurface(figure = "triangle", a = 0, b = 0), "Error")
    
        def test_square(self):
            self.assertEqual(FindSurface(figure = "square", a = 5), 25)
        def test_square_decimal(self):
            self.assertEqual(FindSurface(figure = "square", a = 2.5), 6.25)
        def test_square_errors_negative(self):
            self.assertEqual(FindSurface(figure = "square", a = -5), "Error")
            self.assertEqual(FindSurface(figure = "square", a = -2.5), "Error")
        def test_square_errors_zero(self):
            self.assertEqual(FindSurface(figure = "square", a = 0), "Error")


    unittest.main()