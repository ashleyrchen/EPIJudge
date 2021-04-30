from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    # # -----MY NAIVE SOLUTION, O(n^3) time, O(1) space,
    # result = 0
    # for i in range(len(A)):
    #     for j in range(i+1, len(A) + 1):
    #         temp = sum(A[i:j]) 
    #         if temp > result:
    #             result = temp
    # return result 

    # # -----MY DYNAMIC PROGRAMMING SOLUTION, O(n^2) time, O(n) space, 
    # if len(A) == 0: 
    #     return 0 
    # result = max(A) if max(A) > 0 else 0
    # cache = dict(zip((zip(range(len(A)), range(1, len(A)+1))), A))
    # for step in range(2, len(A) + 1):
    #     for start in range(len(A) - step + 1):
    #         temp = A[start + step - 1] + cache.pop((start, start + step - 1)) 
    #         if temp > result:
    #             result = temp 
    #         if start + step < len(A):
    #             cache[(start, start + step)] = temp
    # return result

    # # -----TEXTBOOK DIVIDE-AND-CONQUER SOLUTION, O(nlogn) time, O(n) space,
    # if len(A) == 0:
    #     return 0 
    # elif len(A) == 1:
    #     return A[0] if A[0] > 0 else 0 
    # else:
    #     m = len(A) // 2
    #     L = find_maximum_subarray(A[:m])
    #     R = find_maximum_subarray(A[m:])
    #     LR = 0 

    #     S, L_index, R_index = [0] * len(A), m-1, m
    #     S[L_index], S[R_index] = A[L_index], A[R_index]
    #     for i in reversed(range(m-1)):
    #         S[i] = S[i+1] + A[i]
    #         if S[i] > S[L_index]:
    #             L_index = i
    #     for i in range(m+1, len(A)):
    #         S[i] = S[i-1] + A[i]
    #         if S[i] > S[R_index]:
    #             R_index = i
    #     LR = S[L_index] + S[R_index]

    #     return max(L, R, LR)
    
    # -----TEXTBOOK DP DIVIDE-AND-CONQUER SOLUTION, O(n) time, O(1) space,
    max_so_far = B = 0
    for j in range(len(A)):
        B = max(0, A[j], B+A[j])
        if B > max_so_far:
            max_so_far = B
    return max_so_far

if __name__ == '__main__':
   
    A = [100, 100, -500, 200, 300, -500, 200, 200]
    assert find_maximum_subarray(A) == 500
    
    A = [904, 40, 523, 12, -335, -385, -124, 481, -31]
    assert find_maximum_subarray(A) == 1479

    A = [0]
    assert find_maximum_subarray(A) == 0

    A = [1]
    assert find_maximum_subarray(A) == 1

    A = [100, 100]
    assert find_maximum_subarray(A) == 200

    A = [-1, -2, -3]
    assert find_maximum_subarray(A) == 0 

    A = [-100, 0, 100, 100, 0, -100]
    assert find_maximum_subarray(A) == 200

    A = [293, -384, -198, 194, 102, 103]  
    assert find_maximum_subarray(A) == 399 

    # NOTE you forgot the case where a single-element subarray produces the max sum
    A = [453, 291, -855, 874, -873, -196, 18, 616, -221, 6, 307, -255, 399]
    assert find_maximum_subarray(A) == 874

    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))