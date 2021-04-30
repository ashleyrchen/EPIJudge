from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
import collections


def naive(tree, k):
# -----NAIVE SOLUTION, O(n) time, O(n) space, 
    if tree: 
        def inorder(tree, L=[]):
            if tree.left:
                inorder(tree.left, L)
            L.append(tree)
            if tree.right:
                inorder(tree.right, L)
            return L 
        for n in inorder(tree):
            if n.data > k:
                return n
    return None


def naive_v2(tree, k):
# -----NAIVE SOLUTION v2, O(n) time, O(d) space, 
    if tree: 
        def inorder(tree):
            a, b, c = None, None, None
            if tree.left:
                a = inorder(tree.left)
            if tree.data > k:
                b = tree
            if tree.right:
                c = inorder(tree.right)
            if a: return a 
            if b: return b 
            if c: return c
        return inorder(tree)
    return None 


def nonrecursive_naive_v2(tree, k):
# -----NAIVE SOLUTION v2, O(n) time, O(d) space,
    Visited = collections.namedtuple('Visited', ('Value'))
    if tree:
        stack = [tree]
        while stack: 
            tree = stack.pop()
            if type(tree) is Visited:
                if tree.Value.data > k:
                    return tree.Value
            else:
                if tree.right:
                    stack.append(tree.right)
                stack.append(Visited(tree))
                if tree.left:
                    stack.append(tree.left)
    return None


def improved(tree, k):
# -----IMPROVED SOLUTION, O(d) time, O(d) space, 
    if tree:
        def inorder(tree):
            a, b, c = None, None, None
            if k < tree.data:
                if tree.left: 
                    a = inorder(tree.left)
                b = tree
            else:
                if tree.right:
                    c = inorder(tree.right)
            if a: return a
            if b: return b 
            if c: return c 
        return inorder(tree)
    return None


def nonrecursive_improved(tree, k):
# -----IMPROVED SOLUTION, O(d) time, O(1) space, 
    qualified = None
    while tree:
        if tree.data > k: 
            qualified = tree
            tree = tree.left 
        else: 
            tree = tree.right
    return qualified 
   

def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    # return naive(tree, k)
    # return naive_v2(tree, k)
    # return nonrecursive_naive_v2(tree, k)
    # return improved(tree, k)
    return nonrecursive_improved(tree, k)


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    three = BstNode(3, left=BstNode(2), right=BstNode(5))
    seven = BstNode(7, left=three, right=BstNode(11, right=BstNode(17, left=BstNode(13))))
    twenty_three = BstNode(23, right=BstNode(37, left=BstNode(29, right=BstNode(31)), right=BstNode(41)))
    forty_seven = BstNode(47, right=BstNode(49, right=BstNode(53)))
    tree = BstNode(19, left=seven, right=BstNode(43, left=twenty_three, right=forty_seven))
    
    # print(find_first_greater_than_k(tree, 17))

    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))