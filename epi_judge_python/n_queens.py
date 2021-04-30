from typing import List

from test_framework import generic_test


# I was literally unable to come up with any solution whatsoever. 
# Except for a O(n!n^2) solution which gave me a headache to think about. 
# This is copied from the textbook. 
def n_queens(n: int) -> List[List[int]]:
    def solve_n_queens(row):
        if row == n:
            # All queens are legally placed.
            result.append(col_placement.copy())
            return
        for col in range(n):
            # Test if a newly placed queen will conflict any earlier queens
            # placed before.
            if all(
                    abs(c - col) not in (0, row - i)
                    for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                solve_n_queens(row + 1)

    result: List[List[int]] = []
    col_placement = [0] * n
    solve_n_queens(0)
    return result


def factorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * factorial(n-1)


def permutations(n):
    if n == 1:
        return [[0]]
    else:
        L = [] 
        for p in permutations(n-1):
            p.append(n-1)
            for j in range(len(p)):
                L.append(p[j:] + p[:j])
        return L


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    print(n_queens(4))
    # print(permutations(2))
    # exit(
    #     generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
    #                                    comp))
