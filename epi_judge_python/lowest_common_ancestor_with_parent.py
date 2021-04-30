import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
# # -----MY NAIVE SOLUTION, O(d**2) time, O(d) space
#     L = list()
#     while node0:
#         L.append(node0)
#         node0 = node0.parent 
#     while node1:
#         if node1 in L:
#             return node1
#         node1 = node1.parent
#     return None

# # -----MY IMPROVED SOLUTION, O(d) time, O(d) space,
#     L0, L1, LCA = list(), list(), None
#     while node0:
#         L0.append(node0)
#         node0 = node0.parent
#     while node1:
#         L1.append(node1)
#         node1 = node1.parent 
#     for i in range(min(len(L0), len(L1)), 0, -1):
#         if L0[-i] == L1[-i]:
#             return L0[-i]
#     return LCA

# -----MY OPTIMAL SOLUTION, O(d) time, O(1) space,
    def helper(node, count=0):
        while node:
            node, count, = node.parent, count + 1
        return count 
    L0, L1 = map(helper, (node0, node1))
    (node0, node1) = (node0, node1) if L0 >= L1 else (node1, node0)
    for _ in range(max(L0, L1) - min(L0, L1)):
        node0 = node0.parent
    for _ in range(min(L0, L1) + 1):
        if node0 == node1:
            return node0
        node0, node1 = node0.parent, node1.parent
    return None


def test_lca():
    D = BinaryTreeNode(data='D',)
    E = BinaryTreeNode(data='E')
    C = BinaryTreeNode(data='C', left=D, right=E,)
    H = BinaryTreeNode(data='H',)
    G = BinaryTreeNode(data='G', left=H,)
    F = BinaryTreeNode(data='F', right=G,)
    B = BinaryTreeNode(data='B', left=C, right=F,)

    M = BinaryTreeNode(data='M',)
    L = BinaryTreeNode(data='L', right=M,)
    N = BinaryTreeNode(data='N',)
    K = BinaryTreeNode(data='K', left=L, right=N,)
    J = BinaryTreeNode(data='J', right=K,)
    P = BinaryTreeNode(data='P')
    O = BinaryTreeNode(data='O', right=P,)
    I = BinaryTreeNode(data='I', left=J, right=O,)

    A = BinaryTreeNode(data='A', left=B, right=I)

    D.parent = C
    C.parent = B
    H.parent = G
    G.parent = F
    F.parent = B
    B.parent = A

    M.parent = L
    L.parent = K
    N.parent = K
    K.parent = J
    J.parent = I
    P.parent = O
    O.parent = I
    I.parent = A

    One = BinaryTreeNode(data=1)

    assert lca(B, I) is A
    assert lca(D, H) is B
    assert lca(M, H) is A
    assert lca(M, N) is K
    assert lca(J, P) is I
    
    assert lca(A, A) is A
    assert lca(A, B) is A
    assert lca(One, A) is None
    assert lca(One, One) is One
    assert lca(BinaryTreeNode(), E) is None
    assert lca(BinaryTreeNode(), BinaryTreeNode()) is None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
