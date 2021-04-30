from test_framework import generic_test
import math, random


def square_root(k: int) -> int:
# # -----MY INITIAL SOLUTION, O(1) time, O(1) space, 
#     return math.floor(math.sqrt(k))

# -----ANOTHER SOLUTION, O(logk) time, O(1) space,
# Does not use math library 
    floor, ceil, candidate = 0, k, 0
    while floor <= ceil:
        candidate = (floor + ceil) // 2
        if candidate*candidate <= k:
            if (candidate+1)*(candidate+1) > k:
                break
            else:
                floor = candidate + 1
        else:
            ceil = candidate - 1
    return candidate


def test_square_root():
    assert square_root(0) == 0
    assert square_root(1) == 1
    assert square_root(2) == 1

    for _ in range(10**5):
        k = random.randint(0, 10**5)
        result = square_root(k)
        assert result**2 <= k
        assert (result+1)**2 > k


if __name__ == '__main__':   
    # assert square_root(0) == 0
    # assert square_root(1) == 1
    # assert square_root(2) == 1
    # assert square_root(16) == 4
    # assert square_root(300) == 17
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
