import unittest
import math


def get_products_of_all_ints_except_at_index(int_list: list[int]) -> list[int]:
    list_length = len(int_list)
    if list_length < 2:
        raise ValueError("There are not enough numbers to calculate the product.")

    # initialize the final list which will be the same length as the original list
    products_all_ints_except_index = [None] * list_length

    # find the product of all the ints prior to the current index
    # initialize the product at index 0 to 1 (since it doesnt have any ints prior to it)
    product = 1
    for i in range(list_length):
        products_all_ints_except_index[i] = product
        product *= int_list[i]
    
    # multiply the int at current index of products_all_ints_except_index by the product
    product = 1
    for i in range(list_length - 1, -1, -1):
        products_all_ints_except_index[i] *= product
        product *= int_list[i]

    return products_all_ints_except_index

# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)
