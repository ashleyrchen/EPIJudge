from test_framework import generic_test
import math


def gcd(x: int, y: int) -> int:
# # -----MY SOLUTION, O(n) time, O(n) space, 
# # where n is the # of bits req to store the inputs 
#     A = [x, y]
#     A.sort()
#     [x_, y_] = [int(math.fabs(e)) for e in A]
#     if x_ == y_ or x_ == 0:
#         return y_ 
#     else:
#         return gcd(x_, y_ % x_)

# # ------THEIR SOLUTION, O(n) time, O(n) space, 
# # Says gcd(-100, -10) is -10, but shouldn't it be 10? 
# # if y > x, gcd(y, x % y), straight from the textbook 
# # if x > y, gcd(y, x % y), which is gcd(y, x) st. y > x 
# # if x == y, gcd(y, x % y), which is gcd(y, 0), which returns y
# # Same big-O as my solution, I think, but this one is much faster  
#     return x if y == 0 else gcd(y, x % y)

# ------ANOTHER solution, O(n) time, O(1) space, 
    flag = -1 if min(x, y) < 0 else 1 
    while True:
        if y == 0:
            return x * flag 
        x, y = y, x % y


if __name__ == '__main__':
    assert gcd(0, 0) == 0
    assert gcd(0, 358935) == 358935
    assert gcd(24, 36) == 12 
    assert gcd(120, 36) == 12
    assert gcd(51, 144) == 3 
    assert gcd(53, 19) == 1
    assert gcd(-100, -10) == 10
    exit(generic_test.generic_test_main('euclidean_gcd.py', 'gcd.tsv', gcd))