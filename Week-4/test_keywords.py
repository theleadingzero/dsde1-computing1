'''
test_keywords.py

Unit tests for functions with keywords.
'''


import unittest

import keywords as k

class TestSum(unittest.TestCase):
    def set_up(self):
        pass


    def test_welcome_message(self):
        '''
        Test welcome_message
        '''
        result = k.welcome_message()
        self.assertEqual(result, "Hello and welcome")
    
    def test_welcome_message_name(self):
        '''
        Test welcome_message
        '''
        result = k.welcome_message(user_name='Sally')
        self.assertEqual(result, "Hello, Sally, and welcome")
    
    def test_welcome_message_place(self):
        '''
        Test welcome_message
        '''
        result = k.welcome_message(place='London')
        self.assertEqual(result, "Hello and welcome to London")

    def test_welcome_message_name_place(self):
        '''
        Test welcome_message
        '''
        result = k.welcome_message(user_name='Sally', place='London')
        self.assertEqual(result, "Hello, Sally, and welcome to London")

    def test_list_average(self):
        '''
        Test list_average
        '''
        result = k.list_average([])
        self.assertEqual(result, 0)

    def test_list_average1(self):
        '''
        Test list_average
        '''
        result = k.list_average([1,2,3,4,5,6,7,8,9])
        self.assertEqual(result, 5)

    def test_list_median(self):
        '''
        Test list_average
        '''
        result = k.list_average([], "median")
        self.assertEqual(result, None)


    def test_list_median1(self):
        '''
        Test list_average
        '''
        result = k.list_average([1,9,1,8,2,4,5,2,4,7,5,5,3], "median")
        self.assertEqual(result, 4)

    def test_list_mode(self):
        '''
        Test list_average
        '''
        result = k.list_average([], "mode")
        self.assertEqual(result, [])


    def test_list_mode1(self):
        '''
        Test list_average
        '''
        result = k.list_average([1,9,1,8,2,4,5,2,4,7,5,5,3], "mode")
        self.assertEqual(result, [5])

 
    def test_list_mode2(self):
        '''
        Test list_average
        '''
        result = k.list_average([1,9,1,8,2,4,5,2,11,4,7,5,5,3,11,11], "mode")
        self.assertEqual(set(result), set([5,11]))

 


if __name__ == '__main__':
    unittest.main()
