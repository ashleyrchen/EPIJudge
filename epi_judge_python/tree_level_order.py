from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections 


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
# -----MY SOLUTION: O(n) time, O(l) space, where n is the number of nodes,
#  where l is the max number of nodes at a single depth, 
    if tree:
        TreePair = collections.namedtuple('TreePair', ('Generation', 'Tree'))
        result, count = collections.defaultdict(lambda: []), 0
        Q = collections.deque([TreePair(0, tree)])
        while len(Q) > 0:
            (generation, temp) = Q.popleft()
            result[generation].append(temp.data)
            generation += 1
            if temp.left:
                Q.append(TreePair(generation, temp.left))
            if temp.right:
                Q.append(TreePair(generation, temp.right))
        return list(result.values())
    return []

# -----TEXTBOOK SOLUTION: O(n) time, O(l) space, (MORE SUCCINCT THAN MINE)
    result, Q = [], [tree]
    if tree:
        while Q:
            result.append([node for node in Q])
            Q.append([[child for child in (node.left, node.right) if child] 
                                                            for node in Q])
    return result 


def test_binary_tree_depth_order():
    D = BinaryTreeNode(data='D')
    assert binary_tree_depth_order(D) == [['D']]
    E = BinaryTreeNode(data='E')
    C = BinaryTreeNode(data='C', left=D, right=E)
    assert binary_tree_depth_order(C) == [['C'], ['D', 'E']]
    H = BinaryTreeNode(data='H')
    G = BinaryTreeNode(data='G', left=H)
    F = BinaryTreeNode(data='F', right=G)
    assert binary_tree_depth_order(F) == [['F'], ['G'], ['H']]
    B = BinaryTreeNode(data='B', left=C, right=F)
    assert binary_tree_depth_order(B) == [['B'], ['C', 'F'], ['D', 'E', 'G'], ['H']]

    M = BinaryTreeNode(data='M')
    L = BinaryTreeNode(data='L', right=M)
    N = BinaryTreeNode(data='N')
    K = BinaryTreeNode(data='K', left=L, right=N)
    J = BinaryTreeNode(data='J', right=K)
    assert binary_tree_depth_order(J) == [['J'], ['K'], ['L', 'N'], ['M']]
    P = BinaryTreeNode(data='P')
    O = BinaryTreeNode(data='O', right=P)
    I = BinaryTreeNode(data='I', left=J, right=O)
    assert binary_tree_depth_order(I) == [['I'], ['J', 'O'], ['K', 'P'], ['L', 'N'], ['M']]

    A = BinaryTreeNode(data='A', left=B, right=I)
    assert binary_tree_depth_order(A) == [['A'], ['B', 'I'], ['C', 'F', 'J', 'O'], ['D', 'E', 'G', 'K', 'P'], ['H', 'L', 'N'], ['M']]

    assert binary_tree_depth_order(BinaryTreeNode()) == [[None]]
    assert binary_tree_depth_order(None) == []
    # assert 1 == 2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
