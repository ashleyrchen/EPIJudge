from test_framework import generic_test
import collections


def can_form_palindrome(s: str) -> bool:
# -----MY solution, O(c) space, O(n) time
# c is the num of unique chars in s
    D = dict() 
    for char in s:
        if D.__contains__(char):
            D[char] += 1
        else:
            D[char] = 1
    temp = [item for item in D.items() if item[1] % 2 == 1]
    return len(s) % 2 == len(temp) 

# -----TEXTBOOK solution, O(c) space, O(n) time 
    # return sum(v % 2 for v in collections.Counter(s).values()) <= 1


if __name__ == '__main__':
    assert(can_form_palindrome('a'))
    assert(can_form_palindrome('aa'))
    assert(not can_form_palindrome('ab'))
    assert(can_form_palindrome('aaa'))
    assert(can_form_palindrome('aba'))
    assert(can_form_palindrome('level'))
    assert(can_form_palindrome('rotator'))
    assert(can_form_palindrome('foobaraboof'))
    assert(can_form_palindrome('edified'))
    assert(not can_form_palindrome('lollos'))
    assert(not can_form_palindrome('rotabtor'))
    assert(can_form_palindrome('lllllllbb'))
    assert(not can_form_palindrome('lllllllb'))
    assert(not can_form_palindrome('sbsbsb'))

    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
