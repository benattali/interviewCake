import unittest


def reverse(list_of_chars: list[str]):
    for i in range(len(list_of_chars) // 2):
        # loop only up until the middle of the middle (rounding down)
        # then find the elements in complementing positions to each other (i.e elem[0] and elem[-1], elem[1] and elem[-2])
        # and switch them so elem[0] now becomes elem[-1] and vice versa
        left_side = list_of_chars[i]
        right_side = list_of_chars[-1 - i]
        list_of_chars[i] = right_side
        list_of_chars[-1 - i] = left_side

# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)
