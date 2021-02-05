import unittest


def sort_scores(unsorted_scores: list[int], highest_possible_score: int) -> list[int]:
    all_possible_scores = {}
    sorted_scores = []

    # create a dictionary with all possible scores
    for i in range(highest_possible_score + 1):
        all_possible_scores[i] = 0

    # incremenet the value of each score in the dictionary
    for score in unsorted_scores:
        all_possible_scores[score] += 1

    # iterate through the socre ranges in reverse
    for i in range(highest_possible_score, -1, -1):
        # if the score value is 0 (i.e that score doesnt exist)
        # continue to the next score
        # otherwise add the score to the final list, as many times as it appears
        if all_possible_scores[i] == 0:
            continue

        num_occurences = all_possible_scores[i]
        sorted_scores.extend([i] * num_occurences)

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


unittest.main(verbosity=2)
