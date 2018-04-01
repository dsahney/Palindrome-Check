def reverse(s): # for some string, s
    ''' (str) -> str
    Return a string that has been reversed.
    >>> reverse('apple')
    'elppa'
    >>> reverse('strts')
    'strts'
    '''
    new_string = '' # this will act as an accumulator.
    for character in s:
        new_string = character + new_string # we add the new characters from iterations before the previous string, thus, reversing the string.

    return new_string

# Algorithm 1: reverse the entire string and compare it to the original string.

def pal_check_1(s):
    ''' (str) -> bool
    Determine whether a string, s, is a palindrome.
    >>> pal_check_1('strts')
    True
    >>> pal_check_1('asdf')
    False
    '''
    return s == reverse(s)
   
