'''
test_pendulum.py

Unit tests for pendulum function.
'''

import unittest
import pendulum as pen

class TestSum(unittest.TestCase):
    def test_valid_input(self):
        '''
        Test two valid number inputs
        '''
        result = pen.period(3.3, 9.81)
        self.assertAlmostEqual(result, 3.6442010977180623)


    def test_string_input(self):
        '''
        Test two valid number inputs
        '''
        with self.assertRaises(TypeError):
            pen.period('hi', 3)
        
        with self.assertRaises(TypeError):
            pen.period(3, 'hi')
        
    def test_zero_gravity(self):
        '''
        Test when gravity is 0
        '''
        with self.assertRaises(ValueError):
            pen.period(5, 0)


if __name__ == '__main__':
    unittest.main()