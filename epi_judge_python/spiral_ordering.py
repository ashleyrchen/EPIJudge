from typing import List

from test_framework import generic_test
import numpy as np


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
# -----MY SOLUTION, O(N**2) time, O(N**2) space (but no additional space is req'd
# beyond the list that is returned)

    def get_next_coordinate(x, y, count,):
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)][count % 4]  # row-major E, S, W, N
        return x + move[0], y + move[1]

    def is_valid_coordinate(x, y) -> bool:
        return (0 <= x < N and 0 <= y < N and not square_matrix[x][y] is True)

    def step(x, y, result=[], count=0):
        for _ in range(N**2):
            result.append(square_matrix[x][y])
            square_matrix[x][y] = True
            nxt = get_next_coordinate(x, y, count,)
            if not is_valid_coordinate(*nxt):
                count += 1
                nxt = get_next_coordinate(x, y, count,)
            x, y = nxt[0], nxt[1]
        return result

    N = len(square_matrix)
    return step(0, 0)
    

if __name__ == '__main__':

    A = [[0]]
    assert matrix_in_spiral_order(A) == [0]

    A = [[0, 1], [2, 3]]
    assert matrix_in_spiral_order(A) == [0, 1, 3, 2]

    A = [list(range(3)), 
        list(range(3, 6)), 
        list(range(6, 9)),]
    assert matrix_in_spiral_order(A) == [0, 1, 2, 5, 8, 7, 6, 3, 4,]

    A = [list(range(4)), 
        list(range(4, 8)), 
        list(range(8, 12)), 
        list(range(12, 16))]
    assert matrix_in_spiral_order(A) == [0, 1, 2, 3, 7, 11, 15, 14, 13, 12, 8, 4, 5, 6, 10, 9,]

    A = np.ones((32, 32,))
    A = list(list(a) for a in A)
    assert matrix_in_spiral_order(A) == [1.0]*(32**2)

    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))