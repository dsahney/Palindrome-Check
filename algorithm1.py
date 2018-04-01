# Below is a function that takes a string, s, and reverses its characters.
def reverse(s):
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
   
