'''
test_toys.py

Unit tests for structures functions.
'''


import unittest
import unittest.mock
import io

import structures as st

class TestSum(unittest.TestCase):
    def set_up(self):
        pass


    def test_first_and_last(self):
        '''
        Test first_and_last function
        '''
        result = st.first_and_last([0,1,2,3])
        self.assertEqual(result, [0,3])

    def test_part_reverse(selff):
        '''
        Test
        '''
        result = st.part_reverse([0,1,2,3,4,5], 1, 4)
        self.assertEqual(result, [3,2,1])

    def test_repeat_at_index(self):
        '''
        Test 
        '''
        result = st.repeat_at_index([0,1,2,3,4,5,6], 3)
        self.assertEqual(result, [0,1,2,3,3,3,4,5,6])

    def test_palindrome_word1(self):
        '''
        Test palindrome word
        '''
        resutl = st.palindrome_word("madam")
        self.asserIs(result, True)

    def test_palindrome_word2(self):
        '''
        Test palindrome word
        '''
        resutl = st.palindrome_word("Madam")
        self.asserIs(result, True)

    def test_palindrome_word3(self):
        '''
        Test palindrome word
        '''
        resutl = st.palindrome_word("palindrome")
        self.asserIs(result, False)


    def test_palindrome_sentence1(self):
        '''
        Test palindrome sentence
        '''
        resutl = st.palindrome_word("Was it a car or a cat I saw")
        self.asserIs(result, True)

    def test_palindrome_sentence2(self):
        '''
        Test palindrome sentence
        '''
        resutl = st.palindrome_word("Random sentence")
        self.asserIs(result, False)

    def test_palindrome_sentence3(self):
        '''
        Test palindrome sentence
        '''
        resutl = st.palindrome_word(" Do geese see God  ")
        self.asserIs(result, True)

    def test_concatenate_sentences1(self):
        '''
        Test sentence concatenation
        '''
        result = st.concatenate_sentences("First sentence.", "Second sentence.")
        self.assertEquual(results, "First sentence. Second sentence.")

     #def test_concatenate_sentences2(self):
     #   '''
     #   Test sentence concatenation
     #   '''
     #   result = st.concatenate_sentences("first sentence.", "Second sentence.")
     #   self.assertRaises(ValueError,

    def test_index_exists1(self):
        '''
        Test 
        '''
        result = st.index_exists({"ind1": "val1", "ind2": "val2"} , "ind1")
        self.assertIs(result, True)

    def test_index_exists2(self):
        '''
        Test 
        '''
        result = st.index_exists({"ind1": "val1", "ind2": "val2"} , "ind3")
        self.assertIs(result, False)

    def test_value_exists1(self):
        '''
        Test 
        '''
        result = st.value_exists({"ind1": "val1", "ind2": "val2"} , "val1")
        self.assertIs(result, True)

    def test_index_exists2(self):
        '''
        Test 
        '''
        result = st.value_exists({"ind1": "val1", "ind2": "val2"} , "val3")
        self.assertIs(result, False)


    def test_merge_dictionaries(self):
        '''
        Test
        '''
        result = st.merge_dictionaries({"a": 1, "c": 3}, {"b:" 2, "d": 4})
        self.assertEqual(result, {"a": 1, "c": 3, "b:" 2, "d": 4})




if __name__ == '__main__':
    unittest.main()
