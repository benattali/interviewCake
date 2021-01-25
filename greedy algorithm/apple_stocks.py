import unittest

def get_max_profit(stock_prices: list[int]) -> int:
    if len(stock_prices) < 2:
        raise ValueError(f'Not enough data to calculate the profit. There are less than 2 stocks')
    
    # initialize buy, sell and best_yield
    buy = stock_prices[0]
    sell = stock_prices[1]
    best_yield = sell - buy
    stock_length = len(stock_prices)

    for i, price in enumerate(stock_prices[1:]):
        # if we are not looking at the last element
            # if the price is lower than the buy
                # set up place holder buy and sell
                # if the place holder buy and sell provide a better yield
                    # set the new buy, sell and best_yield
        # if the price is greater than sell
            # set the new sell amount and calculate the best_yield
        if price < buy and i != stock_length - 2:
            temp_buy = price
            temp_sell = stock_prices[i+2]
            if temp_sell - temp_buy > best_yield:
                buy = temp_buy
                sell = temp_sell
                best_yield = sell - buy
        elif price > sell:
            sell = price
            best_yield = sell - buy

    return best_yield

# Tests

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(ValueError):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(ValueError):
            get_max_profit([1])


unittest.main(verbosity=2)
