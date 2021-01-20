import unittest


def has_palindrome_permutation(the_string):
    char_count = {}

    for char in the_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    num_of_odd_counts = 0
    for value in char_count.values():
        if value % 2 != 0:
            if len(the_string) % 2 == 0:
                return False
            else:
                num_of_odd_counts += 1
                if num_of_odd_counts > 1:
                    return False

    return True

# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
