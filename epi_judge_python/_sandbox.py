from binary_tree_node import BinaryTreeNode
import heapq, itertools

def traverse_tree(root: BinaryTreeNode) -> None:
    # # -----INORDER 
    # if root.left:
    #     traverse_tree(root.left)
    # print(root.data)
    # if root.right:
    #     traverse_tree(root.right)

    # # -----PREORDER 
    # print(root.data)
    # if root.left:
    #     traverse_tree(root.left)
    # if root.right:
    #     traverse_tree(root.right)

    # ----POSTORDER 
    if root.left:
        traverse_tree(root.left)
    if root.right:
        traverse_tree(root.right)
    print(root.data)


def top_k(k, stream):	
	minpq = [(len(s), s) for s in itertools.islice(stream, k)]
	heapq.heapify(minpq)
	for s in stream:
		if len(s) > minpq[0][0]:
			heapq.heapreplace(minpq, (len(s), s))
	return [p[1] for p in heapq.nsmallest(k, minpq)] 


def binary_search(L, e):
	def helper(L, e, i):
		if len(L) == 1:
			return i + 0 
		elif len(L) == 2: 
			return i + 0 if L[0] == e else i + 1 
		elif len(L) > 2:
			k = len(L) // 2
			if e < L[k]:
				return helper(L[:k], e, i)
			elif e == L[k]:
				return i + k
			else:
				return helper(L[(k+1):], e, k+1)
	return helper(L, e, 0)


def bentley_binary_search(A, t):
	L, U = 0, len(A) - 1
	while L <= U:
		M = (L+U) // 2
		if A[M] < t:
			L = M + 1
		elif A[M] == t:
			return M
		else:
			U = M - 1
	return -1


if __name__ == '__main__':
# NOTE Chapter 11 (Search) Bootcamp
	for fun in [
				bentley_binary_search, 
				# binary_search
				]:
		assert(fun([1, 1, 1], 1) == 1)
		assert(fun([0, 0, 1], 1) == 2)
		assert(fun([-1, 0, 0], -1) == 0)
		assert(fun([-2, -1, 0, 1, 2], -2) == 0)
		assert(fun([-2, -2, 2], 2) == 2)
		assert(fun([1], 1) == 0)
		assert(fun([-1, 1], -1) == 0)
	print(bentley_binary_search([-2, -1, 0, 1, 2], -2))


# NOTE Chapter 10 (Priority Queue) Bootcamp 
	# stream = ['Let', 'us' ,'go', 'then',]
	# print(top_k(2, stream))


# NOTE Chapter 9 (Binary Tree) Bootcamp 
	# D = BinaryTreeNode(data='D')
	# E = BinaryTreeNode(data='E')
	# C = BinaryTreeNode(data='C', left=D, right=E)
	# H = BinaryTreeNode(data='H')
	# G = BinaryTreeNode(data='G', left=H)
	# F = BinaryTreeNode(data='F', right=G)
	# B = BinaryTreeNode(data='B', left=C, right=F)

	# M = BinaryTreeNode(data='M')
	# L = BinaryTreeNode(data='L', right=M)
	# N = BinaryTreeNode(data='N')
	# K = BinaryTreeNode(data='K', left=L, right=N)
	# J = BinaryTreeNode(data='J', right=K)
	# P = BinaryTreeNode(data='P')
	# O = BinaryTreeNode(data='O', right=P)
	# I = BinaryTreeNode(data='I', left=J, right=O)

	# A = BinaryTreeNode(data='A', left=B, right=I); traverse_tree(A)