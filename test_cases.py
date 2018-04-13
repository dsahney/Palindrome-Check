import unittest
import algorithm1
# import algorithm2
# import algorithm3

class algorithm1_test(unittest.TestCase):
    ''' Checks the functions in algorithm1 to ensure they are working as desired. '''
    def test_reverse_ex1(self):
        ''' Ensures function reverse, reverses a string. '''
        actual = algorithm1.reverse('apple')
        expected = 'elppa'
        self.assertEqual(actual, expected)
        
    def test_reverse_ex2(self):
        ''' Ensures function reverse, reverses a string. '''
        actual = algorithm1.reverse('strts')
        expected = 'strts'
        self.assertEqual(actual, expected)
        
    def test_pal_check_1_ex1(self):
        ''' Ensures function pal_check_1, reports whether a string is a palindrome or not. '''
        actual = algorithm1.pal_check_1('strts')
        expected = True
        self.assertEqual(actual, expected)
        
    def test_pal_check_1_ex2(self):
        ''' Ensures function pal_check_1, reports whether a string is a palindrome or not. '''
        actual = algorithm1.pal_check_1('asdf')
        expected = False
        self.assertEqual(actual, expected)
        
if _name_ == '_main_':
    unittest.main(exit=False)
