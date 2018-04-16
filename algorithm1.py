import reverse

# Below is a function that compares the original string to the reversed string to determine whether it is a palindrome.
def pal_check_1(s):
    ''' (str) -> bool
    Determine whether a string, s, is a palindrome by comparing the original string to the reversed string.
    >>> pal_check_1('strts')
    True
    >>> pal_check_1('asdf')
    False
    '''
    return s == reverse(s)
   
