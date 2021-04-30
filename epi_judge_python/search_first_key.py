from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
# # -----NAIVE solution, O(1) space, O(n) time
#     L, U = 0, len(A) - 1
#     first = -1
#     while L <= U:
#         M = (U + L) // 2
#         if A[M] < k:
#             L = M + 1
#         elif A[M] > k:
#             U = M - 1
#         else:
#             first = M
#             while first >= 0 and A[first] == k:
#                 first -= 1
#             return first + 1
#     return first

# -----REVISED solution, O(1) space, O(logn) time
    L, U = 0, len(A) - 1
    first = -1
    while L <= U:
        M = (U + L) // 2
        if A[M] < k:
            L = M + 1
        elif A[M] > k:
            U = M - 1
        else:
            U = M - 1
            first = M 
    return first


if __name__ == '__main__':
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    # search_first_of_k(A, 108)
    assert(search_first_of_k(A, 108) == 3)
    assert(search_first_of_k(A, 285) == 6)
    assert(search_first_of_k(A, 23) == -1)
    assert(search_first_of_k([0], 0) == 0)
    assert(search_first_of_k([0, 0], 0) == 0)
    assert(search_first_of_k([2, 2], -2) == -1)

    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
