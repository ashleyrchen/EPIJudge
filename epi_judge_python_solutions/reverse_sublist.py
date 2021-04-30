from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # Reverses sublist.
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next,
                                                           sublist_head.next,
                                                           temp)
        print(dummy_head.next)
    return dummy_head.next


if __name__ == '__main__':
    E = ListNode(2)
    D = ListNode(7, E)
    C = ListNode(5, D)
    B = ListNode(3, C)
    A = ListNode(11, B) 
    print(reverse_sublist(A, 1, 5)) 
    
    # exit(
    #     generic_test.generic_test_main('reverse_sublist.py',
    #                                    'reverse_sublist.tsv', reverse_sublist))
