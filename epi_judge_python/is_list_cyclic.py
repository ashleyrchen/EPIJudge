import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import collections


def has_cycle(head: ListNode) -> Optional[ListNode]:
# # -----MY SOLUTION, O(C + F) time, O(1) space, 
# # where C is the number of nodes to the start of the cycle,
# # F the number of nodes in the cycle
#     Visited = collections.namedtuple('Visited', ('VisitedData'))
#     while not head is None:
#         if type(head.data) is Visited:
#             while type(head.data) is Visited:
#                 head.data, head = head.data.VisitedData, head.next
#             return head
#         head.data, head = Visited(head.data), head.next
#     return head

# # -----NAIVE TEXTBOOK SOLUTION, O(n**2) time, O(1) space,
# # where n is the number of nodes in the linked list
#     i = 1
#     while not head is None:
#         inner = head
#         for _ in range(i):
#             if inner is None:
#                 break
#             inner = inner.next
#         if inner is head:
#             for _ in range(i-1):
#                 inner = inner.next
#             return inner 
#         head = head.next
#         i += 1
#     return head

# -----IMPROVED TEXTBOOK SOLUTION, O(C + F) time, O(1) space,
# better than my solution because it does not modify the list
    fast, i = head.next, 1
    while fast and fast.next:
        if fast is head:
            for _ in range(i-1):
                head = head.next
            return head 
        head, fast, i = head.next, fast.next.next, i + 1
    return None


def test_has_cycle():
    B = ListNode(2)
    A = ListNode(1, B)
    assert str(has_cycle(A)) == 'None'
    B.next = A
    assert str(has_cycle(A)) == str(A)

    D = ListNode(4)
    C = ListNode(3, D)
    B = ListNode(2, C)
    A = ListNode(1, B)
    assert str(has_cycle(A)) == 'None'
    D.next = B
    assert str(has_cycle(A)) == str(B)

    A = ListNode(1)
    assert str(has_cycle(A)) == 'None'
    A.next = A 
    assert str(has_cycle(A)) == str(A)


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
