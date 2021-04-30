import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A: List[int]) -> None:
    # -----REVISED solution, O(n) time, O(1) space, 
    odds = len(A) - 1 
    for i in range(len(A)):
        if A[i] % 2 == 1:
            while odds > i:
                if A[odds] % 2 == 0:
                    A[i], A[odds] = A[odds], A[i]
                    break 
                odds -= 1

    # # # -----TEXTBOOK solution, O(n) time, O(1) space, 
    # evens = 0 
    # odds = len(A) - 1
    # while evens < odds:
    #     if A[evens] % 2 == 0:
    #         evens += 1
    #     else:
    #         A[evens], A[odds] = A[odds], A[evens]
    #         odds -= 1
    return


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
