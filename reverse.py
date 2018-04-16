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
