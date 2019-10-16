'''
test_toys.py

Unit tests for toy functions.
'''


import unittest
import unittest.mock
import io

import toys as toys

class TestSum(unittest.TestCase):
    def test_inc(self):
        '''
        Test that it can increment an integer
        '''
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            toys.inc(10)
        
        result = fake_stdout.getvalue()
        self.assertEqual(result, '11\n')

    def test_inc_return(self):
        '''
        Test that it can sum two integers
        '''
        result = toys.inc_return(9)
        self.assertEqual(result, 10)

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
        self.assertIs(result, False)

    def test_is_even(self):
        '''
        Test can detect an even number
        '''
        result = toys.is_even(8)
        self.assertIs(result, True)
    
    def test_string(self):
        '''
        Test repeating of string
        '''
        result = toys.string_repeat('hey', 4)
        self.assertEqual(result, 'heyheyheyhey')



if __name__ == '__main__':
    unittest.main()
