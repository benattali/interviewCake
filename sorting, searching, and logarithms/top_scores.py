import unittest


def sort_scores(unsorted_scores: list[int], highest_possible_score: int) -> list[int]:
    all_possible_scores = {}
    sorted_scores = []

    # create a dictionary with all possible scores as the keys
    for i in range(highest_possible_score + 1):
        all_possible_scores[i] = 0

    # increment the scores
    for score in unsorted_scores:
        all_possible_scores[score] += 1

    # add the scores to the sorted list in a descending order
    for score in range(highest_possible_score, -1, -1):
        if all_possible_scores[score]:
            add_scores = [score] * all_possible_scores[score]
            sorted_scores.extend(add_scores)

    return sorted_scores


# Tests


class Test(unittest.TestCase):
    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)

    def test_score_of_zero(self):
        actual = sort_scores([3, 6, 0, 3, 4, 9], 10)
        expected = [9, 6, 4, 3, 3, 0]
        self.assertEqual(actual, expected)

    def test_score_of_highgest_value(self):
        actual = sort_scores([3, 6, 10, 3, 4, 9], 10)
        expected = [10, 9, 6, 4, 3, 3]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
