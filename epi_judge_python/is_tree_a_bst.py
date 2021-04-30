from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import math, collections 


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
# -----MY solution, O(n) time, O(h) space, 
    def helper(tree, floor, ceil):
        flag = floor <= tree.data and ceil >= tree.data
        if tree.left:
            flag = flag and helper(tree.left, floor, tree.data)
        if tree.right:
            flag = flag and helper(tree.right, tree.data, ceil)
        return flag 

    if tree is None:
        return True 
    else:
        return helper(tree, -math.inf, math.inf)

# # -----my implementation of the TEXTBOOK solution, inorder traversal, O(n) time, O(h) space 
    # def inorder_traversal(tree, prev=float('-inf'), flag=True):
    #     if tree:
    #         if tree.left:
    #             (prev, flag) = inorder_traversal(tree.left, prev, flag)
    #         if prev > tree.data:
    #             return (prev, False)
    #         prev = tree.data
    #         if tree.right:
    #             (prev, flag) = inorder_traversal(tree.right, prev, flag)
    #     return (prev, flag)
    # return inorder_traversal(tree)[1]

# -----my implementation of the TEXTBOOK solution, BFS approach, O(n) time, O(n) space
    # TreeTuple = collections.namedtuple('TreeTuple', ['tree', 'floor', 'ceil'])
    # if tree:
    #     queue = [TreeTuple(tree, -math.inf, math.inf)]
    #     while queue: 
    #         t = queue.pop(0)
    #         if t.floor > t.tree.data or t.ceil < t.tree.data: 
    #             return False 
    #         if t.tree.left:
    #             queue.append(TreeTuple(t.tree.left, t.floor, t.tree.data))
    #         if t.tree.right:
    #             queue.append(TreeTuple(t.tree.right, t.tree.data, t.ceil))
    # return True 
    

if __name__ == '__main__':
    A = BinaryTreeNode(-1)
    B = BinaryTreeNode(1)
    C = BinaryTreeNode(0, left=A, right=B)

    assert is_binary_tree_bst(C)

    F = BinaryTreeNode(1)
    G = BinaryTreeNode(4)
    E = BinaryTreeNode(2, left=F, right=G)
    H = BinaryTreeNode(5)
    D = BinaryTreeNode(3, left=E, right=H)

    assert not is_binary_tree_bst(D)

    I = BinaryTreeNode(0)

    assert is_binary_tree_bst(I)

    K = BinaryTreeNode(1)
    J = BinaryTreeNode(-1, left=K)

    assert not is_binary_tree_bst(J)

    assert not is_binary_tree_bst(BinaryTreeNode(3, left=E))

    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
