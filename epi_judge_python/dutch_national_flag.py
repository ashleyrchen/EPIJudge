import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # # -----NAIVE solution, O(n) time, O(n) space,
    # one = list(); two = list(); three = list(); 
    # for i in range(len(A)):
    #     if A[i] < A[pivot_index]:
    #         one.append(A[i])
    #     elif A[i] == A[pivot_index]:
    #         two.append(A[i])
    #     else: 
    #         three.append(A[i])
    # del A[:len(A)]
    # for lst in [one, two, three]:
    #     for i in lst:
    #         A.append(i)

    # -----REVISED solution, O(n) time, O(1) space, 
    pivot_value = A[pivot_index]
    lthan = 0
    gthan = len(A) - 1
    i = 0 
    while i < len(A): 
        if A[i] < pivot_value:
            if i == lthan:
                lthan += 1 
                i += 1 
            elif i > lthan:
                A[i], A[lthan] = A[lthan], A[i]
                lthan += 1
            else: 
                i += 1 
        elif A[i] > pivot_value: 
            if i == gthan:
                gthan -= 1
                i += 1
            elif i < gthan:
                A[i], A[gthan] = A[gthan], A[i]
                gthan -= 1
            else:
                i += 1 
        else:
            i += 1

    # # -----TEXTBOOK solution 1, O(n^2) time, O(1) space
    # pivot = A[pivot_index]
    # for evens in range(len(A)): 
    #     for unclassified in range(evens+1, len(A)):
    #         if A[unclassified] < pivot:
    #             A[evens], A[unclassified] = A[unclassified], A[evens]
    #             break 
    # for odds in reversed(range(len(A))):
    #     for unclassified in reversed(range(odds)):
    #         if A[unclassified] > pivot:
    #             A[odds], A[unclassified] = A[unclassified], A[odds]
    #             break

    # # ----TEXTBOOK solution 2, O(n) time, O(1) space
    # pivot = A[pivot_index]
    # evens, odds = 0, len(A) - 1
    # for unclassified in range(len(A)):
    #     if A[unclassified] < pivot:
    #         A[unclassified], A[evens] = A[evens], A[unclassified]
    #         evens += 1
    # for unclassified in reversed(range(len(A))):
    #     if A[unclassified] > pivot:
    #         A[unclassified], A[odds] = A[odds], A[unclassified]
    #         odds -= 1

    # # ----TEXTBOOK solution 3, O(n) time, O(1) space 
    # pivot = A[pivot_index]
    # lthan, eq, gthan = 0, 0, len(A)
    # while eq < gthan:
    #     if A[eq] < pivot:
    #         A[eq], A[lthan] = A[lthan], A[eq]
    #         lthan += 1 
    #         eq += 1
    #     elif A[eq] == pivot:
    #         eq += 1 
    #     else:
    #         gthan -= 1 
    #         A[gthan], A[eq] = A[eq], A[gthan]
    
    return

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    # A = [0, 1, 2, 0, 2, 1, 1]
    # dutch_flag_partition(pivot_index=2, A=A)
    # print(A)
    

    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
