from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections


# -----MY solution, O(n) space, O(1) time 
class Stack: 

    def __init__(self):
        self.s = list() 
        self.maxes = list() 

    def empty(self) -> bool:
        return len(self.s) == 0 

    def max(self) -> int:
        return self.maxes[-1]

    def pop(self) -> int:
        self.maxes.pop()
        return self.s.pop()

    def push(self, x: int) -> None:
        if len(self.maxes) == 0 or x > self.maxes[-1]: 
            self.maxes.append(x)
        else:
            self.maxes.append(self.maxes[-1])
        self.s.append(x)
        return

# # -----TEXTBOOK solution, O(n) space, O(1) time 
# class Stack: 

#     StackElement = collections.namedtuple('StackElement', ['value', 'max'])

#     def __init__(self):
#         self.s = []

#     def empty(self) -> bool:
#         return len(self.s) == 0 

#     def max(self) -> int:
#         return self.s[-1].max

#     def pop(self) -> int:
#         return self.s.pop().value

#     def push(self, x: int) -> None:
#         self.s.append(self.StackElement(x, 
#                 x if self.empty() else max(x, self.max())))
#         return 

#     def __str__(self) -> str:
#         string = '' 
#         for e in self.s:
#             string += "value:{}, max:{}".format(e.value, e.max) + '\n'
#         return string 

def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    # s = Stack()
    # s.push(1)
    # print(s.empty()) # False 
    # s.pop()
    # print(s.empty()) # true 
    # s.push(1) 
    # s.push(2)
    # s.push(-3)
    # s.push(5)
    # print(s.max()) # 5 
    # s.pop()
    # print(s.max()) # 2
    # print(s)

    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
