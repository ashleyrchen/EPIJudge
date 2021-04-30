from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:

    # -----MY solution, O(n+m) time, O(1) space 
    R = ListNode("R") 
    cur = R 
    while L1 and L2:
        if L1.data <= L2.data:
            cur.next = L1
            cur = cur.next
            L1 = L1.next
        else:
            cur.next = L2 
            cur = cur.next
            L2 = L2.next
    if L1:
        cur.next = L1 
    elif L2:
        cur.next = L2 
    return R.next if R.next else None # NOTE if R.next is false, then R.next is None 

    # # -----TEXTBOOK solution, O(n+m) time, O(1) space 
    # cur = R = ListNode("R") # NOTE this is legal in Python! 
    # while L1 and L2:
    #     if L1.data <= L2.data:
    #         cur.next, L1 = L1, L1.next 
    #     else:
    #         cur.next, L2 = L2, L2.next 
    #     cur = cur.next 
    # cur.next = L1 or L2 # NOTE appends the remaining nodes of L1 or L2 
    # return R.next 



if __name__ == '__main__':
    # print(merge_two_sorted_lists(ListNode(1, ListNode(3)), 
    #                        ListNode(2, ListNode(4)),
    #                        ))

    # print(merge_two_sorted_lists(ListNode(2, ListNode(5, ListNode(7))), 
    #                        ListNode(3, ListNode(11)),
    #                        ))
    
    # print(merge_two_sorted_lists(ListNode(), ListNode()))

    # print(merge_two_sorted_lists(None, None))

    # print(merge_two_sorted_lists(ListNode(), None))

    # print(merge_two_sorted_lists(ListNode(2, ListNode(5, ListNode(7))), 
    #                             None))

    # print(merge_two_sorted_lists(ListNode(2, ListNode(2, ListNode(2))), 
    #                        ListNode(3, ListNode(3)),
    #                        ))

    # print(merge_two_sorted_lists(ListNode(2, ListNode(2, ListNode(2))), 
    #                        ListNode(2, ListNode(2)),
    #                        ))

    # print(merge_two_sorted_lists(ListNode(-10, ListNode(-2, ListNode(5))), 
    #                        ListNode(-5, ListNode(0)),
    #                        ))

    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
