def CalculateCheckout(prices):
    total_price_no_discount = sum(prices)
    if len(prices) > 3:
        discount_percentage = 10
        discount = total_price_no_discount * (discount_percentage / 100)
        discounted_price = total_price_no_discount - discount
        print(discounted_price)
        tax_percentage = 5
        tax = discounted_price * (tax_percentage / 100)
        price_with_tax = discounted_price + tax
        return price_with_tax
    else:
        tax_percentage_b = 5
        tax_b = total_price_no_discount * (tax_percentage_b / 100)
        price_with_tax_b = total_price_no_discount + tax_b
        return price_with_tax_b


if __name__ == "__main__":
    import unittest

    class TestCalculateCheckout(unittest.TestCase):
        def test_total_price(self):
            self.assertEqual(CalculateCheckout([10, 20, 5, 3, 7]), 42.525)
            self.assertEqual(CalculateCheckout([10, 20]), 31.5)

        def test_single_price(self):
            self.assertEqual(CalculateCheckout([10]), 10.5)

        def test_empty_list(self):
            self.assertEqual(CalculateCheckout([]), 0)


    unittest.main()
