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
    
# Below is a function that reverses the second half of a string and compares it to the first half to determine whether it is a palindrome.
# If the length of a string is odd, omit the character in the middle.
def pal_check_2(s):
    '''(str) -> bool
    Determine whether a string, s, is a palindrome.
    >>> pal_check_2('asdsa')
    True
    >>> pal_check_2('asd')
    False
    '''
    if len(s) % 2 == 0:
        return s[:len(s)//2] == reverse(s[(len(s)//2):])
    else:
        return s[:len(s)//2] == reverse(s[(len(s)//2) + 1:])
