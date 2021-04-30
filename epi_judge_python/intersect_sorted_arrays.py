from typing import List
import collections, bisect
from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
# # -----my PYTHONIC solution, 
#     return list((collections.Counter(A) & collections.Counter(B)).keys())

# -----my REVISED solution, O(n+m) time, O(1) additional space
    i, j, result = len(A) - 1, len(B) - 1, []
    while i >= 0 and j >= 0:
        curA, curB = A[i], B[j]
        if A[i] > B[j]:
            i -= 1
            while curA == A[i] and i >= 0:
                i -= 1 
        elif B[j] > A[i]:
            j -= 1
            while curB == B[j] and j >= 0:
                j -= 1
        else: # A[i] == B[j]
            result.append(A[i])
            i -= 1
            j -= 1
            while curA == A[i] and i >= 0:
                i -= 1
            while curB == B[j] and j >= 0:
                j -= 1
        curA = A[i]
        curB = B[j]
    return result[::-1] 

# # -----TEXTBOOK solution 1, O(nm) time, O(1) additional space 
#     return [a for (i, a) in enumerate(A) if a in B and 
#                                 (i == 0 or A[i] != A[i - 1])]

# # -----TEXTBOOK solution 2, O(mlogn) time, WLOG m < n, O(1) additional space 
#     def is_k_in_A(A, k):
#         i = bisect.bisect_left(A, k) # Can use binsearch because A, B are sorted
#         return i <= len(A) - 1 and A[i] == k
#     return [a for (i, a) in enumerate(A) if is_k_in_A(B, a) and 
#                                     (i == 0 or A[i] != A[i-1])]

# # -----TEXTBOOK solution 3, O(n+m) time, O(1) additional space
#     i, j, result = 0, 0, []
#     while i < len(A) and j < len(B):
#         if A[i] < B[j]:
#             i += 1
#         elif B[j] < A[i]:
#             j += 1
#         else:
#             if i == 0 or A[i] != A[i-1]: 
#                 result += [A[i]]
#             i += 1
#             j += 1
#     return result


if __name__ == '__main__':
    A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
    B = [5, 5, 6, 8, 8, 9, 10, 10]
    print(intersect_two_sorted_arrays(A, B))
    assert(intersect_two_sorted_arrays(A, B) == [5, 6, 8])

    A = [1, 2]
    B = [4, 5]
    assert(intersect_two_sorted_arrays(A, B) == [])

    A = [0]
    B = [0]
    assert(intersect_two_sorted_arrays(A, B) == [0])

    A = [-1, 0, 1]
    B = [-2, -1, 1]
    assert(intersect_two_sorted_arrays(A, B) == [-1, 1])

    A = [2, 2, 3, 4]
    assert(intersect_two_sorted_arrays(A, A) == [2, 3, 4])

    A = []
    B = [1, 2, 3]
    assert(intersect_two_sorted_arrays(A, B) == [])

    A = [1, 1, 1, 1]
    B = [1, 1, 1]
    assert(intersect_two_sorted_arrays(A, B) == [1])

    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
