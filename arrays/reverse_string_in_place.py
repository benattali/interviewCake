import unittest


def reverse(list_of_chars: list[str]) -> list[str]:
    loop_length = len(list_of_chars) - 1
    
    for i in range(loop_length):
        index_to_move = -2 - i
        char_to_move = list_of_chars.pop(index_to_move)
        list_of_chars.append(char_to_move)
    
    return list_of_chars

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
