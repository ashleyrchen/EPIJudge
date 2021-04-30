from typing import List

from test_framework import generic_test
import bisect


def has_two_sum(A: List[int], t: int) -> bool:
# # -----NAIVE SOLUTION, O(|A|**2) time, O(1) space,
#     for i in range(len(A)):
#         for j in range(i, len(A)):
#             if A[i] + A[j] == t:
#                 return True 
#     return False 

# -----IMPROVED SOLUTION, O(|A|) time, O(1) space,
    i, j = 0, len(A) - 1
    while i <= j:
        if A[i] + A[j] > t:
            j -= 1
        elif A[i] + A[j] == t:
            return True
        else: # A[i] + A[j] < t
            i += 1
    return False 


if __name__ == '__main__':
    A = [-2, 1, 2, 4, 7, 11]
    assert has_two_sum(A, 6)
    assert has_two_sum(A, 0)
    assert has_two_sum(A, 13)
    assert has_two_sum(A, -1)
    assert not has_two_sum(A, 10)

    A = [0]
    assert has_two_sum(A, 0)

    A = [-2, 2]
    assert not has_two_sum(A, 2)
    assert not has_two_sum(A, -2)
    assert has_two_sum(A, 0)

    A = [1, 3]
    assert not has_two_sum(A, 3)

    A = [3]
    assert has_two_sum(A, 6)
    assert not has_two_sum(A, 3)

    exit(
        generic_test.generic_test_main('two_sum.py', 'two_sum.tsv',
                                       has_two_sum))