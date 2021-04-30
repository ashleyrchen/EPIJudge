from typing import List
import heapq, functools
from test_framework import generic_test
import collections


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
# # -----NAIVE solution, O(nlogn) time, O(n) extra space
# # this is actually 10x faster than the textbook & Pythonic solns
# # when run on the tests, but i guess it's bad for v large n 
#     result = []
#     for lst in sorted_arrays:
#         result += lst 
#     result.sort() 
#     return result

# # -----A SOLUTION USING PQs, very Pythonic, & given by the textbook
#     return list(heapq.merge(*sorted_arrays))
    
# -----MY REVISED solution, O(klogn) time, O(k) extra space excluding result
    k = len(sorted_arrays)
    Element = collections.namedtuple('Element', ['value', 'source'])
    minpq = [Element(sorted_arrays[i][0], (i, 0)) for i in range(k)]
    heapq.heapify(minpq)
    result = [] 
    while minpq:
        e = heapq.heappop(minpq)
        result += [e.value]
        k, l = e.source[0], e.source[1]
        if len(sorted_arrays[k]) > l+1:
            heapq.heappush(minpq, Element(sorted_arrays[k][l+1], (k, l+1)))
    return result

# # -----TEXTBOOK solution, O(klogn) time, O(k) space extra space excluding result
#     min_heap: List[Tuple[int, int]] = []
#     sorted_arrays_iters = [iter(x) for x in sorted_arrays]
#     for i, it in enumerate(sorted_arrays_iters):
#         first_element = next(it, None) 
#         if first_element is not None:
#             heapq.heappush(min_heap, (first_element, i))
#     result = []
#     while min_heap: 
#         smallest_entry, smallest_array_i = heapq.heappop(min_heap)
#         smallest_array_iter = sorted_arrays_iters[smallest_array_i]
#         result.append(smallest_entry)
#         next_element = next(smallest_array_iter, None)
#         if next_element is not None: # NOTE 0 is False, that's why `if next_element:` is not ok 
#             heapq.heappush(min_heap, (next_element, smallest_array_i))
#     return result 

if __name__ == '__main__':
    # A = [[-1, 0], [-2]]
    # print(merge_sorted_arrays(A))

    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
