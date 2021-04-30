from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
# # -----MY SOLUTION, O(f) time, O(f-s+1) space, 
#     if start == finish: return L 

#     LN = ListNode('M', L)
#     s_minus, stack = LN, []
#     for i in range(finish + 1):
#         if start <= i <= finish:
#             stack.append(LN)
#         LN = LN.next
#     f_plus = LN
    
#     LN = s_minus
#     for _ in range(start - 1): 
#         s_minus = s_minus.next
#     for _ in range(len(stack)): 
#         temp = stack.pop()
#         s_minus.next = temp
#         s_minus = temp
#     s_minus.next = f_plus

#     return LN.next

# -----TEXTBOOK SOLUTION, O(f) time, O(1) space,
    if start == finish: return L
    LN = ListNode('M', L)
    sentinel = LN
    for _ in range(start - 1):
        sentinel = sentinel.next
    lag = sentinel.next
    for _ in range(finish-start):
        lead = lag.next
        lag.next, lead.next, sentinel.next = lead.next, sentinel.next, lead
    return LN.next


def test_reverse_sublist():
    E = ListNode(2)
    D = ListNode(7, E)
    C = ListNode(5, D)
    B = ListNode(3, C)
    A = ListNode(11, B) 
    assert str(reverse_sublist(A, 2, 4)) == "11 -> 7 -> 5 -> 3 -> 2" # Odd

    E = ListNode(2)
    D = ListNode(7, E)
    C = ListNode(5, D)
    B = ListNode(3, C)
    A = ListNode(11, B)
    assert str(reverse_sublist(A, 3, 4)) == "11 -> 3 -> 7 -> 5 -> 2" # Even

    D = ListNode(4)
    C = ListNode(3, D)
    B = ListNode(2, C)
    A = ListNode(1, B)
    assert str(reverse_sublist(A, 1, 4)) == "4 -> 3 -> 2 -> 1" # All

    E = ListNode(2)
    D = ListNode(7, E)
    C = ListNode(5, D)
    B = ListNode(3, C)
    A = ListNode(11, B)
    reverse_sublist(A, 1, 1) # One 
    assert str(A) == "11 -> 3 -> 5 -> 7 -> 2"

    B = ListNode(-1)
    A = ListNode(1, B)
    assert str(reverse_sublist(A, 1, 2)) == "-1 -> 1" # Len 2

    A = ListNode()
    assert str(reverse_sublist(A, 1, 1)) == "0" # Len 1


if __name__ == '__main__':
    B = ListNode(-1)
    A = ListNode(1, B)
    print(reverse_sublist(A, 1, 2)) # Len 2

    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
