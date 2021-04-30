from typing import List

from test_framework import generic_test
import collections, math, functools


def mine(paragraph): 
# -----MY SOLUTION, O(n) time, O(n) space, 
    LP = len(paragraph)
    if LP >= 2: 
        D = collections.defaultdict(lambda: [])
        for i in range(LP):
            D[paragraph[i]].append(i)
        result = min([compute_min_distance(x) for x in list(D.values())])
        if result < LP:
            return result
    return -1


def textbook_inspired(paragraph):
# ------TEXTBOOK INSPIRED SOLUTION, O(n) time, O(d) space,
# where d is the number of distinct words
    WordCounter = collections.namedtuple('WordCounter', 
                            ('MinDistance', 'LastSeenIdx'))
    D, LP, result = dict(), len(paragraph), math.inf
    if LP < 2:
        return -1
    for i in range(LP):
        if not paragraph[i] in D: # Never seen word 
            D[paragraph[i]] = WordCounter(MinDistance=math.inf, LastSeenIdx=i)
        elif D[paragraph[i]].MinDistance == math.inf: # Seen word once  
            D[paragraph[i]] = WordCounter(
                            MinDistance=i-D[paragraph[i]].LastSeenIdx,
                            LastSeenIdx=i)
        else: # Seen word 2+ times 
            D[paragraph[i]] = WordCounter(
                        MinDistance=min(i-D[paragraph[i]].LastSeenIdx, 
                                        D[paragraph[i]].MinDistance), 
                        LastSeenIdx=i)
        result = min(result, D[paragraph[i]].MinDistance)
    return result if result < LP else -1


def really_textbook_inspired(paragraph):
# ------REALLY TEXTBOOK INSPIRED SOLUTION, O(n) time, O(d) space,
# where d is the number of distinct words
    D, result = dict(), math.inf
    if len(paragraph) >= 2:
        for i, word in enumerate(paragraph):
            if word in D:  
                result = min(result, i-D[word]) 
            D[word] = i
    return result if result != math.inf else -1


def find_nearest_repetition(paragraph: List[str]) -> int:
    return really_textbook_inspired(paragraph)


def compute_min_distance(L: List[int]) -> int:
    result = math.inf
    for i in range(len(L) - 1):
        result = min(result, L[i+1] - L[i])
    return result
        

def test_compute_min_distance():
    L = [1, 5, 8]
    assert compute_min_distance(L) == 3

    L = [0, 6]
    assert compute_min_distance(L) == 6

    L = [0]
    assert compute_min_distance(L) == math.inf


def test_find_nearest_repetition():
    s = 'all work and no play makes for no work no fun and no results'.split(' ')
    assert find_nearest_repetition(s) == 2

    s = 'no no no'.split(' ')
    assert find_nearest_repetition(s) == 1

    s = 'the quick brown fox jumps over the'.split(' ')
    assert find_nearest_repetition(s) == 6

    s = 'the quick brown fox jumps over'.split(' ')
    assert find_nearest_repetition(s) == -1

    s = ['the']
    assert find_nearest_repetition(s) == -1

    s = 'and trust i say and just look and'.split(' ')
    assert find_nearest_repetition(s) == 3


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
