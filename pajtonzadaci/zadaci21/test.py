from weightIndex import ideal_BMI


if __name__ == "__main__":
    import unittest

    class TestBMI(unittest.TestCase):
        def test_female_BMI(self):
            self.assertEqual(ideal_BMI("f", 180, 70), "yes")
            self.assertEqual(ideal_BMI("f", 180, 69), "no")
            self.assertEqual(ideal_BMI("f", 170, 70), "no")
        def test_female_zero(self):
            self.assertEqual(ideal_BMI("f", 0, 70), "no")
            self.assertEqual(ideal_BMI("f", 180, 0), "no")
        def test_female_negative_BMI(self):
            self.assertEqual(ideal_BMI("f", -180, 70), "no")
            self.assertEqual(ideal_BMI("f", 180, -70), "no")

        def test_male_BMI(self):
            self.assertEqual(ideal_BMI("m", 180, 80), "yes")
            self.assertEqual(ideal_BMI("m", 180, 79), "no")
            self.assertEqual(ideal_BMI("m", 170, 80), "no")
        def test_male_zero(self):
            self.assertEqual(ideal_BMI("m", 0, 80), "no")
            self.assertEqual(ideal_BMI("m", 180, 0), "no")
        def test_male_negative_BMI(self):
            self.assertEqual(ideal_BMI("m", -180, 80), "no")
            self.assertEqual(ideal_BMI("m", 180, -80), "no")
        

    unittest.main()