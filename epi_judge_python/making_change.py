from test_framework import generic_test


COINS = [100, 50, 25, 10, 5, 1]
def change_making(cents: int) -> int:
# # -----NAIVE SOLUTION, O(r) time, O(s) space, 
# # where r is magnitude of result, s is the number of coin types 
#     result, i = 0, 0
#     while cents > 0:
#         if COINS[i] <= cents:
#             cents -= COINS[i]
#             result += 1
#         else:
#             i += 1
#     return result

# # -----IMPROVED SOLUTION, O(s) time, O(s) space,
#     result, i = 0, 0
#     while cents > 0:
#         if COINS[i] <= cents:
#             temp = cents % COINS[i]
#             result += (cents - temp) / COINS[i]
#             cents = temp
#         else:
#             i += 1
#     return result

# -----TEXTBOOK SOLUTION, O(s) time, O(s) space, 
    result = 0
    for coin in COINS:
        result += cents // coin
        cents %= coin
    return result 


if __name__ == '__main__':
    assert change_making(1) == 1
    assert change_making(5) == 1
    assert change_making(10) == 1
    assert change_making(25) == 1
    assert change_making(50) == 1
    assert change_making(100) == 1

    assert change_making(75) == 2
    assert change_making(15) == 2
    assert change_making(16) == 3
    assert change_making(24) == 6

    exit(
        generic_test.generic_test_main('making_change.py', 'making_change.tsv',
                                       change_making))
