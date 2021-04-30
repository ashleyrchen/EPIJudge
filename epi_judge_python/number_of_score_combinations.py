from typing import List, Set

from test_framework import generic_test
import numpy as np


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
                                    
# # -----MY NAIVE SOLUTION, so inefficient only four tests run on the autograder
#     def helper(score: int, 
#                 solution: tuple, 
#                 parent: int, 
#                 combinations: Set[tuple]) -> Set[tuple]:
#         for s in individual_play_scores:
#             if score == final_score:
#                 combinations.add(tuple(solution))
#             elif score < final_score:
#                 if s <= parent:
#                     temp = solution[:]
#                     temp[D[s]] += 1
#                     helper(score + s, temp, s, combinations,)
#         return combinations

#     if final_score == 0:
#         return 0 
#     D = dict(zip(individual_play_scores, range(len(individual_play_scores))))
#     combinations = helper(0, 
#                         [0] * len(individual_play_scores), 
#                         max(individual_play_scores), 
#                         set())
#     return len(combinations)

# -----TEXTBOOK DP SOLUTION, O(NS) time, O(NS) space,
# where N is final_score and S is the len of individual_play_scores 
    if final_score == 0: 
        return 1
    N, S = final_score, len(individual_play_scores)
    A = np.zeros((S, N))
    for r in range(S):
        for c in range(N):
                if r-1 >= 0:
                    A[r,c] += A[r-1,c] 
                if c+1 == individual_play_scores[r]:
                    A[r,c] += 1
                if c-individual_play_scores[r] >= 0:
                    A[r,c] += A[r,c-individual_play_scores[r]] 
    return A[S-1,N-1]


if __name__ == '__main__':
    assert num_combinations_for_final_score(2, [2, 3, 7]) == 1
    assert num_combinations_for_final_score(3, [2, 3, 7]) == 1
    assert num_combinations_for_final_score(4, [2, 3, 7]) == 1
    assert num_combinations_for_final_score(6, [2, 3, 7]) == 2
    assert num_combinations_for_final_score(5, [2, 3, 7]) == 1
    assert num_combinations_for_final_score(7, [2, 3, 7]) == 2
    assert num_combinations_for_final_score(12, [2, 3, 7]) == 4
    assert num_combinations_for_final_score(0, [2, 3, 7]) == 1

    assert num_combinations_for_final_score(1, [1]) == 1
    assert num_combinations_for_final_score(2, [1, 2]) == 2

    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))