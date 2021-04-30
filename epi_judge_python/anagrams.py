from typing import List
import collections 
from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    # # -----NAIVE solution,  O(n) space, O(n^2mlogm) time,
    # result = []
    # i = 0
    # visited_set = set() 
    # while i < len(dictionary): # n iterations  
    #     if i not in visited_set:
    #         subresult = [dictionary[i]]
    #         j = i + 1
    #         while j < len(dictionary): # n iterations 
    #             if sorted(dictionary[i]) == sorted(dictionary[j]): # O(mlogm)
    #                 subresult += [dictionary[j]]
    #                 visited_set.add(j)
    #             j += 1 
    #         if len(subresult) > 1:
    #             result += [subresult]
    #     i += 1
    # return result 

    # # # ----REVISED solution, O(n) space, O(nmlogm) time, 
    # hash_table = dict()
    # for s in dictionary: # n iterations 
    # # # NOTE ''.join(sorted(s)) is faster than str(sorted(s))
    #     my_hash = ''.join(sorted(s))
    #     if hash_table.__contains__(my_hash):
    #         hash_table[my_hash].append(s)
    #     else:
    #         hash_table[my_hash] = [s]
    # return ([t[1] for t in hash_table.items() if len(t[1]) > 1])

    # -----TEXTBOOK solution, O(n) space, O(nmlogm) time, 
    sorted_string_to_anagrams: DefaultDict[
        str, List[str]] = collections.defaultdict(list)
    for s in dictionary:
        # Sorts the string, uses it as a key, and then appends the original
        # string as another value into hash table.
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [
        group for group in sorted_string_to_anagrams.values()
        if len(group) >= 2
    ]
    

if __name__ == '__main__':
    A = ['debitcard', 'elvis', 'silent', 'badcredit', 'lives', 
                        'freedom', 'listen', 'levis', 'money',]
    assert(find_anagrams(A) == [['debitcard', 'badcredit'], ['elvis', 'lives', 'levis'], ['silent', 'listen'], ])

    A = ['hello', 'world']
    assert(find_anagrams(A) == [])

    A = ['carpark', 'car', 'park', 'parkcar']
    assert(find_anagrams(A) == [['carpark', 'parkcar']])

    A = ['hello']
    assert(find_anagrams(A) == [])

    A = ['']
    assert(find_anagrams(A) == [])

    A = ['hello', 'hell',]
    assert(find_anagrams(A) == [])

    A = ['abc', 'cab', 'bca']
    assert(find_anagrams(A) == [['abc', 'cab', 'bca']])

    A = ["debit card", "bad credit", "the morse code", "here come dots", "the eyes", "they see", "THL"] 
    assert(find_anagrams(A) == [['debit card', 'bad credit'], ['the morse code', 'here come dots'], ['the eyes', 'they see']])

    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
