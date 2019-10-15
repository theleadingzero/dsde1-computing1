'''
test_toys.py

Unit tests for toy functions.
'''


import unittest

import toys as toys

class TestSum(unittest.TestCase):
    def test_inc(self):
        '''
        Test that it can increment an integer
        '''
        result = toys.inc_return(10)
        self.assertEqual(result, 11)

    def test_sum(self):
        '''
        Test that it can sum two integers
        '''
        result = toys.sum(3, 1)
        self.assertEqual(result, 4)

    def test_sum_inc(self):
        '''
        Test it can increment the sum of two integers
        '''
        result = toys.sum_inc(3, 1)
        self.assertEqual(result, 5)

    def test_is_odd(self):
        '''
        Test can detect an odd number
        '''
        result = toys.is_even(5)
        self.assertFalse(result)

    def test_is_even(self):
        '''
        Test can detect an even number
        '''
        result = toys.is_even(8)
        self.assertTrue(result)
    
    def test_string(self):
        '''
        Test repeating of string
        '''
        result = toys.string_repeat('hey', 4)
        self.assertEqual(result, 'heyheyheyhey')



if __name__ == '__main__':
    unittest.main()