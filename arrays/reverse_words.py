import unittest


def reverse_words(message: list[str]) -> list[str]:
    if not message:
        return(message)
    
    space_indices = [i for i, elem in enumerate(message) if elem == ' ']
    if not space_indices:
        return(message)

    words_list = []
    start = 0
    for indx in space_indices:
        word = message[start: indx]
        words_list.append(word)
        start = indx + 1
    
    del message[:space_indices[-1] + 1]
    
    for word in reversed(words_list):
        message.extend(' ')
        message.extend(word)
    
    return message

# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
