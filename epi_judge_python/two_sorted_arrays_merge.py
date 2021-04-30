from typing import List

from test_framework import generic_test
import random


def succinct(A, m, B, n):
    if A and B and n:
        m, n, i = m-1, n-1, m+n-1
        while min(m, n) >= 0:
            if B[n] > A[m]:
                A[i], n = B[n], n-1
            else:
                A[i], m = A[m], m-1
            i -= 1
        for n in range(n, -1, -1): 
            A[i], i = B[n], i-1 
    return


def my_first_solution(A, m, B, n):
    if A and B and n:
        placeholder = A[-1]
        m, n, i = m-1, n-1, len(A)-1
        while min(m, n) >= 0:
            if B[n] > A[m]:
                A[i], n = B[n], n-1
            else:
                A[i], m = A[m], m-1
            i -= 1
        for m in range(m, -1, -1):
            A[i], i = A[m], i-1
        for n in range(n, -1, -1): 
            A[i], i = B[n], i-1
        rotate = i+1
        A[:rotate] = [placeholder] * rotate
        A[rotate:], A[:rotate] =  A[:rotate], A[rotate:]
    return


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    return succinct(A, m, B, n)


def test_merge_two_sorted_arrays():
    A, m = [3, 13, 17, 0, 0, 0, 0, 0], 3 
    B, n = [3, 7, 11, 19], 4 
    merge_two_sorted_arrays(A, m, B, n) 
    assert A == [3, 3, 7, 11, 13, 17, 19, 0]

    A, m = [3, 0, 0], 1
    B, n = [0, 3], 2
    merge_two_sorted_arrays(A, m, B, n) 
    assert A == [0, 3, 3]

    A, m = [], 0
    B, n = [], 0
    merge_two_sorted_arrays(A, m, B, n) 
    assert A == []

    A, m = [0], 0
    B, n = [3], 1
    merge_two_sorted_arrays(A, m, B, n)
    assert A == [3]

    A, m = [1, 3, 5, 0], 3 
    B, n = [], 0
    merge_two_sorted_arrays(A, m, B, n)
    assert A == [1, 3, 5, 0]

    A, m = [22, 40, 40, 47, 69, 82, 93, 98, 100, 0, 0, 0], 9
    B, n = [39, 70, 81], 3
    merge_two_sorted_arrays(A, m, B, n)
    assert A == sorted(A)

    A, m = [2, 2, 5, 8, 9, 10], 5
    B, n = [0, 3, 4, 7, 9], 5
    A += [0] * (len(B))
    merge_two_sorted_arrays(A, m, B, n)
    assert A == [0, 2, 2, 3, 4, 5, 7, 8, 9, 9, 0]

    A, m = [0, 1, 1, 2, 6, 6, 7], 4
    B, n = [3, 4, 5, 7, 8, 8, 9], 5
    A += [0] * (len(B))
    merge_two_sorted_arrays(A, m, B, n)
    assert A == [0, 1, 1, 2, 3, 4, 5, 7, 8, 0, 0, 0, 0, 0]

    for _ in range(10**2):
        (A, m), (B, n) = list_generator(), list_generator()
        A += [0] * (len(B))
        print(f"A:{A}, m: {m}, n: {n}, B:{B}, ")
        merge_two_sorted_arrays(A, m, B, n)
        assert A[:m+n] == sorted(A)[len(A)-m-n:]


def list_generator(size=random.randint(0, 10)):
    L = []
    for _ in range(size):
        L.append(random.randint(0, 10))
    return (sorted(L), size)


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))