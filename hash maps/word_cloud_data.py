import unittest
import re


class WordCloudData(object):
    def __init__(self, input_string: str):
        self.input_string = input_string
        self.words_to_counts = {}

    def count_words(self) -> dict:
        punctuation = ['.', ',', '!', '?', ':']
        # replace all the punctuation with a space
        # then transform the string to lower case letters and
        # add a space at the end (so we can check the final word)
        for punc in punctuation:
            self.input_string = self.input_string.replace(punc, ' ')
        self.input_string = self.input_string.lower() + ' '

        word = ''
        for char in self.input_string:
            if char == ' ' :
                if not word or word == '-':
                    word = ''
                    continue
                try:
                    self.words_to_counts[word] += 1
                except KeyError:
                    self.words_to_counts[word] = 1
                finally:
                    word = ''
            else:
                word += char
        
        return self.words_to_counts

# Tests

class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.count_words()

        expected = {'i': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.count_words()

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.count_words()

        expected = {'cake': 1, 'strawberry': 1, 'short': 1, 'yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.count_words()

        expected = {'cake': 1, 'dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.count_words()

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.count_words()

        expected = {"bakery": 1, "cakes": 1, "allie's": 1, "sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
