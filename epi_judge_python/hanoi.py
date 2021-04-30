import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3


def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
# # -----MY SOLUTION, O(2**n) space, O(2**n) time,
#     def hanoi_wrapper(source: int, dest: int, other: int, num_rings: int):
#         lst = []
#         if num_rings == 1:
#             lst.append([source, dest])
#         elif num_rings >= 2: 
#             lst += hanoi_wrapper(source, other, dest, num_rings - 1)
#             lst.append([source, dest])
#             lst += hanoi_wrapper(other, dest, source, num_rings - 1)
#         return lst 
#     return hanoi_wrapper(0, 1, 2, num_rings)

# # -----TEXTBOOK SOLUTION, O(2**n) space, O(2**n) time,
# # the pegs represent the physical rings in the tower
#     def steps(num_rings, source, dest, other):
#         if num_rings > 0:
#             steps(num_rings - 1, source, other, dest)
#             pegs[dest].append(pegs[source].pop())
#             result.append([source, dest])
#             steps(num_rings - 1, other, dest, source)
#     result = []
#     pegs = ([list(reversed(range(1, num_rings + 1)))] + 
#                     [[] for _ in range(1, NUM_PEGS)])
#     steps(num_rings, 0, 1, 2)
#     return result

# -----MY SOLUTION w/o RECURSION, O(2**n) space, O(2**n) time, 
    source, dest, other = 0, 1, 2
    first = {0: source, 1: other, 2: dest}
    second = {0: other, 1: dest, 2: source}
    dictionary = {0: [[]], 1: [[0, 1]]}
    for count in range(2, num_rings + 1):
        def helper(mapping):
            return ([[mapping[x] for x in pair] 
                        for pair in dictionary[count - 1]])
        result = []
        result += helper(first)
        result.append([source, dest])
        result += helper(second)
        dictionary[count] = result
    return dictionary[num_rings]


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    assert (compute_tower_hanoi(0)) == [[]]
    assert (compute_tower_hanoi(1)) == [[0, 1]]
    assert (compute_tower_hanoi(2)) == [[0, 2], [0, 1], [2, 1]]
    assert (compute_tower_hanoi(3)) == [[0, 1], [0, 2], [1, 2], [0, 1], [2, 0], [2, 1], [0, 1]]
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
