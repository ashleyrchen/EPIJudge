from test_framework import generic_test
import math 


def is_palindromic(s: str) -> bool:

    # -----MY SOLUTION, O(n) time, O(1) space 
    for i in range(math.floor((len(s)/2))):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

    # # -----TEXTBOOK solution, O(n) time, O(1) space
    # # Note that s[~i] is s[len(s)-1-i]
    # # Note that len(s) // 2 == math.floor(len(s)/2)
    # return all([s[i] == s[~i] for i in range(len(s) // 2)])


if __name__ == '__main__':
    # s = 'abccba'
    # s = 'abcba'
    # s = ''
    # s = 'a'
    # s = 'abcbb'
    # s = 'ab'
    # print(is_palindromic(s))

    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
