from typing import List

from test_framework import generic_test
from two_sum import has_two_sum


def has_three_sum(A: List[int], t: int) -> bool:
# # ----SUPER NAIVE SOLUTION, O(n**3) time, O(1) space,
#     for i in range(len(A)):
#         for j in range(i, len(A)):
#             for k in range(j, len(A)):
#                 if A[i] + A[j] + A[k] == t:
#                     return True 
#     return False

# -----ANOTHER SOLUTION, O(n**2) time, O(1) space,
    A.sort()
    for a in A:
        if has_two_sum(A, t - a):
            return True
    return False 


if __name__ == '__main__':
    A = [11, 2, 5, 7, 3]
    assert has_three_sum(A, 21)
    assert has_three_sum(A, 33)
    assert not has_three_sum(A, 5)
    assert not has_three_sum(A, 22)

    A = [1]
    assert not has_three_sum(A, 1)
    assert has_three_sum(A, 3)

    A = [-5, 5, -5]
    assert not has_three_sum(A, 0)
    assert not has_three_sum(A, 10)
    assert not has_three_sum(A, -10)
    assert has_three_sum(A, 5)
    assert has_three_sum(A, -5)
    assert has_three_sum(A, 15)
    assert has_three_sum(A, -15)

    A = [1, 4, 0, -3, -1, 0, -7]
    assert has_three_sum(A, -17)

    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
