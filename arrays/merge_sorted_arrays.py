import unittest
import itertools


def compare_tuple_to_last_list_element(
    merged_list: list[int], smaller: int, larger: int
) -> None:
    if merged_list and smaller > merged_list[-1]:
        merged_list.extend([smaller, larger])
    else:
        merged_list.insert(-1, smaller)
        merged_list.append(larger)


def merge_lists(my_list: list[int], alices_list: list[int]) -> list[int]:
    merged_list = []

    # iterate through two lists simultaneously until the longer list is done
    for list_elems in itertools.zip_longest(my_list, alices_list):
        first = list_elems[0]
        second = list_elems[1]

        if not first and not second:
            continue

        if (not first and not merged_list) or (not first and second > merged_list[-1]):
            merged_list.append(second)
        elif (not second and not merged_list) or (
            not second and first > merged_list[-1]
        ):
            merged_list.append(first)
        elif not first and second <= merged_list[-1]:
            merged_list.insert(-1, second)
        elif not second and first <= merged_list[-1]:
            merged_list.insert(-1, first)
        else:
            if first > second:
                compare_tuple_to_last_list_element(
                    merged_list=merged_list, smaller=second, larger=first
                )
            else:
                compare_tuple_to_last_list_element(
                    merged_list=merged_list, smaller=first, larger=second
                )

    return merged_list


# Tests


class Test(unittest.TestCase):
    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
