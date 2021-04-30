from typing import List

from test_framework import generic_test
import random, heapq 
from heapq import heapify, heapreplace
import operator


def naive(k, A):
# -----NAIVE SOLUTION, O(nlogn) time, O(1) space,
    A.sort(reverse=True)
    return A[k-1]


def improved(k, A):
# -----IMPROVED SOLUTION, O((n-k)logk) time, O(k) space, 
    x = A[:k]
    heapify(x)
    for a in A[k:]:
        if a > x[0]:
            heapreplace(x, a)
    return x[0]


def my_partition(A: List[int], i=0):
    p = random.randint(0, len(A)-1)
    partition = A[p]
    while i < len(A):
        if i < p:
            if A[i] >= A[p]:
                A[p], A[p-1] = A[p-1], A[p]
                p -= 1
                if i == p:
                    A[p+1], A[i] = A[i], A[p+1] 
                i -= 1
        elif i > p:
            if A[i] < A[p]:
                A[p], A[p+1] = A[p+1], A[p]
                p += 1
                if i != p:
                    A[p-1], A[i] = A[i], A[p-1] 
                i -= 1
        i += 1
    return p


def textbook_inspired(k, A): 
# # ------SOLUTION I WROTE AFTER READING THE TEXTBOOK, O(n) time, O(n) space, 
    while True:
        p = my_partition(A)
        if len(A)-1-p == k-1:
            return A[p]
        elif len(A)-1-p < k-1:
            (A,k) = (A[:p], k-len(A)+p)
        else:
            (A,k) = (A[(p+1):], k)


def find_kth_largest(k: int, A: List[int]) -> int:
# -----SOLUTION I WROTE AFTER STUDYING THE TEXTBOOK, O(n) time, O(1) space, 
    p, r = 0, len(A)-1
    while True:
        p_idx = partition(A, p, r)
        size_b = len(A)-p_idx-1 # number of elements larger than pivot
        if size_b == k-1:
            return A[p_idx]
        elif size_b < k-1:
            r = p_idx-1
        else:
            p = p_idx+1


def partition(A, p, r):
# ------BASICALLY COPIED FROM CLRS
    idx = random.randint(p, r)
    A[idx], A[r] = A[r], A[idx]
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def test_partition():
    L = argument_generator()[1]
    p_idx = partition(L, 0, len(L)-1)
    print(L)
    for i in range(len(L)):
        if i < p_idx:
            assert L[i] <= L[p_idx]
        elif i > p_idx:
            assert L[i] > L[p_idx]


def argument_generator(L=[]):
    for _ in range(random.randint(0, 10**2)):
        L.append(random.randint(0, 10**2))
    return (random.randint(1, len(L)), L)


def test_find_kth_largest():
    A = [3, 1, -1, 2]
    assert find_kth_largest(1, A) == naive(1, A) 
    assert find_kth_largest(2, A) == naive(2, A)
    assert find_kth_largest(3, A) == naive(3, A)
    assert find_kth_largest(4, A) == naive(4, A)

    A = [3, 2, 1, 5, 4]
    assert find_kth_largest(1, A) == naive(1, A)
    assert find_kth_largest(3, A) == naive(3, A)
    assert find_kth_largest(5, A) == naive(5, A)

    A = [-1]
    assert find_kth_largest(1, A) == naive(1, A)

    A = [3, 3, 3, 2, 2, 1]
    assert find_kth_largest(3, A) == naive(3, A)

    for _ in range(10**2):
        (k, A) = argument_generator()
        print(f"k:{k}, A:{A}")
        assert naive(k, A) == find_kth_largest(k, A)
        

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))