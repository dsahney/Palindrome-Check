import unittest
import reverse
import algorithm1
import algorithm2
import algorithm3

# Test cases for function reverse
class revese_test(unittest.TestCase):
    ''' Checks the reverse function, to ensure it works as desired. '''
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

# Test cases for algorithm 1
class algorithm1_test(unittest.TestCase):
    ''' Checks the functions in algorithm1, to ensure they are working as desired. '''
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
        
# Test cases for algorithm 2
class algorithm2_test(unittest.TestCase):
    ''' Checks the functions in algorithm2, to ensure they are working as desired. '''
    def test_pal_check_2_ex1(self):
        ''' Ensures function pal_check_2, reports whether a string is a palindrome or not. '''
        actual = algorithm2.pal_check_2('asdsa')
        expected = True
        self.assertEqual(actual, expected)
        
    def test_pal_check_2_ex2(self):
        ''' Ensures function pal_check_2, reports whether a string is a palindrome or not. '''
        actual = algorithm2.pal_check_2('asd')
        expected = False
        self.assertEqual(actual, expected)
        
# Test cases for algorithm 3
class algorithm3_test(unittest.TestCase):
    ''' Checks the functions in algorithm3, to ensure they are working as desired. '''
    def test_pal_check_3_ex1(self):
        ''' Ensures function pal_check_3, reports whether a string is a palindrome or not. '''
        actual = algorithm3.pal_check_3('strts')
        expected = True
        self.assertEqual(actual, expected)
        
    def test_pal_check_3_ex2(self):
        ''' Ensures function pal_check_3, reports whether a string is a palindrome or not. '''
        actual = algorithm3.pal_check_3('asd')
        expected = False
        self.assertEqual(actual, expected)
    
if _name_ == '_main_':
    unittest.main(exit=False)
