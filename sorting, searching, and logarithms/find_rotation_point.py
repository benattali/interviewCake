import unittest


def find_rotation_point(words: list[str]) -> int:
    if len(words) < 2:
        raise ValueError("The words list has less than 2 words in it")

    floor_index = 0
    ceiling_index = len(words) - 1

    while True:
        # if there is only 1 element between the floor_index and ceiling_index
        # and if the element at the ceiling_index is greater than the words[0]
        # return the ceiling_index
        if len(words[floor_index:ceiling_index]) == 1:
            if words[ceiling_index] < words[0]:
                return ceiling_index
            else:
                return -1

        # find the midway point between floor_index and ceiling_index
        mid_point = (ceiling_index + floor_index) // 2

        # if the word at the midway point is smaller than words[0]
        # then the rotation point is either to the left of the mid_point or the mid_point
        # assign ceiling_index to mid_point, so in the next iteration we look only up to the mid_point (cutting the list in half)
        # otherwise
        # assign the floor_index to the mid_point, so in the next iteration we look from the mid_point to the ceiling_index (again curring the list in half)
        if words[mid_point] < words[0]:
            ceiling_index = mid_point
        else:
            floor_index = mid_point

    return -1


# Tests


class Test(unittest.TestCase):
    def test_small_list(self):
        actual = find_rotation_point(["cape", "cake"])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(["grape", "orange", "plum", "radish", "apple"])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(
            [
                "ptolemaic",
                "retrograde",
                "supplant",
                "undulate",
                "xenoepist",
                "asymptote",
                "babka",
                "banoffee",
                "engender",
                "karpatka",
                "othellolagkage",
            ]
        )
        expected = 5
        self.assertEqual(actual, expected)

    def test_rotation_point_last_word(self):
        actual = find_rotation_point(["quartz", "row", "speed", "total", "canada"])
        expected = 4
        self.assertEqual(actual, expected)

    def test_rotation_point_last_word(self):
        actual = find_rotation_point(["canada", "quartz", "row", "speed", "total"])
        expected = -1
        self.assertEqual(actual, expected)

    def test_odd_elements_in_list(self):
        actual = find_rotation_point(["f", "j", "l", "c", "d"])
        expected = 3
        self.assertEqual(actual, expected)

    def test_even_elements_in_list(self):
        actual = find_rotation_point(["f", "j", "l", "c", "d", "e"])
        expected = 3
        self.assertEqual(actual, expected)

    def test_rotation_point_directly_left_of_middle(self):
        actual = find_rotation_point(["r", "a", "d", "k", "o"])
        expected = 1
        self.assertEqual(actual, expected)

    def test_rotation_point_directly_right_of_middle(self):
        actual = find_rotation_point(["r", "u", "z", "k", "o"])
        expected = 3
        self.assertEqual(actual, expected)

    def test_rotation_point_is_middle(self):
        actual = find_rotation_point(["r", "u", "d", "k", "o"])
        expected = 2
        self.assertEqual(actual, expected)

    def test_error_with_empty_words(self):
        with self.assertRaises(ValueError):
            find_rotation_point([])

    def test_error_with_one_word(self):
        with self.assertRaises(ValueError):
            find_rotation_point(["middle"])


unittest.main(verbosity=2)
