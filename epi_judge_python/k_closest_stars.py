import functools
import math
from typing import Iterator, List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
import heapq
from heapq import heapify, heappush, heappushpop, heapreplace, nlargest
import random


class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)
        # return f"x:{self.x}, y:{self.y}, z:{self.z}, dist:{self.distance}"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    # return naive_find_closest_k_stars(stars, k)
    return improved_find_closest_k_stars(stars, k)


def improved_find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
# -----IMPROVED SOLUTION, O(nlogk) time, O(k) space, 
    if k == 0: 
        return []
    x = []
    for star in stars:
        if len(x) < k:
            x.append((-star.distance, star)) 
        else:
            if len(x) == k:
                heapify(x) 
            if -star.distance > x[0][0]:
                heapreplace(x, (-star.distance, star))
    # x.sort(reverse=True)
    # return [b for (a, b) in list(x)]
    return [b for (a, b) in nlargest(k, x)]


def naive_find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
# -----NAIVE SOLUTION, O(nlogn) time, O(n) space,
    if k == 0: 
        return []
    x = []
    heapify(x)
    for star in stars:
        heappush(x, (star.distance, star))
    x.sort()
    return [b for (a, b) in x[:k]]


def test_find_closest_k_stars():
    A = Star(0, 0, 0)
    assert find_closest_k_stars(iter([A]), 0) == []
    assert find_closest_k_stars(iter([]), 0) == []
    assert find_closest_k_stars(iter([A]), 1) == [A]

    B = Star(-1, 10, 5)
    C = Star(-1, -1, -1)
    D = Star(0, 500, 12)
    assert find_closest_k_stars(iter([A, B, C, D,]), 3) == [A, C, B]

    def star_generator():
        def rand_int():
            return random.randint(0, 10**20)
        return Star(rand_int(), rand_int(), rand_int())
    
    def galaxy_tester():
        N, L = random.randint(0, 10**6), []
        for _ in range(N):
            L.append(star_generator())
        k = random.randint(0, N)
        # for s in L:
        #     print(f"x:{s.x}, y:{s.y}, z:{s.z}, dist:{s.distance}")
        assert (find_closest_k_stars(iter(L), k) == 
                naive_find_closest_k_stars(iter(L), k))

    for _ in range(10):
        galaxy_tester()
    

def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars, iter(stars),
                                          k))


if __name__ == '__main__':
    # s = Star(50, 10, 22)
    # print(s.distance)
    exit(
        generic_test.generic_test_main('k_closest_stars.py',
                                       'k_closest_stars.tsv',
                                       find_closest_k_stars_wrapper, comp))
