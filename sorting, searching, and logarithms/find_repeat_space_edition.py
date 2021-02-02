import unittest


def find_repeat(numbers: list[int]) -> int:
    if len(numbers) < 2:
        raise ValueError('The list contains less than 2 numbers')

    numbers.sort()
    previous_num = numbers[0]

    for num in numbers[1:]:
        if num == previous_num:
            return num
        previous_num = num
    
    return None

# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)
    
    def test_no_duplicates(self):
        actual = find_repeat([1,2,3,4])
        expected =  None
        self.assertEqual(actual, expected)
    
    def test_list_with_zeros(self):
        actual = find_repeat([0,1,2,3,2])
        expected = 2
        self.assertEqual(actual, expected)
    
    def test_multiple_duplicates(self):
        actual = find_repeat([1,1,3,4,5,4,8])
        expected = 1
        self.assertEqual(actual, expected)
    
    def test_negative_ints_positive_result(self):
        actual = find_repeat([-1, 3, 3, 0])
        expected = 3
        self.assertEqual(actual, expected)

    def test_negative_ints_negative_result(self):
        actual = find_repeat([-1, 3, -1, 0])
        expected = -1
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(ValueError):
            find_repeat([])
    
    def test_error_with_1_number(self):
        with self.assertRaises(ValueError):
            find_repeat([1])


unittest.main(verbosity=2)
