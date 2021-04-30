from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils
import collections


D = BstNode(2)
E = BstNode(5)
C = BstNode(3, D, E)
H = BstNode(13)
G = BstNode(17, left=H)
F = BstNode(11, right=G)
B = BstNode(7, C, F)

M = BstNode(31)
L = BstNode(29, right=M)
N = BstNode(41)
K = BstNode(37, left=L, right=N)
J = BstNode(23, right=K)
P = BstNode(53)
O = BstNode(47, right=P)
I = BstNode(43, J, O)

A = BstNode(19, B, I)

Test = BstNode(6, BstNode(None), None)


def inorder(tree):
    if tree.left:
        inorder(tree.left)
    print(tree.data)
    if tree.right:
        inorder(tree.right)


def anti_inorder(tree):
    if tree.right:
        anti_inorder(tree.right)
    print(tree.data)
    if tree.left:
        anti_inorder(tree.left)


def sort_bst(tree, reverse=False):
    if tree: 
        if reverse:
            return sort_bst(tree.right, reverse=True) + [tree] + sort_bst(tree.left, reverse=True)
        else:
            return sort_bst(tree.left) + [tree] + sort_bst(tree.right)
    return []


def naive(tree, k):
# ------O(n) time, O(d) space, 
    return [n.data for n in sort_bst(tree, reverse=True)[:k]]


def improved(tree, k):
# -----O(d+k) time, O(d+k) space, 
# You descend the tree in d steps, and ascend k steps => O(d+k) runtime
    stack, L, = [tree], [],
    while stack:
        tree = stack.pop()
        if type(tree) is list:
            L.append(tree[0].data)
            if len(L) == k:
                return L
        else: 
            if tree.left:
                stack.append(tree.left)
            stack.append([tree])
            if tree.right:
                stack.append(tree.right)
    return L


def recursive_improved(tree, k):
    def helper(tree):
        if tree.right:
            helper(tree.right)
        if len(L) < k:
            L.append(tree.data)
            if tree.left:
                helper(tree.left)
    L = [] 
    helper(tree)
    return L


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    # return naive(tree, k)
    # return improved(tree, k)
    return recursive_improved(tree, k)


def test_find_k_largest_in_bst():
    assert find_k_largest_in_bst(A, 3) == naive(A, 3)
    assert find_k_largest_in_bst(A, 10) == naive(A, 10)
    assert find_k_largest_in_bst(B, 1) == naive(B, 1)
    assert find_k_largest_in_bst(M, 1) == naive(M, 1)
    assert find_k_largest_in_bst(J, 5) == naive(J, 5)
    assert find_k_largest_in_bst(A, 4) == naive(A, 4)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))