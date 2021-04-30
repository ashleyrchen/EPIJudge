import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
import collections


def replace_and_remove(size: int, s: List[str]) -> int:
# # -----MY SOLUTION, O(n) time, O(n) space, 
#     if size == 0 or len(s) == 0:
#         return len(s)
#     Q = collections.deque([])
#     for i in range(size):
#         Q.extend(s[i])
#     i = 0
#     while len(Q) > 0:
#         temp = Q.popleft()
#         if temp == 'b':
#             pass 
#         elif temp == 'a':
#             s[i] = 'd'
#             s[i+1] = 'd'
#             i += 2
#         else:
#             s[i] = temp
#             i += 1
#     s[:] = s[:i]
#     return len(s) 

# -----TEXTBOOK SOLUTION, O(n) time, O(1) space,
    if size == 0 or len(s) == 0:
        return len(s)
        
    count = 0
    for e in s[:size]:
        if e == 'a':
            count += 2
        elif e != 'b':
            count += 1
    if count == 0:
        s[:] = []
        return 0
    return count

    i, j = 0, 0
    while j < size:
        if s[j] == 'b':
            j += 1
            s[i] = s[j]
        else:
            s[i] = s[j]
            j += 1
            i += 1
    
    k, l = len(s)-1, i-1
    for l in range(i-1, -1, -1):
        if s[l] != 'a':
            s[k] = s[l]
            k -= 1
        else:
            s[k] = 'd'
            s[k-1] = 'd'
            k -= 2

    s[:] = s[-count:]
    return count


def test_replace_and_remove():
    A = list('acdbbca')
    n = replace_and_remove(7, A)
    assert A == list('ddcdcdd')
    assert n == 7

    A = list('abac00')
    n = replace_and_remove(4, A)
    assert A == list('ddddc')
    assert n == 5

    A = list('acdbbca')
    assert replace_and_remove(0, A) == 7
    assert A == list('acdbbca')

    A = []
    assert replace_and_remove(0, A) == 0
    assert A == []

    A = list('bbaa')
    assert replace_and_remove(4, A) == 4
    assert A == list('dddd')

    A = list('bbbb')
    assert replace_and_remove(4, A) == 0
    assert A == []

    A = ['c', 'b', 'b', '', '', ''] # FROM AUTOGRADER
    assert replace_and_remove(3, A) == 1
    assert A == ['c']


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
