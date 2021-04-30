from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import math
import collections

# Tree rooted at A 
D = BinaryTreeNode(data='D')
E = BinaryTreeNode(data='E')
C = BinaryTreeNode(data='C', left=D, right=E)
H = BinaryTreeNode(data='H')
G = BinaryTreeNode(data='G', left=H)
F = BinaryTreeNode(data='F', right=G)
B = BinaryTreeNode(data='B', left=C, right=F)

M = BinaryTreeNode(data='M')
L = BinaryTreeNode(data='L', right=M)
N = BinaryTreeNode(data='N')
K = BinaryTreeNode(data='K', left=L, right=N)
J = BinaryTreeNode(data='J', right=K)
P = BinaryTreeNode(data='P')
O = BinaryTreeNode(data='O', right=P)
I = BinaryTreeNode(data='I', left=J, right=O)

A = BinaryTreeNode(data='A', left=B, right=I)

# Tree rooted at Q
T = BinaryTreeNode(data='T')
U = BinaryTreeNode(data='U')
S = BinaryTreeNode(data='S', left=T, right=U)
V = BinaryTreeNode(data='V')
R = BinaryTreeNode(data='R', left=S, right=V)
W = BinaryTreeNode(data='W')
Q = BinaryTreeNode(data='Q', left=R, right=W)
    
def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool: 
# # -----MY solution, O(h) space, O(n) time
# # NOTE fails when all nodes in tree are balanced except for root
#     if tree: 
#         if tree.left:
#             if tree.right:  
#                 return (is_balanced_binary_tree(tree.left) and 
#                             is_balanced_binary_tree(tree.right))
#             return (not tree.left.left and not tree.left.right)
#         else:
#             if tree.right: 
#                 return (not tree.right.left and not tree.right.right) 
#             return True 
#     return True


# # -----MY INTERMEDIATE REVISED solution 
#     def height(tree: BinaryTreeNode) -> int: 
#         if tree:
#             if tree.left:
#                 if tree.right:
#                     return 1 + max(height(tree.left), height(tree.right))
#                 else:
#                     return 1 + height(tree.left) 
#             else:
#                 if tree.right:
#                     return 1 + height(tree.right)
#                 else:
#                     return 0
#         else:
#             return -1 
#     if tree: 
#         if tree.left:
#             if tree.right: 
#                 return (
#                     is_balanced_binary_tree(tree.left) and 
#                     is_balanced_binary_tree(tree.right) and 
#                     height(tree.left) - height(tree.right) <= 1
#                             )
#             return (not tree.left.left and not tree.left.right)
#         else:
#             if tree.right: 
#                 return (not tree.right.left and not tree.right.right) 
#             return True 
#     return True


# -----MY REVISED solution, O(h) space, O(n) time
    BinTreePair = collections.namedtuple('BinTreePair', 
                                    ['tree', 'bool', 'height'])
    def helper(btp: BinTreePair) -> BinTreePair: 
        # print(btp.tree.data)
        if btp.tree:
            if btp.tree.left:
                if btp.tree.right:
                    lt = helper(BinTreePair(btp.tree.left, None, None))
                    rt = helper(BinTreePair(btp.tree.right, None, None))
                    return BinTreePair(
                        btp.tree, 
                        lt.bool and rt.bool and lt.height-rt.height <= 1,
                        1 + max(rt.height, lt.height)
                    )
                else: 
                    return BinTreePair(
                        btp.tree,
                        (not btp.tree.left.left and not btp.tree.left.right),
                        1 + helper(BinTreePair(btp.tree.left, None, None)).height
                    )
            else: 
                if btp.tree.right:
                    return BinTreePair(
                        btp.tree,
                        (not btp.tree.right.left and not btp.tree.right.right),
                        1 + helper(BinTreePair(btp.tree.right, None, None)).height
                    )
                else: 
                    return BinTreePair(
                        btp.tree,
                        True,
                        0
                    )
        else: 
            return BinTreePair(
                btp.tree,
                True,
                -1
            )
    return helper(BinTreePair(tree=tree, bool=None, height=None)).bool

# # -----TEXTBOOK solution, O(h) time, O(n) space 
#     IsBalanced = collections.namedtuple('IsBalanced', ['balanced', 'height'])
#     def check_balanced(tree):
#         if not tree:
#             return IsBalanced(True, -1)
#         lt = check_balanced(tree.left)
#         if not lt.balanced: 
#             # If any node in the node is unbalanced, the tree is unbalanced.
#             return IsBalanced(False, None)
#         rt = check_balanced(tree.right)
#         if not rt.balanced:
#             return IsBalanced(False, None)
#         # Check that the root node is balanced
#         # If we are here, then we already know that all the non-root nodes 
#         # in the tree are balanced 
#         is_balanced = math.fabs(lt.height - rt.height) <= 1 
#         height = max(lt.height, rt.height) + 1
#         return IsBalanced(is_balanced, height)
#     return check_balanced(tree).balanced 
             

if __name__ == '__main__':
    assert (is_balanced_binary_tree(C))
    assert (is_balanced_binary_tree(K))
    assert (is_balanced_binary_tree(G))
    assert (is_balanced_binary_tree(P))
    assert (not is_balanced_binary_tree(A))
    assert (not is_balanced_binary_tree(B))
    assert (not is_balanced_binary_tree(F))
    assert (not is_balanced_binary_tree(Q))

    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
