from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections 


# -----TEXTBOOK SOLUTION, O(1) lookup, insertion, deletion
class LruCache:
    def __init__(self, capacity: int,) -> None:
        self.capacity = capacity
        self.dictionary = collections.OrderedDict()
        return

    def lookup(self, isbn: int) -> int:
        if isbn in self.dictionary:
            price = self.dictionary.pop(isbn)
            self.dictionary[isbn] = price
            return price
        return -1

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.dictionary:
            price = self.dictionary.pop(isbn)
        elif len(self.dictionary) == self.capacity:
            self.dictionary.popitem(last=False) # Remove in FIFO order
        self.dictionary[isbn] = price
        return

    def erase(self, isbn: int) -> bool:
        if isbn in self.dictionary:
            self.dictionary.pop(isbn)
            return True
        return False


# ------MY ORIGINAL SOLUTION, O(1) lookup, O(n) insertion, O(1) deletion 
# ISBNData = collections.namedtuple('ISBNData', ('Price', 'Time'))
# class LruCache:
#     def __init__(self, capacity: int,) -> None:
#         self.capacity = capacity
#         self.dictionary = dict()
#         self.time = 0
#         return

#     def lookup(self, isbn: int) -> int:
#         if isbn in dictionary:
#             self.time += 1
#             self.dictionary[isbn].Time = self.time
#             return self.dictionary[isbn].Price
#         return -1

#     def insert(self, isbn: int, price: int) -> None:
#         self.time += 1
#         if isbn in dictionary:
#             self.dictionary[isbn].Time = self.time
#         else: 
#             if len(self.dictionary) == self.capacity:
#                 erase(min(list(D.items()), key=lambda x: x[1].Time)[0])
#             self.dictionary[isbn] = ISBNData(price, self.time)
#         return

#     def erase(self, isbn: int) -> bool:
#         if isbn in dictionary:
#             dictionary.__delitem__(isbn)
#             return True
#         return False


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
