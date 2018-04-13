# Below is a function that compares characters at each index of a string to determine whether the string is a palindrome.
def pal_check_3(s):
    ''' (str) -> bool
    Determine whether a string, s, is a palindrome.
    >>> pal_check_3('strts')
    True
    >>> pal_check_3('asd')
    False
    '''
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    return j <= i
