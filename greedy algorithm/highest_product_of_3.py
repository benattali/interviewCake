import unittest


def highest_product_of_3(list_of_ints: list[int]) -> int:
    if len(list_of_ints) < 3:
        raise ValueError("The list provided has less than 3 numbers")

    # create 2 lists of numbers, one for the negative case, one for the positive case
    # and sort both
    first = list_of_ints[0]
    second = list_of_ints[1]
    third = list_of_ints[2]
    largest_nums = [first, second, third]
    negative_list = [first, second, third]
    largest_nums.sort()
    negative_list.sort()

    if len(list_of_ints) >= 3:
        for num in list_of_ints[3:]:
            # if num is negative
                # if num is less than the first element of negative_list
                    # assign the first element of negative_list to num
                # if num is less than the second element of negative_list
                    # assing the second element of negative_list to num
            # if num is greater than the smallest element in largest_nums
                # assign the first element (smallest number) to num, then sort the list
            if num < 0:
                if num < negative_list[0]:
                    negative_list[0] = num
                elif num < negative_list[1]:
                    negative_list[1] = num
            if num > largest_nums[0]:
                largest_nums[0] = num
                largest_nums.sort()

    largest_product_positive = 1
    largest_product_negative = 1
    for i in range(len(largest_nums)):
        largest_product_positive *= largest_nums[i]
        largest_product_negative *= negative_list[i]

    max_product = max(largest_product_negative, largest_product_positive)
    return max_product

# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
