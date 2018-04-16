import reverse
    
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
