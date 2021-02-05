import unittest


def can_two_movies_fill_flight(movie_lengths: list[int], flight_length: int) -> bool:
    if not movie_lengths:
        return False

    length_complements = {}
    count = 0

    # create a dictionary with the complement movie lengths (i.e the flight length - the movie length)
    for i, length in enumerate(movie_lengths):
        length_complements[i] = flight_length - length

    for length in movie_lengths:
        # if the length is half the flight time (edge case), then you have to make sure there are at least 2 elements of that length
        # incremenet the count by 1
        # if the count is 2 or more, return True
        # otherwise if the length is in the complements dictionary it means that there is a movie length which will add up to the total flight time
        # so return True
        if length == flight_length / 2:
            count += 1
            if count >= 2:
                return True
        elif length in length_complements.values():
            return True

    return False


# Tests


class Test(unittest.TestCase):
    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_movie(self):
        result = can_two_movies_fill_flight([4, 3, 2], 5)
        self.assertTrue(result)

    def test_multiple_movies_shorter_than_flight(self):
        result = can_two_movies_fill_flight([5, 6, 7, 8], 9)
        self.assertFalse(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)
